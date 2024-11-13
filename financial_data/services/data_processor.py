from typing import List
from sqlalchemy.engine import Engine
import pandas as pd
import yfinance as yf
from utils.db_utils import DatabaseConnection
from utils.data_utils import DataTransformer
from services.yahoo_finance import YahooFinanceService
from datetime import datetime


class DataProcessor:
    """Service for processing financial data."""
    
    @staticmethod
    def write_to_db(df: pd.DataFrame, table_name: str = 'annual_income_statements') -> bool:
        """Write DataFrame to database if record doesn't exist."""
        engine = DatabaseConnection.connect_to_db()
        if engine is None:
            return False
        
        try:
            for _, row in df.iterrows():
                exists = DatabaseConnection.check_duplicate_record(
                    engine, 
                    row['ticker'], 
                    row['report_date'], 
                    table_name
                )
                
                if not exists:
                    pd.DataFrame([row]).to_sql(
                        name=table_name,
                        con=engine,
                        if_exists='append',
                        index=False,
                        schema='public'
                    )
                    print(f"Added record for {row['ticker']} on {row['report_date']}")
                else:
                    print(f"Skipped duplicate record for {row['ticker']} on {row['report_date']}")
                    
            return True
        except Exception as e:
            print(f"Error writing to database: {e}")
            return False
        finally:
            engine.dispose()

    @staticmethod
    def write_metrics_to_db(df: pd.DataFrame) -> bool:
        """Write stock metrics DataFrame to database."""
        engine = DatabaseConnection.connect_to_db()
        if engine is None:
            return False
        
        try:
            if 'ticker' not in df.columns and 'symbol' in df.columns:
                df['ticker'] = df['symbol']

            if 'ticker' not in df.columns or 'report_date' not in df.columns:
                print("Missing required columns 'ticker' or 'report_date'")
                return False

            for _, row in df.iterrows():
                exists = DatabaseConnection.check_duplicate_record(
                    engine, 
                    row['ticker'], 
                    row['report_date'], 
                    'stock_metrics'
                )
                
                if not exists:
                    row_df = pd.DataFrame([row])
                    row_df.to_sql(
                        name='stock_metrics',
                        con=engine,
                        if_exists='append',
                        index=False,
                        schema='public'
                    )
                    print(f"Added stock metrics for {row['ticker']} on {row['report_date']}")
                else:
                    print(f"Skipped duplicate stock metrics for {row['ticker']} on {row['report_date']}")
                    
            return True
        except Exception as e:
            print(f"Error writing metrics to database: {e}")
            return False
        finally:
            engine.dispose()
    
    @staticmethod
    def process_ticker(ticker: str, data_types: List[str], engine: Engine) -> None:
        """Process a single ticker for specified data types."""
        try:
            company = yf.Ticker(ticker)
            
            for data_type in data_types:
                print(f"Processing {data_type} for {ticker}")
                
                data = YahooFinanceService.get_company_data(company, data_type)
                table_name = YahooFinanceService.get_table_name(data_type)
                
                if data is None or table_name is None:
                    print(f"Skipping invalid data type: {data_type}")
                    continue
                
                table_columns = DatabaseConnection.get_table_columns(engine, table_name)
                if not table_columns:
                    print(f"Could not get columns for table {table_name}")
                    continue
                
                df = DataTransformer.transpose_data(ticker, data, table_columns)
                success = DataProcessor.write_to_db(df, table_name=table_name)
                
                if success:
                    print(f"Successfully processed {data_type} for {ticker}")
                else:
                    print(f"Failed to process {data_type} for {ticker}")
                    
        except Exception as e:
            print(f"Error processing ticker {ticker}: {e}")
              
    @staticmethod
    def process_stock_metrics(ticker: str, engine: Engine) -> None:
        """
        Process stock metrics for a single ticker.
        
        Args:
            ticker (str): Stock ticker symbol
            engine (Engine): SQLAlchemy database engine
        """
        try:
            print(f"Processing stock metrics for {ticker}")
            
            stock = yf.Ticker(ticker)
            info = stock.info
            
            if not info:
                print(f"No metrics found for {ticker}")
                return
            
            metrics = { 
                'ticker': ticker,
                'report_date': datetime.now().date(),
                'company_name': info.get('longName'),
                'exchange': info.get('exchange'),
                'currency': info.get('financialCurrency'),
                'current_price': info.get('currentPrice'),
                'previous_close': info.get('previousClose'),
                'open_price': info.get('open'),
                'day_low': info.get('dayLow'),
                'day_high': info.get('dayHigh'),
                'regular_market_previous_close': info.get('regularMarketPreviousClose'),
                'regular_market_open': info.get('regularMarketOpen'),
                'regular_market_day_low': info.get('regularMarketDayLow'),
                'regular_market_day_high': info.get('regularMarketDayHigh'),
                'dividend_rate': info.get('dividendRate'),
                'dividend_yield': info.get('dividendYield'),
                'ex_dividend_date': info.get('exDividendDate'),
                'payout_ratio': info.get('payoutRatio'),
                'five_year_avg_dividend_yield': info.get('fiveYearAvgDividendYield'),
                'beta': info.get('beta'),
                'trailing_pe': info.get('trailingPE'),
                'forward_pe': info.get('forwardPE'),
                'volume': info.get('volume'),
                'regular_market_volume': info.get('regularMarketVolume'),
                'average_volume': info.get('averageVolume'),
                'average_volume_10days': info.get('averageVolume10days'),
                'average_daily_volume_10day': info.get('averageDailyVolume10Day'),
                'bid': info.get('bid'),
                'ask': info.get('ask'),
                'bid_size': info.get('bidSize'),
                'ask_size': info.get('askSize'),
                'market_cap': info.get('marketCap'),
                'fifty_two_week_low': info.get('fiftyTwoWeekLow'),
                'fifty_two_week_high': info.get('fiftyTwoWeekHigh'),
                'price_to_sales_trailing_12months': info.get('priceToSalesTrailing12Months'),
                'fifty_day_average': info.get('fiftyDayAverage'),
                'two_hundred_day_average': info.get('twoHundredDayAverage'),
                'trailing_annual_dividend_rate': info.get('trailingAnnualDividendRate'),
                'trailing_annual_dividend_yield': info.get('trailingAnnualDividendYield'),
                'enterprise_value': info.get('enterpriseValue'),
                'profit_margins': info.get('profitMargins'),
                'float_shares': info.get('floatShares'),
                'shares_outstanding': info.get('sharesOutstanding'),
                'shares_short': info.get('sharesShort'),
                'shares_short_prior_month': info.get('sharesShortPriorMonth'),
                'shares_short_previous_month_date': info.get('sharesShortPreviousMonthDate'),
                'date_short_interest': info.get('dateShortInterest'),
                'shares_percent_shares_out': info.get('sharesPercentSharesOut'),
                'held_percent_insiders': info.get('heldPercentInsiders'),
                'held_percent_institutions': info.get('heldPercentInstitutions'),
                'short_ratio': info.get('shortRatio'),
                'short_percent_of_float': info.get('shortPercentOfFloat'),
                'book_value': info.get('bookValue'),
                'price_to_book': info.get('priceToBook'),
                'earnings_quarterly_growth': info.get('earningsQuarterlyGrowth'),
                'net_income_to_common': info.get('netIncomeToCommon'),
                'trailing_eps': info.get('trailingEps'),
                'forward_eps': info.get('forwardEps'),
                'peg_ratio': info.get('pegRatio'),
                'last_split_factor': info.get('lastSplitFactor'),
                'last_split_date': info.get('lastSplitDate'),
                'enterprise_to_revenue': info.get('enterpriseToRevenue'),
                'enterprise_to_ebitda': info.get('enterpriseToEbitda'),
                'last_dividend_value': info.get('lastDividendValue'),
                'last_dividend_date': info.get('lastDividendDate'),
                'target_high_price': info.get('targetHighPrice'),
                'target_low_price': info.get('targetLowPrice'),
                'target_mean_price': info.get('targetMeanPrice'),
                'target_median_price': info.get('targetMedianPrice'),
                'recommendation_mean': info.get('recommendationMean'),
                'recommendation_key': info.get('recommendationKey'),
                'number_of_analyst_opinions': info.get('numberOfAnalystOpinions'),
                'total_cash': info.get('totalCash'),
                'total_cash_per_share': info.get('totalCashPerShare'),
                'ebitda': info.get('ebitda'),
                'total_debt': info.get('totalDebt'),
                'quick_ratio': info.get('quickRatio'),
                'current_ratio': info.get('currentRatio'),
                'debt_to_equity': info.get('debtToEquity'),
                'revenue_per_share': info.get('revenuePerShare'),
                'return_on_assets': info.get('returnOnAssets'),
                'return_on_equity': info.get('returnOnEquity'),
                'free_cashflow': info.get('freeCashflow'),
                'operating_cashflow': info.get('operatingCashflow'),
                'earnings_growth': info.get('earningsGrowth'),
                'revenue_growth': info.get('revenueGrowth'),
                'gross_margins': info.get('grossMargins'),
                'ebitda_margins': info.get('ebitdaMargins'),
                'operating_margins': info.get('operatingMargins'),
                'trailing_peg_ratio': info.get('trailingPegRatio')
            }
            
            df = pd.DataFrame([metrics])
            df['report_date'] = pd.to_datetime(df['report_date']).dt.date
            success = DataProcessor.write_to_db(df, table_name='stock_metrics')
            
            if success:
                print(f"Successfully processed stock metrics for {ticker}")
            else:
                print(f"Failed to process stock metrics for {ticker}")
                
        except Exception as e:
            print(f"Error processing stock metrics for {ticker}: {e}")


