#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
total_bill=int(input("what was total bill ?"))
a=int(total_bill*10/100)
b=int(total_bill*12/100)
c=int(total_bill*15/100)
tip_from_custmer=int(input("what tip would you like to give ? ,10,12 or 15 ?"))
splitting=int(input("how many to split the bill"))
if tip_from_custmer==10:
  split=(total_bill+a)/splitting
  print(f"Every person should give {split} Rs")
elif tip_from_custmer==12:
  split=(total_bill+b)/splitting
  print(f"Every person should give {split} Rs")
elif tip_from_custmer==15:
  split=(total_bill+c)/splitting
  print(f"Every person should give {split} Rs")
else:
  print("Choose between 10 or 12 or 15")
