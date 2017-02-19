
f = open("sum.data", "r")

if not f:
   print("Il file verra' creato automotacamente se non esiste")


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


  

