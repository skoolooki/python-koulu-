
"File reader can only read the files that is in the code folder"

def input_validator():
    """Ask the user for a number and print its square."""
    print("1) Input Validator ---")
    try:
        number = float(input("Enter a number: "))
        print(f"The square of {number} is {number ** 2}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")



def file_reader():
    """Ask the user for a filename and try to read it."""
    print(" 2) File Reader ---")
    filename = input("Enter a filename: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    except PermissionError:
        print("Permission denied. You are not allowed to open this file.")
    except OSError as e:
        print(f"An operating system error occurred: {e}")



def division_calculator():
    """Ask for two numbers and divide them."""
    print("3) Division Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    else:
        print(f"Result: {num1} / {num2} = {result}")



def product_price_lookup():
    """Look up a product price in a dictionary and handle KeyError."""
    print("4) Product Price Lookup")
    products = {
        "apple": 1.2,
        "banana": 0.8,
        "orange": 1.5,
        "milk": 2.3,
        "bread": 2.0,
    }

    print("Available products:", ", ".join(products.keys()))
    product_name = input("Enter a product name: ").strip().lower()

    try:
        price = products[product_name]
        print(f"The price of {product_name} is {price} euros.")
    except KeyError:
        print("Product not found.")



def validate_age(age):
    """Raise ValueError if age is negative or over 120."""
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")
    return age



def custom_age_validator():
    """Handle age validation in the main program."""
    print("5) Custom Age Validator")
    try:
        age = int(input("Enter age: "))
        valid_age = validate_age(age)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Age {valid_age} is valid.")
    finally:
        print("Age validation finished.")



def contact_manager():
    """Optional advanced challenge: simple contact manager."""
    print("6) Mini Contact Manager (Optional Bonus)")
    contacts = {}

    while True:
        print("Contact Manager Menu")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Exit contact manager")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            try:
                name = input("Enter name: ").strip()
                if not name:
                    raise ValueError("Name cannot be empty.")
                if name in contacts:
                    raise ValueError("A contact with this name already exists.")

                phone = input("Enter phone number: ").strip()
                int(phone)  # validation: must be numeric

                contacts[name] = phone
                print(f"Contact '{name}' added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            if contacts:
                print("Saved contacts:")
                for name, phone in contacts.items():
                    print(f"- {name}: {phone}")
            else:
                print("No contacts saved yet.")

        elif choice == "3":
            name = input("Enter name to search: ").strip()
            try:
                print(f"{name}: {contacts[name]}")
            except KeyError:
                print("Contact not found.")

        elif choice == "4":
            print("Exiting contact manager...")
            break

        else:
            print("Invalid option. Please choose between 1 and 4.")



def main():
    """Main menu to access all assignment tasks in one file."""
    while True:
        print("==============================")
        print(" Exception Handling Assignment ")
        print("==============================")
        print("1. Input Validator")
        print("2. File Reader")
        print("3. Division Calculator")
        print("4. Product Price Lookup")
        print("5. Custom Age Validator")
        print("6. Mini Contact Manager (Optional Bonus)")
        print("0. Exit")

        choice = input("Select a task (0-6): ").strip()

        if choice == "1":
            input_validator()
        elif choice == "2":
            file_reader()
        elif choice == "3":
            division_calculator()
        elif choice == "4":
            product_price_lookup()
        elif choice == "5":
            custom_age_validator()
        elif choice == "6":
            contact_manager()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number from 0 to 6.")


if __name__ == "__main__":
    main()