# inventory_system.py
import copy

def create_inventory() -> dict:
    """
    Create and return an inventory using different dictionary creation methods.

    Returns:
        dict: A dictionary representing the inventory with categories as keys.
    """
    # Using dict() constructor
    electronics = dict(
        Laptop={"name": "Laptop", "price": 1000, "quantity": 5},
        Smartphone={"name": "Smartphone", "price": 500, "quantity": 10}
    )
    
    # Using dictionary comprehension
    groceries = {
        item: {"name": item, "price": price, "quantity": 100} 
        for item, price in [("Apple", 0.5), ("Banana", 0.3), ("Milk", 2.5)]
    }
    
    # Combining all categories into the main inventory
    inventory = {
        "Electronics": electronics,
        "Groceries": groceries
    }
    
    return inventory

def update_inventory(inventory: dict, category: str, item_name: str, update_info: dict) -> bool:
    """
    Update item information in the inventory.

    Args:
        inventory (dict): The inventory to update.
        category (str): The category of the item.
        item_name (str): The name of the item to update.
        update_info (dict): A dictionary containing the update information.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    if category in inventory and item_name in inventory[category]:
        inventory[category][item_name].update(update_info)
        return True
    return False

def merge_inventories(inv1: dict, inv2: dict) -> dict:
    """
    Merge two inventory systems without losing any data.

    Args:
        inv1 (dict): The first inventory to merge.
        inv2 (dict): The second inventory to merge.

    Returns:
        dict: A merged inventory.
    """
    merged = copy.deepcopy(inv1)
    for category, items in inv2.items():
        if category in merged:
            for item, details in items.items():
                if item in merged[category]:
                    # Combine quantity and keep the higher price
                    merged[category][item]["quantity"] += details["quantity"]
                    merged[category][item]["price"] = max(merged[category][item]["price"], details["price"])
                else:
                    merged[category][item] = details
        else:
            merged[category] = items
    return merged

def get_items_in_category(inventory: dict, category: str) -> dict:
    """
    Retrieve all items in a specified category.

    Args:
        inventory (dict): The inventory to search.
        category (str): The category to retrieve items from.

    Returns:
        dict: A dictionary of items in the specified category.
    """
    return inventory.get(category, {})

def find_most_expensive_item(inventory: dict) -> dict:
    """
    Find and return the most expensive item in the inventory.

    Args:
        inventory (dict): The inventory to search.

    Returns:
        dict: The details of the most expensive item, or None if the inventory is empty.
    """
    most_expensive = None
    max_price = float('-inf')
    
    for category, items in inventory.items():
        for item, details in items.items():
            if details["price"] > max_price:
                max_price = details["price"]
                most_expensive = details
    
    return most_expensive

def check_item_in_stock(inventory: dict, item_name: str) -> dict:
    """
    Check if an item is in stock and return its details if available.

    Args:
        inventory (dict): The inventory to search.
        item_name (str): The name of the item to check.

    Returns:
        dict: The details of the item if in stock, None otherwise.
    """
    for category, items in inventory.items():
        if item_name in items:
            if items[item_name]["quantity"] > 0:
                return items[item_name]
    return None

def view_categories(inventory: dict) -> list:
    """
    View available categories in the inventory.

    Args:
        inventory (dict): The inventory to check.

    Returns:
        list: A list of category names.
    """
    return list(inventory.keys())

def view_all_items(inventory: dict) -> list:
    """
    View all items in the inventory.

    Args:
        inventory (dict): The inventory to check.

    Returns:
        list: A list of all items in the inventory.
    """
    return [item for category in inventory.values() for item in category.values()]

def view_category_item_pairs(inventory: dict) -> list:
    """
    View category-item pairs in the inventory.

    Args:
        inventory (dict): The inventory to check.

    Returns:
        list: A list of tuples containing category and item pairs.
    """
    return [(category, item) for category, items in inventory.items() for item in items]

def copy_inventory(inventory: dict, deep: bool = True) -> dict:
    """
    Copy the entire inventory structure.

    Args:
        inventory (dict): The inventory to copy.
        deep (bool): If True, perform a deep copy; otherwise, a shallow copy.

    Returns:
        dict: A copy of the inventory.
    """
    if deep:
        return copy.deepcopy(inventory)
    else:
        return copy.copy(inventory)
