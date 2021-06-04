class Menu1:
   
    def MenuPrincipale(self,chaine):
            print("\n ------------------------------------------------------- \n" )
            print("\n   '1'      Gestion des etudiants du groupe PR214 \n" )
            print("\n   '2'      Gestion des modules de formations de PR308 \n" )
            print("\n   '3'      Gestion des Seances de cours  \n" )
            print("\n   '4'      Geston des Notes des modules du groupe PR214 \n" )
            print("\n   '5'      Gestion des Resultat Accademiques \n" )
            print("\n ------------------------------------------------------- \n\n" )
            chaine =  input("\n             ----------> Faite votre choix  <-------- \n")
            try:
                return int(chaine) 
            except:
                    print("Vous devez saisir un entier compris entre 1--5 SVP ")
                    return 0

    def MenuEtudiant(self,chaine):
            print("\n ------------------------------------------------------- \n" )
            print("\n '1' Ajouter un Etudiant dans le groupe PR214 \n" )
            print("\n '2' Modifier les Informations d\'un Etudiant \n" )
            print("\n '3' Afficher les information de l\'etudiant  \n" )
            print("\n '4' Supprimer un Etudiant dans le groupe PR214 \n" )
            print("\n '5' Afficher tous les Etudiants du groupe PR214 \n" )
            print("\n ------------------------------------------------------- \n\n" )
            chaine =  input("\n ----------> Faite votre choix  <-------- \n")
            try:
                return int(chaine) 
            except:
                    print("Vous devez saisir un entier compris entre 1--5 SVP ")
                    return 0
    def MenuModule(self,chaine):
            print("\n ------------------------------------------------------- \n" )
            print("\n '1' Ajouter un Module \n" )
            print("\n '2' Modifier les donnees d\'un module \n" )
            print("\n '3' Rechercher et Afficher les information d\'un module  \n" )
            print("\n '4' Supprimer un Module \n" )
            print("\n '5' Afficher tous les Modules \n" )
            print("\n ------------------------------------------------------- \n\n" )
            chaine =  input("\n ----------> Faite votre choix  <-------- \n")
            try:
                return int(chaine) 
            except:
                    print("Vous devez saisir un entier compris entre 1--5 SVP ")
                    return 0

    def MenuSeance(self,chaine):
            print("\n ------------------------------------------------------- \n" )
            print("\n '1' Ajouter une Seance \n" )
            print("\n '2' Modifier les Informations d\'une Seance \n" )
            print("\n '3' Afficher les information d\'une Seance  \n" )
            print("\n '4' Supprimer une Seance \n" )
            print("\n '5' Afficher toutes les Seance \n" )
            print("\n ------------------------------------------------------- \n\n" )
            chaine =  input("\n ----------> Faite votre choix  <-------- \n")
            try:
                return int(chaine) 
            except:
                    print("Vous devez saisir un entier compris entre 1--5 SVP ")
                    return 0
    
    def MenuNotes(self,chaine):
            print("\n ------------------------------------------------------- \n" )
            print("\n '1' Saisir les Notes d\'un Module pour tous les etudiant du groupe \n" )
            print("\n '2' Modifier une note \n" )
            print("\n '3' Afficher la note d\'un etudiant par un module donne \n" )
            print("\n '4' Afficher les notes d\'un etudiant pour tous les module \n" )
            print("\n '5' Afficher la note de tous les etudiant pour tous les modules \n" )
            print("\n ------------------------------------------------------- \n\n" )
            chaine =  input("\n ----------> Faite votre choix  <-------- \n")
            try:
                return int(chaine) 
            except:
                    print("Vous devez saisir un entier compris entre 1--5 SVP ")
                    return 0

    def MenuResultat(self,chaine):
            print("\n ------------------------------------------------------- \n" )
            print("\n '1' Calculer les moyennes des etudiants pour les differents modules de formation \n" )
            print("\n '2' Generer le bulltin d\'un etudiant \n" )
            print("\n '3' Afficher tous les bulletin de notes\n" )
            print("\n ------------------------------------------------------- \n\n" )
            chaine =  input("\n ----------> Faite votre choix  <-------- \n")
            try:
                return int(chaine) 
            except:
                    print("Vous devez saisir un entier compris entre 1--5 SVP ")
                    return 0