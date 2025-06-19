Cafe_Menu = {
    "Pizza": 100, "Burger": 70, "Toast": 55, "Clubsandwich": 60,
    "FrenchFries": 55, "Nachos": 50, "Bhajis": 45, "Patties": 40,
    "Soda": 35, "Coke": 40, "ColdCoffee": 55, "Tea": 20
}

def Billing_Bill(Menu):
    Billing_Cart = []
    print("The Menu is")
    print("*" * 20)
    serial_no = 1

    for Food, Price in Menu.items():
        print(f"{serial_no}.{Food:<17}{Price:>10} ₹") 
        serial_no += 1

    while True:
        while True:
            try:
                User_Order = int(input("\nEnter the number of Item in menu to add item to cart: "))
            except:
                print("Please enter a valid number.")
                continue

            Comp_order = User_Order - 1 

           
            if 0 <= Comp_order < len(Menu):
                Order_item = list(Menu)[Comp_order]  
                print(f"{Order_item} added to the cart")
                break
            else:
                print("Please Enter the valid item number from the Menu") 

        while True:
            try:
                Quantity = int(input("Enter the quantity of item to add up: "))
            except:
                print("Please enter a valid number.")
                continue

            if Quantity > 0:
                break
            else:
                print("Please enter a valid quantity") 

        total = 0

        
        Price_value = Menu[Order_item]  
        total += Quantity * Price_value

        Billing_Cart.append((Order_item, Price_value, Quantity, total))
        print(f"{Quantity} of {Order_item} are added to cart.")

        Order_continue = input("If you want to continue ordering, type 'Yes'; else type 'Done': ").lower().strip()
     
        if Order_continue == "done":
            break

    print("\nThe Bill for Maddy's Cafe")
    print("*" * 35)
    Final_bill = 0
    for Order_item, Price_value, Quantity, total in Billing_Cart:
        print(f"{Order_item:<20} @ {Price_value:>5} x {Quantity:<3} = {total}")
        Final_bill += total

    print("*" * 35)
    print(f"Total Bill:{Final_bill:>25} ₹")
    print("You're welcome again for having food!")
    print("Thank you for visiting.")

Billing_Bill(Cafe_Menu)
