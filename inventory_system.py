"""
Inventory System Module
Handles basic inventory management, loading/saving data, and reporting.
"""

import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)


def add_item(stock_data, item="default", qty=0, logs=None):
    """Add an item and quantity to stock_data, log the operation."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.error(
            "Invalid input types: %s (%s), %s (%s)",
            item, type(item), qty, type(qty)
        )
        return
    if qty < 0:
        logging.warning(
            "Negative quantity not allowed: %d for %s",
            qty, item
        )
        return
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(
        f"{datetime.now()}: Added {qty} of {item}"
    )


def remove_item(stock_data, item, qty):
    """
    Remove a quantity from an item,
    log errors if item doesn't exist.
    """
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.error(
            "Invalid input types for removal: %s (%s), %s (%s)",
            item, type(item), qty, type(qty)
        )
        return
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.error(
            "Item not found for removal: %s",
            item
        )


def get_qty(stock_data, item):
    """Return current quantity for an item."""
    return stock_data.get(item, 0)


def load_data(file_name="inventory.json"):
    """Load inventory data from a file."""
    try:
        with open(file_name, "r", encoding="utf-8") as file_obj:
            return json.loads(file_obj.read())
    except (FileNotFoundError, json.JSONDecodeError) as error:
        logging.error(
            "Error loading data: %s",
            error
        )
        return {}


def save_data(stock_data, file_name="inventory.json"):
    """Save current inventory data to a file."""
    try:
        with open(file_name, "w", encoding="utf-8") as file_obj:
            file_obj.write(json.dumps(stock_data))
    except IOError as error:
        logging.error(
            "Error saving data: %s",
            error
        )


def print_data(stock_data):
    """Print a report of all inventory items."""
    print("Items Report")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")


def check_low_items(stock_data, threshold=5):
    """Return list of items with qty below threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Main execution block for inventory operations."""
    logs = []
    stock_data = load_data()

    if not stock_data:
        stock_data = {}

    add_item(stock_data, "apple", 10, logs)
    add_item(stock_data, "banana", 2, logs)
    add_item(stock_data, "orange", 3, logs)

    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)

    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print(f"Low items: {check_low_items(stock_data)}")

    save_data(stock_data)
    print_data(stock_data)

    for log_entry in logs:
        logging.info("%s", log_entry)


if __name__ == "__main__":
    main()
