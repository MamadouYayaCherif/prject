import os
import string
import random
import sys
import Menu
import EtudiantModel
import ModuleModel
import SeanceModel
import ModelNote
#sys.path.append('F:\mes cours L3\PYTON\Projet_Final_Python_Licence_Mballou\Model')
#print(sys)

def main():
    menu = 0
    while menu <= 0 or menu >=6 :
        menu = Menu.Menu1.MenuPrincipale('',"")
        effacer= os.system('cls')
        my_listeEtudiant = []
        my_listeModul = []
        my_listeSeance = []
        my_listNote = []
        if menu==1:
            
            choix = Menu.Menu1.MenuEtudiant('',"")
            while choix != 0 :
                if choix == 1 : 
                    #effacer= os.system('cls')
                    my_listeEtudiant= EtudiantModel.Etudiant.ajouterEtudiant('',my_listeEtudiant)
                   # effacer= os.system('cls')
                    choix = Menu.Menu1.MenuEtudiant('',"")
                    EtudiantModel.Etudiant.printListEtudiant('',my_listeEtudiant)
                if choix == 2 : 
                    effacer= os.system('cls')
                    my_listeEtudiant =EtudiantModel.Etudiant.Modifier('',my_listeEtudiant)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix = Menu.Menu1.MenuEtudiant('',"")    
                if choix == 3 : 
                    effacer= os.system('cls')
                    EtudiantModel.Etudiant.printInfosEtudiantByMatricul('',my_listeEtudiant)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix = Menu.Menu1.MenuEtudiant('',"")    
                if choix == 4 : 
                    effacer= os.system('cls')
                    my_listeEtudiant = EtudiantModel.Etudiant.deletEtudiantByMatricul('',my_listeEtudiant)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix = Menu.Menu1.MenuEtudiant('',"")    
                if choix == 5 : 
                    effacer= os.system('cls')
                    EtudiantModel.Etudiant.printListEtudiant('',my_listeEtudiant)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix = Menu.Menu1.MenuEtudiant('',"")    
                if choix == 0 :
                    effacer= os.system('cls')
                    menu = Menu.Menu1.MenuPrincipale('',"")

        if menu==2:
            
            choix1 = Menu.Menu1.MenuModule('',"")
            while choix1 != 0 :
                if choix1 == 1 : 
                    #effacer= os.system('cls')
                    my_listeModul= ModuleModel.Module.ajouterModule('',my_listeModul)
                   # effacer= os.system('cls')
                    choix1 = Menu.Menu1.MenuModule('',"")
                if choix1 == 2 : 
                    effacer= os.system('cls')
                    my_listeModul= ModuleModel.Module.ModifierModule('',my_listeModul)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix1 = Menu.Menu1.MenuModule('',"")
                if choix1 == 3 : 
                    effacer= os.system('cls')
                    ModuleModel.Module.printInfosModuleById('',my_listeModul)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix1 = Menu.Menu1.MenuModule('',"")
                if choix1 == 4 : 
                    effacer= os.system('cls')
                    my_listeModul= ModuleModel.Module.deletModuleById('',my_listeModul)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix1 = Menu.Menu1.MenuModule('',"")
                if choix1 == 5 : 
                    effacer= os.system('cls')
                    ModuleModel.Module.printListModule('',my_listeModul)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix1 = Menu.Menu1.MenuModule('',"")
                if choix1 == 0 :
                    effacer= os.system('cls')
                    menu = Menu.Menu1.MenuPrincipale('',"")
        if menu==3:
            choix1 = Menu.Menu1.MenuSeance('',"")
            while choix1 != 0 :
                if choix1 == 1 : 
                    #effacer= os.system('cls')
                    my_listeSeance= SeanceModel.Seance.ajouterSeance('',my_listeSeance)
                   # effacer= os.system('cls')
                    choix1 = Menu.Menu1.MenuSeance('',"")
                if choix1 == 2 : 
                    effacer= os.system('cls')
                    my_listeSeance= SeanceModel.Seance.ModifierSeance('',my_listeSeance)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix1 = Menu.Menu1.MenuSeance('',"")
                if choix1 == 3 : 
                    effacer= os.system('cls')
                    SeanceModel.Seance.printInfosSeanceById('',my_listeSeance)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix1 = Menu.Menu1.MenuSeance('',"")
                if choix1 == 4 : 
                    effacer= os.system('cls')
                    my_listeSeance= SeanceModel.Seance.deleteSeanceById('',my_listeSeance)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix1 = Menu.Menu1.MenuSeance('',"")
                if choix1 == 5 : 
                    effacer= os.system('cls')
                    SeanceModel.Seance.printListSeance('',my_listeSeance)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix1 = Menu.Menu1.MenuSeance('',"")
                if choix1 == 0 :
                    effacer= os.system('cls')
                    menu = Menu.Menu1.MenuPrincipale('',"")
        if menu==4:
            choix4 = Menu.Menu1.MenuNotes('',"")
            while choix4 != 0 :
                if choix4 == 1 : 
                    effacer= os.system('cls')
                    if len(my_listeModul) > 0 and len(my_listeEtudiant) > 0:
                        ModuleModel.Module.printListModule('',my_listeModul)
                        idModule = ModelNote.Note.VerifModulExist('',my_listeModul)
                        if idModule != 0:
                            my_listNote= ModelNote.Note.ajouterNote('',my_listeEtudiant,idModule,my_listNote)                       
                    else:
                        print("\n Vous devez Saisir au moins un module et un etudiant \n" )
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix4 = Menu.Menu1.MenuNotes('',"")
                if choix4 == 2 : 
                    effacer= os.system('cls')
                    if len(my_listeModul) > 0 and len(my_listeEtudiant) > 0:
                        ModuleModel.Module.printListModule('',my_listeModul)
                        idModule = ModelNote.Note.VerifModulExist('',my_listeModul)
                        if idModule != 0:
                            effacer= os.system('cls')
                            matriculEtudiant = ModelNote.Note.VerifMatricul('',my_listeEtudiant)    
                        if matriculEtudiant != 0:
                            my_listNote = ModelNote.Note.ModifierNote('',idModule,matriculEtudiant,my_listeEtudiant,my_listNote)
                    else:
                        print("\n Vous devez Saisir au moins un module et un etudiant \n" )
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix4 = Menu.Menu1.MenuNotes('',"")
                if choix4 == 3 : 
                    effacer= os.system('cls')
                    if len(my_listeModul) > 0 and len(my_listeEtudiant) > 0:
                        ModuleModel.Module.printListModule('',my_listeModul)
                        idModule = ModelNote.Note.VerifModulExist('',my_listeModul)
                        if idModule != 0:
                            effacer= os.system('cls')
                            matriculEtudiant = ModelNote.Note.VerifMatricul('',my_listeEtudiant)      
                        if matriculEtudiant != 0:
                            ModelNote.Note.printNoteByInfos('',idModule,matriculEtudiant,my_listNote)
                    else:
                        print("\n Vous devez Saisir au moins un module et un etudiant \n" )
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix4 = Menu.Menu1.MenuNotes('',"")
                if choix4 == 4 : 
                    effacer= os.system('cls')
                    my_listeSeance= SeanceModel.Seance.deleteSeanceById('',my_listeSeance)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix4 = Menu.Menu1.MenuNotes('',"")
                if choix4 == 5 : 
                    effacer= os.system('cls')
                    SeanceModel.Seance.printListSeance('',my_listeSeance)
                    ok = input("\n")
                    effacer= os.system('cls')
                    choix4 = Menu.Menu1.MenuNotes('',"")
                if choix4 == 0 :
                    effacer= os.system('cls')
                    menu = Menu.Menu1.MenuPrincipale('',"")
        if menu==5:
            menu = Menu.Menu1.MenuResultat('',"")
            effacer= os.system('cls')


main()