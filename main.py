import numpy as np

from backend.core import SignalData
from signals import ECGAnalyzer


def main():
    # Example: create fake ECG-like data (just for testing)
    fs = 250  # sampling frequency in Hz
    duration_seconds = 5
    n_samples = fs * duration_seconds

    # Fake signal (random for now) - later you will load real ECG from file
    samples = np.random.randn(n_samples)

    # Wrap into SignalData object
    signal_data = SignalData(samples=samples, fs=fs)

    # Create ECG analyzer
    analyzer = ECGAnalyzer(signal_data)

    # Run preprocessing and analysis
    analyzer.preprocess()
    analyzer.analyze()

    # Get and print results
    results = analyzer.get_results()
    print("ECG analysis results:")
    for key, value in results.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
