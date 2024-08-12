#Menu of Restaurant
menu={
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 70,
    "Coffee": 80,
    "Coke" : 40,
    "Pepsi" : 40,
}

#Greeting customers
print("Welcome to our restaurant...")
#Our menu
print("Pizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffee: Rs 80\nCoke: Rs 40\nPepsi: Rs 40")

#Start order
order_total = 0   

#Input from customer
item_1= input("Enter your order :")
if item_1 in menu:
    order_total += menu[item_1]    #0+40= 40
    print(f"Your order of {item_1} has been added to cart.")
else:
    print(f"Ordered item {item_1} is not available now.")


#If customer want to add another item in order
another_item= input("Do you want to add another item? (Yes/No)")
if another_item == "Yes":
    item_2= input("Enter your next order :")  
    if item_2 in menu:
        order_total += menu[item_2]    #40+40= 80
        print(f"Your order of {item_2} has been added to cart.")
    else:
        print("Not available")
   

#Total amount
print(f"The total amount of your order is :{order_total}")










 
