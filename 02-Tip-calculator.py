total_bill = float(input("What was tota the total bill? $"))
tip = int(input("How mucho tip would like to give? 10, 15, 20? "))
people_split = int(input("How many people split the bill?"))
tip_per = tip /100 + 1
total_split = float((total_bill * tip_per) / people_split)
final_amount = round(total_split)
print(f"Each person should pay: ${final_amount}")