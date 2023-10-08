PHT = float(input("entrer PHT de produit :"))
cat = input(entrer la catégorie de produit :")
if cat =="A" :
print("le prix TTC de produit est :",PHT+PHT*0.07)
elif cat == "B" :
print("le prix TTC de produit est :",PHT+PHT*0.2)
elif cat == "C" :
print("le prix TTC de produit est :",PHT+PHT*0.25)
else:
print("la catégorie nexiste pas")


