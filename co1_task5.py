from decimal import Decimal

try:
    farmer_id = input("Enter Farmer ID: ").strip()
    litres = Decimal(input("Enter Litres: "))
    fat = Decimal(input("Enter Fat Percentage: "))
    snf = Decimal(input("Enter SNF Percentage: "))
    shift = input("Enter Shift (Morning/Evening): ").strip()

    if farmer_id == "":
        print("Error: Farmer ID cannot be empty")

    elif litres < 0:
        print("Error: Litres cannot be negative")

    elif not (Decimal("2.0") <= fat <= Decimal("7.0")):
        print("Error: Fat percentage out of range")

    elif shift.lower() not in ["morning", "evening"]:
        print("Error: Invalid shift")

    else:
        print("Valid Entry")
        print("Farmer ID :", farmer_id)
        print("Litres :", litres)
        print("Fat :", fat)
        print("SNF :", snf)
        print("Shift :", shift)

except Exception:
    print("Error: Invalid numeric input")
