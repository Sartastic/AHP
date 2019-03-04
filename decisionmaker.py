import ahp as ahplib

print("Hello this is Mr. Decision Maker Man")
print("We're gonna start reaaaaal simple: deciding between TWO things!\n")

altcount = 2
alt = []
for i in range(altcount):
    alt.append(input("Name Alternative {}: ".format(i+1)))

print("\nOkay now how are we gonna rank these guys?  Come up with THREE criteria!")

critcount = 3
crit = []
for i in range(critcount):
    crit.append(input("Name Criteria {}: ".format(i+1)))

print("\ncool!!\n")
print("Your alternatives are:\n\t", alt)
print("Your criteria are:\n\t", crit)

a1 = ahplib.ahp()
a1.esecuzione(alt,crit,[],[],grafico="no")
