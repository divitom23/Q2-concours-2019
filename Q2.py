x = int(input())
y = 0
parking = 0
park1 = input()
list = [*park1]
park2 = input()
list2 = [*park2]
for i in range(x):
    if list[y] == "C":
        if list[y] == list2[y]:
            parking = parking + 1
    y = y + 1
print(parking)
