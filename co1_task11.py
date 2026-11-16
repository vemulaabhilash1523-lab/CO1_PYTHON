from decimal import Decimal
 
BASE_RATE = Decimal("30.00")
 
def calculate_payment(litres, rate):
	return litres * rate
 
payment = calculate_payment(
Decimal("10"),
BASE_RATE
)
 
print("Payment =", payment)
