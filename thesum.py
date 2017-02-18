f = open("sum.data", "r")

if not f:
   f = open("sum.data", "w")
   print("Il file verrà creato automotacamente se non esiste")


else:
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
ris= str(ris)
f.write(ris)
f.close()


  

