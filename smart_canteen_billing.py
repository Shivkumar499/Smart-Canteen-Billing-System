print("======SMART CANTEEN======")
subtotal=0
item_count=0
receipt=" "
while True:
  print("\n1.Veg Sandwich-Rs.60")
  print("2.Masala Dosa-Rs.80")
  print("3.Chole Rice-Rs.85")
  print("4.Paneer Roll-Rs.100") 
  print("5.Tea-Rs.20")

  choice=int(input("choose item number:"))
  if  choice==1:
        item="Veg Sandwich"
        price=60
  elif choice==2:
        item="Masala Dosa"
        price=80
  elif choice==3:
        item="Chole Rice"
        price=85
  elif choice==4:
        item="Paneer Roll"
        price=100
  elif choice==5:
        item="Tea"
        price=20
  else:
       print("invalid choise")
       continue
  quantity=int(input("enter the quantity:"))
  if quantity<=0:
      print("invalid quantity:!")

 #item ki total cost
  cost=price*quantity
  subtotal=subtotal+cost
 #selected item  receipt mein add
  receipt= receipt+f"{item}X{quantity}:Rs{cost:.2f}\n"
  print(f"Added:{item}X{quantity}:Rs.{cost:.2f}")
  again=input("add another item? (y/n):").lower() 
  if again=="n":
      break
if subtotal==0:
       print("no order placed:")
else:
    #subtotal ke according discount
   if subtotal>=500:
        discount=subtotal*0.10
   elif subtotal>=250:
        discount=subtotal*0.05
   else:
        discount=0                                                  
   final_total=subtotal-discount
   #display receipt
   print("\n=======RECEIPT=======")
   print(receipt)
   print(f"Subtotal:Rs{subtotal:.2f}")
   print(f"Dicount:Rs{discount:.2f}")    
   print(f"Final total:Rs{final_total:.2f}")
   print("Thank you!")