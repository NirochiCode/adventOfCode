# linke rechte liste erstellen
leftSite = []
rightSite = []

# zahlen aus der Liste auslesen
with open("2024/1-advent-input.txt") as f:
    for line in f:

        parts = line.split()

        leftSite.append(int(parts[0]))
        rightSite.append(int(parts[1]))

result = 0

# schaue wie oft die Zahl in der Rechten Seite vorkommt und die schleife läuft mit der Anzahl der Zeilen von der Linken Seite
for x in leftSite:

    x_count = rightSite.count(x)

    result += x * x_count

print(result)
