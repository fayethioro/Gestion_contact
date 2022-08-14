from genericpath import exists
import sys

#on importe le paquetage database et ses modules
from database import Connect

Menu = """
    Choississez parmi les 7 options suivantes :
    1: Ajouter un contact  
    2: Afficher la liste des contact 
    3: Supprimer un contact via son numero de telephone
    4: Supprimer un contact via son id
    5: Modifier un contact 
    6:Rechercher un contact par son numero de telephone
    7: Quitter le programme
    👉 Votre choix svp : """
Choix_menu=["1", "2", "3", "4", "5","6","7"]

def  menu() :
    connexion = Connect()
    
    while True :
        mon_choix="" 
        while mon_choix not in Choix_menu :
              mon_choix=input(Menu)
              if mon_choix not in Choix_menu :
                 print("votre choix est incorrecte")
            
        if mon_choix == "1" :
            Nom               = input("Donner votre nom : ")
            Prenom            = input("Donner votre prenom : ")
            Email             = input("Donner votre  adresse email : ")
            Numero_telephone  = int (input("Donner votre  numero de telephone : "))
            Adresse           = input("Donner votre adressse :")
            connexion.ajouter_contact(Nom,Prenom,Email,Numero_telephone,Adresse)


        elif mon_choix == "2" :
           Mes_contacts = connexion.afficher_liste_contact()
           for Mon_contact in Mes_contacts :
              print(f"{Mon_contact[0]}: Prenoms et nom :{Mon_contact[2]} {Mon_contact[1]} ,Email:{Mon_contact[3]}, telephone:{Mon_contact[4]}, Adresse:{Mon_contact[5]} ")


        elif mon_choix == "3" :
            Numero_telephone  = int (input("Donner le numero de telephone que vous voulez supprimer : "))             
            connexion.supprimer_contact_tel(Numero_telephone )
           
                


        elif mon_choix == "4" :
             identifiant  = int (input("Donner l'identifier vous voulez supprimer : ")) 
             connexion.supprimer_contact_id(identifiant)
             
              
             

        elif mon_choix == "5" :
            Numero_telephone  = int (input("Donner le nouveau numero de telephone: ")) 
            identifiant  = int (input("Donner l'identifier que vous voulez modifier : "))
            connexion.modifier_contact(Numero_telephone ,identifiant)

        elif mon_choix == "6" :
            Numero_telephone  = int (input("Donner le numero de telephone que vous vous chercher : "))             
            Mes_contacts =connexion.recherche_contact(Numero_telephone )
            for Mon_contact in Mes_contacts :
              print(f" Prenoms et nom :{Mon_contact[2]} {Mon_contact[1]} ")

        elif mon_choix == "7" :
            print("A bientot")
            sys.exit()
    
    print("-" *50)

menu()