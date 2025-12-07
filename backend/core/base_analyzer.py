from .signal_data import SignalData


class BaseSignalAnalyzer:
    """
    Base class for all signal analyzers (ECG, EEG, EMG, EOG).
    Every specific analyzer will inherit from this class.
    """

    def __init__(self, signal_data: SignalData):
        self.signal_data = signal_data
        self.results = {}

    def preprocess(self):
        """
        Apply preprocessing steps (filtering, noise removal, etc.).
        Must be implemented in child classes.
        """
        raise NotImplementedError("preprocess() must be implemented in child class")

    def analyze(self):
        """
        Extract features from the signal.
        Must be implemented in child classes.
        """
        raise NotImplementedError("analyze() must be implemented in child class")

    def get_results(self):
        """Return results as a dictionary (key -> value)."""
        return self.results
