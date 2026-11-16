from decimal import Decimal

float_total = 0.0

for i in range(300):
    float_total += 283.90

decimal_total = Decimal("0.00")

for i in range(300):
    decimal_total += Decimal("283.90")

print("Float Total =", float_total)
print("Decimal Total =", decimal_total)
