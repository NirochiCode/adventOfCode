pos = 50
counter = 0
steps = 0

with open ("2025/1-advent.txt") as data:
    for line in data:

        parts = line.split()

        if parts[0][0] == "L":

            for i in range (int(parts[0][1:])):
                pos -= 1
                pos %= 100
                
                if pos == 0:
                    counter += 1
        
        elif parts[0][0] == "R":

            for i in range (int(parts[0][1:])):
                pos += 1
                pos %= 100
                
                if pos == 0:
                    counter += 1

print(counter)




    


