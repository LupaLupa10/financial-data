# main.py
from utils.db_utils import DatabaseConnection
from services.data_processor import DataProcessor
from data_args import DataArgs

def main():
    """Main execution function."""
    args = DataArgs.parse_arguments()
    tickers, data_types = DataArgs.process_args(args)

    try:
        engine = DatabaseConnection.connect_to_db()
        if not engine:
            raise ValueError("Could not connect to database")

        for ticker in tickers:
            # Split processing between stock_metrics and other data types
            if 'stock_metrics' in data_types:
                # Process stock metrics directly without transformation
                DataProcessor.process_stock_metrics(ticker, engine)
                
                # Get other data types (excluding stock_metrics)
                other_types = [dt for dt in data_types if dt != 'stock_metrics']
                
                # Process other data types if any exist
                if other_types:
                    DataProcessor.process_ticker(ticker, other_types, engine)
            else:
                # If no stock_metrics, use regular processing
                DataProcessor.process_ticker(ticker, data_types, engine)

    except Exception as e:
        print(f"Error in main execution: {e}")
    finally:
        if engine:
            engine.dispose()

if __name__ == "__main__":
    main()