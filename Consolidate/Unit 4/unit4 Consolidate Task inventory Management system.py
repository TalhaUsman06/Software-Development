# Unit 4 Consolidate Task

# Inventory Management system that uses
# different data types

# String
product_name= "Mx Airbuds Pro"

# Integer
quantity= 10

# Float
unit_price= 29.99

# Boolean
available= True

# to calculate total value of the inventory


print("\n*** Menu ***")
print("Press 1 to Display Inventory")
print("Press 2 for Updating Inventory")
print("Press 3 to Exit")

choice= input("\nEnter your choice: ")
print("\n\n*** Inventory Management System ***")

if choice == "1":
    print("\n\tProduct: ",product_name)
    print("\tQuanitity: ",quantity)
    print("\tPrice $: ",unit_price)
    invetory_value= quantity * unit_price
    print("\tInventory Value $: ",invetory_value)
    
elif choice =="2":
    quantity = int(input("Enter new Quantity avialable in Inventory: "))
    
    print("** Updated Inventory ***\n")
    print("\tProduct: ",product_name)
    print("\tQuanitity: ",quantity)
    print("\tPrice $: ",unit_price)
    invetory_value= quantity * unit_price
    print("\tInventory Value $: ",invetory_value)
    
elif choice == "3":
    print("\t......Exiting Program!!!")
    
else:
    print("Invalid Choice, TRY AGAIN!!")
    
    
