# Mayank Chapaneri 
# id 22050908
print(("Melanie Dental Clinic").center(100))
P_name=input(("Enter patient's name: "))
Cleaning=input("Was cleaning performed? (y/n): ")
Cavity_yn=input("Was cavity-filling performed? (y/n): ") 
xray=input("Was X-Ray performed? (y/n): ")
count=0
if Cleaning=="y":
    count+=60
if Cavity_yn=="y":
    count+=200
if xray=="y":
    count+=100

if count>300:
    count=count-count*(0.10)
elif count>200:
    count=count-count*(0.5)
else:
    pass
output=count*0.15
print("\n")
print("Melanie Dental Clinic")
print(("-"*150).center(100))
print("Receipt for patient name: ",P_name)
print("-"*150)
print(" Subtotal: ",count)
print("      Tax: ",output)
print("-"*150)
print("    total: ",count+output)

