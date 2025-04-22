print("Welcome to the Tip Calculator!")

t_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10%, 12%, or 15%? "))
no = float(input("How many people to split the bill?"))

pay01 = (float((t_bill * (1 + (tip / 100))) / no))
pay = round(pay01,2)

print(f"Each person should pay: ${pay}")
