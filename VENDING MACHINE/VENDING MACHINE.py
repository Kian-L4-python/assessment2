# Define the menu with items and their corresponding codes and prices
menu = {
    'A1': {'item': 'Cola', 'price': 1.50},
    'A2': {'item': 'Pringles', 'price': 1.00},
    'B1': {'item': 'Water', 'price': 1.25},
    'B2': {'item': 'Mars Bar', 'price': 1.75}
}

def display_menu():
    """Display the menu to the user."""
    print("Vending Machine Menu:")
    for code, item_info in menu.items():
        print(f"{code}: {item_info['item']} - ${item_info['price']}")

def get_user_selection():
    """Prompt the user to input a code and return the selected item."""
    while True:
        user_input = input("Enter the code of the item you want to purchase: ").upper()
        if user_input in menu:
            return user_input
        else:
            print("Invalid code. Please try again.")

def get_user_money():
    """Prompt the user to input the amount of money they want to insert."""
    while True:
        try:
            money_input = float(input("Insert money (in dollars): "))
            if money_input >= 0:
                return money_input
            else:
                print("Invalid amount. Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_change(item_price, user_money):
    """Calculate and return the change to be given to the user."""
    return user_money - item_price

def dispense_item(item_code, item_price):
    """Dispense the selected item and display a message."""
    print(f"\nDispensing {menu[item_code]['item']}...")
    print(f"Thank you for your purchase! You paid ${item_price:.2f}.")

def main():
    display_menu()  # Display the vending machine menu
    selected_code = get_user_selection()  # Get the user's selected item code
    selected_item = menu[selected_code]
    
    user_money = get_user_money()  # Get the amount of money from the user
    item_price = selected_item['price']

    if user_money < item_price:
        print("Insufficient funds. Please insert more money.")
    else:
        change = calculate_change(item_price, user_money)
        dispense_item(selected_code, item_price)
        print(f"Change: ${change:.2f}")

if __name__ == "__main__":
    main()