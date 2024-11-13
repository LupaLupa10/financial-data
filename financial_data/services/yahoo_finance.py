import yfinance as yf
import pandas as pd
from typing import Optional, Dict, Any
from datetime import datetime


class YahooFinanceService:
    """Service for interacting with Yahoo Finance API."""
    
    @staticmethod
    def get_company_data(ticker_obj: yf.Ticker, data_type: str) -> Optional[pd.DataFrame]:
        """Fetch specific financial data type from yfinance Ticker object."""
        data_mapping = {
            'annual_income': ticker_obj.financials,
            'quarterly_income': ticker_obj.quarterly_financials,
            'annual_balance': ticker_obj.balance_sheet,
            'quarterly_balance': ticker_obj.quarterly_balance_sheet,
            'annual_cashflow': ticker_obj.cashflow,
            'quarterly_cashflow': ticker_obj.quarterly_cashflow,
            'actions': ticker_obj.actions,
            'calendar': ticker_obj.calendar,
            'recommendations': ticker_obj.recommendations,
            'upgrades_downgrades': ticker_obj.upgrades_downgrades,
            'news': pd.DataFrame(ticker_obj.news),
            'stock_metrics': YahooFinanceService._get_stock_metrics(ticker_obj)
        }
        
        try:
            data = data_mapping.get(data_type)
            if data is not None and not data.empty:
                return data
            else:
                print(f"No data available for {data_type}")
                return None
        except Exception as e:
            print(f"Error fetching {data_type} data: {e}")
            return None

    @staticmethod
    def get_table_name(data_type: str) -> Optional[str]:
        """Map data type to corresponding database table name."""
        table_mapping = {
            'annual_income': 'annual_income_statements',
            'quarterly_income': 'quarterly_income_statements',
            'annual_balance': 'annual_balance_sheet',
            'quarterly_balance': 'quarterly_balance_sheet',
            'annual_cashflow': 'annual_cash_flow',
            'quarterly_cashflow': 'quarterly_cash_flow',
            'actions': 'stock_actions',
            'calendar': 'earnings_calendar',
            'recommendations': 'analyst_recommendations',
            'upgrades_downgrades': 'upgrades_downgrades',
            'news': 'company_news',
            'stock_metrics': 'stock_metrics'
        }
        return table_mapping.get(data_type)
    
    @staticmethod
    def _get_stock_metrics(ticker_obj: yf.Ticker) -> pd.DataFrame:
        """
        Extract stock metrics from ticker object and format as DataFrame.
        
        Args:
            ticker_obj: yfinance Ticker object
            
        Returns:
            pd.DataFrame: DataFrame containing stock metrics
        """
        try:
            info = ticker_obj.info
            if not info:
                return pd.DataFrame()

            metrics = {
                'report_date': datetime.now().date(), 
                'symbol': info.get('symbol'),
                'company_name': info.get('longName'),
                'exchange': info.get('exchange'),
                'currency': info.get('financialCurrency'),
                'current_price': info.get('currentPrice'),
                'previous_close': info.get('previousClose'),
                'open': info.get('open'),
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
            return pd.DataFrame([metrics])

        except Exception as e:
            print(f"Error extracting stock metrics: {e}")
            return pd.DataFrame()