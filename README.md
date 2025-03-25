# Multi-Label-Image_Classification

This project provides a framework for multi-label image classification using a dynamic dataset. Users can apply this framework to their own dataset by following the instructions below.

## Overview

The project includes a Jupyter Notebook (`ML_img_classifier_project1.ipynb`) that contains all the necessary code for training a multi-label image classification model. The notebook covers data preparation, model training, and prediction.

## Getting Started

1. Clone the repository: `git clone https://github.com/VoyagerNik/Multi-Label-Image-Classification.git`
2. Install requirements: `pip install -r requirements.txt`

## Structure

```plaintext
Multi-Label-Image-Classification/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── data/
│   └── README.md
├── notebooks/
│   └── ML_img_classifier_project1-1.ipynb
├── src/
│   ├── data/
│   │   └── make_dataset.py
│   └── utils/
│       └── helper_functions.py
```

## Code Structure

- **`notebooks/ML_img_classifier_project.ipynb`**: This Jupyter Notebook contains the main code for data preparation, model training, and prediction.
- **`src/`**: This directory contains Python scripts for modularity:
- **`data/make_dataset.py`**: Prepares the dataset for training.
- **`utils/helper_functions.py`**: Utility functions for tasks like plotting training history.
- **`requirements.txt`**: Lists all Python packages required to run the project.
- **`.gitignore`**: Specifies files and directories to ignore in version control.

## Model Details

The model used in this project is a convolutional neural network (CNN) designed for multi-label image classification. It consists of several convolutional and pooling layers followed by fully connected layers. The model is trained using binary cross-entropy loss and Adam optimizer.

## Example Output

Here's an example output from running the code:

| Animal          | Match Percentage |
|-----------------|------------------|
| butterfly       | 0.096146         |
| cat             | 0.000029         |
| cow             | 86.320374        |
| dog             | 83.536407        |
| elephant        | 0.057069         |
| goat            | 85.153244        |
| hen             | 89.700546        |
| horse           | 81.004318        |
| squirrel        | 0.114980         |
| spider          | 0.000007         |

**Prediction Result**: The model predicts that the image is most likely a **hen**.

## Dataset Preparation

1. Create a folder named `data` in the root directory.
2. Place your dataset inside the `data` folder. Ensure it is structured as follows:
   - `data/train/`
     - `class1/`
     - `class2/`
     - ...
   - `data/test/`
     - `class1/`
     - `class2/`
     - ...


## Contributing

Pull requests are welcome. For major changes/errors, please open an issue to discuss and resolve it.

## License

[MIT License](LICENSE)


