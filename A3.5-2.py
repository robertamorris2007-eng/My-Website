print("Enter 5 menu items and their prices:")

item1 = input("Enter item 1: ")
price1 = float(input("Enter price for " + item1 + ": "))

item2 = input("Enter item 2: ")
price2 = float(input("Enter price for " + item2 + ": "))

item3 = input("Enter item 3: ")
price3 = float(input("Enter price for " + item3 + ": "))

item4 = input("Enter item 4: ")
price4 = float(input("Enter price for " + item4 + ": "))

item5 = input("Enter item 5: ")
price5 = float(input("Enter price for " + item5 + ": "))


while (search := input("\nEnter an item to search (or type 'exit' to quit): ")) != "exit":
    
    if search == item1:
        print(item1, "costs", price1)
    elif search == item2:
        print(item2, "costs", price2)
    elif search == item3:
        print(item3, "costs", price3)
    elif search == item4:
        print(item4, "costs", price4)
    elif search == item5:
        print(item5, "costs", price5)
    else:
        print("Error: Item not found. Try again.")
        continue   

    
    stop = input("Do you want to stop searching? (yes/no): ")
    if stop == "yes":
        break

print("Exiting program...")
