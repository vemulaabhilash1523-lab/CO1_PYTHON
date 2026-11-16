from decimal import Decimal

BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")

FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")


def rate_per_litre(fat, snf):
	"""Calculate milk rate."""
	fat_steps = round((fat - STANDARD_FAT) / Decimal("0.1"))
	snf_steps = round((snf - STANDARD_SNF) / Decimal("0.1"))

	return (
		BASE_RATE
		+ fat_steps * FAT_STEP_VALUE
		+ snf_steps * SNF_STEP_VALUE
	)


def payout(litres, fat, snf):
	"""Calculate milk payment."""
	return litres * rate_per_litre(fat, snf)


if __name__ == "__main__":
	entries = [
		(Decimal("10"), Decimal("3.5"), Decimal("8.5")),
		(Decimal("8.5"), Decimal("4.2"), Decimal("8.7")),
		(Decimal("12"), Decimal("3.1"), Decimal("8.3")),
	]

	for litres, fat, snf in entries:
		rate = rate_per_litre(fat, snf)
		payment = payout(litres, fat, snf)
		print("Rate =", rate)
		print("Payment =", payment)
		print()
