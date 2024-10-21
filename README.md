# Dynamic Inventory System Using Nested Dictionaries

## Overview

This inventory management system allows for real-time updates and complex queries using a nested dictionary structure. Each category in the inventory is a dictionary with individual items represented by another dictionary, containing details such as name, price, and quantity. The system supports the creation, updating, and merging of inventory data, along with functionality to query and manage items across categories.

## Requirements Covered

### 1. **Create Inventory**:
The system provides functions to dynamically populate the inventory using different dictionary creation methods, including `dict()` constructor and dictionary comprehensions.

### 2. **Update & Merge**:
Functions are provided to update item information (e.g., price, quantity) and to merge two inventory systems, ensuring no data is lost.

### 3. **Querying**:
Functions allow for:
- Retrieving all items in a category.
- Finding the most expensive item across the inventory.
- Checking if an item is in stock and returning its details.

### 4. **Dictionary Views**:
Functions allow for viewing available categories, listing all items, and viewing category-item pairs.

### 5. **Serialization (Copying)**:
The system can create deep and shallow copies of the inventory, allowing independent modifications of a copy without affecting the original.

---

## Function Details

### `create_inventory() -> dict`
This function initializes and returns the inventory. It populates different categories (e.g., Electronics, Groceries) using dictionary comprehensions and the `dict()` constructor.

#### Example:
```python
inventory = create_inventory()
print(inventory)
```

#### Tests:
- Test if the inventory contains the correct categories and items.
- Test if the correct number of items are initialized in each category.

### `update_inventory(inventory: dict, category: str, item_name: str, update_info: dict) -> bool`
This function allows updating information (e.g., price, quantity) for a specific item in the inventory. It returns `True` if the update is successful and `False` otherwise.

#### Example:
```python
update_inventory(inventory, "Electronics", "Laptop", {"quantity": 10})
```

#### Tests:
- Test updating existing items in the inventory.
- Test handling updates for non-existing items.

### `merge_inventories(inv1: dict, inv2: dict) -> dict`
This function merges two inventories without losing data. If items overlap between inventories, their quantities are summed, and the higher price is retained.

#### Example:
```python
merged_inventory = merge_inventories(inventory1, inventory2)
```

#### Tests:
- Test merging inventories with overlapping and non-overlapping categories.
- Test proper quantity summation and price selection.

### `get_items_in_category(inventory: dict, category: str) -> dict`
This function retrieves all items in a specified category. If the category doesn't exist, it returns an empty dictionary.

#### Example:
```python
electronics = get_items_in_category(inventory, "Electronics")
```

#### Tests:
- Test retrieval of items in existing categories.
- Test empty dictionary return for non-existing categories.

### `find_most_expensive_item(inventory: dict) -> dict`
This function searches through all items in the inventory and returns the most expensive item.

#### Example:
```python
most_expensive = find_most_expensive_item(inventory)
```

#### Tests:
- Test finding the most expensive item in a populated inventory.
- Test handling of an empty inventory.

### `check_item_in_stock(inventory: dict, item_name: str) -> dict`
This function checks if an item is in stock by searching across categories. It returns the item's details if found and in stock; otherwise, it returns `None`.

#### Example:
```python
item_details = check_item_in_stock(inventory, "Laptop")
```

#### Tests:
- Test stock availability for existing items.
- Test handling for out-of-stock or non-existing items.

### `view_categories(inventory: dict) -> list`
This function returns a list of all available categories in the inventory.

#### Example:
```python
categories = view_categories(inventory)
```

#### Tests:
- Test retrieving categories from an inventory with multiple categories.
- Test handling of an empty inventory.

### `view_all_items(inventory: dict) -> list`
This function returns a list of all items in the inventory, regardless of category.

#### Example:
```python
all_items = view_all_items(inventory)
```

#### Tests:
- Test retrieving all items across categories.
- Test handling of an empty inventory.

### `view_category_item_pairs(inventory: dict) -> list`
This function returns a list of tuples where each tuple contains a category name and an item name.

#### Example:
```python
category_item_pairs = view_category_item_pairs(inventory)
```

#### Tests:
- Test returning correct category-item pairs for all items.
- Test handling of empty inventory.

### `copy_inventory(inventory: dict, deep: bool = True) -> dict`
This function creates either a deep copy or a shallow copy of the entire inventory. A deep copy allows independent modification of the copy without affecting the original.

#### Example:
```python
inventory_copy = copy_inventory(inventory, deep=True)
```

#### Tests:
- Test deep copying to ensure no changes reflect back on the original inventory.
- Test shallow copying to ensure changes reflect back on the original inventory.

---

## Testing

All functions are tested using the `unittest` framework. Below is an outline of the test coverage in `test_inventory.py`.

### Tests Implemented:
- **Inventory Creation Tests**: Verifying the correct creation of categories and items.
- **Update Tests**: Ensuring updates are correctly applied to items.
- **Merge Tests**: Verifying the merging behavior between two inventories.
- **Query Tests**: Ensuring correct results for retrieving items, checking stock, and finding the most expensive item.
- **View Tests**: Ensuring correct viewing of categories, items, and category-item pairs.
- **Copy Tests**: Verifying deep and shallow copying behavior.

---

## Example Usage

1. **Creating Inventory**:
   ```python
   inventory = create_inventory()
   ```

2. **Updating Inventory**:
   ```python
   update_inventory(inventory, "Groceries", "Apple", {"price": 0.6})
   ```

3. **Merging Inventories**:
   ```python
   merged_inventory = merge_inventories(inventory1, inventory2)
   ```

4. **Querying**:
   - Retrieve items from a category:
     ```python
     get_items_in_category(inventory, "Electronics")
     ```
   - Find most expensive item:
     ```python
     find_most_expensive_item(inventory)
     ```

---

## Conclusion

This dynamic inventory system allows users to manage a nested dictionary structure efficiently. With real-time updates, querying capabilities, and inventory merging, it is designed to handle complex inventory management tasks. The provided functionality covers all requirements, including handling dictionary views, serialization, and dynamic updates. The system is fully tested using `unittest` to ensure correctness.

