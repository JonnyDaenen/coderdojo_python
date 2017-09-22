# Oplossing verstoppertje
<pre>
from random import randint
import time

print("VERSTOPPERTJE")
print("--------------")

computer = "Alfred"
speler = input("Hallo! Ik ben %s. Hoe heet jij?" % computer)

print("Dag %s! Laten we verstoppertje spelen!" % speler)
verstopplaatsen = int(input("Hoeveel verstopplaatsen zijn er?"))

print("Ik ga me verstoppen!")
verstopt = randint(1, verstopplaatsen)

teller = 1
while teller <= 10:
  print(teller)
  teller += 1
  time.sleep(1)
  
print("Wie niet weg is is gezien!")

gevonden = False
pogingen = 0
while not gevonden:
  pogingen += 1   
  nummer = int(input("Er zijn %d verstopplaatsen. Waar denk je dat ik ben? Geef het nummer:" % verstopplaatsen))
  if nummer == verstopt:
    gevonden = True
    print("Je hebt me gevonden in %d poging(en)! GOED GEDAAN!" % pogingen)
  else:
    print("Fout! Probeer het nog eens!")
  </pre>
