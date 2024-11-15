-- Annual Income Statements
DROP TABLE IF EXISTS annual_income_statements;

CREATE TABLE IF NOT EXISTS annual_income_statements (
    ticker VARCHAR(20) NOT NULL,
    report_date DATE NOT NULL,
    tax_effect_of_unusual_items NUMERIC,
    tax_rate_for_calcs NUMERIC,
    normalized_ebitda NUMERIC,
    net_income_from_continuing_operations NUMERIC,
    reconciled_depreciation NUMERIC,
    reconciled_cost_of_revenue NUMERIC,
    ebitda NUMERIC,
    ebit NUMERIC,
    net_interest_income NUMERIC,
    interest_expense NUMERIC,
    interest_income NUMERIC,
    normalized_income NUMERIC,
    net_income_continuing_and_discontinued NUMERIC,
    total_expenses NUMERIC,
    total_operating_income_as_reported NUMERIC,
    diluted_average_shares NUMERIC,
    basic_average_shares NUMERIC,
    diluted_eps NUMERIC,
    basic_eps NUMERIC,
    diluted_ni_available_to_com_stockholders NUMERIC,
    net_income_common_stockholders NUMERIC,
    net_income NUMERIC,
    net_income_including_noncontrolling_interests NUMERIC,
    net_income_continuous_operations NUMERIC,
    tax_provision NUMERIC,
    pretax_income NUMERIC,
    other_income_expense NUMERIC,
    other_non_operating_income_expenses NUMERIC,
    net_non_operating_interest_income_expense NUMERIC,
    interest_expense_non_operating NUMERIC,
    interest_income_non_operating NUMERIC,
    operating_income NUMERIC,
    operating_expense NUMERIC,
    research_and_development NUMERIC,
    selling_general_and_administration NUMERIC,
    gross_profit NUMERIC,
    cost_of_revenue NUMERIC,
    total_revenue NUMERIC,
    operating_revenue NUMERIC,
    PRIMARY KEY (ticker, report_date)
);

CREATE INDEX idx_annual_income_statements_date ON annual_income_statements(report_date);
CREATE INDEX idx_annual_income_statements_ticker ON annual_income_statements(ticker);

-- Quarterly Income Statements
DROP TABLE IF EXISTS quarterly_income_statements;

CREATE TABLE IF NOT EXISTS quarterly_income_statements (
    LIKE annual_income_statements INCLUDING ALL
);

CREATE INDEX idx_quarterly_income_statements_date ON quarterly_income_statements(report_date);
CREATE INDEX idx_quarterly_income_statements_ticker ON quarterly_income_statements(ticker);

-- Annual Balance Sheet
DROP TABLE IF EXISTS annual_balance_sheet;

CREATE TABLE IF NOT EXISTS annual_balance_sheet (
    ticker VARCHAR(20) NOT NULL,
    report_date DATE NOT NULL,
    treasury_shares_number NUMERIC,
    ordinary_shares_number NUMERIC,
    share_issued NUMERIC,
    net_debt NUMERIC,
    total_debt NUMERIC,
    tangible_book_value NUMERIC,
    invested_capital NUMERIC,
    working_capital NUMERIC,
    net_tangible_assets NUMERIC,
    capital_lease_obligations NUMERIC,
    common_stock_equity NUMERIC,
    total_capitalization NUMERIC,
    total_equity_gross_minority_interest NUMERIC,
    minority_interest NUMERIC,
    stockholders_equity NUMERIC,
    gains_losses_not_affecting_retained_earnings NUMERIC,
    other_equity_adjustments NUMERIC,
    retained_earnings NUMERIC,
    additional_paid_in_capital NUMERIC,
    capital_stock NUMERIC,
    common_stock NUMERIC,
    preferred_stock NUMERIC,
    total_liabilities_net_minority_interest NUMERIC,
    total_non_current_liabilities_net_minority_interest NUMERIC,
    other_non_current_liabilities NUMERIC,
    preferred_securities_outside_stock_equity NUMERIC,
    non_current_accrued_expenses NUMERIC,
    non_current_deferred_liabilities NUMERIC,
    non_current_deferred_revenue NUMERIC,
    non_current_deferred_taxes_liabilities NUMERIC,
    long_term_debt_and_capital_lease_obligation NUMERIC,
    long_term_capital_lease_obligation NUMERIC,
    long_term_debt NUMERIC,
    long_term_provisions NUMERIC,
    current_liabilities NUMERIC,
    other_current_liabilities NUMERIC,
    current_deferred_liabilities NUMERIC,
    current_deferred_revenue NUMERIC,
    current_debt_and_capital_lease_obligation NUMERIC,
    current_capital_lease_obligation NUMERIC,
    current_debt NUMERIC,
    other_current_borrowings NUMERIC,
    line_of_credit NUMERIC,
    current_provisions NUMERIC,
    payables_and_accrued_expenses NUMERIC,
    current_accrued_expenses NUMERIC,
    interest_payable NUMERIC,
    payables NUMERIC,
    total_tax_payable NUMERIC,
    accounts_payable NUMERIC,
    total_assets NUMERIC,
    total_non_current_assets NUMERIC,
    other_non_current_assets NUMERIC,
    non_current_deferred_assets NUMERIC,
    non_current_deferred_taxes_assets NUMERIC,
    non_current_note_receivables NUMERIC,
    goodwill_and_other_intangible_assets NUMERIC,
    other_intangible_assets NUMERIC,
    goodwill NUMERIC,
    net_ppe NUMERIC,
    accumulated_depreciation NUMERIC,
    gross_ppe NUMERIC,
    leases NUMERIC,
    construction_in_progress NUMERIC,
    other_properties NUMERIC,
    machinery_furniture_equipment NUMERIC,
    land_and_improvements NUMERIC,
    properties NUMERIC,
    current_assets NUMERIC,
    other_current_assets NUMERIC,
    restricted_cash NUMERIC,
    prepaid_assets NUMERIC,
    inventory NUMERIC,
    other_inventories NUMERIC,
    finished_goods NUMERIC,
    work_in_process NUMERIC,
    raw_materials NUMERIC,
    receivables NUMERIC,
    accounts_receivable NUMERIC,
    cash_cash_equivalents_and_short_term_investments NUMERIC,
    other_short_term_investments NUMERIC,
    cash_and_cash_equivalents NUMERIC,
    cash_equivalents NUMERIC,
    cash_financial NUMERIC,
    PRIMARY KEY (ticker, report_date)
);

CREATE INDEX idx_annual_balance_sheet_date ON annual_balance_sheet(report_date);
CREATE INDEX idx_annual_balance_sheet_ticker ON annual_balance_sheet(ticker);

-- Quarterly Balance Sheet
DROP TABLE IF EXISTS quarterly_balance_sheet;

CREATE TABLE IF NOT EXISTS quarterly_balance_sheet (
    LIKE annual_balance_sheet INCLUDING ALL
);

CREATE INDEX idx_quarterly_balance_sheet_date ON quarterly_balance_sheet(report_date);
CREATE INDEX idx_quarterly_balance_sheet_ticker ON quarterly_balance_sheet(ticker);

-- Annual Cash Flow
DROP TABLE IF EXISTS annual_cash_flow;

CREATE TABLE IF NOT EXISTS annual_cash_flow (
    ticker VARCHAR(20) NOT NULL,
    report_date DATE NOT NULL,
    free_cash_flow NUMERIC,
    repayment_of_debt NUMERIC,
    issuance_of_debt NUMERIC,
    issuance_of_capital_stock NUMERIC,
    capital_expenditure NUMERIC,
    interest_paid_supplemental_data NUMERIC,
    income_tax_paid_supplemental_data NUMERIC,
    end_cash_position NUMERIC,
    beginning_cash_position NUMERIC,
    effect_of_exchange_rate_changes NUMERIC,
    changes_in_cash NUMERIC,
    financing_cash_flow NUMERIC,
    cash_flow_from_continuing_financing_activities NUMERIC,
    net_other_financing_charges NUMERIC,
    proceeds_from_stock_option_exercised NUMERIC,
    net_common_stock_issuance NUMERIC,
    common_stock_issuance NUMERIC,
    net_issuance_payments_of_debt NUMERIC,
    net_long_term_debt_issuance NUMERIC,
    long_term_debt_payments NUMERIC,
    long_term_debt_issuance NUMERIC,
    investing_cash_flow NUMERIC,
    cash_flow_from_continuing_investing_activities NUMERIC,
    net_other_investing_changes NUMERIC,
    net_investment_purchase_and_sale NUMERIC,
    sale_of_investment NUMERIC,
    purchase_of_investment NUMERIC,
    net_business_purchase_and_sale NUMERIC,
    sale_of_business NUMERIC,
    purchase_of_business NUMERIC,
    net_intangibles_purchase_and_sale NUMERIC,
    sale_of_intangibles NUMERIC,
    purchase_of_intangibles NUMERIC,
    net_ppe_purchase_and_sale NUMERIC,
    purchase_of_ppe NUMERIC,
    operating_cash_flow NUMERIC,
    cash_flow_from_continuing_operating_activities NUMERIC,
    change_in_working_capital NUMERIC,
    change_in_other_working_capital NUMERIC,
    change_in_other_current_liabilities NUMERIC,
    change_in_other_current_assets NUMERIC,
    change_in_payables_and_accrued_expense NUMERIC,
    change_in_payable NUMERIC,
    change_in_account_payable NUMERIC,
    change_in_prepaid_assets NUMERIC,
    change_in_inventory NUMERIC,
    change_in_receivables NUMERIC,
    changes_in_account_receivables NUMERIC,
    other_non_cash_items NUMERIC,
    stock_based_compensation NUMERIC,
    asset_impairment_charge NUMERIC,
    deferred_tax NUMERIC,
    deferred_income_tax NUMERIC,
    depreciation_amortization_depletion NUMERIC,
    depreciation_and_amortization NUMERIC,
    depreciation NUMERIC,
    operating_gains_losses NUMERIC,
    net_foreign_currency_exchange_gain_loss NUMERIC,
    gain_loss_on_sale_of_ppe NUMERIC,
    net_income_from_continuing_operations NUMERIC,
    PRIMARY KEY (ticker, report_date)
);

CREATE INDEX idx_annual_cash_flow_date ON annual_cash_flow(report_date);
CREATE INDEX idx_annual_cash_flow_ticker ON annual_cash_flow(ticker);

-- Quarterly Cash Flow
DROP TABLE IF EXISTS quarterly_cash_flow;

CREATE TABLE IF NOT EXISTS quarterly_cash_flow (
    LIKE annual_cash_flow INCLUDING ALL
);

CREATE INDEX idx_quarterly_cash_flow_date ON quarterly_cash_flow(report_date);
CREATE INDEX idx_quarterly_cash_flow_ticker ON quarterly_cash_flow(ticker);

-- Company Stock Metrics
DROP TABLE IF EXISTS stock_metrics;

CREATE TABLE IF NOT EXISTS stock_metrics (
    id SERIAL,  
    ticker VARCHAR(20) NOT NULL,
    report_date DATE NOT NULL,
    company_name VARCHAR(255),
    exchange VARCHAR(50),
    currency VARCHAR(10),
    current_price NUMERIC,
    previous_close NUMERIC,
    open_price NUMERIC,
    day_low NUMERIC,
    day_high NUMERIC,
    regular_market_previous_close NUMERIC,
    regular_market_open NUMERIC,
    regular_market_day_low NUMERIC,
    regular_market_day_high NUMERIC,
    dividend_rate NUMERIC,
    dividend_yield NUMERIC,
    ex_dividend_date BIGINT,
    payout_ratio NUMERIC,
    five_year_avg_dividend_yield NUMERIC,
    beta NUMERIC,
    trailing_pe NUMERIC,
    forward_pe NUMERIC,
    volume BIGINT,
    regular_market_volume BIGINT,
    average_volume BIGINT,
    average_volume_10days BIGINT,
    average_daily_volume_10day BIGINT,
    bid NUMERIC,
    ask NUMERIC,
    bid_size INTEGER,
    ask_size INTEGER,
    market_cap BIGINT,
    fifty_two_week_low NUMERIC,
    fifty_two_week_high NUMERIC,
    price_to_sales_trailing_12months NUMERIC,
    fifty_day_average NUMERIC,
    two_hundred_day_average NUMERIC,
    trailing_annual_dividend_rate NUMERIC,
    trailing_annual_dividend_yield NUMERIC,
    enterprise_value BIGINT,
    profit_margins NUMERIC,
    float_shares BIGINT,
    shares_outstanding BIGINT,
    shares_short BIGINT,
    shares_short_prior_month BIGINT,
    shares_short_previous_month_date BIGINT,
    date_short_interest BIGINT,
    shares_percent_shares_out NUMERIC,
    held_percent_insiders NUMERIC,
    held_percent_institutions NUMERIC,
    short_ratio NUMERIC,
    short_percent_of_float NUMERIC,
    book_value NUMERIC,
    price_to_book NUMERIC,
    earnings_quarterly_growth NUMERIC,
    net_income_to_common BIGINT,
    trailing_eps NUMERIC,
    forward_eps NUMERIC,
    peg_ratio NUMERIC,
    last_split_factor VARCHAR(20),
    last_split_date BIGINT,
    enterprise_to_revenue NUMERIC,
    enterprise_to_ebitda NUMERIC,
    last_dividend_value NUMERIC,
    last_dividend_date BIGINT,
    target_high_price NUMERIC,
    target_low_price NUMERIC,
    target_mean_price NUMERIC,
    target_median_price NUMERIC,
    recommendation_mean NUMERIC,
    recommendation_key VARCHAR(20),
    number_of_analyst_opinions INTEGER,
    total_cash BIGINT,
    total_cash_per_share NUMERIC,
    ebitda BIGINT,
    total_debt BIGINT,
    quick_ratio NUMERIC,
    current_ratio NUMERIC,
    debt_to_equity NUMERIC,
    revenue_per_share NUMERIC,
    return_on_assets NUMERIC,
    return_on_equity NUMERIC,
    free_cashflow BIGINT,
    operating_cashflow BIGINT,
    earnings_growth NUMERIC,
    revenue_growth NUMERIC,
    gross_margins NUMERIC,
    ebitda_margins NUMERIC,
    operating_margins NUMERIC,
    trailing_peg_ratio NUMERIC,
    PRIMARY KEY (id),
    CONSTRAINT stock_metrics_unique_record UNIQUE (ticker, report_date)
);

CREATE INDEX idx_stock_metrics_ticker ON stock_metrics(ticker);
CREATE INDEX idx_stock_metrics_date ON stock_metrics(report_date);
