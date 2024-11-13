import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

class DatabaseConfig:
    """Database configuration settings."""
    
    @staticmethod
    def get_db_params():
        """Get database connection parameters from environment variables."""
        return {
            'host': os.getenv('DB_HOST'),
            'database': os.getenv('DB_NAME'),                     
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'port': os.getenv('DB_PORT', '5432')
        }

    @staticmethod
    def create_connection_string(db_params):
        """Create database connection string."""
        return f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"


