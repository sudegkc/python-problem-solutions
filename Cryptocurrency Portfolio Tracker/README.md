
💰 Project: Cryptocurrency Portfolio Tracker

This Python script calculates and analyzes the historical value of a cryptocurrency portfolio by processing structured CSV data.

Key Features:

Data Integration: Merges user holdings from token.csv with historical market rates from token_prices.csv.

Portfolio Valuation: Dynamically computes daily total portfolio value in USD across all monitored dates.

Peak Analysis: Identifies and reports the specific date and value when the portfolio reached its maximum worth.

Technical Implementation:

CSV Parsing: Efficiently handles semicolon-separated data files.

Data Structures: Uses dictionaries to map tokens to quantities and group price data by date.

Precision: Manages floating-point calculations for accurate financial reporting.
