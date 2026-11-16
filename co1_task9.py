def test_payment():
    test_cases = [
        (10, 3.5, 8.5, 300.00),
        (10, 4.2, 8.7, 334.00),
        (12, 3.1, 8.3, 333.60)
    ]

    for litres, fat, snf, expected in test_cases:
        fat_steps = round((fat - 3.5) / 0.1)
        snf_steps = round((snf - 8.5) / 0.1)

        rate = 30 + fat_steps * 0.40 + snf_steps * 0.30
        payment = litres * rate

        print("Expected:", expected)
        print("Actual:", payment)


test_payment()
