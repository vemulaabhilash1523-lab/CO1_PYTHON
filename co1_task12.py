from decimal import Decimal
 
def bonus(total_litres):
 
	if total_litres > 500:
		return total_litres * Decimal("0.50")
 
	return Decimal("0.00")
 
 
total_litres = Decimal("550")
 
bonus_amount = bonus(total_litres)
 
print("Bonus =", bonus_amount)
