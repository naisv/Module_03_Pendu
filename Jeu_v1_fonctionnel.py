"""
VIGROUX Naïs - VIGN90290401
MGA802-01 ETE26
Module 03 - Jeu du Pendu
"""
import random
import unicodedata
import string

# FONCTIONS DE CONFIGURATION -------------------------------------------------------------------------------------------
""" Cette fonction permet au joueur de fournir son propre fichier de mots en répondant "oui" exactement (sans majuscule): 
- le fichier doit contenir seulement des mots (pas de tabulation) et ne pas être vide
- l'utilisateur doit donner le chemin d'accès de l'ordinateur vers ce fichier
- les mots peuvent contenir des accents que le code triera ensuite
Pour toute autre réponse, le code prendra le fichier de mots par défaut fourni sur Moodle """
def fournir_mots():
    rep=str(input("Voulez-vous utiliser votre propre fichier texte ? oui ou non"))
    if rep== "oui":
        fichier=input("Insérez l'adresse complète du fichier :")
    else:
        fichier="set_de_mots_moodle.txt"
    return fichier

"""Cette fonction enregistre les mots du fichier fourni en paramètre dans une liste "mots" 
puis en retourne un choisi aléatoirement"""
def selectionner_mot(fichier):
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            mots=f.read().split()
    except FileNotFoundError:
        print("Fichier introuvable. Utilisation du fichier par défaut.")
        with open("set_de_mots_moodle.txt", 'r', encoding='utf-8') as f:
            mots = f.read().split()
    return random.choice(mots)

#Cette fonction supprime les accents du mot fourni en paramètre et retourne le mot sans accent
def supprimer_accents(mot):
    forme_nfd = unicodedata.normalize('NFD', mot)
    mot_propre = "".join(c for c in forme_nfd if unicodedata.category(c) != 'Mn')
    return mot_propre

#FONCTIONS DE JEU -----------------------------------------------------------------------------------------------------
#Cette fonction affiche le nombre de chances qu'il reste au joueur
def afficher_chances(chances):
    print(f"Il vous reste {chances} chances.")

#Cette fonction vérifie s'il reste des lettres à deviner, sinon il indique au joueur qu'il a gagné
def gagner_partie(mot_devine, mot_complet):
    if "_" not in mot_devine:
        print(f"Bravo! Vous avez gagné. Le mot à deviner était {mot_complet}.")
        return True
    else:
        return False

#Cette fonction affiche au joueur qu'il a perdu et le mot qu'il cherchait à deviner
def perdu_partie(mot_complet):
    print(f"Dommage, vous avez perdu.Le mot à deviner était {mot_complet}.")

#Cette fonction affiche une lettre non présente dans le mot à deviner ni dans celles déjà tentées par l'utilisateur
def donner_bonus(mot_complet,liste_lettres):
    alphabet = string.ascii_lowercase
    lettres_absentes=[]
    for lettre in alphabet:
        if lettre not in mot_complet and lettre not in liste_lettres:
            lettres_absentes.append(lettre)
    bonus= random.choice(lettres_absentes)
    print(f"BONUS: La lettre {bonus} n'est pas dans le mot à deviner.")

#Cette fonction permet de rejouer en relançant la fonction "jouer_pendu" ou de quitter selon le souhait du joueur
def fin_de_partie():
    rep=str(input("Souhaitez-vous rejouer ? oui ou non "))
    if rep=="oui":
        jouer_pendu()
    else:
        exit()

"""Cette fonction demande au joueur d'entrer une lettre et vérifie qu'il s'agit bien d'une lettre unique non essayée précédemment
sinon elle boucle jusqu'à avoir une lettre valide"""
def demander_lettre(liste_lettres):
    while True:
        lettre = input("Entrez une lettre: ").lower()
        if len(lettre)!=1:
            print("Erreur: vous devez entrer une seule lettre")
        elif not   lettre.isalpha():
            print("Erreur: ce n'est pas une lettre valide")
        elif lettre in liste_lettres:
            print("Vous avez déjà deviné cette lettre")
        else:
            return lettre

"""Cette fonction vérifie si la lettre donnée par l'utilisateur se trouve dans le mot à deviner 
la variable mot_devine enregistre cette lettre à son emplacement et indique au joueur qu'il a trouvé
sinon elle indique au joueur que la lettre n'est pas dans le mot
la fonction retourne un booléen selon si la lettre devinée était dans le mot (True) ou pas (False)
Elle enregistre également les lettres données par le joueur et retourne la liste de lettres 
"""
def verifier_dans_le_mot(mot_devine, mot_complet, liste_lettres):
    reponse = False
    lettre=demander_lettre(liste_lettres)
    liste_lettres.append(lettre)
    for i in range (len(mot_complet)):
        if lettre==mot_complet[i]:
            mot_devine[i]=lettre
            reponse=True
    if reponse:
        print("La lettre est bien dans le mot.")
    else:
        print("La lettre ne se trouve pas dans le mot.")
    return reponse, liste_lettres

#FONCTION JEU COMPLET --------------------------------------------------------------------------------------------------
#Fonction jouer au pendu qui peut reboucler sur elle-même si le joueur souhaite rejouer :
def jouer_pendu(chances=6):
    print("Bienvenue dans le jeu du Pendu!")  # message de bienvenue
    fichier = fournir_mots()
    mot_initial = selectionner_mot(fichier)
    mot_complet = supprimer_accents(mot_initial).lower() #mot à deviner sans accent et en minuscule
    mot_devine = ["_"]*len(mot_complet) #initialisation de la variable qui enregistre l'avancée du joueur
    liste_lettres = [] #initialisation de la liste de lettres essayées par le joueur
    afficher_chances(chances)
    while chances > 0:
        print(mot_devine) #affichage de l'état d'avancée du joueur = lettres trouvées ou pas avec leur emplacement
        rep, liste_lettres=verifier_dans_le_mot(mot_devine, mot_complet, liste_lettres)
        if not rep:
            chances-=1

        if gagner_partie(mot_devine, mot_complet):
            fin_de_partie()

        if chances==1:
            donner_bonus(mot_complet, liste_lettres)

        afficher_chances(chances)

    if chances==0:
        perdu_partie(mot_complet)
        fin_de_partie()

#Lancement d'une partie de pendu ---------------------------------------------------------------------------------------
jouer_pendu()





