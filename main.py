#main.py
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from crypto_compare_data import CryptoCompareData
from AnomalyDetector import AnomalyDetector
from visualization import update_plot


def main():
    symbol = "BTC"
    currency = "USD"
    
    # Initialize data stream
    crypto_stream = CryptoCompareData(symbol, currency)
    
    # Initialize anomaly detector
    detector = AnomalyDetector(sliding_window_size=20, number_of_standard_deviations=3)

    # Set up the plot
    fig = plt.figure()

    # Create an animated plot
    ani = FuncAnimation(fig, update_plot, fargs=(crypto_stream, detector), interval=1000)

    # Show the plot
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()





