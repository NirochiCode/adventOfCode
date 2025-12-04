
result = 0

with open ("2025/2-advent.txt") as data:

    for line in data:

        blocks = line.split(",")

        for bl in blocks:

            a, b = bl.split("-")

            partA = int(a)
            partB = int(b)

            for number in range(partA, partB + 1):

                s = str(number)

                if s[0] == '0':
                    continue

                if len(s) % 2 == 0:

                    half = len(s) // 2

                    firstPart = s[:half]
                    secondPart = s[half:]

                    if firstPart == secondPart:
                            
                        result += number

print(result)     