# Financial Data Collector

A Python tool for collecting and storing financial data from Yahoo Finance.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/LupaLupa10/financial-data.git
```

2. Navigate to the project directory:
```bash
cd financial_data
```

3. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

4. Install dependencies using Poetry:
```bash
poetry install
```

## Usage

### Activate Poetry Shell
```bash
poetry shell
```

### Basic Commands

Collect financial data using the following command structure:
```bash
python main.py --tickers "TICKER1,TICKER2" --data-types "TYPE1,TYPE2"
```

Example command:
```bash
python main.py --tickers "TSLA,AAPL" --data-types "annual_income,quarterly_income"
```

### Available Data Types

- `annual_income`: Annual income statements
- `quarterly_income`: Quarterly income statements
- `annual_balance`: Annual balance sheets
- `quarterly_balance`: Quarterly balance sheets
- `annual_cashflow`: Annual cash flow statements
- `quarterly_cashflow`: Quarterly cash flow statements
- `stock_metrics`: Stock Metrics
<!-- - `actions`: Stock actions (dividends, splits)
- `calendar`: Earnings calendar
- `recommendations`: Analyst recommendations
- `upgrades_downgrades`: Upgrade/downgrade history
- `news`: Company news -->

### Optional Arguments

- `--output`: Specify output format (db, csv, json)
- `--verbose` or `-v`: Increase output verbosity

Example with options:
```bash
python main.py --tickers "TSLA,AAPL" --data-types "annual_income" --output csv -v
```

## Configuration

### Poetry Configuration (pyproject.toml)
```toml
[tool.poetry]
name = "financial-data"
version = "0.1.0"
description = "A tool for collecting financial data from Yahoo Finance"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.9"
pandas = "^2.0.0"
yfinance = "^0.2.0"
sqlalchemy = "^2.0.0"
python-dotenv = "^1.0.0"
psycopg2-binary = "^2.9.0"

[tool.poetry.dev-dependencies]
pytest = "^7.0.0"
black = "^23.0.0"
flake8 = "^6.0.0"
```

### Environment Configuration
Create a `.env` file in the project root:
```bash
DB_HOST=localhost
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=5432
```

## Project Structure
```
financial_data/
│
├── config/
│   ├── __init__.py
│   └── database.py
│
├── utils/
│   ├── __init__.py
│   ├── db_utils.py
│   └── data_utils.py
│
├── services/
│   ├── __init__.py
│   ├── yahoo_finance.py
│   └── data_processor.py
│
├── __init__.py
├── data_args.py
├── main.py
├── pyproject.toml
├── poetry.lock
└── .env
```