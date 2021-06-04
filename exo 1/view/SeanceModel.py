
class Seance:
   
    def __init__(self,dateSeance, heurDebutSeance, heurFinSeance,nomSall,nomProf, voulumHoraire,infosChapitre, objectifPedagogique):
        self.dateSeance = dateSeance
        self.heurDebutSeance = heurDebutSeance
        self.heurFinSeance = heurFinSeance
        self.nomSall = nomSall
        self.nomProf = nomProf
        self.voulumHoraire = voulumHoraire
        self.infosChapitre = infosChapitre
        self.objectifPedagogique = objectifPedagogique
    
    def ajouterSeance (self, my_liste):
                dateSeance =  input("\n Date de la Seance : \n")
                heurDebutSeance =  input("\n Heur Debut de la Seance : \n")
                heurFinSeance =  input("\n heur de Fin de la Seance : \n")
                nomSall =  input("\n Nom de la Sall : \n")
                nomProf =  input("\n Nom du Prof : \n")
                voulumHoraire =  input("\n voulum Horaire : \n")
                infosChapitre =  input("\n Numero et  titre du chapitre : \n")
                objectifPedagogique =  input("\n Objectif pedagogique : \n")
                Seance1 =Seance(dateSeance, heurDebutSeance, heurFinSeance,nomSall,nomProf, voulumHoraire,infosChapitre, objectifPedagogique)     
                my_liste.append(Seance1)
                return my_liste

    def ModifierSeance (self , my_liste):
                try:
                    id = int(input("\n Saisir l\'id  de la Seance : \n"))
                    pos = -1
                    i = 0
                    while i <= len(my_liste):
                        if i == id :
                            pos = id
                        i = i + 1
                    if pos == -1:
                        print(len(my_liste))
                        print(" cette Seance n\'existe pas dans la liste ") 
                    else:
                        dateSeance =  input("\n Date de la Seance : \n")
                        heurDebutSeance =  input("\n Heur Debut de la Seance : \n")
                        heurFinSeance =  input("\n heur de Fin de la Seance : \n")
                        nomSall =  input("\n Nom de la Sall : \n")
                        nomProf =  input("\n Nom du Prof : \n")
                        voulumHoraire =  input("\n voulum Horaire : \n")
                        infosChapitre =  input("\n Numero et  titre du chapitre : \n")
                        objectifPedagogique =  input("\n Objectif pedagogique : \n")
                        my_liste[pos].dateSeance = dateSeance
                        my_liste[pos].heurDebutSeance = heurDebutSeance
                        my_liste[pos].heurFinSeance = heurFinSeance
                        my_liste[pos].nomSall = nomSall
                        my_liste[pos].nomProf = nomProf
                        my_liste[pos].voulumHoraire = voulumHoraire
                        my_liste[pos].infosChapitre = infosChapitre
                        my_liste[pos].objectifPedagogique = objectifPedagogique
                except:  
                        print("  Vous devez saisir un entier svp !! ")
                return my_liste

    def printListSeance(self,my_liste):
        for id,Seance1 in enumerate(my_liste):
            print("\n-------------------------------------------------------------------------\n")
            print(" Seance N  :  ", id , "\n Date de la Seance :  ", Seance1.dateSeance,"\n Heur Debut de la Seance :  ", Seance1.heurDebutSeance, "\n Heur Fin Seance :  ", Seance1.heurFinSeance, "\n Nom de la Sall ", Seance1.nomSall, "\n Nom du Prof ", Seance1.nomProf, "\n Voulum Horaire ",  Seance1.voulumHoraire,"\n Infos Chapitre",  Seance1.infosChapitre,"\n Objectif Pedagogique ", Seance1.objectifPedagogique)
            print("\n-------------------------------------------------------------------------\n")      
    
    def printInfosSeanceById(self,my_liste):
                try:
                    id = int(input("\n Saisir l\'id : \n"))
                    pos = -1
                    i = 0
                    while i <= len(my_liste):
                        if i == id :
                            pos = id
                        i = i + 1
                    if pos == -1:
                        print(len(my_liste))
                        print(" cette Seance n\'existe pas dans la liste ") 
                    else:
                        Seance1 = my_liste
                        print("\n-------------------------------------------------------------------------\n")
                        print(" Seance N  :  ", id , "\n Date de la Seance :  ", Seance1[pos].dateSeance,"\n Heur Debut de la Seance :  ", Seance1[pos].heurDebutSeance, "\n Heur Fin Seance :  ", Seance1[pos].heurFinSeance, "\n Nom de la Sall ", Seance1[pos].nomSall, "\n Nom du Prof ", Seance1[pos].nomProf, "\n Voulum Horaire ",  Seance1[pos].voulumHoraire,"\n Infos Chapitre",  Seance1[pos].infosChapitre,"\n Objectif Pedagogique ", Seance1[pos].objectifPedagogique)
                        print("\n-------------------------------------------------------------------------\n")      
                except:  
                        print("  Vous devez saisir un entier svp !! ")   


    def deleteSeanceById(self,my_liste):
                try:
                    id = int(input("\n Saisir l\'id : \n"))
                    pos = -1
                    i = 0
                    while i <= len(my_liste):
                        if i == id :
                            pos = id
                        i = i + 1
                    if pos == -1:
                        print(len(my_liste))
                        print(" cette Seance n\'existe pas dans la liste ") 
                    else:
                        my_liste.pop(pos)
                        print(" Supprission effectuee avec succes ....!!! ") 
                except:  
                    print("  Vous devez saisir un entier svp !! ")
                return my_liste
                
    
       