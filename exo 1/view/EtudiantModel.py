
class Etudiant:
   
    def __init__(self, matricul, prenom, nom, dateNaissance,lieuNaissance,adresse,telephone, email,dateInscription, prenomContact, nomContact, telephoneContact):
        self.matricul = matricul
        self.prenom = prenom
        self.nom = nom
        self.dateNaissance = dateNaissance
        self.lieuNaissance = lieuNaissance
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.dateInscription = dateInscription
        self.prenomContact = prenomContact
        self.nomContact = nomContact
        self.telephoneContact = telephoneContact
    
    def ajouterEtudiant (self, my_liste):
                matricul =  input("\n Matricul : \n")
                prenom =  input("\n Prenom : \n")
                nom =  input("\n Nom : \n")
                dateNaissance =  input("\n Date de Naissance : \n")
                lieuNaissance =  input("\n Lieu de Naissance : \n")
                adresse =  input("\n Adresse : \n")
                telephone =  input("\n Telephone : \n")
                email =  input("\n Email : \n")
                dateInscription =  input("\n date d\' inscription : \n")
                prenomContact =  input("\n Prenom du Contact : \n")
                nomContact =  input("\n Nom du Contact : \n")
                telephoneContact =  input("\n telephone du Contact : \n")
                Etudiant1 =Etudiant(matricul,prenom,nom,dateNaissance,lieuNaissance,adresse,telephone,email,dateInscription, prenomContact,nomContact,telephoneContact)     
                my_liste.append(Etudiant1)
                return my_liste

    def Modifier (self , my_liste):
                matricul =  input("\n Donnez le Matricul : \n")
                pos = -1
                for id,Etudiant in enumerate(my_liste):
                    if Etudiant.matricul == matricul :
                        pos = id
                
                if pos == -1:
                    print(" cet etudiant n\'existe pas dans la liste des etudiants") 
                else:
                    matricul =  input("\n Matricul : \n")
                    prenom =  input("\n Prenom : \n")
                    nom =  input("\n Nom : \n")
                    dateNaissance =  input("\n Date de Naissance : \n")
                    lieuNaissance =  input("\n Lieu de Naissance : \n")
                    adresse =  input("\n Adresse : \n")
                    telephone =  input("\n Telephone : \n")
                    email =  input("\n Email : \n")
                    dateInscription =  input("\n date d\' inscription : \n")
                    prenomContact =  input("\n Prenom du Contact : \n")
                    nomContact =  input("\n Nom du Contact : \n")
                    telephoneContact =  input("\n telephone du Contact : \n")
                    my_liste[pos].matricul = matricul
                    my_liste[pos].prenom = prenom
                    my_liste[pos].nom = nom
                    my_liste[pos].dateNaissance = dateNaissance
                    my_liste[pos].lieuNaissance = lieuNaissance
                    my_liste[pos].adresse = adresse
                    my_liste[pos].telephone = telephone
                    my_liste[pos].email = email
                    my_liste[pos].dateInscription = dateInscription
                    my_liste[pos].prenomContact = prenomContact
                    my_liste[pos].nomContact = nomContact
                    my_liste[pos].telephoneContact = telephoneContact
                    #Etudiant1 =Etudiant[matricul,prenom,nom,dateNaissance,lieuNaissance,adresse,telephone,email,dateInscription, prenomContact,nomContact,telephoneContact]    
                    #my_liste[pos] = Etudiant1
                return my_liste
                #print(my_liste)

    def printListEtudiant(self,my_liste):
        for id,Etudiant in enumerate(my_liste):
            print("\n-------------------------------------------------------------------------\n")
            print(" Position ", id , "\n Matricule ", Etudiant.matricul,"\n Prenom ", Etudiant.prenom, "\n Nom  ", Etudiant.nom, "\n Date de Naissance ", Etudiant.dateNaissance, "\n Lieu de Naissance ", Etudiant.lieuNaissance, "\n Adresse ",  Etudiant.adresse,"\n Telephone",  Etudiant.telephone,"\n Email ", Etudiant.email,"\n date d\'inscription ", Etudiant.dateInscription, " \n Prenom Contact ",Etudiant.prenomContact," \n Nom Contact ", Etudiant.nomContact,"\n Telephone contact", Etudiant.telephoneContact )
            print("\n-------------------------------------------------------------------------\n")      
    
    def printInfosEtudiantByMatricul(self,my_liste):
                matricul =  input("\n Donnez le Matricul : \n")
                pos = -1
                for id,Etudiant in enumerate(my_liste):
                    if Etudiant.matricul == matricul :
                        pos = id
                
                if pos == -1:
                    print(" cet etudiant n\'existe pas dans la liste des etudiants") 
                else:
                    for id,Etudiant in enumerate(my_liste):
                        if id == pos :
                            print("\n-------------------------------------------------------------------------\n")
                            print(" Position ", id , "\n Matricule ", Etudiant.matricul,"\n Prenom ", Etudiant.prenom, "\n Nom  ", Etudiant.nom, "\n Date de Naissance ", Etudiant.dateNaissance, "\n Lieu de Naissance ", Etudiant.lieuNaissance, "\n Adresse ",  Etudiant.adresse,"\n Telephone",  Etudiant.telephone,"\n Email ", Etudiant.email,"\n date d\'inscription ", Etudiant.dateInscription, " \n Prenom Contact ",Etudiant.prenomContact," \n Nom Contact ", Etudiant.nomContact,"\n Telephone contact", Etudiant.telephoneContact )
                            print("\n-------------------------------------------------------------------------\n")      
   
    def deletEtudiantByMatricul(self,my_liste):
                matricul =  input("\n Donnez le Matricul : \n")
                pos = -1
                for id,Etudiant in enumerate(my_liste):
                    if Etudiant.matricul == matricul :
                        pos = id
                if pos == -1:
                    print(" cet etudiant n\'existe pas dans la liste des etudiants") 
                else:
                    my_liste.pop(pos)
                return my_liste
                
    
       