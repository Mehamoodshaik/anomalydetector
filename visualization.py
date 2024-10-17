#visualization.py
import matplotlib.pyplot as plt

# Global variables for visualization
prices = []
anomalies = []

def update_plot(i, crypto_stream, detector):
    # Fetch the latest price
    price = crypto_stream.get_latest_price()
    
    if price:
        prices.append(price)
        # Detect anomaly
        is_anomaly = detector.update(price)
        anomalies.append(is_anomaly)
        print(f"Current price: {price} - Anomaly: {is_anomaly}")

        # Limit the number of data points displayed to avoid memory overload
        if len(prices) > 100:
            prices.pop(0)
            anomalies.pop(0)

        # Clear the plot
        plt.cla()

        # Plot prices
        plt.plot(prices, label="Price")

        # Track if anomaly label has been added
        anomaly_label_added = False

        # Highlight anomalies
        for idx, anomaly in enumerate(anomalies):
            if anomaly:
                if not anomaly_label_added:
                    plt.scatter(idx, prices[idx], color='red', label="Anomaly", zorder=2)
                    anomaly_label_added = True  # Only add the label once
                else:
                    plt.scatter(idx, prices[idx], color='red', zorder=2)  # No label

        # Add labels and formatting
        plt.title('Real-time Cryptocurrency Prices with Anomalies')
        plt.xlabel('Time (intervals)')
        plt.ylabel('Price (USD)')
        plt.legend()