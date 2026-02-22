#1
for oneI in range(1, 11):
    print(oneI)

#2
for twoI in range(10, 0, -1):
    print(twoI)

#3
for threeI in range(2, 21, 2):
    print(threeI)

#4
fourNumber = int(input("Enter a number: "))

for fourI in range(1, 11):
    print(f"{fourNumber} x {fourI} = {fourNumber * fourI}")

#5
fiveTotal = 0

for fiveI in range(1, 101):
    fiveTotal += fiveI

print("The sum from 1 to 100 is:", fiveTotal)

#6
sixFoods = ["Pizza", "Sushi", "Pasta", "Tacos", "Ice cream"]

for sixFood in sixFoods:
    print(f"{sixFood} is delicious!")

#7
sevenNumbers = [12, 45, 67, 89, 23]

sevenLargest = sevenNumbers[0]  # start by assuming the first is the largest

for sevenNum in sevenNumbers:
    if sevenNum > sevenLargest:
        sevenLargest = sevenNum

print("The largest number is", sevenLargest)

#8
import random

eightSecret = random.randint(1, 10)

eightGuess = int(input("Guess a number between 1 and 10: "))

while eightGuess != eightSecret:
    if eightGuess > eightSecret:
        print("Too high, try again!")
    else:
        print("Too low, try again!")
    
    eightGuess = int(input("Guess again: "))

print("Correct! You guessed it!")

#9
for nineI in range(1, 21):
    if nineI % 3 == 0:
        continue
    print(nineI)

#10
tenSquares = [tenI ** 2 for tenI in range(1, 11)]
print(tenSquares)