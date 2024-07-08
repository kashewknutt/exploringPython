import cv2
import numpy as np
from tensorflow.keras.models import load_model
from colorCNN import get_data_generator

# Load the trained CNN model
model = load_model('ball_color_classifier_with_color_focus.h5')

# Define constants for colors (for drawing purposes)
DRAW_COLORS = {
    'dull_yellow': (0, 255, 255),    # Yellow color for drawing
    'whitish_grey': (255, 255, 255),  # White color for drawing
    'aqua_bluish_green': (255, 255, 0),  # Aqua color for drawing
    'orange_ping_pong': (0, 165, 255),  # Orange color for drawing
}

# Define quadrants with adjusted coordinates (format: (top-left x, top-left y, width, height))
QUADRANTS = {
    1: (520, 300, 205, 260),
    2: (330, 300, 180, 260),
    3: (330, 13, 180, 267),
    4: (520, 14, 205, 265),
}

# Video file path
video_path = 'E:/Github/exploringPython/openCV/AIAssignmentVideo.mp4'

# Output video and text file paths
output_video_path = 'output_video.avi'  # Update with desired output video path
output_text_path = 'events.txt'  # Update with desired output text file path

# Open video file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video file")

# Create video writer for output video
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

# Initialize variables for ball tracking and event logging
balls = {}  # Dictionary to store information about tracked balls (ID, color, current quadrant, etc.)
events = []  # List to store event logs (Time, Quadrant Number, Ball Color, Event Type)

# Function to calculate timestamp from frame number
def calculate_timestamp(frame_number):
    return frame_number / fps

# Function to classify the ball color using the CNN
def classify_ball_color(image):
    # Resize the image to match the expected input size of your model
    image_resized = cv2.resize(image, (64, 64))
    
    # Prepare the image array and normalize
    image_array = np.array(image_resized) / 255.0
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    
    # Predict using the model
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions)
    
    # Map the predicted class index to color name
    return list(DRAW_COLORS.keys())[predicted_class]


# Function to detect and track balls
def detect_and_track_balls(frame):
    # Convert frame to HSV for color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 220], dtype="uint8")
    upper = np.array([180, 25, 255], dtype="uint8")
    mask = cv2.inRange(hsv, lower, upper)

    # Apply some morphological operations to remove noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # Find contours in the mask and initialize the centroid of the ball
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Calculate the area and filter out small contours
        area = cv2.contourArea(contour)
        if area < 500:
            continue

        # Get the bounding box for each contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Extract the ball region from the frame
        ball_region = frame[y:y+h, x:x+w]

        # Classify the ball color
        ball_color = classify_ball_color(ball_region)

        # Draw a bounding box and label the ball
        cv2.rectangle(frame, (x, y), (x + w, y + h), DRAW_COLORS[ball_color], 2)
        cv2.putText(frame, ball_color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, DRAW_COLORS[ball_color], 2)

        # Calculate the centroid of the ball
        center = (int(x + w / 2), int(y + h / 2))

        # Update ball information (ID, color, current quadrant, etc.)
        ball_id = len(balls) + 1
        if ball_id not in balls:
            balls[ball_id] = {
                'id': ball_id,
                'color': ball_color,
                'centroid': center,
                'last_quadrant': None,  # To store the last quadrant the ball was detected in
                'path': [center],  # List to store centroid path for tracking
            }
        else:
            # Track movement path of the ball
            balls[ball_id]['centroid'] = center
            balls[ball_id]['path'].append(center)

    return frame

# Function to detect entry and exit events in quadrants
def detect_entry_exit_events(frame_number):
    for ball_id, ball_info in balls.items():
        current_centroid = ball_info['centroid']
        ball_color = ball_info['color']
        
        # Check if ball has moved into a new quadrant
        for quadrant_num, (x, y, w, h) in QUADRANTS.items():
            if x <= current_centroid[0] <= x + w and y <= current_centroid[1] <= y + h:
                if ball_info['last_quadrant'] != quadrant_num:
                    if ball_info['last_quadrant'] is not None:
                        events.append({
                            'timestamp': calculate_timestamp(frame_number),
                            'quadrant_number': ball_info['last_quadrant'],
                            'ball_color': ball_color,
                            'event_type': 'Exit'
                        })
                    events.append({
                        'timestamp': calculate_timestamp(frame_number),
                        'quadrant_number': quadrant_num,
                        'ball_color': ball_color,
                        'event_type': 'Entry'
                    })
                    ball_info['last_quadrant'] = quadrant_num
                    break
            else:
                if ball_info['last_quadrant'] == quadrant_num:
                    events.append({
                        'timestamp': calculate_timestamp(frame_number),
                        'quadrant_number': quadrant_num,
                        'ball_color': ball_color,
                        'event_type': 'Exit'
                    })
                    ball_info['last_quadrant'] = None

# Function to overlay text on video frame
def overlay_text(frame, text, position):
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Function to draw ball paths on the frame
def draw_ball_paths(frame):
    for ball_id, ball_info in balls.items():
        path = ball_info['path']
        if len(path) > 1:
            for i in range(1, len(path)):
                cv2.line(frame, path[i-1], path[i], DRAW_COLORS[ball_info['color']], 2)

# Function to draw rectangles for each quadrant
def draw_quadrant_rectangles(frame):
    for quadrant_num, (x, y, w, h) in QUADRANTS.items():
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
        cv2.putText(frame, f"Q{quadrant_num}", (x + 5, y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Main loop for processing video frames
frame_number = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Resize frame for proper display
    frame = cv2.resize(frame, (800, 600))  # Adjust dimensions as needed
    
    # Draw quadrant rectangles on the frame
    draw_quadrant_rectangles(frame)
    
    # Process frame: detect and track balls
    frame = detect_and_track_balls(frame)
    
    # Detect entry and exit events in quadrants
    detect_entry_exit_events(frame_number)
    
    # Draw ball paths on the frame
    draw_ball_paths(frame)
    
    # Overlay entry and exit events on the video frame
    for event in events:
        timestamp = event['timestamp']
        quadrant_number = event['quadrant_number']
        ball_color = event['ball_color']
        event_type = event['event_type']
        text = f"{ball_color} - {event_type} in Q{quadrant_number} at {timestamp:.2f}s"
        position = (20, 50 + 50 * (list(DRAW_COLORS.keys()).index(ball_color)))
        overlay_text(frame, text, position)
    
    # Write the frame with overlays to the output video
    out.write(frame)
    
    # Display the frame
    cv2.imshow('Frame', frame)
    
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Increment frame number
    frame_number += 1

# Release video capture and writer objects
cap.release()
out.release()
cv2.destroyAllWindows()

# Write events to the text file
with open(output_text_path, 'w') as f:
    for event in events:
        f.write(f"{event['timestamp']:.2f}s - {event['ball_color']} - {event['event_type']} in Q{event['quadrant_number']}\n")

print("Video processing completed and events logged.")
