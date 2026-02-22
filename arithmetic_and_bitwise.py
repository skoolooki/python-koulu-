#1. Basic coding

oneA = float(input("Enter the first number:"))
oneB = float(input("Enter the second number"))


print(f"Addition: {oneA + oneB}")
print(f"Substraction: {oneA - oneB}")
print(f"Multiplication: {oneA * oneB}")


# Handle division and modulus by zero
if oneB != 0:
    print(f"Division: {oneA / oneB}")
    print(f"Modulus: {oneA % oneB}")
else:
    print("Division: Undefined (cannot divide by zero)")
    print("Modulus: Undefined (cannot mod by zero)")

print(f"Exponentiation: {oneA ** oneB}")

#2. Evaluate the following 
result = (5 + 3) * 2 ** 2 // 3 - 4
# result = 6
# Steps: (5 + 3) = 8, 
# 8 * 2 ** 2 // 3 - 4, 
# 2 ** 2 = 4, 
# 8 * 4 // 3 - 4, 
# 8 * 4 = 32, 
# 32 // 3 = 10, 
# 10 - 4,
# 10 - 4 = 6
print(result)

#3. Error indentification.
# Error: ZeroDivisionError: division by zerp
# Correction:
threeA = 10
threeB = 0

if b != 0:
    print(threeA / threeB)
    print(threeA // threeB)
else:
    print("Cannot divide by zero.")

#4. Coding challenge
# A)
fourN = int(input("Enter a number: "))

if fourN < 0:
    print("Negative numbers cannot be perfect squares (in real numbers).")
else:
    root = int(fourN ** 0.5)       
    if root ** 2 == fourN:
        print(f"{fourN} is a perfect square.")
    else:
        print(f"{fourN} is NOT a perfect square.")

# B)
fourA = float(input("Enter side a: "))
fourB = float(input("Enter side b: "))

hypotenuse = (fourA ** 2 + fourB ** 2) ** 0.5

print(f"The hypotenuse is: {hypotenuse}")

#5. Decimal ↔ Binary Conversion
print("Input:")
fiveDec = int(input("Enter a decimal number: "))

fiveBinary = bin(fiveDec)

fiveBack_to_decimal = int(fiveBinary[2:], 2)

print("\nOutput:")
print("Binary:", fiveBinary)
print("Decimal:", fiveBack_to_decimal)

#6. Logical Thinking: Bitwise Operations
print("Input:")
sixA = int(input("Enter first integer: "))
sixB = int(input("Enter second integer: "))

print("\nOutput:")
print(f"a (decimal): {sixA}, a (binary): {bin(sixA)}")
print(f"b (decimal): {sixB}, b (binary): {bin(sixB)}\n")

print("Operations:")
print(f"a & b = {sixA & sixB}   (binary: {bin(sixA & sixB)})")
print(f"a | b = {sixA | sixB}   (binary: {bin(sixA | sixB)})")
print(f"a ^ b = {sixA ^ sixB}   (binary: {bin(sixA ^ sixB)})")
print(f"~a    = {~sixA}   (binary: {bin(~sixA)})")

#7. Data masking
print("Input:")
sevenN = int(input("Enter a number: "))

sevenMasked = sevenN & 0b11110000   # keeps top 4 bits, clears last 4 bits (8-bit style)

print("\nOutput:")
print(f"Masked: {sevenMasked} (Binary: {bin(sevenMasked)})")

#8. Bitwise Image Data
print("Input:")
eightPixel = int(input("Pixel value: "))
eightMask = int(input("Mask: "))

eightNew_pixel = eightPixel ^ eightMask

print("\nOutput:")
print(f"New pixel value: {eightNew_pixel} (Binary: {bin(eightNew_pixel)})")

#9. Custom Binary
print("Input:")
nineA = int(input("Enter first number: "))
nineB = int(input("Enter second number: "))
nineOp = input("Enter operator (&, |, ^, <<, >>): ").strip()

if nineOp == "&":
    result = nineA & nineB
elif nineOp == "|":
    result = nineA | nineB
elif nineOp == "^":
    result = nineA ^ nineB
elif nineOp == "<<":
    result = nineA << nineB
elif nineOp == ">>":
    result = nineA >> nineB
else:
    result = None

print("\nOutput:")
if result is None:
    print("Invalid operator. Please use one of: &, |, ^, <<, >>")
else:
    print(f"Result: {result}")

#10. Symmetric key
print("Input:")
plaintext = int(input("Plaintext: "))
key = int(input("Key: "))

ciphertext = plaintext ^ key
decrypted = ciphertext ^ key

print("\nOutput:")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted}")