import random


largeur = 50
longueur = 25

joueur = "🧍"
shop = "🏫"

arbre = "🌲", "🌴", "🌵", "🌳"
rocher = "🗿"
batiment1 = "🏡"
batiment2 = "🏢"
batiment3 = "🏬"
batiment4 = "🏯"
batiment5 = "🏰"

pepette = 0
bois = 0
pierre = 0


carte = [["⬛" for _ in range(largeur)] for _ in range(longueur)]

for y in range(longueur):
    for x in range(largeur):
        if random.random() < 0.01:
            carte[y][x] = random.choice(arbre)
        elif random.random() < 0.009:
            carte[y][x] = random.choice(rocher)
        else:
            carte[y][x] = random.choice("⬛")


joueur_x = 0
joueur_y = 0
carte[joueur_x][joueur_y] = joueur

shop_x = 12
shop_y = 25
carte[shop_x][shop_y] = shop

print("\n")

def se_deplacer(joueur_x, joueur_y, carte, bois, pierre):
    deplacement_joueur_x = int(input("Vers quelle case souhaitez-vous vous déplacer ? (y) : "))
    deplacement_joueur_y = int(input("Vers quelle case souhaitez-vous vous déplacer ? (x) : "))

    if 0 <= deplacement_joueur_x < largeur or 0 <= deplacement_joueur_y < longueur :                                

        carte[joueur_x][joueur_y] = '⬛'  
        if carte [deplacement_joueur_x][deplacement_joueur_y] in arbre :                                         
            bois += 20
            print("Vous avez récupéré 20 bois !")
        elif carte[deplacement_joueur_x][deplacement_joueur_y] == rocher :
            pierre += 10
            print("Vous avez récupéré 10 pierre !")


        carte[deplacement_joueur_x][deplacement_joueur_y] = joueur
        joueur_x, joueur_y = deplacement_joueur_x, deplacement_joueur_y
    
    else:
        print("Déplacement hors des limites de la carte !")


    return joueur_x, joueur_y, bois, pierre


def build(batiment1, carte, joueur_x, joueur_y):
    if pepette >= 200 :                                                    
        carte[joueur_y][joueur_x +1] = batiment1

    else:
        print("Il vous faut 200 pepettes pour construire un bâtiment ! ")

        return carte


def upgrade(batiment1, batiment2, batiment3, batiment4, batiment5, carte, joueur_x, joueur_y) :
    
    if pepette >= 500 :
        if carte [joueur_y][joueur_x +1] == batiment1 :
            carte[joueur_y][joueur_x +1] = batiment2
        elif carte [joueur_y][joueur_x +1] == batiment2 :
            carte[joueur_y][joueur_x +1] = batiment3
        elif carte [joueur_y][joueur_x +1] == batiment3 :
            carte[joueur_y][joueur_x +1] = batiment4
        elif carte [joueur_y][joueur_x +1] == batiment4 :
            carte[joueur_y][joueur_x +1]= batiment5

    else:
        print("Il vous faut 500 pepettes pour améliorer ce bâtiment ! ")

        return carte

def vendre(bois, pierre, pepette, joueur_x, joueur_y, shop_x, shop_y) :
    var2 = True
    if var2 :
        if joueur_x == shop_x and joueur_y == shop_y - 1:
        
            pepette += bois * 2
            pepette += pierre * 3
        
            bois = 0
            pierre = 0

            print(f"Vente réussie! Vous avez maintenant {pepette} pepettes.")

        else:
            print("Vous devez vous trouver devant le shop pour vendre vos ressources !")

        return bois, pierre, pepette, joueur_x, joueur_y, shop_x, shop_y



run = True
while run :
    for ligne in carte:
        print("".join(ligne))



    print(f'''
 |=============================================================|                            - Tapez 1 pour déplacer votre personnage (x & y) \n  
  |                      *** Ressources ***                     |                            - Tapez 2 pour récupérer une ressource (vous devez vous trouver sur la case de la ressource)  \n
   |    💲 = {pepette}                                                   |                            - Tapez 3 pour construire un bâtiment \n
    |    Bois = {bois}                                                 |                            - Tapez 4 pour améliorer un bâtiment \n                      
     |    Pierre = {pierre}                                               |                            - Tapez sur 5 pour vendre vos ressource  \n 
      |=============================================================|
''' )


    match int(input("Que souhaitez-vous faire ? : ")) :
        case 1 :
            joueur_x, joueur_y, bois, pierre= se_deplacer(joueur_x, joueur_y, carte, bois, pierre)

        case 2 : 
            recup(arbre, rocher, bois, joueur_x, joueur_y)
        case 3 :
            build(batiment1, carte, joueur_x, joueur_y)
        case 4 :
            upgrade(batiment1, batiment2, batiment3, batiment4, batiment5, carte, joueur_x, joueur_y)
        case 5 :
            bois, pierre, pepette, joueur_x, joueur_y, shop_x, shop_y = vendre(bois, pierre, pepette, joueur_x, joueur_y, shop_x, shop_y)
        case 6 :
            run = False