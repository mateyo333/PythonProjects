principal_amount = 1000.0
interestRate = 0.05
time = 3

# Calculate the total interest earned over 3 years
interest_earned = principal_amount * interestRate * time

# Calculate the new principal (original principal + total interest)
newPrincipal = principal_amount + interest_earned

print("The total interest earned after 3 years is: $", interest_earned)
print("Your new principal after 3 years is: $", newPrincipal)