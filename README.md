# ImageMed Classifier YOLO-NAS

## Description
 ImageMed YOLO-NAS is a tool specialized in medical image classification and analysis. Using advanced YOLO and NAS algorithms

## Characteristics
- **Advanced Detection and Classification:** Use YOLO to identify key features in medical images.
- **Optimization with NAS:** Implement NAS techniques to optimize the architecture of neural networks.
- **Focus on Medical Imaging:** Specially designed for mammography, cervical imaging and others.

## Project Structure

Below is the project directory structure:
```
proyecto_yolo/
│
├── checkpoints/
│   └── class_mamma/       # Checkpoints are saved
│       └── class_ckpt /
|
├── config/
|
├── data/
│   ├── processed/
│   ├── raw/
│   ├── train/
│   ├── test/
│   └── valid/
|
├── logs/
│   └── tarining_logs/  # Logs are saved during training
│
├── models/      # the specific version of YOLO you are using
│
└── notebooks/
    └── yolo_nas_classifier/
        ├── 0.1_data_processing.ipynb  # Notebook for data processing
        ├── 0.2_Training.ipynb  # Notebook for the data training process
        ├── 0.3_evaluation.ipynb  # Notebook for model evaluation and data inference
        └── full_yolo_nas_class.ipynb   # Notebook containing all the sessions to develop a neural network
```


## Install
```
coockiecutter gh:cristianDaksha/ImageMed-Classifier-YOLO-NAS
```


to install cookiecutter
1. Conda

We create channel with conda
```
conda config --add channels conda-forge
```

Once the conda-forge channel has been enabled, cookiecutter can be installed with:
```
conda install cookiecutter
```

2. Pip

```
pip install cookiecutter
```

to install supergradients
```
pip install super-gradients==3.5.0
```
to install pytorch with cuda
```
pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/cu118
```