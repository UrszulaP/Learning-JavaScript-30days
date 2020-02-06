# 1. Filter the list of inventors for those who were born in the 1500's
result = list(filter(lambda x: x["year"] >= 1900 and x["year"] < 2000, inventors))
print(result)

# ZMIENIĆ NA LISTĘ STRINGÓW
# 2. Give us an array of the inventors first and last names
result = list(map(lambda x: {x["first"], x["last"]}, inventors))
print(result)

# REVERSE = FALSE ?
# 3. Sort the inventors by birthdate, oldest to youngest
result = sorted(inventors, key=(lambda x: x["year"]), reverse=True) # sorted() creates a new list
# WRONG: result = inventors[:].sort(reverse=True, lambda x: x["year"]) - sort() doesn`t work on list copy
print(result)

# REDUCE, SUMA ŻYCIA WSZYSTKICH, NIE WSPÓLNY CZAS
# 4. How many years did all the inventors live all together?
first_dead = min(list(map(lambda x: x["passed"], inventors)))
last_born = max(list(map(lambda x: x["year"], inventors)))
result = first_dead - last_born
print(result)

# OD NAJDŁUŻEJ DO NAJKRÓCEJ
# 5. Sort the inventors by years lived
result = sorted(inventors, key=(lambda x: x["passed"] - x["year"]))
print(result)


# 6. create a list of Boulevards in Paris that contain 'de' anywhere in the name
# https://en.wikipedia.org/wiki/Category:Boulevards_in_Paris

# LISTA PEOPLE, NIE INVENTORS
# 7. Sort the people alphabetically by last name
result = sorted(inventors, key=(lambda x: x["last"]))
print(result)


# 8. Reduce Exercise, Sum up the instances of each of these
