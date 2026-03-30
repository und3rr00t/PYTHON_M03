import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}
    i: int = 1
    while i < len(sys.argv):
        arg: str = sys.argv[i]
        i += 1

        parts: list[str] = arg.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item: str = parts[0].strip()
        qty_str: str = parts[1].strip()

        if item in inventory.keys():
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            qty: int = int(qty_str)
            inventory.update({item: qty})
        except ValueError:
            print(f"Quantity error for '{item}': "
                  f"invalid literal for int() with base 10: '{qty_str}'")
            continue

    print(f"Got inventory: {inventory}")

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty: int = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total_qty}")

    if total_qty > 0:
        most_abundant: str = ""
        most_qty: int = -1
        least_abundant: str = ""
        least_qty: int = -1

        for item in item_list:
            qty = inventory[item]
            pct: float = (qty / total_qty) * 100.0
            print(f"Item {item} represents {round(pct, 1)}%")

            if most_qty == -1 or qty > most_qty:
                most_qty = qty
                most_abundant = item

            if least_qty == -1 or qty < least_qty:
                least_qty = qty
                least_abundant = item

        print(f"Item most abundant: {most_abundant} with quantity {most_qty}")
        print(
            f"Item least abundant: {least_abundant} "
            f"with quantity {least_qty}"
        )

    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
