Menu = {"Pizza" : 110 , "Burger" : 80 , "Coffee" : 50 , "Tea" : 30} 
a = ("The Menu")
b=1
print(f"{a:^17}")
print("_"*20)

total = 0 
print("Please tell the order Sir/Madam ^^")
order_cart = []
while True :
    b = 1  # ✅ Fix: Reset b every time the menu is shown
    for Item , Price in Menu.items():
        print(f"{b:>2}.{Item :<10}{Price:>15} ₹")
        b+=1
    print("*"*20)   
    
    Order_Item = input("Enter the product You want \n or Say Done When order are over from your side \t ").capitalize()
    if Order_Item == "Done" :
        break 
    while True :
        if Order_Item in Menu:
            break 
        else:
            print("Please check if the item is in the Menu  ") 
            Order_Item = input("Re-enter the product: ").capitalize()
        
    while True : 
        qut = int(input("Enter the quantity You want to have : "))
        if qut > 0 :
            break 
        else:
            print("Please enter valid number ") 
    
    item_price = qut * Menu[Order_Item]  # ✅ Fix: Use correct price from Menu
    total += item_price
      
    order_cart.append((Order_Item , qut , item_price)) 
    print(f"{Order_Item} X {qut} is added to bill")

print("***Final Bill***")
grand_total = 0 
for Item , qut , item_price in order_cart:  # ✅ Fix: Correct unpacking
    print(f"{Item:<15} x{qut:<3} @ {item_price//qut:<3} ₹ = {item_price} ₹")
    grand_total += item_price

print("-" * 35)
print(f"{'TOTAL':<25}{grand_total} ₹")
print("🧾 Thank you for ordering!\n")
