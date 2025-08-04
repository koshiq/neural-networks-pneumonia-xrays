import requests
import os
from PIL import Image
import numpy as np

def create_sample_image(filename, size=(224, 224), color='gray'):
    """Create a sample X-ray-like image"""
    if color == 'gray':
        # Create a grayscale image that looks like an X-ray
        img_array = np.random.randint(0, 255, size + (1,), dtype=np.uint8)
        # Add some structure to make it look more like an X-ray
        for i in range(size[0]):
            for j in range(size[1]):
                # Add some vertical and horizontal lines
                if i % 50 == 0 or j % 50 == 0:
                    img_array[i, j, 0] = 255
                # Add some random bright spots
                if np.random.random() < 0.01:
                    img_array[i, j, 0] = 255
    else:
        img_array = np.random.randint(0, 255, size + (3,), dtype=np.uint8)
    
    img = Image.fromarray(img_array.squeeze())
    img.save(filename)
    print(f"Created sample image: {filename}")

def main():
    # Create sample images for testing
    sample_images = [
        ('chest_xray/train/NORMAL/sample_normal_1.jpg', (224, 224), 'gray'),
        ('chest_xray/train/NORMAL/sample_normal_2.jpg', (224, 224), 'gray'),
        ('chest_xray/train/PNEUMONIA/sample_pneumonia_1.jpg', (224, 224), 'gray'),
        ('chest_xray/train/PNEUMONIA/sample_pneumonia_2.jpg', (224, 224), 'gray'),
        ('chest_xray/test/NORMAL/sample_normal_test_1.jpg', (224, 224), 'gray'),
        ('chest_xray/test/PNEUMONIA/sample_pneumonia_test_1.jpg', (224, 224), 'gray'),
        ('chest_xray/val/NORMAL/sample_normal_val_1.jpg', (224, 224), 'gray'),
        ('chest_xray/val/PNEUMONIA/sample_pneumonia_val_1.jpg', (224, 224), 'gray'),
    ]
    
    print("Creating sample X-ray images for testing...")
    
    for filename, size, color in sample_images:
        # Ensure directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        create_sample_image(filename, size, color)
    
    print("\nSample images created! You can now test your notebook.")
    print("Note: These are synthetic images for testing only.")
    print("For real training, download the actual dataset from Kaggle.")

if __name__ == "__main__":
    main() 