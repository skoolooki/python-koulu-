# =========================
# Exercise 1: Names List
# =========================
print("\n--- Exercise 1: Names List ---")

names = ["Koralli", "Manteli", "Kinuski"]

for name in names:
    print(name)


# =========================
# Exercise 2: Personalized Messages
# =========================
print("\n--- Exercise 2: Personalized Messages ---")

for name in names:
    print(f"Hi {name}, I hope you're having a great day!")


# =========================
# Exercise 3: Transportation Preferences
# =========================
print("\n--- Exercise 3: Transportation Preferences ---")

vehicles = ["bicycle", "bus", "train", "car"]

for vehicle in vehicles:
    if vehicle == "bicycle":
        print(f"{vehicle.title()}: Great for short trips and it's healthy.")
    elif vehicle == "bus":
        print(f"{vehicle.title()}: Convenient for getting around the city without parking stress.")
    elif vehicle == "train":
        print(f"{vehicle.title()}: Comfortable and fast for longer travel between cities.")
    elif vehicle == "car":
        print(f"{vehicle.title()}: Flexible and useful when carrying groceries or traveling with family.")


# =========================
# Exercise 4: Dinner Invitations
# =========================
print("\n--- Exercise 4: Dinner Invitations ---")

guests = ["Jeesus", "Leonardo da Vinci", "Fyodor dostoyefsky"]

for guest in guests:
    print(f"Dear {guest}, you are warmly invited to dinner this Friday at 7 PM. It would be an honor to host you!")


# =========================
# Exercise 5: Guest List Update
# =========================
print("\n--- Exercise 5: Guest List Update ---")

canceled_guest = "Jeesus"
print(f"Canceled guest: {canceled_guest}")

# remove the unavailable guest
guests.remove(canceled_guest)

# add a replacement guest
guests.append("Nikolai")

print("\nUpdated invitations:")
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner this Friday at 7 PM. Looking forward to seeing you!")


# =========================
# Exercise 6: Expanding the Guest List
# =========================
print("\n--- Exercise 6: Expanding the Guest List ---")

print("Good news! I found a bigger table, so I can invite more guests!")

# add to beginning
guests.insert(0, "Albert Einstein")

# add to middle
middle_index = len(guests) // 2
guests.insert(middle_index, "Frida Kahlo")

# add to end
guests.append("Martin Luther King Jr.")

print("\nExpanded invitations:")
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner this Friday at 7 PM. Please join us!")


# =========================
# Exercise 7: Shrinking the Guest List
# =========================
print("\n--- Exercise 7: Shrinking the Guest List ---")

print("Unfortunately, the bigger table won't arrive in time. I can only invite two people.")

while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry {removed}, I can't invite you to dinner this time.")
    print(f"Current guest list: {guests}")

# confirm remaining two guests
print("\nFinal confirmations:")
for guest in guests:
    print(f"{guest}, you're still invited! See you at dinner.")

# empty the list
del guests[:]
print("\nGuest list after dinner (should be empty):")
print(guests)


# =========================
# Exercise 8: Favorite Places
# =========================
print("\n--- Exercise 8: Favorite Places ---")

places = ["Kyoto", "London", "New Zealand", "Mikkeli", "Tokyo"]

print("Original order:")
print(places)

print("\nAlphabetical order (temporary):")
print(sorted(places))

print("\nReverse alphabetical (temporary):")
print(sorted(places, reverse=True))

print("\nPermanently sorted alphabetically:")
places.sort()
print(places)

print("\nPermanently reversed order:")
places.reverse()
print(places)


# =========================
# Exercise 9: Modifying Lists
# =========================
print("\n--- Exercise 9: Modifying Lists ---")

activities = ["reading", "running", "coding", "cooking", "music"]

print("Original activities:")
print(activities)

# change one item using indexing
activities[1] = "swimming"
print("\nAfter changing one item:")
print(activities)

# add a new item
activities.append("photography")
print("\nAfter adding a new item:")
print(activities)

# remove an item using del()
del activities[3]
print("\nAfter deleting one item:")
print(activities)


# =========================
# Exercise 10: Numerical Lists
# =========================
print("\n--- Exercise 10: Numerical Lists ---")

squares = [n**2 for n in range(1, 11)]

print("Square numbers (1^2 to 10^2):")
for value in squares:
    print(value)

print("\nMinimum:", min(squares))
print("Maximum:", max(squares))
print("Sum:", sum(squares))