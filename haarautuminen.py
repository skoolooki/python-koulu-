# Employee Bonus Calculator

# Ask the user for salary and years of service
salary_input = input("Enter your salary: ")
years_input = input("Enter your years of service: ")

# Validate numeric input
if salary_input.isdigit() and years_input.isdigit():
    salary = float(salary_input)
    years = int(years_input)

    # Check bonus eligibility
    if years >= 5:
        bonus = salary * 0.05   # 5% bonus
        print("Bonus awarded: $", bonus)
    else:
        print("No bonus awarded")
else:
    print("Invalid input. Please enter numeric values only.")