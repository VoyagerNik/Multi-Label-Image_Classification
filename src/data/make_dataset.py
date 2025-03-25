import os
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def prepare_dataset(data_dir, test_size=0.2):
    # Define data generator for training and testing
    train_datagen = ImageDataGenerator(rescale=1./255)
    test_datagen = ImageDataGenerator(rescale=1./255)

    # Load dataset
    train_generator = train_datagen.flow_from_directory(
        os.path.join(data_dir, 'train'),
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical'
    )

    test_generator = test_datagen.flow_from_directory(
        os.path.join(data_dir, 'test'),
        target_size=(224, 224),
        batch_size=32,
        class_mode='categorical'
    )

    return train_generator, test_generator

# Example usage
if __name__ == "__main__":
    data_dir = 'data'
    train_generator, test_generator = prepare_dataset(data_dir)
