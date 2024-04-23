principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (in %): "))
time = float(input("Enter time period (in years): "))

compound_interest = principal * ((1 + rate / 100) ** time - 1)

print("Compound interest:", compound_interest)
