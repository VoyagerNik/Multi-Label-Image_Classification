import numpy as np
import matplotlib.pyplot as plt

def plot_training_history(history):
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.legend()
    plt.show()

def display_image(image, label):
    plt.imshow(image)
    plt.title(label)
    plt.axis('off')
    plt.show()

# Example usage
if __name__ == "__main__":
    # Assuming you have an image and its label
    image = np.random.rand(224, 224, 3)
    label = "Example Image"
    display_image(image, label)
