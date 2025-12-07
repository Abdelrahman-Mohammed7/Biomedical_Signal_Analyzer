import numpy as np

from backend.core import SignalData, BaseSignalAnalyzer
from backend.core import preprocessing as pp


class ECGAnalyzer(BaseSignalAnalyzer):
    """
    ECG analyzer:
    - preprocess(): filtering and noise removal
    - analyze(): extract basic features (later: heart rate, RR intervals, etc.)
    """

    def __init__(self, signal_data: SignalData):
        super().__init__(signal_data)

    def preprocess(self):
        """Apply basic ECG preprocessing: bandpass + notch + baseline removal."""
        fs = self.signal_data.fs
        x = self.signal_data.samples

        # Convert to numpy array if needed
        x = np.asarray(x)

        # Basic filters (you can adjust values later)
        # 0.5–40 Hz bandpass for ECG
        x = pp.bandpass_filter(x, low=0.5, high=40.0, fs=fs)

        # Notch filter at 50 Hz (or 60 Hz depending on your power line)
        x = pp.notch_filter(x, freq=50.0, fs=fs)

        # Remove baseline wander
        x = pp.remove_baseline(x, fs=fs, cutoff=0.5)

        # Save back the cleaned signal
        self.signal_data.samples = x

    def analyze(self):
        """
        Temporary simple analysis:
        Later we will add:
        - R-peak detection
        - Heart rate
        - RR intervals
        For now, we just compute basic stats.
        """
        x = np.asarray(self.signal_data.samples)

        self.results["mean_value"] = float(np.mean(x))
        self.results["max_value"] = float(np.max(x))
        self.results["min_value"] = float(np.min(x))
