import cv2
import os
import numpy as np
import random


# Function to perform data augmentation on an image
def augment_image(image_path, save_path, num_augmentations=5):
    # Read the image
    image = cv2.imread(image_path)
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)

    # Define the transformations
    transformations = [
        ("flipped_horizontal", cv2.flip(image, 1)),
        ("flipped_vertical", cv2.flip(image, 0)),
        ("flipped_both", cv2.flip(image, -1)),
        ("rotated_90_clockwise", cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)),
        ("rotated_90_counterclockwise", cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)),
        ("rotated_180", cv2.rotate(image, cv2.ROTATE_180)),
        ("scaled_up", cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)),
        ("scaled_down", cv2.resize(image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)),
        ("translated_right", np.roll(image, 50, axis=1)),
        ("translated_down", np.roll(image, 50, axis=0)),
        # Add more transformations as needed
    ]

    # Apply transformations and save augmented images
    for i in range(num_augmentations):
        transform_name, transformed_image = random.choice(transformations)
        augmented_filename = f"{name}_{transform_name}_{i + 1}{ext}"
        augmented_path = os.path.join(save_path, augmented_filename)
        cv2.imwrite(augmented_path, transformed_image)


# Example usage
if __name__ == "__main__":
    # Path to the image to be augmented
    image_path = "0JbZcZcTjXmjqr4utPHj_1L_PET_1.png"
    # Directory to save augmented images
    save_path = "augmented_images"

    # Create save directory if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Perform data augmentation
    augment_image(image_path, save_path)
