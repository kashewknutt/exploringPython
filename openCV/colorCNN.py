import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
import numpy as np
import cv2
import os

# Define the batch size
BATCH_SIZE = 32
IMAGE_SIZE = 64

# Define the colors and their corresponding HSV ranges
COLORS = {
    'dull_yellow': ((20, 100, 100), (30, 255, 255)),  # HSV range for dull yellow
    'whitish_grey': ((0, 0, 200), (180, 50, 255)),    # HSV range for whitish grey
    'aqua_bluish_green': ((75, 100, 50), (95, 255, 255)),  # HSV range for aqua bluish green
    'orange_ping_pong': ((5, 150, 150), (15, 255, 255))  # HSV range for orange ping pong
}

def preprocess_image(image, lower_color, upper_color):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower_color, upper_color)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result

def augment_with_color_focus(image):
    masks = []
    for color_name, (lower, upper) in COLORS.items():
        processed_image = preprocess_image(image, lower, upper)
        masks.append(processed_image)
    
    # Resize the original image to IMAGE_SIZE
    resized_image = cv2.resize(image, IMAGE_SIZE)
    
    # Concatenate the original image with all the masks as additional channels
    combined_image = np.concatenate([resized_image] + masks, axis=-1)
    return combined_image

# Custom data generator
class CustomImageDataGenerator(tf.keras.utils.Sequence):
    def __init__(self, image_paths, labels, batch_size, target_size, num_classes):
        self.image_paths = image_paths
        self.labels = labels
        self.batch_size = batch_size
        self.target_size = target_size
        self.num_classes = num_classes
        self.on_epoch_end()

    def __len__(self):
        return len(self.image_paths) // self.batch_size

    def __getitem__(self, index):
        batch_image_paths = self.image_paths[index * self.batch_size:(index + 1) * self.batch_size]
        batch_labels = self.labels[index * self.batch_size:(index + 1) * self.batch_size]

        images = [cv2.imread(img_path) for img_path in batch_image_paths]
        processed_images = [augment_with_color_focus(img, self.target_size) for img in images]

        X = np.array(processed_images, dtype=np.float32) / 255.0
        y = tf.keras.utils.to_categorical(batch_labels, self.num_classes)

        print(f"Batch X shape: {X.shape}, Batch y shape: {y.shape}")

        return X, y

    def on_epoch_end(self):
        p = np.random.permutation(len(self.image_paths))
        self.image_paths = np.array(self.image_paths)[p]
        self.labels = np.array(self.labels)[p]

# Instantiate the data generator
def get_data_generator(data_dir, batch_size, image_size, num_classes):
    # Prepare image paths and labels
    classes = os.listdir(data_dir)
    image_paths = []
    labels = []

    for idx, class_name in enumerate(classes):
        class_dir = os.path.join(data_dir, class_name)
        for image_name in os.listdir(class_dir):
            image_path = os.path.join(class_dir, image_name)
            image_paths.append(image_path)
            labels.append(idx)

    # Instantiate the data generator
    return CustomImageDataGenerator(image_paths, labels, batch_size, image_size, num_classes)
