cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
for x in cars:
    print(x)

cars[0] = "Toyota"

for x in cars:
    print(x)

x = len(cars)
print(x)
cars.append("Honda")

for x in cars:
    print(x)

cars.pop(0)

for x in cars:
    print(x)

cars.remove("Volvo")
for x in cars:
    print(x)