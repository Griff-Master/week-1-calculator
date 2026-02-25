print("1. Add(+)")
print("2. Subtract(-)")
print("3. Multiply(*)")
print("4. Devide(/)")
choice = input("Enter your choice(1-4): ")
if choice in["1","2","3","4"]:
   num1 = int(input("Enter your first number: "))
   num2 = int(input("Enter your second number: "))
if choice =="1": 
    print("Result:",num1+num2)
elif choice =="2":
 print("Result: ",num1-num2)

elif choice == "3":
 print("Result: ",num1*num2)

elif choice == "4":
  if num2==0:
       print("Error: You can't devide by 0.")
  else:
    print("Result: ",num1/num2)
else:
  print("Invalid choice")