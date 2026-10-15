# Exercice Code PIN

code_pin = int(input("Veuillez entrer le code pin : ")) #définition de la variable
if code_pin == 4567: #définition du code PIN
    print("Code correct") 
else: 
    print("code incorrect")

# Exercice signe d'un nombre

entier = int(input("Veuillez saisir un nombre entier : ")) #définition de la variable
if entier < 0 : #définition des chiffres entiers négatifs
    print("Négatif") # écrire négatif si le chiffre est inferieur à 0
elif entier == 0 : #définition du chiffre 
    print("Nul") # écrire Nul si le chriffre est 0
else: 
    print("Positif") #sinon si le chiffre est supérieur à 0 écrire positif

# Exercice Parité

chiffre = int(input("Veuillez saisir un chiffre entier : ")) # définition de la variable
if chiffre % 2 == 0: #définition du résultat
    print("chiffre pair") #Si le résultat = 0 écrire "pair"
else: 
    print("chiffre impair") # Si le résultat = 1 écrire "impair"

# Exercice Age

age = int(input("Entrez votre âge : "))
if age <= 12 :
    print("A", age, "ans, vous êtes un enfant.")
elif age <= 17 :
    print("A", age, "ans, vous êtes un adolescent.")
else :
    print("A", age, "ans, vous êtes un adulte.")

# Exercice Perte ou Profit 

fabrication = float(input("Entrez le prix de fabrication : ")) # définition de la variable
vente = float(input("Entrez le prix de vente : ")) #définition du résultat
if vente <= fabrication : #Si le prix de vente est inferieur ou égal au prix de fabrication "afficher profit"
    print("profit")
else : #Si le prix de vente est superieur au prix de fabrication "afficher perte"
    print("perte")

# Exercice Maximum
# Ce programme permet de voir quel est le plus grand nombre sur 3 nombres
premier = float(input("Entrez le premier nombre: ")) 
second = float(input("Entrez le second nombre: "))
troisième = float(input("Entrez le troisième nombre: "))
if premier > second and premier > troisième : 
    print("Le maximum est le premier nombre", premier)
elif second > premier and second > troisième :
    print("Le maximum est le second chiffre", second)
elif troisième > premier and troisième > second :
    print("Le maximum est le troisième chiffre", troisième)
    
# Exercice Triangle Rectangle 
# Ce programme détermine si c'est un triangle rectangle ou non
BC = float(input("Entrez la longueur de BC: "))
AC = float(input("Entrez la longueur de AC: "))
AB = float(input("Entrez la longueur de AB: "))
BC2 = float(AC**AB)
AC2 = float(BC**AB)
AB2 = float(BC**AC)
if AB2 > AC2 + BC2 :
    print("Le triangle est rectangle")
else :
    print("Le triangle n'est pas rectangle")

# Exercice Année Bissextile
# Ce programme sert à savoir si l'année est bissextile ou non
annee = int(input("Entrez l'année actuelle: "))
if annee%4 == 0 and annee%100 != 0 :
    print("L'année est bissextile")
else :
    print("l'année n'est pas bissextile")

# Exercice Société de Transport
# Calcul du tarif en fontion de l'âge
age = float(input("Entrez votre âge: "))
prix = 10
total = "Votre prix est de" 
if age >= 51 :
    print(total, prix*0.9,"€")
elif age <= 5 :
    print("Votre tarif est gratuit")
elif age <= 16 :
    print(total, prix*0.5,"€")
elif age <= 21 :
    print(total, prix*0.6,"€")
elif age < 51 :
    print(total, prix,"€")

#Exercice Voyage scolaire
# Calcul en fontion du nombre d'élèves et de la durée du voyage
eleve = int(input("Entrez le nombre total d'élève: "))
duree = int(input("Entrez la durée du voyage (en jours): "))
herbergement20 = 4.20
herbergement35 = 3.80
herbergement40 = 4.00
nourriture = 3.50
transport0 = 110
transport1 = 100
voyage = "Le prix du voyage est de "
if eleve <= 20 :
    print(voyage, transport0+nourriture*duree+herbergement20*duree, "€", "par élève")
elif eleve < 35 :
    print(voyage, transport1+nourriture*duree+herbergement35*duree, "€", "par élève")
elif eleve >= 35 :
    print(voyage, transport1+nourriture*duree+herbergement40*duree, "€", "par élève")

# Exercice Vinci Location

typevoiture = input("Saisir le type de vehicule: ")
typecarburant = input("Saisir le type de carburant: ")
offre = input("Souhitez vous profiter d'une offre commerciale ? (Repondez par oui ou non)")
kmloc = input("Quel distance avez vous parcouru ? (en km)")
durloc = input("Quel est la durée de la location ? (en jours)")
totloc = "Le prix total de la location est de"
citadine = 80
berline = 100
sportive = 130
essence = 1.93
diesel = 1.89
if typevoiture = citadine :
    print(totloc)