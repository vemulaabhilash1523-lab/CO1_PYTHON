from decimal import Decimal
 
BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
 
fat = Decimal("4.2")
snf = Decimal("8.7")
litres = Decimal("10")
 
fat_steps = round((fat - STANDARD_FAT) / Decimal("0.1"))
snf_steps = round((snf - STANDARD_SNF) / Decimal("0.1"))
 
rate = (
BASE_RATE
+ fat_steps * Decimal("0.40")
+ snf_steps * Decimal("0.30")
)
 
payment = litres * rate
 
print("Rate =", rate)
print("Payment =", payment)
