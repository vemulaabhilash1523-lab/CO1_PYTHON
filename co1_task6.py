from decimal import Decimal
 
BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
 
 
def validate_entry(farmer_id, litres, fat, snf, shift):
	"""Validate milk collection entry"""
 
	if farmer_id == "":
		return False
 
	if litres < 0:
		return False
 
	if not (Decimal("2.0") <= fat <= Decimal("7.0")):
		return False
 
	if shift.lower() not in ["morning", "evening"]:
		return False
 
	return True
 
 
def rate_per_litre(fat, snf):
	"""Calculate rate per litre"""
 
	fat_steps = round((fat - STANDARD_FAT) / Decimal("0.1"))
	snf_steps = round((snf - STANDARD_SNF) / Decimal("0.1"))
 
	rate = (BASE_RATE +
			fat_steps * FAT_STEP_VALUE +
			snf_steps * SNF_STEP_VALUE)
 
	return rate
 
 
def payout(litres, fat, snf):
	"""Calculate payment amount"""
 
	rate = rate_per_litre(fat, snf)
 
	return litres * rate
 
 
def ten_day_total(records):
	"""Calculate total payment"""
 
	total = Decimal("0.00")
 
	for record in records:
		litres, fat, snf = record
		total += payout(litres, fat, snf)
 
	return total
 
 
records = [
(Decimal("10"), Decimal("3.5"), Decimal("8.5")),
(Decimal("8.5"), Decimal("4.2"), Decimal("8.7")),
(Decimal("12"), Decimal("3.1"), Decimal("8.3"))
]
 
total = ten_day_total(records)
 
print("Ten-Day Total =", total)
