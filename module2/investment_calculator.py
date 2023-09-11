#Prabesh K Singh
#CIS131
#Date 09/04/2023

#This code snippet that calculates and displays how much money you'll have after 10, 20, and 30 years of investing $1000 at a 7% annual return rate:

# Define the initial principal amount
p = 1000  # Initial principal amount in dollars

# Define the annual rate of return as a decimal
r = 0.07  # 7% annual rate of return

# Define the list of years to calculate for
years = [10, 20, 30]

# Calculate and display the amount on deposit for each year
for n in years:
    a = p * (1 + r) ** n
    print(f"After {n} years, you'll have ${a:.2f}")
