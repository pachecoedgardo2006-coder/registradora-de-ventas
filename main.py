# Import the function and the list from the 'registrar' module
from registrar import Add_sale
from registrar import Sales

# Display initial menu options
print("--- MENU ---")
print("1. Add sale \n2. Exit system\n")

# Capture user option
flag = input("Select Option: ")

# Loop to continue adding sales as long as the option is "1"
while flag == "1":
    Add_sale() # Calls the function to register a new product
    print("\n--- MENU ---")
    print("1. Add sale \n2. Exit system\n")
    flag = input("Select option: ")

# Display detailed list of all sales made
print("\nSales history")
for s in Sales:
    print(f"Product Name: {s['product']} | Quantity sold: {s['quantity']} |Price per unit: ${s['unit price']} | Total ${s['total']}")
 
# Calculate the total amount by summing the 'total' key values in each dictionary
total_sum = sum(s['total'] for s in Sales)

# Display the final accumulated total sum
print(f"\nAccumulated total of all sales: ${total_sum}")

