import ahp as ahplib
a1 = ahplib.ahp()
a1.separatore()
print("SIMPLE AHP TOOL")
a1.separatore()

altcount = int(input("How many alternatives are you considering? "))
alt = []
for i in range(altcount):
    alt.append(input("\tName Alternative {}: ".format(i+1)))

critcount = int(input("And how many criteria are you going to use to rank your alternatives? "))
crit = []
for i in range(critcount):
    crit.append(input("\tName Criteria {}: ".format(i+1)))

# print("Your alternatives are:\n\t", alt)
# print("Your criteria are:\n\t", crit)

a1.esecuzione(alt,crit,[],[],grafico="no")