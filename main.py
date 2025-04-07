# Input statements with prompts for user clarity
salary = float(input("Please enter salary: "))
numDependents = float(input("Please enter number of dependents: "))

# Tax rates and fixed dependent deduction amount
State_Tax_Rate = 0.065  # 6.5% state tax rate
Federal_Tax_Rate = 0.28  # 28% federal tax rate
dependent_deduction = 0.025  # 2.5% deduction per dependent

# Calculate state tax and federal tax based on the salary
stateTax = salary * State_Tax_Rate
federalTax = salary * Federal_Tax_Rate

# Calculate total tax before applying dependent deductions
totalTax = stateTax + federalTax

# Calculate dependent deduction total
dependentDeductionRate = dependent_deduction * salary * numDependents

# Apply dependent deductions to the total tax withheld
# Subtract dependent deductions from the total tax withheld (not salary)
totalWithholding = stateTax + federalTax + dependentDeductionRate

# Calculate take-home pay (salary - total withholding)
takeHomePay = salary - totalWithholding

# Output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeductionRate))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))        