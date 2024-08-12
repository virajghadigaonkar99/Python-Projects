# Inpute we need from the users
# Total rent
# Total food ordered for snacking
# Electricity units spend 
# Charge per unit
# Persons living in home

## Output = Total amount you have to pay is:

rent = int(input("Enter your house rent:"))
food = int(input("Enter the amount of food order:"))
electricity_spend = int(input("Enter the total of electricity spend:"))
charge_per_unit = int(input("Charge per unit:"))
persons = int(input("Enter the No.of persons living in room:"))

total_bill = electricity_spend * charge_per_unit

output =  (food + rent +total_bill)// persons

print("Each person will pay= ",output)

