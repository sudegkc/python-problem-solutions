Project: Shell Shop Promotion Engine

This Python program simulates a retail checkout system that applies complex promotional offers ("Buy X, Get Y Free") to a customer's shopping cart.

Key Features:

Dynamic Offer Matching: Scans the shopping cart to identify sets of items that qualify for a "free gift" based on rules defined in an external file.

Smart Pricing: Calculates the final total by excluding the price of items that were successfully claimed as part of a promotion.

Offer Validation: Ensures that items used to trigger a gift, as well as the gifted items themselves, cannot be reused to generate further rewards (preventing infinite loops).

Technical Implementation:

Data Parsing: Reads and structures data from three different file formats (.dat and .txt), handling shell names, prices (Euro/Eurocents), and multi-item offer strings.

Collection Management: Utilizes Python lists and dictionaries to track inventory, prices, and the current state of the user's cart during the promotion matching phase.

String Formatting: Outputs detailed descriptions of each matched offer and provides a formatted final price in EUR.

File Structure:

prices.dat: Catalog of items and their unit prices.

offers.dat: List of promotional rules (e.g., ItemA ItemA: ItemB).

cart.dat: The list of items the customer intends to purchase.

solution.py: The core promotion engine logic.
