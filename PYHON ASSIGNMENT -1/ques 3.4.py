basic_salary = float(input("Enter basic salary: "))

if basic_salary >= 20000:
    DA = 0.3 * basic_salary
    HRA = 0.2 * basic_salary
else:
    DA = 0.2 * basic_salary
    HRA = 0.1 * basic_salary

print("DA:", DA)
print("HRA:", HRA)
