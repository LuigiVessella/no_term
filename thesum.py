f = open("sum.data","r")


print("Lettura dal file sum.data...: ")
line = f.readline()
num = int(line)
f.close()
   
print(" Ho letto : ", num)
num2=input("Inserisci il numero da sommare: ")
ris=num+num2

print("Il nuovo valora e' :", ris)
print("Salvataggio in sum.data...")

f = open("sum.data","w")
f.write(ris)
f.close()


  

