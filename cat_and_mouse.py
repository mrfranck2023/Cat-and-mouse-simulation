#-------------------------------------fonctionnement de la simulation---------------------------------------------
# on crée un tableau a une dimension de 25 lignes et 25 colonnes

# On insert dans le tableau de manière aléatoire à l'aide de la fonction new_insert() les chats qui est represente ici par C(modifiable) qui sont les mâle et par n(modifiable) qui sont les femelles

# On insert dans le tableau de manière aléatoire à l'aide de la fonction new_insert() les souris qui est represente ici par #(modifiable) qui sont les mâle et par ~(modifiable) qui sont les femelles

# On entre dans la boucle infini qui nous permettra de simuler notre programme

# On verifie si dans le tableau il existe deja du maïs à l'aide de la fonction vérification si il n'y a pas de maïs, on les insert dans le tableau de manière aléatoire à l'aide de la fonction new_insert() le maïs qui est represente ici par 15 si non on continue dans le programme

# A l'aide de la fonction détecteur, je détermine la position des souris présentent dans le tableau puis je vérifie si les souris peuvent se reproduire à l'aide de la fonction procreation() 

# puis je  deplace les souris qui ont ete detectes par la fonction detecteur() à l'aide de la fonction déplacement()

# puis je lance la fonction dégustation qui permettra à la souris de manger si elle le peut ou de mourir si sa vie atteint 0

# ensuite j everifie si les souris on mangé tous les maïs si oui le remet les maïs a l'aide de la fonction new_insert() sinon

# on utilise la fonction detecteur() pour trouver la position des chats presents dans le tableau une fois trouvés on verifie si toutes les souris sont mortes lors de l'etape precedente

# si oui on les remet à l'aide de la fonctio new_insert() sinon on lance la fonction reproduction pour permettre aux chats de se reproduire si ils le peuvent

# ensuite on les deplace dans le tableau a l'aide de la fonction deplacement()      

# puis je lance la fonction dégustation qui permettra au chat de manger si il le peut ou de mourir si sa vie atteint 0

# apres, je verifie si toutes les souris on ete manger si oui je les remet a l'aide de la fonction new_insert si non je verifie si tous les chats on ete mange si oui je les remet si non la grande boucle continue

#-------------------------------------fonctionnement des tableaux statistique---------------------------------------------
# les tableaux presentent le nom de l'animal sa position et son nombre de vie 

# le nombre de se reduit de 1 si le predateur fait un deplacement sans manger et reviens a 6 si le predateur mange, 

# si son nbre de vie atteint 0 il meurt
#-------------------------------------fonctionnement des tableaux statistique---------------------------------------------


#-------------------------------------fonctionnement de la simulation---------------------------------------------



import random #fonction permettant d'obtenir de la machine des nombres aleatoires ou de creer des listes de choix aleatoires
import os #permet d'utiliser dans notre code certaine fonctions du systeme d'exploitation 
import time #permet de controller le temps dans notre cas de le stoper
    

tableau = [
    "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",#ceci est la declaration de notre espace de travail
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "O",
    "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",
    ]

apparence_des_entites = ["m", "~", "#", "n", "C"]#le premier represente le maïs, le deuxieme et le troisieme

#representent respectivement la souris femelle et le souris mâle, les deux derniers representent respectivement le chat femelle et le chat mâle 

#vous pouvez changer grace a ce tableau l'apparence des entités à conditions qu'elles soient toutes différentes ex: a la place de "~" on peut mettre "f" pour rempllacer la souris femelle

#si vous voulez modifier les apparences, nous vous recommandons pour une question de meilleur affichage d'utiliser des apparences represente par un seul caractere exemple: "f" plutot que "ff"   


tab_chat = [3]#permet de stocker apres son deplacement la nouvelle position du chat
tab_souris = [4]#permet de stocker apres son deplacement la nouvelle position de la souris
tab_pos_ante_chat = [3]#permet de stocker la position du chat avant son deplacement 
tab_pos_ante_souris = [4]#permet de stocker la position de la souris avant son deplacement 
#3 4 present dans les tableau si dessus ont ete insere juste pour eviter que le tableau soit vide 

# ****************************************************************************************************************************************************************************************************************************************************************************************************************************************
# ****************************************************************************************************************************************************************************************************************************************************************************************************************************************


        

# ****************************************************************************************************************************************************************************************************************************************************************************************************************************************
# ****************************************************************************************************************************************************************************************************************************************************************************************************************************************

#la fonction ci dessous permet de faire afficher notre espace de travail

def afficher_terrain(tableau):
    i = 0

    while i < len(tableau):
        print(tableau[i], tableau[i+1], tableau[i+2], tableau[i+3], tableau[i+4], tableau[i+5], tableau[i+6], tableau[i+7], tableau[i+8], tableau[i+9], tableau[i+10], tableau[i+11], tableau[i+12], tableau[i+13], tableau[i+14],            tableau[i+15], tableau[i+16], tableau[i+17], tableau[i+18], tableau[i+19], tableau[i+20], tableau[i+21], tableau[i+22], tableau[i+23], tableau[i+24], "\n")  
        i += 25 



# # ****************************************************************************************************************************************************************************************************************************************************************************************************************************************
# # ****************************************************************************************************************************************************************************************************************************************************************************************************************************************


# ****************************************************************************************************************************************************************************************************************************************************************************************************************************************
#------------------------------- --------------------------------------VERSION ORIENTEE OBJET-------------------------------------------------------------------------------------------------------
# ****************************************************************************************************************************************************************************************************************************************************************************************************************************************
#Dans notre exercice, le mais est represente par m(modifiable) la souris femelle par ~(modifiable), la souris mâle par #(modifiable); le chat femelle par n(modifiable) ; le chat mâle par C(modifiable)
class animal:

    def __init__(self, chasseur, proie, coor_mere, genre):
        self.chasseur = chasseur
        self.proie = proie
        self.mere = coor_mere
        self.genre = genre
        

    

class souris(animal):
    def __init__(self, predateur, proie, coor_mere, genre):
        animal.__init__(self, predateur, proie, coor_mere, genre)


    

class chat(animal):
    def __init__(self, predateur, proie, coor_mere, genre):
        animal.__init__(self, predateur, proie, coor_mere, genre)




#permet de verifier la presence dans le tableau de l'element indice qui a ete entré en parametre
def verification(array, indice):
    compteur = 0
    intrus = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 49, 74, 99, 124, 149, 174, 199, 224, 249, 274, 299, 324, 349, 374, 399, 424, 449, 474, 499, 524, 549, 574, 599]#les quatres limites du tableau 
  
    for i in range(25, 599):
        if i not in intrus:
            if array[i] == indice:  
                compteur += 1
            else:
                pass
        else:
            pass

    return compteur



#permet d'inserer dans le tableau de maniere aleatoire l'element occupant qui lui est entre en parametre
def new_insert(array, occupant):
    
    intrus = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 49, 74, 99, 124, 149, 174, 199, 224, 249, 274, 299, 324, 349, 374, 399, 424, 449, 474, 499, 524, 549, 574, 599]
  
    choice = random.randint(25, 599)#cettte fonction genere des nbres entier aleatoires entre 25 et 599
    if array[choice] != " ":
        while(array[choice] != " "):
            choice = random.randint(25, 599)
        array[choice] = occupant

        return choice
    else:
        array[choice] = occupant
        return choice
#permet d'entrer dans le tableau conteneur qui est dans les parametres la position de tous les element dont la valeur est element qui ont ete trouve dans le tableau 
def detecteur(array, conteneur, element):
    for i in range(25, 599):
        if(array[i] == element):
            conteneur.append(i)
        else:
            pass









#rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr


#permet au predateur à la position pos_predateur de se deplacer vers la proie à la position pos_proie chasseur est soit ~ # n ou C 
#ici on essai de tracer une ligne soit en dessous soit au dessus du chasseur afin de detecteur sa proie et de le mener vers elle 
def deplacement(array, pos_proie, pos_predateur, chasseur): 
    intrus = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575]#limite gauche du tableau
    intrus1 = [600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624]#limite du bas du tableau
    intrus2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]#limite du haut du tableau
    intrus3 = [49, 74, 99, 124, 149, 174, 199, 224, 249, 274, 299, 324, 349, 374, 399, 424, 449, 474, 499, 524, 549, 574, 599]#limite droite du tableau
    i = 25
    y = 25
    coor_chasseur = pos_predateur
    coor_proie = pos_proie
    if (chasseur == apparence_des_entites[3]) or (chasseur == apparence_des_entites[4]):
        tab_pos_ante_chat[0] = coor_chasseur
        if coor_proie > coor_chasseur: #alors la proie est soit a la droite du chasseur soit quelque part en dessous de lui
            tempo = coor_chasseur + 25
            comptage = 0 #cette variable nous permettra de compter le nombre de case qui se situent sur la meme ligne et en dessous du chasseur
            compter = coor_chasseur + 25
            plus_un = 0
            parcours = 0
            z = 0

            while tempo not in intrus1:
                comptage += 1
                tempo += 25
            comptage -= 1 
            
            while  z < comptage: #dans cette boucle on cherche a savoir si la proie se trouve a gauche de la ligne verticale a laquelle le chasseur appartient
                parcours = compter - 1
               
                while parcours not in intrus:
                    if parcours == coor_proie:
                        plus_un += 1
                    else:
                        plus_un += 0
                    parcours -= 1
                
                compter += 25
                
                z += 1
                    
            road = coor_chasseur + 25#tableau qui contiendra tous les elements qui seront a gauche de la premiere case en dessous du chasseur
            indice = [] 

            while road not in intrus:
                indice.append(road)
                road -= 1

            if plus_un == 1: #cela veut dire que la proie a ete trouve a gauche de la ligne verticale a laquelle le chasseur appartient 
                array[coor_chasseur] = " "
                coor_chasseur -= 1 #donc le chasseur recule pour alle le manger
                if coor_chasseur not in intrus:
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur

                else:
                    coor_chasseur += 1
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur += 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur


                if coor_proie == coor_chasseur + 25:
                    array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat

                elif coor_proie == coor_chasseur - 1: 
                    array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat
                    
                else:
                    array[coor_chasseur] = " "
                    coor_chasseur += 25 #apres avoir recule de 1 le chasseur descend 
                    if coor_chasseur not in intrus1:
                        if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                            if array[coor_chasseur + 25] == " ":
                                coor_chasseur += 25
                                array[coor_chasseur] = chasseur
                            elif array[coor_chasseur - 25] == " ":
                                coor_chasseur -= 25
                                array[coor_chasseur] = chasseur
                            else:
                                coor_chasseur += 25
                                array[coor_chasseur] = chasseur
                        else:
                            array[coor_chasseur] = chasseur
                        tab_chat[0] = coor_chasseur
                        repeat = tab_chat[0]
                        return repeat
                        
                    else:
                        coor_chasseur -= 25
                        if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                            if array[coor_chasseur + 25] == " ":
                                coor_chasseur += 25
                                array[coor_chasseur] = chasseur
                            elif array[coor_chasseur - 25] == " ":
                                coor_chasseur -= 25
                                array[coor_chasseur] = chasseur
                            else:
                                coor_chasseur -= 25
                                array[coor_chasseur] = chasseur
                        else:
                            array[coor_chasseur] = chasseur
                        tab_chat[0] = coor_chasseur
                        repeat = tab_chat[0]
                        return repeat
                        
            elif coor_proie in indice:
                array[coor_chasseur] = " "
                coor_chasseur -= 1
                if coor_chasseur not in intrus:
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat
                else:
                    coor_chasseur += 1
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur += 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat

            else: 
                array[coor_chasseur] = " "
                coor_chasseur += 1
                if coor_chasseur not in intrus3:
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur += 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                else:
                    coor_chasseur -= 1
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur

                if coor_proie == coor_chasseur + 25:
                    array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat
                elif coor_proie == coor_chasseur + 1:
                    array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat

                else:
                    array[coor_chasseur] = " "
                    coor_chasseur += 25
                    if coor_chasseur not in intrus1:
                        if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                            if array[coor_chasseur + 25] == " ":
                                coor_chasseur += 25
                                array[coor_chasseur] = chasseur
                            elif array[coor_chasseur - 25] == " ":
                                coor_chasseur -= 25
                                array[coor_chasseur] = chasseur
                            else:
                                coor_chasseur += 25
                                array[coor_chasseur] = chasseur
                        else:
                            array[coor_chasseur] = chasseur
                        tab_chat[0] = coor_chasseur
                        repeat = tab_chat[0]
                        return repeat   
                    else:
                        coor_chasseur -= 25
                        if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                            if array[coor_chasseur + 25] == " ":
                                coor_chasseur += 25
                                array[coor_chasseur] = chasseur
                            elif array[coor_chasseur - 25] == " ":
                                coor_chasseur -= 25
                                array[coor_chasseur] = chasseur
                            else:
                                coor_chasseur -= 25
                                array[coor_chasseur] = chasseur
                        else:
                            array[coor_chasseur] = chasseur
                        tab_chat[0] = coor_chasseur
                        repeat = tab_chat[0]
                        return repeat
                   
        else:
            tempo = coor_chasseur - 25
            comptage = 0
            compter = coor_chasseur - 25
            plus_un = 0
            z = 0
            while tempo not in intrus2:
                comptage += 1
                tempo -= 25
            comptage -= 1
        
            while  z < comptage:
                parcours = compter - 1
             
                while parcours not in intrus:
                    if parcours == coor_proie:
                        plus_un += 1
                    else:
                        plus_un += 0
                    parcours -= 1
                
                compter -= 25    
                z += 1


            road = coor_chasseur
            indice = []

            while road not in intrus:
                indice.append(road)
                road -= 1  

            if plus_un == 1:
                array[coor_chasseur] = " "
                coor_chasseur -= 1
                if coor_chasseur not in intrus:
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                else:
                    coor_chasseur += 1
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur += 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur

                if coor_proie == coor_chasseur - 25:
                    array[coor_chasseur] = " "
                    array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat

                else:
                    array[coor_chasseur] = " "
                    coor_chasseur -= 25
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat

            elif coor_proie in indice:
                array[coor_chasseur] = " "
                coor_chasseur -= 1
                if coor_chasseur not in intrus:
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat
                else:
                    coor_chasseur += 1
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur += 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat
            else:
                array[coor_chasseur] = " "
                coor_chasseur += 1
                if coor_chasseur not in intrus3:
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur += 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                else:
                    coor_chasseur -= 1
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur

                if coor_proie == coor_chasseur - 25:
                    array[coor_chasseur] = " "
                    array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat

                elif coor_proie == coor_chasseur + 1:
                    array[coor_chasseur] = " "
                    array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat

                else:
                    array[coor_chasseur] = " "
                    coor_chasseur -= 25
                    if array[coor_chasseur] == apparence_des_entites[0] or array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[4]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                    tab_chat[0] = coor_chasseur
                    repeat = tab_chat[0]
                    return repeat


####

####
    else:
        tab_pos_ante_souris[0] = coor_chasseur
        if coor_proie > coor_chasseur: #alors la proie est soit a la droite du chasseur soit quelque part en dessous de lui
            tempo = coor_chasseur + 25
            comptage = 0 #cette variable nous permettra de compter le nombre de case qui se situe sur la meme ligne et en dessous du chasseur
            compter = coor_chasseur + 25
            plus_un = 0
            parcours = 0
            z = 0

            while tempo not in intrus1:
                comptage += 1
                tempo += 25
            comptage -= 1 
            
            while  z < comptage: #dans cette boucle on cherche a savoir si la proie se trouve a gauche de la ligne verticale a laquelle le chasseur appartient
                parcours = compter - 1
               
                while parcours not in intrus:
                    if parcours == coor_proie:
                        plus_un += 1
                    else:
                        plus_un += 0
                    parcours -= 1
                    
                compter += 25
                
                z += 1
                    
            road = coor_chasseur + 25
            indice = [] 

            while road not in intrus:
                indice.append(road)
                road -= 1

            if plus_un == 1: #cela veut dire que la proie a ete trouve a gauche de la ligne verticale a laquelle le chasseur appartient 
                array[coor_chasseur] = " "
                coor_chasseur -= 1 #donc le chasseur recule pour alle le manger
                if coor_chasseur not in intrus: 
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                else:
                    coor_chasseur += 1
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur += 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur

                if coor_proie == coor_chasseur + 25:
                    array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat

                elif coor_proie == coor_chasseur - 1: 
                    array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat
                    
                else:
                    array[coor_chasseur] = " "
                    coor_chasseur += 25 #apres avoir recule de 1 le chasseur descend 
                    if coor_chasseur not in intrus1:
                        if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4]  or array[coor_chasseur] == apparence_des_entites[1]:
                            if array[coor_chasseur + 25] == " ":
                                coor_chasseur += 25
                                array[coor_chasseur] = chasseur
                            elif array[coor_chasseur - 25] == " ":
                                coor_chasseur -= 25
                                array[coor_chasseur] = chasseur
                            else:
                                coor_chasseur += 25
                                array[coor_chasseur] = chasseur
                        else:
                            array[coor_chasseur] = chasseur
                        tab_souris[0] = coor_chasseur
                        repeat = tab_souris[0]
                        return repeat
                        
                    else:
                        coor_chasseur -= 25
                        if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                            if array[coor_chasseur + 25] == " ":
                                coor_chasseur += 25
                                array[coor_chasseur] = chasseur
                            elif array[coor_chasseur - 25] == " ":
                                coor_chasseur -= 25
                                array[coor_chasseur] = chasseur
                            else:
                                coor_chasseur -= 25
                                array[coor_chasseur] = chasseur
                        else:
                            array[coor_chasseur] = chasseur
                        tab_souris[0] = coor_chasseur
                        repeat = tab_souris[0]
                        return repeat
                        
            elif coor_proie in indice:
                array[coor_chasseur] = " "
                coor_chasseur -= 1
                if coor_chasseur not in intrus:
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat
                else:
                    coor_chasseur += 1
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur += 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat

            else: 
                array[coor_chasseur] = " "
                coor_chasseur += 1
                if coor_chasseur not in intrus3:
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur += 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                else:
                    coor_chasseur -= 1
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur

                if coor_proie == coor_chasseur + 25:
                    array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat
                elif coor_proie == coor_chasseur + 1:
                    array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat

                else:
                    array[coor_chasseur] = " "
                    coor_chasseur += 25
                    if coor_chasseur not in intrus1:
                        if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4]  or array[coor_chasseur] == apparence_des_entites[1]:
                            if array[coor_chasseur + 25] == " ":
                                coor_chasseur += 25
                                array[coor_chasseur] = chasseur
                            elif array[coor_chasseur - 25] == " ":
                                coor_chasseur -= 25
                                array[coor_chasseur] = chasseur
                            else:
                                coor_chasseur += 25
                                array[coor_chasseur] = chasseur
                        else:
                            array[coor_chasseur] = chasseur
                        tab_souris[0] = coor_chasseur
                        repeat = tab_souris[0]
                        return repeat    
                    else:
                        coor_chasseur -= 25
                        if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                            if array[coor_chasseur + 25] == " ":
                                coor_chasseur += 25
                                array[coor_chasseur] = chasseur
                            elif array[coor_chasseur - 25] == " ":
                                coor_chasseur -= 25
                                array[coor_chasseur] = chasseur
                            else:
                                coor_chasseur -= 25
                                array[coor_chasseur] = chasseur
                        else:
                            array[coor_chasseur] = chasseur
                        tab_souris[0] = coor_chasseur
                        repeat = tab_souris[0]
                        return repeat
                   
        else:
            tempo = coor_chasseur - 25
            comptage = 0
            compter = coor_chasseur - 25
            plus_un = 0
            z = 0
            while tempo not in intrus2:
                comptage += 1
                tempo -= 25
            comptage -= 1
            
            while  z < comptage:
                parcours = compter - 1
                
                while parcours not in intrus:
                    if parcours == coor_proie:
                        plus_un += 1
                    else:
                        plus_un += 0
                    parcours -= 1
            
                compter -= 25    
                z += 1


            road = coor_chasseur
            indice = []

            while road not in intrus:
                indice.append(road)
                road -= 1  

            if plus_un == 1:
                array[coor_chasseur] = " "
                coor_chasseur -= 1
                if coor_chasseur not in intrus:
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                else:
                    coor_chasseur += 1
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur += 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur

                if coor_proie == coor_chasseur - 25:
                    array[coor_chasseur] = " "
                    array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat

                else:
                    array[coor_chasseur] = " "
                    coor_chasseur -= 25
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat

            elif coor_proie in indice:
                array[coor_chasseur] = " "
                coor_chasseur -= 1
                if coor_chasseur not in intrus:
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat
                else:
                    coor_chasseur += 1
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur += 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat
            else:
                array[coor_chasseur] = " "
                coor_chasseur += 1
                if coor_chasseur not in intrus3:
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur += 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                else:
                    coor_chasseur -= 1
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 1
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur

                if coor_proie == coor_chasseur - 25:
                    array[coor_chasseur] = " "
                    array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat

                elif coor_proie == coor_chasseur + 1:
                    array[coor_chasseur] = " "
                    array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat

                else:
                    array[coor_chasseur] = " "
                    coor_chasseur -= 25
                    if array[coor_chasseur] == apparence_des_entites[3] or array[coor_chasseur] == apparence_des_entites[2] or array[coor_chasseur] == apparence_des_entites[4] or array[coor_chasseur] == apparence_des_entites[1]:
                        if array[coor_chasseur + 25] == " ":
                            coor_chasseur += 25
                            array[coor_chasseur] = chasseur
                        elif array[coor_chasseur - 25] == " ":
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                        else:
                            coor_chasseur -= 25
                            array[coor_chasseur] = chasseur
                    else:
                        array[coor_chasseur] = chasseur
                    tab_souris[0] = coor_chasseur
                    repeat = tab_souris[0]
                    return repeat


#rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr





#fontion qui permettra au chasseur de manger ou de mourir
# pos_ante_predateur est la position qu'occupait le predateur avant son deplacement
def degustation(array, pos_proie, pos_predateur, chasseur, stat, pos_ante_predateur):

    coor_chasseur = pos_predateur
    coor_proie = pos_proie

    if coor_proie == coor_chasseur - 1: #si la proie se trouve a la gauche du predateur
        temp = coor_chasseur - coor_proie #l'ecart qui separe les deux points
        array[coor_chasseur] = " "
        array[coor_proie] = " "
        coor_chasseur -= temp
        array[coor_chasseur] = chasseur
        if pos_ante_predateur in stat:#ceci aidera a faire les tableaux statistique; stat ici present est le tableau qui content la statistique du type de predateur entre en parametre 
            state = 0
            i = 0

            while i < len(stat):
                if stat[i] == pos_ante_predateur:
                    state = i
                    stat[state] = pos_predateur
                    state += 1
                    if stat[state] != 0:
                        stat[state] = 6

                    else:
                        del stat[state]
                        del stat[state - 1]
                        del stat[state - 2]
                        array[pos_predateur] = " "
                else:
                    pass
                i += 1

        else:

            if (stat[len(stat) - 3 + 1]) != "Position":     
                stat.append(stat[len(stat) - 3] + 1)
                stat.append(pos_predateur)
                stat.append(6)
            else:
                stat.append(1)
                stat.append(pos_predateur)
                stat.append(6)
 
        return array

    elif coor_proie == coor_chasseur + 25: #si la proie se trouve en dessous du predateur
        temp = coor_proie - coor_chasseur  #l'ecart qui separe les deux points
        array[coor_chasseur] = " "
        array[coor_proie] = " "
        coor_chasseur += temp
        array[coor_chasseur] = chasseur
        if pos_ante_predateur in stat:
            state = 0
            i = 0

            while i < len(stat):
                if stat[i] == pos_ante_predateur:
                    state = i
                    stat[state] = pos_predateur
                    state += 1
                    if stat[state] != 0:
                        stat[state] = 6
                    else:
                        del stat[state]
                        del stat[state - 1]
                        del stat[state - 2]
                        array[pos_predateur] = " "
                else:
                    pass
                i += 1     

        else:

            if (stat[len(stat) - 3 + 1]) != "Position":     
                stat.append(stat[len(stat) - 3] + 1)
                stat.append(pos_predateur)
                stat.append(6)
            else:
                stat.append(1)
                stat.append(pos_predateur)
                stat.append(6)
 
        return array

    elif coor_proie == coor_chasseur + 1: #si la proie se trouve a la droite du predateur
        temp = coor_proie - coor_chasseur  #l'ecart qui separe les deux points
        array[coor_chasseur] = " "
        array[coor_proie] = " "
        coor_chasseur += temp
        array[coor_chasseur] = chasseur
        if pos_ante_predateur in stat:
            state = 0
            i = 0

            while i < len(stat):
                if stat[i] == pos_ante_predateur:
                    state = i
                    stat[state] = pos_predateur
                    state += 1
                    if stat[state] != 0:
                        stat[state] = 6
                    else:
                        del stat[state]
                        del stat[state - 1]
                        del stat[state - 2]
                        array[pos_predateur] = " "
                else:
                    pass
                i += 1

        else:

            if (stat[len(stat) - 3 + 1]) != "Position":     
                stat.append(stat[len(stat) - 3] + 1)
                stat.append(pos_predateur)
                stat.append(6)
            else:
                stat.append(1)
                stat.append(pos_predateur)
                stat.append(6) 
        return array
    
    elif coor_proie == coor_chasseur - 25: #si la proie se trouve au dessus du predateur
        temp = coor_chasseur - coor_proie  #l'ecart qui separe les deux points
        array[coor_chasseur] = " "
        array[coor_proie] = " "
        coor_chasseur -= temp
        array[coor_chasseur] = chasseur
        if pos_ante_predateur in stat:
            state = 0
            i = 0

            while i < len(stat):
                if stat[i] == pos_ante_predateur:
                    state = i
                    stat[state] = pos_predateur
                    state += 1
                    if stat[state] != 0:
                        stat[state] = 6
                    else:
                        del stat[state]
                        del stat[state - 1]
                        del stat[state - 2]
                        array[pos_predateur] = " "
                else:
                    pass
                i += 1 

        else:
         
            if (stat[len(stat) - 3 + 1]) != "Position":     
                stat.append(stat[len(stat) - 3] + 1)
                stat.append(pos_predateur)
                stat.append(6)
            else:
                stat.append(1)
                stat.append(pos_predateur)
                stat.append(6)

        return array
    else:

        if pos_ante_predateur in stat:

            state = 0
            i = 0

            while i < len(stat):
                if stat[i] == pos_ante_predateur:
                    state = i
                 
                    stat[state] = pos_predateur
                    state += 1
                    if stat[state] != 0:
                        stat[state] -= 1
                       
                    else:
                        del stat[state]
                        del stat[state - 1]
                        del stat[state - 2]
                        array[pos_predateur] = " "
                else:
                    pass
                i += 1


        else:  
            if (stat[len(stat) - 3 + 1]) != "Position":     
                stat.append(stat[len(stat) - 3] + 1)
                stat.append(pos_predateur)
                stat.append(6)
            else:
                stat.append(1)
                stat.append(pos_predateur)
                stat.append(6)



#fonction qui permettra a l'individu entrer en parametre de se reproduire si il le peut
def procreation(array, p_male, p_femelle, male, femelle):
    super_intrus = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 49, 74, 99, 124, 149, 174, 199, 224, 249, 274, 299, 324, 349, 374, 399, 424, 449, 474, 499, 524, 549, 574, 599]
    coor_pere = p_male
    coor_mere = p_femelle
    
    ma_liste = [male, femelle]

    choice = random.choice(ma_liste)

    if coor_mere == coor_pere - 1:
        if ((coor_mere + 50) in range(0, 625)) and ((coor_mere + 50) not in super_intrus) and ((coor_mere - 50) in range(0, 625)) and ((coor_mere - 50) not in super_intrus) and ((coor_mere - 2) in range(0, 625)) and ((coor_mere - 2) not in super_intrus):
            if (array[coor_mere + 50] == " "):
                coor_mere += 50
                array[coor_mere] = choice
            elif (array[coor_mere - 50] == " "):
                coor_mere -= 50
                array[coor_mere] = choice

            elif (array[coor_mere - 2] == " "):
                coor_mere -= 2
                array[coor_mere] = choice
            else:
                pass
        else:
            pass
        

    elif coor_mere == coor_pere + 25:
        if ((coor_mere + 50) in range(0, 625)) and ((coor_mere + 50) not in super_intrus) and ((coor_mere - 2) in range(0, 625)) and ((coor_mere - 2) not in super_intrus) and ((coor_mere + 2) in range(0, 625)) and ((coor_mere + 2) not in super_intrus):
            if (array[coor_mere + 50] == " "):
                coor_mere += 50
                array[coor_mere] = choice
            elif (array[coor_mere - 2] == " "):
                coor_mere -= 2
                array[coor_mere] = choice

            elif (array[coor_mere + 2] == " "):
                coor_mere += 2
                array[coor_mere] = choice
            else:
                pass
        else:
            pass


    elif coor_mere == coor_pere + 1:
        if ((coor_mere + 50) in range(0, 625)) and ((coor_mere + 50) not in super_intrus) and ((coor_mere - 50) in range(0, 625)) and ((coor_mere - 50) not in super_intrus) and ((coor_mere + 2) in range(0, 625)) and ((coor_mere + 2) not in super_intrus):
            if (array[coor_mere + 50] == " "):
                coor_mere += 50
                array[coor_mere] = choice
            elif (array[coor_mere - 50] == " "):
                coor_mere -= 50
                array[coor_mere] = choice

            elif (array[coor_mere + 2] == " "):
                coor_mere += 2
                array[coor_mere] = choice
            else:
                pass
        else:
            pass





    elif coor_mere == coor_pere - 25:
        if ((coor_mere - 50) in range(0, 625)) and ((coor_mere - 50) not in super_intrus) and ((coor_mere - 2) in range(0, 625)) and ((coor_mere - 2) not in super_intrus) and ((coor_mere + 2) in range(0, 625)) and ((coor_mere + 2) not in super_intrus):
            if (array[coor_mere - 50] == " "):
                coor_mere -= 50
                array[coor_mere] = choice
            elif (array[coor_mere - 2] == " "):
                coor_mere -= 2
                array[coor_mere] = choice

            elif (array[coor_mere + 2] == " "):
                coor_mere += 2
                array[coor_mere] = choice
            else:
                pass
        else:
            pass
    else:
        pass







# ****************************************************************************************************************************************************************************************************************************************************************************************************************************************
#------------------------------- --------------------------------------VERSION ORIENTEE OBJET-------------------------------------------------------------------------------------------------------
# ****************************************************************************************************************************************************************************************************************************************************************************************************************************************


statistique_chats = ['Chat', 'Position', 'Vie']#tableau qui contiendra la statistique des chats
statistique_souris = ['Souris', 'Position', 'Vie']#tableau qui contiendra la statistique des chats
chats_presents = []#tableau qui contiendra la position des chats retrouvés par la fonction detecteur()
souris_presentes = []#tableau qui contiendra la position des souris retrouvés par la fonction detecteur()

chat1 = chat(apparence_des_entites[3], [apparence_des_entites[1], apparence_des_entites[2]], 0, 'femelle')#creation d'un chat
state = new_insert(tableau, chat1.chasseur)#insertion du chat dans le tableau

chat2 = chat(apparence_des_entites[4], [apparence_des_entites[1], apparence_des_entites[2]], 0, 'mâle')
state = new_insert(tableau, chat2.chasseur)

chat3 = chat(apparence_des_entites[3], [apparence_des_entites[1], apparence_des_entites[2]], 0, 'femelle')
state = new_insert(tableau, chat3.chasseur)

chat2 = chat(apparence_des_entites[4], [apparence_des_entites[1], apparence_des_entites[2]], 0, 'mâle')
state = new_insert(tableau, chat2.chasseur)

chat3 = chat(apparence_des_entites[3], [apparence_des_entites[1], apparence_des_entites[2]], 0, 'femelle')
state = new_insert(tableau, chat3.chasseur)

souris1 = souris(apparence_des_entites[1], apparence_des_entites[0], 0, 'femelle')#creation d'une souris
sta_te = new_insert(tableau, souris1.chasseur)#insertion de la souris dans le tableau

souris2 = souris(apparence_des_entites[2], apparence_des_entites[0], 0, 'mâle')
sta_te = new_insert(tableau, souris2.chasseur)





detecteur(tableau, chats_presents, apparence_des_entites[3])
detecteur(tableau, chats_presents, apparence_des_entites[4])

detecteur(tableau, souris_presentes, apparence_des_entites[1])
detecteur(tableau, souris_presentes, apparence_des_entites[2])

#fonction qui permettra d'inserer dans les tableaux statistiques, les chats presents qinsi que leurs positions et leurs nombre initiale de vie
def count_position_life(tab_stat, unit_position):
    b = 0
    d = 1
    life = 6
    while b < len(unit_position):
        tab_stat.append(d)
        tab_stat.append(unit_position[b])
        tab_stat.append(life)
        b += 1
        d += 1
#fonction qui permettra d'afficher les tableaux statistique
def afficher_ter(statistique):
    i = 0
    j = 1
    while i < len(statistique):
       print(statistique[i], statistique[i+1], statistique[i+2],"\n") 
       i += 3

count_position_life(statistique_chats, chats_presents)
count_position_life(statistique_souris, souris_presentes)

chats_presents = []
souris_presentes = []
while 1:#boucle infinie qui fait tourner la simulation
    time.sleep(0.5)
    os.system('clear')

    control = verification(tableau, apparence_des_entites[0])
    if control == 0:
        for i in range(0, 3):
            pose = new_insert(tableau, apparence_des_entites[0])
    else:
        pass

 
    detecteur(tableau, souris_presentes, apparence_des_entites[1])
    detecteur(tableau, souris_presentes, apparence_des_entites[2])
    
    i = 0
#on s'occupe des souris qui ont ete trouve par detecteur()
    while i < len(souris_presentes):
        control = verification(tableau, apparence_des_entites[1])
        
        controlle = verification(tableau, apparence_des_entites[2])
        
        if (control == 0) and (controlle == 0):
            mouse = apparence_des_entites[2]
            typ_e = "mâle"
            t = 0
            while t < 5:
                souris6 = souris(mouse, apparence_des_entites[0], 0, typ_e)
                encore_souris = new_insert(tableau, mouse)
                ma_liste = [apparence_des_entites[2], apparence_des_entites[1]]
                mouse = random.choice(ma_liste)
                t += 1

        else:
            pass

        cible = []#contiendra les positions de toutes les souris
        detecteur(tableau, cible, apparence_des_entites[0])
        
        comparateur = []#contiendra les differences de position qui existe entre le chat de la position j et les souris ciblee
        k = 0   
        tempo = 0    
        while k <len(cible):
            tempo = souris_presentes[i] - cible[k]
            comparateur.append(tempo)
            k += 1


        negatif = []
        positif = []
        classeur = []
        positiveur = 0
        z = 0
        # dans la fonction ci dessous, on cherche la proie la plus proche de la souris, on va donc mettre les negatifs de comparateur dans un tableau et les positifs 
        # dans un autre ensuite, on va rendre toutes les valeurs qui etaient negative positives, puis on va joindre les nouveaux positifs a ceux qui l'etaient depuis
        # et on va chercher le plus petit dans ce nouveau tableau puis on va verifier si il etait negatif avant, on le retransformera en negatif sinon on coninuera avec lui
        while z < len(comparateur):
            if comparateur[z] in range(-1000, 0):
                positiveur = comparateur[z] * (-1)
                negatif.append(positiveur)
            else:
                positif.append(comparateur[z])

            z += 1
        z = 0

        while z < len(negatif):
            classeur.append(negatif[z])
            z += 1
        z = 0
        while z < len(positif):
            classeur.append(positif[z])
            z += 1

        z = 0
        less_than = classeur[0]
        while z < len(classeur):
            if less_than > classeur[z]:
                less_than = classeur[z]
            else:
                pass
            z += 1

        vrai_less_than = 0

        if less_than in negatif:
            vrai_less_than = less_than * (-1)
        else:
            vrai_less_than = less_than
        
        control = verification(tableau, apparence_des_entites[1])
        controlle = verification(tableau, apparence_des_entites[2])
        somme = control + controlle
        if (somme <= 7):
            if tableau[souris_presentes[i]] == apparence_des_entites[2]:
                if tableau[souris_presentes[i] + 1] == apparence_des_entites[1]:
                    coor_pere = souris_presentes[i]
                    coor_mere = souris_presentes[i] + 1
                    procreation(tableau, coor_pere, coor_mere, tableau[souris_presentes[i]], tableau[souris_presentes[i] + 1])
            
                elif tableau[souris_presentes[i] - 1] == apparence_des_entites[1]:
                    coor_pere = souris_presentes[i]
                    coor_mere = souris_presentes[i] - 1
                    procreation(tableau, coor_pere, coor_mere, tableau[souris_presentes[i]], tableau[souris_presentes[i] - 1])
            
                elif tableau[souris_presentes[i] + 25] == apparence_des_entites[1]:
                    coor_pere = souris_presentes[i]
                    coor_mere = souris_presentes[i] + 25
                    procreation(tableau, coor_pere, coor_mere, tableau[souris_presentes[i]], tableau[souris_presentes[i] + 25])
        
                elif tableau[souris_presentes[i] - 25] == apparence_des_entites[1]:
                    coor_pere = souris_presentes[i]
                    coor_mere = souris_presentes[i] - 25
                    procreation(tableau, coor_pere, coor_mere, tableau[souris_presentes[i]], tableau[souris_presentes[i] - 25])
            
                else:
                    pass
            else:
                if tableau[souris_presentes[i] + 1] == apparence_des_entites[2]:
                    coor_pere = souris_presentes[i] + 1
                    coor_mere = souris_presentes[i]
                    procreation(tableau, coor_pere, coor_mere, tableau[souris_presentes[i] + 1], tableau[souris_presentes[i]])
            
                elif tableau[souris_presentes[i] - 1] == apparence_des_entites[2]:
                    coor_pere = souris_presentes[i] - 1
                    coor_mere = souris_presentes[i]
                    procreation(tableau, coor_pere, coor_mere, tableau[souris_presentes[i] - 1], tableau[souris_presentes[i]])
            
                elif tableau[souris_presentes[i] + 25] == apparence_des_entites[2]:
                    coor_pere = souris_presentes[i] + 25
                    coor_mere = souris_presentes[i]
                    procreation(tableau, coor_pere, coor_mere, tableau[souris_presentes[i] + 25], tableau[souris_presentes[i]])
        
                elif tableau[souris_presentes[i] - 25] == apparence_des_entites[2]:
                    coor_pere = souris_presentes[i] - 25
                    coor_mere = souris_presentes[i]
                    procreation(tableau, coor_pere, coor_mere, tableau[souris_presentes[i] - 25], tableau[souris_presentes[i]])
            
                else:
                    pass

        else:
            pass

    
        proie_ciblee = souris_presentes[i] - vrai_less_than #position de la cible
        dp_souris = deplacement(tableau, proie_ciblee, souris_presentes[i], tableau[souris_presentes[i]])
        mouse_eat = degustation(tableau, proie_ciblee, tab_souris[0], tableau[tab_souris[0]], statistique_souris, tab_pos_ante_souris[0])

        control = verification(tableau, apparence_des_entites[0])
        if control == 0:
            for i in range(0, 5):
                pose = new_insert(tableau, apparence_des_entites[0])
        else:
            pass
        i += 1


    souris_presentes  = []

    detecteur(tableau, chats_presents, apparence_des_entites[3])
    detecteur(tableau, chats_presents, apparence_des_entites[4])

    j = 0

    while j < len(chats_presents):
        control = verification(tableau, apparence_des_entites[1])
        
        controlle = verification(tableau, apparence_des_entites[2])
        
        if (control == 0) and (controlle == 0):
            mouse = apparence_des_entites[2]
            typ_e = "mâle"
            t = 0
            while t < 5:
                souris6 = souris(mouse, apparence_des_entites[0], 0, typ_e)
                encore_souris = new_insert(tableau, mouse)
                ma_liste = [apparence_des_entites[2], apparence_des_entites[1]]
                mouse = random.choice(ma_liste)
                t += 1

        else:
            pass
        cible = []#contiendra les positions de toutes les souris
        detecteur(tableau, cible, apparence_des_entites[1])
        detecteur(tableau, cible, apparence_des_entites[2])
        comparateur = []#contiendra les differences de position qui existe entre le chat de la position j et les souris ciblee
        k = 0   
        tempo = 0    
        while k <len(cible):
            tempo = chats_presents[j] - cible[k]
            comparateur.append(tempo)
            k += 1

        negatif = []
        positif = []
        classeur = []
        positiveur = 0
        z = 0
        # dans la fonction ci dessous, on cherche la proie la plus proche de la souris, on va donc mettre les negatifs de comparateur dans un tableau et les positifs 
        # dans un autre ensuite, on va rendre toutes les valeurs qui etaient negative positives, puis on va joindre les nouveaux positifs a ceux qui l'etaient depuis
        # et on va chercher le plus petit dans ce nouveau tableau puis on va verifier si il etait negatif avant, on le retransformera en negatif sinon on coninuera avec lui
        while z < len(comparateur):
            if comparateur[z] in range(-1000, 0):
                positiveur = comparateur[z] * (-1)
                negatif.append(positiveur)
            else:
                positif.append(comparateur[z])

            z += 1
        z = 0

        while z < len(negatif):
            classeur.append(negatif[z])
            z += 1
        z = 0
        
        while z < len(positif):
            classeur.append(positif[z])
            z += 1

        z = 0
    
        less_than = classeur[0]
        
        while z < len(classeur):
            if less_than > classeur[z]:
                less_than = classeur[z]
            else:
                pass
            z += 1

        vrai_less_than = 0

        if less_than in negatif:
            vrai_less_than = less_than * (-1)
        
        else:
            vrai_less_than = less_than

        control = verification(tableau, apparence_des_entites[3])
        
        controlle = verification(tableau, apparence_des_entites[4])
        
        somme = control + controlle
        
        if (somme <= 7):
            if tableau[chats_presents[j]] == apparence_des_entites[4]:
                if tableau[chats_presents[j] + 1] == apparence_des_entites[3]:
                    coor_pere = chats_presents[j]
                    coor_mere = chats_presents[j] + 1
                    procreation(tableau, coor_pere, coor_mere, tableau[chats_presents[j]], tableau[chats_presents[j] + 1])
            
                elif tableau[chats_presents[j] - 1] == apparence_des_entites[3]:
                    coor_pere = chats_presents[j]
                    coor_mere = chats_presents[j] - 1
                    procreation(tableau, coor_pere, coor_mere, tableau[chats_presents[j]], tableau[chats_presents[j] - 1])
            
                elif tableau[chats_presents[j] + 25] == apparence_des_entites[3]:
                    coor_pere = chats_presents[j]
                    coor_mere = chats_presents[j] + 25
                    procreation(tableau, coor_pere, coor_mere, tableau[chats_presents[j]], tableau[chats_presents[j] + 25])
        
                elif tableau[chats_presents[j] - 25] == apparence_des_entites[3]:
                    coor_pere = chats_presents[j]
                    coor_mere = chats_presents[j] - 25
                    procreation(tableau, coor_pere, coor_mere, tableau[chats_presents[j]], tableau[chats_presents[j] - 25])
            
                else:
                    pass
            else:
                if tableau[chats_presents[j] + 1] == apparence_des_entites[4]:
                    coor_pere = chats_presents[j] + 1
                    coor_mere = chats_presents[j]
                    procreation(tableau, coor_pere, coor_mere, tableau[chats_presents[j] + 1], tableau[chats_presents[j]])
            
                elif tableau[chats_presents[j] - 1] == apparence_des_entites[4]:
                    coor_pere = chats_presents[j] - 1
                    coor_mere = chats_presents[j]
                    procreation(tableau, coor_pere, coor_mere, tableau[chats_presents[j] - 1], tableau[chats_presents[j]])
            
                elif tableau[chats_presents[j] + 25] == apparence_des_entites[4]:
                    coor_pere = chats_presents[j] + 25
                    coor_mere = chats_presents[j]
                    procreation(tableau, coor_pere, coor_mere, tableau[chats_presents[j] + 25], tableau[chats_presents[j]])
        
                elif tableau[chats_presents[j] - 25] == apparence_des_entites[4]:
                    coor_pere = chats_presents[j] - 25
                    coor_mere = chats_presents[j]
                    procreation(tableau, coor_pere, coor_mere, tableau[chats_presents[j] - 25], tableau[chats_presents[j]])
            
                else:
                    pass
        else:
            pass
    
        proie_ciblee = chats_presents[j] - vrai_less_than

        dp_chat = deplacement(tableau, proie_ciblee, chats_presents[j], tableau[chats_presents[j]])
        
        cat_eat = degustation(tableau, proie_ciblee, tab_chat[0], tableau[tab_chat[0]], statistique_chats, tab_pos_ante_chat[0])
        if tableau[proie_ciblee] != apparence_des_entites[2] and tableau[proie_ciblee] != apparence_des_entites[1]:

            r = 0
            while r < len(statistique_souris):
                if statistique_souris[r] == proie_ciblee:

                    del statistique_souris[r]
                    del statistique_souris[r-1]
                    del statistique_souris[r-1]
                else:
                    pass
                r += 1

        else:
            pass


        t = 3
        #permet d'effacer du tableau statistiques des souris les traces des souris mortes ou non existantes
        while t < len(statistique_souris):
            if tableau[statistique_souris[t + 1]] != apparence_des_entites[1] and tableau[statistique_souris[t + 1]] != apparence_des_entites[2]:
                del statistique_souris[t]
                del statistique_souris[t]
                del statistique_souris[t]
            else:
                pass
            t += 3

        t = 3
        #permet d'effacer du tableau statistiques des chats les traces des chats morts ou non existants
        while t < len(statistique_chats):
            if tableau[statistique_chats[t + 1]] != apparence_des_entites[3] and tableau[statistique_chats[t + 1]] != apparence_des_entites[4]:
                del statistique_chats[t]
                del statistique_chats[t]
                del statistique_chats[t]
            else:
                pass
            t += 3

        

        j += 1
        
        control = verification(tableau, apparence_des_entites[1])
        
        controlle = verification(tableau, apparence_des_entites[2])
        
        if (control == 0) and (controlle == 0):
            mouse = apparence_des_entites[2]
            typ_e = "mâle"
            t = 0
            while t < 5:
                souris6 = souris(mouse, apparence_des_entites[0], 0, typ_e)
                encore_souris = new_insert(tableau, mouse)
                ma_liste = [apparence_des_entites[2], apparence_des_entites[1]]
                mouse = random.choice(ma_liste)
                t += 1

        else:
            pass

    control = verification(tableau, apparence_des_entites[3])    
    controlle = verification(tableau, apparence_des_entites[4])
        
    if (control == 0) and (controlle == 0):
        cat = apparence_des_entites[4]
        typ_e = "mâle"
        t = 0
        while t < 5:
            chat6 = chat(cat, [apparence_des_entites[1], apparence_des_entites[2]], 0, typ_e)
            encore_chat = new_insert(tableau, cat)
            ma_liste = [apparence_des_entites[4], apparence_des_entites[3]]
            mouse = random.choice(ma_liste)
            t += 1

    else:
        pass
    chats_presents = []

    super_intrus = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 49, 74, 99, 124, 149, 174, 199, 224, 249, 274, 299, 324, 349, 374, 399, 424, 449, 474, 499, 524, 549, 574, 599]
    
    stock_pos_condanne = 0
    
    for i in range(0, 625):
        if (i in super_intrus) and ((tableau[i] == apparence_des_entites[2]) or (tableau[i] == apparence_des_entites[1]) or (tableau[i] == apparence_des_entites[4]) or (tableau[i] == apparence_des_entites[3])):
            tableau[i] = "O"
        else:
            pass 
    
    afficher_terrain(tableau)
    afficher_ter(statistique_chats)
    afficher_ter(statistique_souris)
#ces deux dernieres lignes permettent d'afficher les deux tableaux statistiques veuiller les mettre en commentaire pour mieux apprecier les deplacements des entités 
