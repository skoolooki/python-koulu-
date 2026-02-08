#1 Employee Bonus Calculator

salary_input = input("Enter your salary: ")
years_input = input("Enter your years of service: ")

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


#2 Square or Not? 
length_input = input("Enter the length: ")
width_input = input("Enter the width: ")

# Validate numeric input
if length_input.isdigit() and width_input.isdigit():
    length = float(length_input)
    width = float(width_input)

    # Check if it's a square
    if length == width:
        print("This is a square.")
    else:
        print("This is not a square.")
else:
    print("Invalid input. Please enter numeric values only.")


#3 Which Number is Greater?
num1_input = input("Enter the first number: ")
num2_input = input("Enter the second number: ")
try:
    num1 = float(num1_input)
    num2 = float(num2_input)

    # Compare the numbers
    if num1 == num2:
        print("The numbers are the same.")
    else:
        if num1 > num2:
            print("The first number is larger.")
        else:
            print("The second number is larger.")

except ValueError:
    print("Invalid input. Please enter valid numbers (e.g., 10, -3, 4.5).")

#4 Store Discount System

SHIPPING_COST = 4.90

order_input = input("Enter your order total (EUR): ")

try:
    order_total = float(order_input)

    if order_total < 0:
        print("Invalid input. Order total cannot be negative.")
    else:
        # 10% discount only if order is above 69 EUR
        discount_rate = 0.10 if order_total > 69 else 0.0
        total_after_discount = order_total * (1 - discount_rate)

        # Free shipping only if final price is above 100 EUR
        shipping = 0.0 if total_after_discount > 100 else SHIPPING_COST

        final_to_pay = total_after_discount + shipping

        print(f"Final amount to pay: €{final_to_pay:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid number (e.g., 49.90, 120).")

#5 Grade Calculator
score_input = input("Enter exam score (0-90): ")

try:
    score = int(score_input)

    # Input validation
    if score < 0 or score > 90:
        print("Invalid score. Please enter a number between 0 and 90.")
    else:
        # Grade rules (if-elif-else)
        if score < 25:
            print("Failed")
        elif score <= 45:
            print("Grade 5")
        elif score <= 50:
            print("Grade 6")
        elif score <= 60:
            print("Grade 7")
        elif score <= 70:
            print("Grade 8")
        elif score <= 80:
            print("Grade 9")
        else:  # 81-90
            print("Grade 10")

except ValueError:
    print("Invalid input. Please enter a whole number (e.g., 45, 70, 90).")

#6 Find the Youngest User
# Person 1
name1 = input("Enter the first person's name: ").strip()
age1_input = input("Enter the first person's age: ")

# Person 2
name2 = input("Enter the second person's name: ").strip()
age2_input = input("Enter the second person's age: ")

# Person 3
name3 = input("Enter the third person's name: ").strip()
age3_input = input("Enter the third person's age: ")

# Input validation for ages (must be whole numbers, not negative)
try:
    age1 = int(age1_input)
    age2 = int(age2_input)
    age3 = int(age3_input)

    if age1 < 0 or age2 < 0 or age3 < 0:
        print("Invalid input. Ages cannot be negative.")
    else:
        # Find the youngest
        # (If there is a tie, this will pick the first youngest found.)
        if age1 <= age2 and age1 <= age3:
            youngest_name = name1
            youngest_age = age1
        elif age2 <= age1 and age2 <= age3:
            youngest_name = name2
            youngest_age = age2
        else:
            youngest_name = name3
            youngest_age = age3

        print(f"The youngest person is {youngest_name} ({youngest_age} years old).")

except ValueError:
    print("Invalid input. Please enter whole numbers for ages (e.g., 18, 25, 40).")

#7 Absolute Value Calculator
num_input = input("Enter a number: ")

try:
    num = float(num_input)  # allows decimals and negative numbers

    # If the number is negative, make it positive
    if num < 0:
        abs_value = -num
    else:
        abs_value = num

    print("Absolute value:", abs_value)

except ValueError:
    print("Invalid input. Please enter a valid number (e.g., -5, 3, 2.75).")

#8 Exam Eligibility Checker 

MIN_PERCENT = 75

try:
    lec_total = int(input("Total lectures: "))
    prac_total = int(input("Total practice sessions: "))
    lec_att = int(input("Lectures attended: "))
    prac_att = int(input("Practice attended: "))

    total = lec_total + prac_total
    attended = lec_att + prac_att

    # Simple validation
    if total <= 0 or lec_total < 0 or prac_total < 0 or lec_att < 0 or prac_att < 0 or lec_att > lec_total or prac_att > prac_total:
        print("Invalid input.")
    else:
        percent = (attended / total) * 100
        print(f"Attendance: {percent:.2f}%")

        if percent >= MIN_PERCENT:
            print("You are eligible to take the final exam.")
        else:
            print("You are NOT eligible to take the final exam.")

except ValueError:
    print("Invalid input. Please enter whole numbers only.")

#9 Sick Leave Consideration

MIN_PERCENT = 75

try:
    lec_total = int(input("Total lectures: "))
    prac_total = int(input("Total practice sessions: "))
    lec_att = int(input("Lectures attended: "))
    prac_att = int(input("Practice attended: "))
    sick_days = int(input("Sick days (count as present): "))

    total_sessions = lec_total + prac_total
    attended_sessions = lec_att + prac_att

    # Input validation
    if (lec_total < 0 or prac_total < 0 or lec_att < 0 or prac_att < 0 or sick_days < 0):
        print("Invalid input. Numbers cannot be negative.")
    elif total_sessions <= 0:
        print("Invalid input. Total sessions must be greater than 0.")
    elif lec_att > lec_total or prac_att > prac_total:
        print("Invalid input. Attended sessions cannot exceed total sessions.")
    elif sick_days > (total_sessions - attended_sessions):
        print("Invalid input. Sick days cannot exceed the sessions you missed.")
    else:
        # Sick days count as present
        effective_attendance = attended_sessions + sick_days
        percent = (effective_attendance / total_sessions) * 100

        print(f"Attendance (including sick leave): {percent:.2f}%")

        # Eligibility
        if percent >= MIN_PERCENT:
            print("You are eligible to take the final exam.")
        else:
            print("You are NOT eligible to take the final exam.")

except ValueError:
    print("Invalid input. Please enter whole numbers only.")

#10 Find largest number

try:
    # Ask the user for five numbers (one by one)
    n1 = float(input("Enter number 1: "))
    n2 = float(input("Enter number 2: "))
    n3 = float(input("Enter number 3: "))
    n4 = float(input("Enter number 4: "))
    n5 = float(input("Enter number 5: "))

    # Assume the first number is the largest at the start
    largest = n1

    # Compare each number to the current largest
    if n2 > largest:
        largest = n2

    if n3 > largest:
        largest = n3

    if n4 > largest:
        largest = n4

    if n5 > largest:
        largest = n5

    # Print the result
    print("The largest number is:", largest)

except ValueError:
    print("Invalid input. Please enter valid numbers (e.g., 10, -3, 4.5).")

#11 login system

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "1234"

attempts_left = 3

while attempts_left > 0:
    print("Please enter your username and password")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Check credentials
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("Login successful!")
        break
    elif attempts_left > 1:
        attempts_left -= 1
        print(f"Incorrect login, try again. Attempts left: {attempts_left}")
    else:
        # Last attempt failed
        print("Incorrect login. No attempts left. Program exiting.")
        attempts_left -= 1