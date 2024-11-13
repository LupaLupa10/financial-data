from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine import Engine
from typing import List, Optional
from config.database import DatabaseConfig

class DatabaseConnection:
    """Database connection utilities."""
    
    @staticmethod
    def connect_to_db() -> Optional[Engine]:
        """Create database connection."""
        try:
            db_params = DatabaseConfig.get_db_params()
            connection_string = DatabaseConfig.create_connection_string(db_params)
            engine = create_engine(connection_string)
            return engine
        except SQLAlchemyError as e:
            print(f"Database connection error: {e}")
            return None

    @staticmethod
    def get_table_columns(engine: Engine, table_name: str) -> Optional[List[str]]:
        """Get column names from database table."""
        try:
            query = text("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name = :table_name 
                ORDER BY ordinal_position;
            """)
            
            with engine.connect() as conn:
                result = conn.execute(query, {"table_name": table_name})
                columns = [row[0] for row in result]
                return columns
        except SQLAlchemyError as e:
            print(f"Error getting table columns: {e}")
            return None

    @staticmethod
    def check_duplicate_record(engine: Engine, ticker: str, report_date: str, table: str) -> bool:
        """Check if record already exists in database."""
        try:
            query = text(f"""
                SELECT EXISTS (
                    SELECT 1
                    FROM {table}
                    WHERE ticker = :ticker
                    AND report_date = :report_date
                )
            """)
            
            with engine.connect() as conn:
                result = conn.execute(query, {"ticker": ticker, "report_date": report_date})
                return result.scalar()
        except SQLAlchemyError as e:
            print(f"Error checking for duplicate record: {e}")
            return False