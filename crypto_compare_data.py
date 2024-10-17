#crypto_compare_data.py
import requests
import time

class CryptoCompareData:
    def __init__(self, symbol="BTC", currency="USD", retries=5, retry_wait=5):
        """
        Initialize the CryptoCompareData class with the desired cryptocurrency symbol and currency.
        Define the number of retries and wait time in case of a failed request.
        
        :param symbol: Cryptocurrency symbol (e.g., 'BTC' for Bitcoin)
        :param currency: Target currency for conversion (e.g., 'USD')
        :param retries: Number of retry attempts on failure
        :param retry_wait: Waiting time (in seconds) between retries
        """
        self.symbol = symbol  # Cryptocurrency symbol (e.g., 'BTC' for Bitcoin)
        self.currency = currency  # Target currency (e.g., 'USD')
        self.retries = retries  # Maximum number of retries for failed API requests
        self.retry_wait = retry_wait  # Wait time (in seconds) between retries

    def get_latest_price(self):
        """
        Fetch the latest price of the cryptocurrency in the specified currency from CryptoCompare API.
        If the request fails, it will retry based on the retry count and retry wait settings.
        
        :return: The latest price as a float, or None if the request fails.
        """
        for _ in range(self.retries):  # Attempt to fetch data, retrying on failure
            try:
                # API endpoint to fetch the latest price for the specified cryptocurrency and currency
                url = f"https://min-api.cryptocompare.com/data/price?fsym={self.symbol}&tsyms={self.currency}"
                response = requests.get(url, timeout=10)  # Make a GET request with a timeout of 10 seconds
                response.raise_for_status()  # Raise an exception for unsuccessful status codes
                data = response.json()  # Parse the JSON response
                
                # Check if the target currency is in the response and return the price
                if self.currency in data:
                    return float(data[self.currency])
                else:
                    raise ValueError(f"Currency '{self.currency}' not found in API response.")
            except (requests.exceptions.RequestException, ValueError) as e:
                # Print an error message if the request fails and wait before retrying
                print("Attempt Failed")
                time.sleep(self.retry_wait)
        
        # After retrying, print an error message if the data couldn't be fetched
        print(f"Error fetching data from CryptoCompare for {self.symbol}/{self.currency}: {e}")
        return None  # Return None if all retries fail

    def start_stream(self):
        """
        Continuously fetch the latest price of the cryptocurrency at regular intervals.
        Prints the latest price every second.
        """
        while True:
            price = self.get_latest_price()  # Get the latest price
            if price:  # If a valid price is returned, print it
                print(f"Current price of {self.symbol}/{self.currency}: {price}")
            time.sleep(1)  # Wait for 1 second before fetching the next update
