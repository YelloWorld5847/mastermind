# Jeu du Mastermind - Python Console

Ce projet est une implémentation du célèbre jeu **Mastermind** en Python, jouable directement dans la console. L'objectif est de deviner une combinaison de couleurs générée aléatoirement par l'ordinateur, avec des indices donnés après chaque tentative.

---

## Fonctionnalités principales

1. **Interface console colorée** :
   - Les couleurs sont représentées à l'aide de la bibliothèque `colorama`.
   - Les combinaisons et les indices s'affichent en couleurs pour une meilleure expérience visuelle.

2. **Logique du jeu Mastermind** :
   - Le joueur doit deviner une combinaison de 4 couleurs parmi 6 disponibles.
   - Après chaque tentative :
     - Un **cercle rouge** (`●`) indique une couleur bien placée.
     - Un **cercle blanc** (`●`) indique une couleur correcte mais mal placée.

3. **Personnalisation des paramètres** :
   - Nombre de tentatives (par défaut : 12).
   - Les couleurs disponibles :
     - Jaune, Bleu, Rouge, Vert, Blanc, Magenta.

4. **Génération aléatoire de la combinaison secrète** :
   - L'ordinateur génère une combinaison de 4 couleurs aléatoires au début de chaque partie.

5. **Système de validation** :
   - Vérifie si l'entrée du joueur respecte le format attendu (4 chiffres entre 1 et 6).

---

## Prérequis

1. **Python 3.8 ou supérieur**
2. **Bibliothèque requise** :
   - `colorama` : Affichage coloré dans la console.

Installez la bibliothèque avec la commande :
```bash
pip install colorama
