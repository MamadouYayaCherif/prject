
class Note:
   
    def __init__(self, idModul, matriculEtudiant, Note):
        self.idModul = idModul
        self.matriculEtudiant = matriculEtudiant
        self.Note = Note
    
    def ajouterNote (self, my_listeEtudiant, idModul, my_listNote):
        for id,Etudiant in enumerate(my_listeEtudiant):
            print("\n-------------------------------------------------------------------------\n")
            print(" Position ", id , "\n Matricule ", Etudiant.matricul,"\n Prenom ", Etudiant.prenom, "\n Nom  ", Etudiant.nom)
            print("\n-------------------------------------------------------------------------\n")      
            try:
                note = int(input("\n Saisir sa note : \n")) 
                Note1 = Note(idModul,Etudiant.matricul, note)    
                my_listNote.append(Note1)
            except :
                print("\n-Vous devez saisir un entier -\n")
        return my_listNote            

    def VerifModulExist (self , my_liste):
                try:
                    idModul = int(input("\n Faite votre choix de la liste: \n"))
                    pos = -1
                    i = 0
                    while i <= len(my_liste):
                        if i == idModul :
                            pos = idModul
                            return int(idModul)
                        i = i + 1
                    if pos == -1:
                        print(" Ce Modul n\'existe pas dans la liste ") 
                        return int(0)                       
                except:  
                        print("  Vous devez saisir un entier svp !! ")

    def VerifMatricul (self , my_listeEtudiant):
                try:
                    matricul = input("\n Saisir le matricul de l\'Etudiant: \n")
                    pos = -1
                    for id,Etudiant in enumerate(my_listeEtudiant):
                        if Etudiant.matricul == matricul :
                            return matricul
                    if pos == -1:
                        print(" Ce Matricul n\'existe pas dans la liste ")
                        return 0                         
                except:  
                        print("  Vous devez saisir un entier svp !! ")

    def ModifierNote (self ,idModul, matriculEtudiant, my_listeEtudiant,my_listeNote):
                try:
                    note = int(input("\n Saisir la novelle Note : \n"))
                    for i,note1 in enumerate(my_listeNote):
                        if idModul == note1.idModul and matriculEtudiant == note1.matriculEtudiant :
                                my_listeNote[i].Note = note
                                print("\n Modification effectuer avec succes \n")
                         
                except:  
                        print("  Vous devez saisir un entier svp !! ")
                return my_listeNote
    
    

    def printListModule(self,my_liste):
        for i,Module in enumerate(my_liste):
            print("\n-------------------------------------------------------------------------\n")
            print(" id :  ", i , "\n Nom  : ", Module.nom,"\n Volume Horaire Total ", Module.voulumeHoraireTotal)
            print("\n-------------------------------------------------------------------------\n")      
    
    def printNoteByInfos(self,idModul, matriculEtudiant, my_listeNote):
                try:
                    pos = -1
                    for i,note1 in enumerate(my_listeNote):
                        if idModul == note1.idModul and matriculEtudiant == note1.matriculEtudiant :
                            pos = id
                            print(" il a eu : ", note1.Note, "  dans ce module")
                            break 
                    if pos == -1:
                        print(len(my_liste))
                        print(" Ces informations n\'existe pas dans la liste des notes ") 
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
                
    
       