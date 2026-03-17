factorial =int(input("Enter a number -->"))


for multiplier in range(factorial-1, 1, -1):
    factorial *=multiplier
print(f"The factorial is ---->{factorial}")
