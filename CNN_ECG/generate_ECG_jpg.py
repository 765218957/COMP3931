import wfdb
import numpy as np
import matplotlib.pyplot as plt
import pywt
import csv
import os
from wfdb import processing
import datetime


def denoise(ecg):
    index = []
    data = []
    for i in range(len(ecg) - 1):
        X = float(i)
        Y = float(ecg[i])
        index.append(X)
        data.append(Y)

    # Create wavelet object and define parameters.
    w = pywt.Wavelet('db8')  # Select Daubechies8 wavelets
    maxlev = pywt.dwt_max_level(len(data), w.dec_len)
    threshold = 0.04  # Threshold for filtering

    # Decompose into wavelet components up to the selected level.
    coeffs = pywt.wavedec(data, 'db8', level=maxlev)  # Wavelet decomposition of the signal

    plt.figure()
    for i in range(1, len(coeffs)):
        coeffs[i] = pywt.threshold(coeffs[i], threshold * max(coeffs[i]))  # Filtering out the noise

    datarec = pywt.waverec(coeffs, 'db8')  # Wavelet reconstruction of the signal

    mintime = 0
    maxtime = mintime + len(data) + 1
    return data, datarec


def find_peak(record):
    # Use the GQRS algorithm to detect QRS locations in the first channel
    qrs_inds = processing.qrs.gqrs_detect(sig=record.p_signal[:, 0], fs=record.fs)

    # Correct the peaks shifting them to local maxima
    max_bpm = 230
    # Use the maximum possible bpm as the search radius
    search_radius = int(record.fs * 60 / max_bpm)
    corrected_peak_inds = processing.peaks.correct_peaks(record.p_signal[:, 0],
                                                         peak_inds=qrs_inds,
                                                         search_radius=search_radius,
                                                         smooth_window_size=150)

    return sorted(corrected_peak_inds)


def get_data(file_addr, type_addr):
    print("reading " + file_addr + " data....")
    # Read wfdb files
    record = wfdb.rdrecord("training2017/" + file_addr, sampfrom=0)
    try:
        peak_index = find_peak(record)
        ecg_data = record.p_signal.flatten()
        data, datarec = denoise(ecg_data)
        # Select heartbeat segment
        signal_beat = datarec[peak_index[5]:peak_index[10]]
        plt.plot(signal_beat)
        # Save to specified path
        plt.savefig("training/" + type_addr + "/" + file_addr + ".jpg")
        plt.close()
        print("saved " + "training/" + type_addr + "/" + file_addr + ".jpg")
    except IndexError as e:
        print("except", e)


def save_ecg():
    # read csv file
    with open("training2017/REFERENCE.csv") as f:
        reader = csv.reader(f)
        # The first row is the name of the file and the second row is the type of ECG.
        for row in reader:
            file_addr = row[0]
            type_addr = row[1]
            get_data(file_addr, type_addr)


if __name__ == '__main__':
    save_ecg()
