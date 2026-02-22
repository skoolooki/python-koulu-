# Exercise 1
fruits = ("apple", "banana", "cherry", "orange", "mango")

print("Entire tuple:", fruits)
print("First item:", fruits[0])
print("Last item:", fruits[-1])

# Trying to change an item (this will cause an error)
fruits[1] = "grape"

# Exercise 2
fruits = ("apple", "banana", "cherry", "orange", "mango")

for fruit in fruits:
    print(fruit)

# Exercise 3
colors = {"red", "blue", "green", "yellow", "purple"}
print("Original set:", colors)

colors.add("blue")  # duplicate
print("After adding duplicate 'blue':", colors)

# Exercise 4
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "date", "fig"}

# Intersection (common elements)
print("Intersection:", set1 & set2)

# Union (all unique elements)
print("Union:", set1 | set2)

# Difference (in set1 but not in set2)
print("Difference (set1 - set2):", set1 - set2)

# Exercise 5
person = {
    "name": "Alice",
    "age": 25,
    "city": "Helsinki"
}

print("Person's name:", person["name"])

# Add a new key-value pair
person["favorite_color"] = "blue"

# Change age
person["age"] = 26

print("Updated dictionary:", person)

# Exercise 6
person = {
    "name": "Alice",
    "age": 26,
    "city": "Helsinki",
    "favorite_color": "blue"
}

for key, value in person.items():
    print(key, ":", value)

# Exercise 7
favorite_foods = {
    "Emma": "Pizza",
    "Liam": "Sushi",
    "Sophia": "Burgers",
    "Noah": "Pasta"
}

print("Noah's favorite food:", favorite_foods["Noah"])

# Add a new friend
favorite_foods["Olivia"] = "Tacos"

# Remove Liam
favorite_foods.pop("Liam")

print("Updated favorite foods:", favorite_foods)

# Exercise 8
sentence = input("Enter a sentence: ")
words = sentence.split()

word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)

# Exercise 9
sentence = input("Enter a sentence: ")
words = sentence.split()

unique_words = set(words)

print("Unique words:", unique_words)

# Exercise 10
books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]

for book in books:
    print(book["title"], "-", book["author"])
