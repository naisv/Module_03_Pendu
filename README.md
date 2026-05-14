VIGROUX Naïs - VIGN90290401 \
MGA802-01 ETE26 
# Module 03 - Jeu du Pendu
Bienvenue dans ce Jeu du Pendu!   
Ce script permet de jouer au jeu du pendu dans la console Python de manière interactive.
## Fonctionnalités
* **Bibliothèque de mots**: le joueur peut fournir son propre fichier de mots (qui ne doit pas contenir de tabulation ni être vide) ou utiliser celui fourni par défaut
* **Casse et accents**: les accents sont supprimés par le code et la casse est gérée par le code pour ne pas impacter le jeu 
* **Nombre de chances**: le joueur a 6 chances par défaut, mais peut modifier cette valeur en précisant un nombre de chances en paramètre lors de l'appel de la fonction *jouer_pendu*
* **Bonus**: le joueur bénéficie d'un bonus lorsqu'il ne lui reste qu'une seule chance: le code lui indiquera une lettre non présente dans le mot ni dans ce qu'il a déjà deviné
* **Erreurs d'entrée**: le code reboucle si le joueur n'a pas entré une lettre valide unique ou s'il entre une lettre déjà devinée pour éviter de perdre des chances à cause d'erreurs de frappe
* **Fin de partie**: à la fin de la partie, le joueur a la possibilité de rejouer ou de quitter le jeu
* **Comment jouer ?**: il suffit de *Run* le code et la partie se lancera automatiquement
## Prérequis
**Version Python 3.9**  
**Bibliothèques**: *random*, *unicodedata*, *string* dont l'importation est dans le script
## Installation
Il faut clôner le dépôt Github sur votre machine.  
Télécharger le fichier de mots sous le nom *set_de_mots_moodle.txt* dans le même dossier que le code.   
*Run* le code et la partie commence. 
