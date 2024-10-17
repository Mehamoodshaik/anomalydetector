#AnomalyDetector.py
import numpy as np

class AnomalyDetector:
    def __init__(self, sliding_window_size=20, number_of_standard_deviations=3):
        """
        Initialize the AnomalyDetector class with a sliding window size and threshold 
        based on the number of standard deviations.
        """
        self.sliding_window_size = sliding_window_size  # The size of the sliding window used for analysis
        self.number_of_standard_deviations = number_of_standard_deviations  # Threshold in terms of standard deviations
        self.prices = []  # List to hold the sliding window of prices

    def update(self, value):
        """
        Update the sliding window with a new price and check if it is an anomaly.
        
        :param value: New price to be added to the window
        :return: True if the value is an anomaly, False otherwise
        """
        self.prices.append(value)  # Add the new value to the prices list
        
        # If the list exceeds the sliding window size, remove the oldest price
        if len(self.prices) > self.sliding_window_size:
            self.prices.pop(0)
        
        # If there aren't enough data points to perform analysis, return False
        if len(self.prices) < self.sliding_window_size:
            return False
        
        # Calculate the mean and standard deviation of the current sliding window
        mean = np.mean(self.prices)
        standard_deviation = np.std(self.prices)
        
        # Define the upper and lower bounds for anomaly detection
        upper_half = mean + (self.number_of_standard_deviations * standard_deviation)
        lower_half = mean - (self.number_of_standard_deviations * standard_deviation)
        
        # Return True if the value is outside the normal range, indicating an anomaly
        return value > upper_half or value < lower_half
