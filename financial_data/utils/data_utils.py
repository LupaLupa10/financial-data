import pandas as pd
from typing import List

class DataTransformer:
    """Data transformation utilities."""
    
    @staticmethod
    def transpose_data(ticker: str, df: pd.DataFrame, table_columns: List[str]) -> pd.DataFrame:
        """Transpose the metrics to column names, and report date to row names."""
        df_transposed = (df.transpose()
                        .reset_index()
                        .rename(columns={'index': 'report_date'})
                        .assign(ticker=ticker))
        
        df_transposed.columns = (df_transposed.columns
                               .str.strip()
                               .str.replace(' ', '_')
                               .str.replace(',', '')
                               .str.replace('&', 'and')
                               .str.lower())
        
        df_transposed['report_date'] = pd.to_datetime(df_transposed['report_date']).dt.date
        
        # Handle invalid and missing columns
        invalid_columns = [col for col in df_transposed.columns if col not in table_columns]
        if invalid_columns:
            print(f"Dropping invalid columns: {invalid_columns}")
            df_transposed = df_transposed.drop(columns=invalid_columns)
        
        missing_columns = [col for col in table_columns if col not in df_transposed.columns]
        if missing_columns:
            print(f"Adding missing columns: {missing_columns}")
            for col in missing_columns:
                df_transposed[col] = None
        
        return df_transposed[table_columns]