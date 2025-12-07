import numpy as np
from scipy.signal import butter, filtfilt, iirnotch


def bandpass_filter(signal, low, high, fs, order=4):
    """
    Apply a Butterworth bandpass filter.

    signal: 1D numpy array
    low: low cutoff frequency (Hz)
    high: high cutoff frequency (Hz)
    fs: sampling frequency (Hz)
    order: filter order
    """
    nyq = 0.5 * fs
    low_norm = low / nyq
    high_norm = high / nyq
    b, a = butter(order, [low_norm, high_norm], btype="band")
    filtered = filtfilt(b, a, signal)
    return filtered


def notch_filter(signal, freq, fs, quality=30.0):
    """
    Apply a notch filter to remove a specific frequency (e.g. 50 or 60 Hz).

    freq: notch frequency (Hz)
    fs: sampling frequency (Hz)
    quality: quality factor (Q)
    """
    nyq = 0.5 * fs
    w0 = freq / nyq
    b, a = iirnotch(w0, quality)
    filtered = filtfilt(b, a, signal)
    return filtered


def remove_baseline(signal, fs, cutoff=0.5, order=2):
    """
    Remove slow baseline wander using a high-pass filter.

    cutoff: cutoff frequency (Hz)
    """
    nyq = 0.5 * fs
    cutoff_norm = cutoff / nyq
    b, a = butter(order, cutoff_norm, btype="high")
    filtered = filtfilt(b, a, signal)
    return filtered
