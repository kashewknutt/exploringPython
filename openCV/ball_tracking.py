import cv2
import numpy as np

# Define constants for colors (BGR format)
COLORS = {
    'red': (0, 0, 255),
    'blue': (255, 0, 0),
    'green': (0, 255, 0),
    # Add more colors as needed
}

# Define quadrants (example)
# Format: (top-left x, top-left y, width, height)
QUADRANTS = {
    1: (50, 50, 200, 200),
    2: (300, 50, 200, 200),
    3: (50, 300, 200, 200),
    4: (300, 300, 200, 200),
}

# Video file path
video_path = 'E:/Github/exploringPython/openCV/AIAssignmentVideo.mp4'  # Update with your video file path

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

# Function to detect and track balls
def detect_and_track_balls(frame):
    # Convert frame to HSV for color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Track balls of predefined colors
    for color_name, color_value in COLORS.items():
        # Define color range for detection (example for red balls)
        if color_name == 'red':
            lower_color = np.array([0, 100, 100])
            upper_color = np.array([10, 255, 255])
            mask1 = cv2.inRange(hsv, lower_color, upper_color)
            lower_color = np.array([160, 100, 100])
            upper_color = np.array([179, 255, 255])
            mask2 = cv2.inRange(hsv, lower_color, upper_color)
            mask = mask1 + mask2
        else:
            lower_color = np.array([50, 100, 100])
            upper_color = np.array([70, 255, 255])
            mask = cv2.inRange(hsv, lower_color, upper_color)
        
        # Find contours in the mask and initialize the centroid of the ball
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center = None
        
        # Proceed if at least one contour was found
        if len(contours) > 0:
            # Find the largest contour in the mask
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            
            # Only proceed if the radius meets a minimum size
            if radius > 10:
                # Calculate centroid of the ball
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                
                # Update ball information (ID, color, current quadrant, etc.)
                ball_id = len(balls) + 1
                if ball_id not in balls:
                    balls[ball_id] = {
                        'id': ball_id,
                        'color': color_name,
                        'centroid': center,
                        'last_quadrant': None,  # To store the last quadrant the ball was detected in
                        'path': [center],  # List to store centroid path for tracking
                    }
                else:
                    # Track movement path of the ball
                    balls[ball_id]['centroid'] = center
                    balls[ball_id]['path'].append(center)
                
                # Perform ball tracking logic here (e.g., Kalman filter, etc.)

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
                cv2.line(frame, path[i-1], path[i], COLORS[ball_info['color']], 2)

# Function to draw rectangles for each quadrant
def draw_quadrant_rectangles(frame):
    for quadrant_num, (x, y, w, h) in QUADRANTS.items():
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)  # White rectangle

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
    detect_and_track_balls(frame)
    
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
        
        # Display event on frame
        overlay_text(frame, f"{event_type} - {ball_color}", (20, 50))
        overlay_text(frame, f"Quadrant: {quadrant_number}", (20, 100))
        overlay_text(frame, f"Time: {timestamp:.2f} seconds", (20, 150))
    
    # Write the frame with overlays to the output video
    out.write(frame)
    
    # Display the frame
    cv2.imshow('Frame', frame)
    
    # Clear events list for next frame
    events.clear()
    
    # Wait for the next frame at the video's frame rate
    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break
    
    # Increment frame number
    frame_number += 1

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

# Save event logs to a text file
with open(output_text_path, 'w') as f:
    for event in events:
        f.write(f"Timestamp: {event['timestamp']:.2f}, Quadrant Number: {event['quadrant_number']}, "
                f"Ball Color: {event['ball_color']}, Type: {event['event_type']}\n")

print("Processing complete. Output video saved at:", output_video_path)
print("Event logs saved at:", output_text_path)
