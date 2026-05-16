families = []
colony_db = []

def calculate_bill(units):
    if units <= 100:
        charge = units * 4.22
    elif units <= 200:
        charge = (100 * 4.22) + ((units - 100) * 5.02)
    else:
        charge = (100 * 4.22) + (100 * 5.02) + ((units - 200) * 6.50)
    return charge

total_families = int(input("Enter total number of families: "))

for i in range(total_families):
    name = input(f"Enter family {i+1} name: ")
    families.append(name)

for name in families:
    print(f"\nProcessing family: {name}")
    prev = int(input("Enter the previous reading: "))
    now = int(input("Enter the current reading: "))
    
    units = now - prev
    bill = calculate_bill(units)
    
    print(f"Units consumed: {units}")
    print(f"Electricity bill: ₹{bill:.2f}")
    
    colony_db.append([name, units, bill])

print("\n--- Colony Database ---")
for data in colony_db:
    print(data)
