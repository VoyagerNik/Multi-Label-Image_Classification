# Multi-Label-Image_Classification


This project provides a framework for multi-label image classification using a dynamic dataset. Users can apply this framework to their own dataset.

## Getting Started

1. Clone the repository: `git clone https://github.com/VoyagerNik/Multi-Label-Image-Classification.git`
2. Install requirements: `pip install -r requirements.txt`

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

## Usage

1. Train the model: `python src/model/train_model.py`
2. Use the trained model for predictions.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)

## Structure

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

