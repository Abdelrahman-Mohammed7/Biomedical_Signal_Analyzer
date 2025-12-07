class SignalData:
    """
    A simple container for signal data.
    """

    def __init__(self, samples, fs, channels=None):
        """
        samples: 1D or 2D array-like, the signal values
        fs: sampling frequency (Hz)
        channels: optional list of channel names
        """
        self.samples = samples
        self.fs = fs
        self.channels = channels

    def duration_seconds(self):
        """Return the duration of the signal in seconds."""
        if self.samples is None:
            return 0
        # assume samples is 1D or 2D (time x channels)
        n_samples = len(self.samples)
        return n_samples / float(self.fs)
