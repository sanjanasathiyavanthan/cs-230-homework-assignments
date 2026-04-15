"""
Class: CS230--Section 5
Name: Sanjana Sathiyavanthan
Date: 09.25.2025
Description: This is a program that calculates the cost of operating a car for five year
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""

# These are the constants for this assignment
MILES_PER_YEAR = 10000
CITY_MILES_PER_GALLON = 31
HWY_MILES_PER_GALLON = 40
DEPRECIATION_RATE = 0.08
MAINTENANCE_RATE = 0.055
INSURANCE_RATE = 0.05
YEARS = 5

# This is the heading for the inputs
print("=== Driving Costs Calculator ===\n")

# These are the inputs for this program
msrp = int(input("Sales price of car: $ "))
fuel_price = float(input("Enter fuel price per gallon: $ "))
percent_city = int(input("Enter percentage of city driving: "))



# This is the processing for this program
percent_hwy = 100 - percent_city

# This is the combined MPG formula from assignment
combined_mpg = 1 / ((percent_city/100)/CITY_MILES_PER_GALLON + (percent_hwy/100)/HWY_MILES_PER_GALLON)

# These are the formulas for fuel costs
gallons_per_year = MILES_PER_YEAR / combined_mpg
fuel_year = gallons_per_year * fuel_price
fuel_total = fuel_year * YEARS

# These are the formulas for depreciation
depreciation_year = msrp * DEPRECIATION_RATE
depreciation_total = depreciation_year * YEARS

# These are the formulas for maintenance
maintenance_year = msrp * MAINTENANCE_RATE
maintenance_total = maintenance_year * YEARS

# These are the formulas for insurance
insurance_year = msrp * INSURANCE_RATE
insurance_total = insurance_year * YEARS

# These are the total formulas
total_year = fuel_year + depreciation_year + maintenance_year + insurance_year
total_five = total_year * YEARS
cost_per_mile = total_year / MILES_PER_YEAR

# I am rounding everything to 2 decimal places
fuel_year = round(fuel_year, 2)
fuel_total = round(fuel_total, 2)
depreciation_year = round(depreciation_year, 2)
depreciation_total = round(depreciation_total, 2)
maintenance_year = round(maintenance_year, 2)
maintenance_total = round(maintenance_total, 2)
insurance_year = round(insurance_year, 2)
insurance_total = round(insurance_total, 2)
total_year = round(total_year, 2)
total_five = round(total_five, 2)
cost_per_mile = round(cost_per_mile, 2)

# This is what the output should look like
print("\n=== Ownership Cost Summary ===\n")

print("Total Driving Cost")
print("Per Year\t          $", total_year)
print("Per Mile\t          $", cost_per_mile)
print("5-Year Total\t      $", total_five)

print("\nCosts Breakdown")
print("Category\t\t Cost/Year\t    5-Year Total")
print("Fuel\t\t     $", fuel_year, "\t    $", fuel_total)
print("Maint & Repair\t $", maintenance_year, "\t    $", maintenance_total)
print("Depreciation\t $", depreciation_year,"\t    $", depreciation_total)
print("Insurance\t     $", insurance_year, "\t    $", insurance_total)


