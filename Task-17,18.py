print("Demonsatration of Continue statement")
for char in "GeeksforGeeks":
    if char == "e":
        continue
    print(char, end=" ")

print("\nDemonsatrtion of break statement")
i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("No Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("No Break")