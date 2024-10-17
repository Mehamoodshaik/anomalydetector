# Cryptocurrency Price Anomaly Detection

This project monitors the real-time price of a cryptocurrency (e.g., Bitcoin) and detects anomalies in the price using statistical methods. It fetches price data from the CryptoCompare API, processes it with an anomaly detection algorithm, and visualizes the data in real-time using `matplotlib`.

## Features

- **Real-time Data Fetching:** Fetches cryptocurrency price data from the [CryptoCompare API](https://min-api.cryptocompare.com/).
- **Anomaly Detection:** Detects anomalies in the price data using a sliding window and standard deviation-based detection.
- **Real-time Visualization:** Displays a live plot of the cryptocurrency prices, highlighting detected anomalies in red.

## Files

- **`AnomalyDetector.py`**: Contains the `AnomalyDetector` class, which checks if a new price is an anomaly based on statistical analysis (mean and standard deviation).
- **`crypto_compare_data.py`**: Contains the `CryptoCompareData` class, which fetches the latest cryptocurrency prices from the CryptoCompare API.
- **`visualization.py`**: Handles the real-time plotting and visualization of prices and anomalies.
- **`main.py`**: The entry point of the project that sets up the data stream, anomaly detector, and visualization.

## Dependencies

- Python 3.x
- `matplotlib` for plotting and visualization
- `numpy` for statistical analysis
- `requests` for fetching data from the API

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## How it Works

1. **CryptoCompare API Integration**: 
   The `CryptoCompareData` class in `crypto_compare_data.py` fetches the current price of a cryptocurrency (e.g., Bitcoin) in a specific currency (e.g., USD).

2. **Anomaly Detection**:
   The `AnomalyDetector` class in `AnomalyDetector.py` monitors the fetched prices and identifies anomalies. An anomaly is defined as a price that deviates from the mean by more than a specified number of standard deviations within a sliding window of previous prices.

3. **Real-Time Visualization**:
   In `visualization.py`, the fetched prices and detected anomalies are plotted in real-time using `matplotlib`. Anomalies are highlighted as red points on the plot.

4. **Main Program**:
   The `main.py` file ties everything together by setting up the data stream, anomaly detection, and real-time plotting.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/mehamoodshaik/anomalydetector.git
   cd anomalydetector
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python main.py
   ```

The program will start fetching real-time cryptocurrency price data, detect anomalies, and plot the prices along with anomaly markers in real-time.

## Customization

- **Cryptocurrency Symbol**: You can change the cryptocurrency symbol and currency in the `main.py` file. For example, to fetch Ethereum (ETH) prices in USD, modify:
  ```python
  symbol = "ETH"
  currency = "USD"
  ```

- **Sliding Window Size and Standard Deviation Threshold**: You can change the parameters for anomaly detection in the `AnomalyDetector` class in `main.py`:
  ```python
  detector = AnomalyDetector(sliding_window_size=30, number_of_standard_deviations=2)
  ```


## Algorithm: Sliding Window with Standard Deviation for Anomaly Detection

This project uses a **sliding window** anomaly detection algorithm based on statistical measures of central tendency (mean) and variability (standard deviation). Here's how it works:

- A **sliding window** of a fixed size (e.g., 20 recent data points) is maintained, containing the latest cryptocurrency prices.
- The algorithm calculates the **mean** and **standard deviation** of the prices within this window.
- Prices are classified as **anomalies** if they fall outside of a pre-defined threshold. This threshold is set as a certain number of standard deviations away from the mean. In this case, 3 standard deviations are used, which captures the majority of data in a normal distribution (99.7%).

### Why This Algorithm?
- This method is simple yet effective for detecting sudden price spikes or drops in a data stream.
- It dynamically adjusts based on recent price data, making it well-suited for real-time monitoring.
- By leveraging standard deviation, the algorithm accounts for natural variations in the data while identifying points that are statistically uncommon.

The sliding window approach allows the system to focus on the most recent price movements, which is crucial for timely detection in volatile markets like cryptocurrency.



## Acknowledgements

- The price data is fetched using the [CryptoCompare API](https://min-api.cryptocompare.com/).
- Visualization is handled using `matplotlib`, a Python plotting library.
  
