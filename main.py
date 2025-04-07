# Input statements
salary = float(input())
numDependents = float(input())


# Calculate taxes here
State_Tax_Rate = 0.065 #6.5% state tax rate
Federal_Tax_Rate = 0.28 #28% federal tax rate
Dependent_Deduction_Rate = 0.025 #2.5 deduction per dependent


#Calculate taxes and deductions
stateTax = salary * State_Tax_Rate
federalTax = salary * Federal_Tax_Rate
depdendentDeduction = salary * Dependent_Deduction_Rate * numDependents


# Calculate total withholding and take home pay
totalWithholding = stateTax + federalTax - depdendentDeduction # Subtract deductions because of dependents
takeHomePay = salary - totalWithholding


# Output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(depdendentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))