
class Module:
   
    def __init__(self, nom, voulumeHoraireTotal):
        self.nom = nom
        self.voulumeHoraireTotal = voulumeHoraireTotal
    
    def ajouterModule (self, my_liste):
                nom =  input("\n Nom : \n")
                voulumeHoraireTotal = input("\n voulume Horaire Total : \n")
                Module1 = Module (nom,voulumeHoraireTotal)    
                my_liste.append(Module1)
                return my_liste

    def ModifierModule (self , my_liste):
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
                        print(" cet Module n\'existe pas dans la liste ") 
                    else:
                        nom =  input("\n Nom : \n")
                        voulumeHoraireTotal = input("\n voulume Horaire Total : \n")
                        my_liste[pos].nom = nom
                        my_liste[pos].voulumeHoraireTotal = voulumeHoraireTotal
                except:  
                        print("  Vous devez saisir un entier svp !! ")
                return my_liste

    def printListModule(self,my_liste):
        for i,Module in enumerate(my_liste):
            print("\n-------------------------------------------------------------------------\n")
            print(" id :  ", i , "\n Nom  : ", Module.nom,"\n Volume Horaire Total ", Module.voulumeHoraireTotal)
            print("\n-------------------------------------------------------------------------\n")      
    
    def printInfosModuleById(self,my_liste):
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
                        print(" cet Module n\'existe pas dans la liste ") 
                    else:
                        for i,Module in enumerate(my_liste):
                            if i == pos :
                                print("\n-------------------------------------------------------------------------\n")
                                print(" id :  ", i , "\n Nom  : ", Module.nom,"\n Volume Horaire Total ", Module.voulumeHoraireTotal)
                except:  
                        print("  Vous devez saisir un entier svp !! ")   
                     

    def deletModuleById(self,my_liste):
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
                        print(" cet Module n\'existe pas dans la liste ") 
                    else:
                        my_liste.pop(pos)
                        print(" Supprission effectuee avec succes ....!!! ") 
                except:  
                    print("  Vous devez saisir un entier svp !! ")
                return my_liste
                
    
       