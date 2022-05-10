# COMP3931

## Simulation of ECG

#### Construction of non-linear dynamic model

File [ddefun.m](https://github.com/765218957/COMP3931/blob/main/simulated ECG/ddefun.m) is the handle to the `dde23()` function.

File [history.m](https://github.com/765218957/COMP3931/blob/main/simulated ECG/history.m) is the initial condition for the simulation.

#### Generation of atrial fibrillation ECG

File [main2.m](https://github.com/765218957/COMP3931/blob/main/simulated ECG/main2.m) is the calculation of the dde23 equation and the plotting of the AF image.

These picture show the final drawing result:

[AF.png](https://github.com/765218957/COMP3931/blob/main/simulated ECG/AF.png)

[AV.png](https://github.com/765218957/COMP3931/blob/main/simulated ECG/AV.png)

[HP.png](https://github.com/765218957/COMP3931/blob/main/simulated ECG/HP.png)

[SA.png](https://github.com/765218957/COMP3931/blob/main/simulated ECG/SA.png)

## Processing of training data

- File [generate_ECG_jpg.py](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/generate_ECG_jpg.py) is used for the processing of the data set:
- [generate_ECG_jpg.py: 20](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/generate_ECG_jpg.py#L57)  is used to read the wfdb data.
- [```denoise()```](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/generate_ECG_jpg.py#L11) is used to wavelet  denoise.
- [```find_peak()```](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/generate_ECG_jpg.py#L39) is used to find the index of qrs peaks.
- [generate_ECG_jpg.py: 64](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/generate_ECG_jpg.py#L11) is used to segment the ECG by heartbeat.
- [generate_ECG_jpg.py: 67](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/generate_ECG_jpg.py#L11) is used to Save the generated images.



[1.jpg](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/simulated_dataset/training/A/1.jpg) [2.jpg](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/simulated_dataset/training/A/2.jpg) [3.jpg](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/simulated_dataset/training/A/3.jpg) [4.jpg](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/simulated_dataset/training/A/4.jpg) [5.jpg](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/simulated_dataset/training/A/5.jpg) are the simulated ECG image after segmentation.

## CNN

[original_dataset](https://github.com/765218957/COMP3931/tree/main/CNN_ECG/original_dataset) is the original ECG dataset.

[simulated_dataset](https://github.com/765218957/COMP3931/tree/main/CNN_ECG/simulated_dataset)  simulated_dataset is the dataset with simulated ECG images added to the training set.



Both [original_dataset](https://github.com/765218957/COMP3931/tree/main/CNN_ECG/original_dataset) and [simulated_dataset](https://github.com/765218957/COMP3931/tree/main/CNN_ECG/simulated_dataset)  have a training set and a validation set folder, and each folder has four subfolders with images:

The "A" subfolder is for the AF ECG type, the "O" subfolder is for other ECG types, the "N" subfolder is for the normal ECG type, and The "~" subfolder is for Noisy ECG types.





[tensorflow_original_dataset.ipynb](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/tensorflow_original_dataset.ipynb)  uses original dataset for CNN training
[tensorflow_simulated_dataset.ipynb](https://github.com/765218957/COMP3931/blob/main/CNN_ECG/tensorflow_simulated_dataset.ipynb) uses data with simulated ECG dataset for CNN training