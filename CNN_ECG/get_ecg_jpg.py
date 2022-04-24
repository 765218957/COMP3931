import wfdb
import numpy as np
import matplotlib.pyplot as plt
import pywt
import csv
import os
from wfdb import processing
import datetime


def denoise(data):

    coeffs = pywt.wavedec(data=data, wavelet='db5', level=9)
    cA9, cD9, cD8, cD7, cD6, cD5, cD4, cD3, cD2, cD1 = coeffs

    threshold = (np.median(np.abs(cD1)) / 0.6745) * (np.sqrt(2 * np.log(len(cD1))))
    cD1.fill(0)
    cD2.fill(0)
    for i in range(1, len(coeffs) - 2):
        coeffs[i] = pywt.threshold(coeffs[i], threshold)

    rdata = pywt.waverec(coeffs=coeffs, wavelet='db5')
    return rdata


def find_peak(record):
    #     record = wfdb.rdrecord(file_addr, sampfrom=0)

    # Use the GQRS algorithm to detect QRS locations in the first channel
    qrs_inds = processing.qrs.gqrs_detect(sig=record.p_signal[:, 0], fs=record.fs)

    # Correct the peaks shifting them to local maxima
    min_bpm = 20
    max_bpm = 230
    # min_gap = record.fs * 60 / min_bpm
    # Use the maximum possible bpm as the search radius
    search_radius = int(record.fs * 60 / max_bpm)
    corrected_peak_inds = processing.peaks.correct_peaks(record.p_signal[:, 0],
                                                         peak_inds=qrs_inds,
                                                         search_radius=search_radius,
                                                         smooth_window_size=150)

    return sorted(corrected_peak_inds)


def get_data(file_addr, type_addr):
    print("reading " + file_addr + " data....")
    record = wfdb.rdrecord("validation/" + file_addr, sampfrom=0)
    try:
        peak_index = find_peak(record)
        data = record.p_signal.flatten()
        rdata = denoise(data=data)
        #     start = 10
        #     end = 5
        #     i = start
        #     j = len(peak_index) - end

        signal_beat = rdata[peak_index[5]:peak_index[10]]
        plt.plot(signal_beat)
        plt.savefig("valida/" + type_addr + "/" + file_addr + ".jpg")
        plt.close()
        print("saved " + "train/" + type_addr + "/" + file_addr + ".jpg")
    except IndexError as e:
        print("except", e)


def save_ecg():
    # read csv file
    with open("validation/REFERENCE.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            file_addr = row[0]
            type_addr = row[1]
            get_data(file_addr, type_addr)


if __name__ == '__main__':
    save_ecg()
