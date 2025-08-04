# Fixed code section for pneumonia classification

import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define parameters
batch_size = 16
img_height = 224
img_width = 224

# Set up dataset paths - LOCAL PATHS (fixed)
train_path = './chest_xray/train'
test_path = './chest_xray/test'
valid_path = './chest_xray/val'

# Check if directories exist
print(f"Train directory exists: {os.path.exists(train_path)}")
print(f"Test directory exists: {os.path.exists(test_path)}")
print(f"Validation directory exists: {os.path.exists(valid_path)}")

# Create data generators
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(rescale=1./255)

# Load and preprocess training images (with augmentation)
train = train_datagen.flow_from_directory(
    train_path,
    target_size=(img_height, img_width),
    color_mode='grayscale',
    class_mode='binary',
    batch_size=batch_size
)

# Load and preprocess test images (no augmentation, no shuffle)
test = test_datagen.flow_from_directory(
    test_path,
    target_size=(img_height, img_width),
    color_mode='grayscale',
    shuffle=False,
    class_mode='binary',
    batch_size=batch_size
)

# Load and preprocess validation images (no augmentation)
valid = test_datagen.flow_from_directory(
    valid_path,
    target_size=(img_height, img_width),
    color_mode='grayscale',
    class_mode='binary',
    batch_size=batch_size
)

print(f"Training samples: {train.samples}")
print(f"Test samples: {test.samples}")
print(f"Validation samples: {valid.samples}")
print(f"Class indices: {train.class_indices}") 