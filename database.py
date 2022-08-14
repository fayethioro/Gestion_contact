import sqlite3

#creation de la table contact
create_table_contact = """ CREATE TABLE IF NOT EXISTs contact(
                           ID                 INTEGER PRIMARY KEY AUTOINCREMENT,
                           Nom                TEXT   NOT NULL,
                           Prenom             TEXT   NOT NULL,
                           Email              TEXT   NOT NULL,
                           Numero_Telephone   INTEGER NOT NULL,
                           Adresse            TEXT    NOT NULL
                           );
"""
#inserer un contact
insertion_contact = """INSERT INTO contact ('Nom' , 'Prenom' , 'Email' , 'Numero_telephone' , 'Adresse')
                            VALUES (? , ? , ? , ? , ?); """

#afficher la liste des contacts
AFFICHER_LISTE_CONTACT = "select * from contact"

#Supprimer un contact via son numero de telephone
SUPPRIMER_CONTACT_TEL ="delete from contact where Numero_Telephone =?"
#Supprimer un contact via son id
SUPPRIMER_CONTACT_ID ="delete from contact where ID =?"

#modifier contact via son id
MODIFIER_CONTACT = "update contact set Numero_Telephone =? where ID=?"

#recherch un contact via son numero de telephone
RECHERCHE_CONTACT ="select Nom ,Prenom from contact where Numero_Telephone =?"

class Connect:
    def __init__(self):
        self.bd = sqlite3.connect("Moncontact.db")
        self.bd.row_factory = sqlite3.Row
        self.bd.execute(create_table_contact)
        self.bd.commit()

    def ajouter_contact(self, Nom,Prenom,Email,Numero_telephone,Adresse):
        self.bd.row_factory = sqlite3.Row
        self.bd.execute(insertion_contact, (Nom,Prenom,Email,Numero_telephone,Adresse))
        self.bd.commit()
   

    def afficher_liste_contact(self):
        cursor = self.bd.execute(AFFICHER_LISTE_CONTACT).fetchall()
        return cursor



    def supprimer_contact_tel(self, Numero_Telephone):
        self.bd.row_factory = sqlite3.Row
        self.bd.execute(SUPPRIMER_CONTACT_TEL , (Numero_Telephone ,)).fetchall()
        self.bd.commit()

    def supprimer_contact_id(self, ID):
        self.bd.row_factory = sqlite3.Row
        self.bd.execute(SUPPRIMER_CONTACT_ID , (ID ,)).fetchall()
        self.bd.commit()


    def modifier_contact(self, Numero_Telephone, ID):
        self.bd.row_factory = sqlite3.Row
        self.bd.execute(MODIFIER_CONTACT, (Numero_Telephone, ID)).fetchall()
        self.bd.commit()
    
    def recherche_contact(self, Numero_Telephone):
        self.bd.row_factory = sqlite3.Row
        self.bd.execute(RECHERCHE_CONTACT, (Numero_Telephone,)).fetchall()
        self.bd.commit()
        
       


