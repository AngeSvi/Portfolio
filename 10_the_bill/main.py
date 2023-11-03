#link to replit : https://replit.com/@AngelineSauvi/day-10100-days-THE-BILL

"""Output : equal bill for each guest"""

myBill = float(input("How much is the bill ? (€) > "))
numberOfPeople = int(input("How many people are paying ? > "))
tip = float(input("What % of the tip will they leave to be added to the total bill ? > "))
bill_tip = myBill * tip / 100 + myBill
answer = bill_tip / numberOfPeople
answer = round(answer, 2) #garde deux chiffres apres la virgule
print("You all owe", answer)