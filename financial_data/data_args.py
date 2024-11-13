import argparse
from typing import Tuple, List

class DataArgs:
    """Command-line interface handler."""
    
    @staticmethod
    def parse_arguments() -> argparse.Namespace:
        """Parse command line arguments."""
        parser = argparse.ArgumentParser(description='Fetch and store financial data from Yahoo Finance')
        
        parser.add_argument(
            '--tickers',
            type=str,
            required=True,
            help='Comma-separated list of stock tickers (e.g., TSLA,AAPL,MSFT)'
        )
        
        parser.add_argument(
            '--data-types',
            type=str,
            required=True,
            help='Comma-separated list of data types to fetch'
        )
        
        return parser.parse_args()
    
    @staticmethod
    def process_args(args: argparse.Namespace) -> Tuple[List[str], List[str]]:
        """Process and validate command line arguments."""
        tickers = [ticker.strip() for ticker in args.tickers.split(',')]
        data_types = [dtype.strip() for dtype in args.data_types.split(',')]
        return tickers, data_types
