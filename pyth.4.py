price=float(input("Item price: "))
quantity=int(input("Enter the qty: "))
total=price*quantity
gst=total*0.18
print(f"Total price of the items: {total+gst}")