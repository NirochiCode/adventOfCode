# Listen für linke und rechte Spalte initialisieren
left_list = []
right_list = []

# Datei öffnen und Zeilen einlesen
with open("2024/1-advent-input.txt") as f:
    for line in f:
        # Zahlen aus der Zeile extrahieren und in Integer umwandeln
        parts = line.split()
        
        if len(parts) == 2:
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))

# Beide Listen sortieren
left_list.sort()
right_list.sort()

# Ergebnis-Summe initialisieren
total_distance = 0

# Annahme: Beide Listen haben die gleiche Länge
for i in range(len(left_list)):
    distance = abs(left_list[i] - right_list[i])
    total_distance += distance

# Ergebnis ausgeben
print(total_distance)
