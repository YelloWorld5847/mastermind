from colorama import Fore, init
import random

init(autoreset=True)

couleurs_arc_en_ciel = [
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.BLUE,
    Fore.MAGENTA
]


class Game:
    def __init__(self):
        super().__init__()

        self.carre = '\u25A0'
        self.rond = '\u25CF'

        self.tentatives = 12

        self.couleurs = {
            1: Fore.LIGHTYELLOW_EX,
            2: Fore.LIGHTBLUE_EX,
            3: Fore.LIGHTRED_EX,
            4: Fore.LIGHTGREEN_EX,
            5: Fore.LIGHTWHITE_EX,
            6: Fore.LIGHTMAGENTA_EX
        }

        print(f"{Fore.LIGHTWHITE_EX}JEU DU MASTERMIND\n"
              "Trouver la bonne combinaison de chaque couleur secrète que notre 'IA' aura généré.\n"
              "À chaque couleur bien positionnée, vous aurez en retour un indicateur rouge.\n"
              "À chaque couleur présente mais mal positionnée, vous aurez en retour un indicateur blanc.\n"
              "Entrer une combinaison secrète en utilisant les chiffres des couleurs disponibles.\n"
              f"{Fore.LIGHTWHITE_EX}[1]: {self.couleurs[1]}Jaune    {Fore.LIGHTWHITE_EX}[2]: {self.couleurs[2]}Bleu    "
              f"{Fore.LIGHTWHITE_EX}[3]: {self.couleurs[3]}Rouge    {Fore.LIGHTWHITE_EX}[4]: {self.couleurs[4]}Vert    "
              f"{Fore.LIGHTWHITE_EX}[5]: {self.couleurs[5]}Blanc    {Fore.LIGHTWHITE_EX}[6]: {self.couleurs[6]}Magenta")

        self.solution_combinaison = [random.randint(1, 6) for i in range(4)]

    def traduire_combinaison(self, combinaison):
        combinaison_couleurs = ""
        for i in combinaison:
            combinaison_couleurs += f"{self.couleurs[int(i)]}{self.carre}   "

        return combinaison_couleurs

    def verifier(self, combinaison):
        if len(combinaison) != 4:
            return False

        if not combinaison.isdigit():
            return False

        for char in combinaison:
            if int(char) > 6:
                return False

        return True

    def choisir_combinaison(self):
        self.combinaison = input(f"{Fore.LIGHTWHITE_EX}veuillez saisir vos 4 chiffres pour les couleurs : ")
        return self.combinaison

    def comparer(self, combinaison):
        liste_rond = []
        combinaison2 = list(combinaison).copy()
        solution_combinaison2 = self.solution_combinaison.copy()
        if list(map(int, combinaison)) == self.solution_combinaison:
            gagne = True
        else:
            gagne = False

        # identifier les bien placés
        for i in range(4):
            if int(combinaison[i]) == self.solution_combinaison[i]:
                liste_rond.append(Fore.RED)
                combinaison2[i] = None
                solution_combinaison2[i] = None

        # identifier les mal placés
        for i in range(4):
            if combinaison2[i] is not None and int(combinaison2[i]) in solution_combinaison2:
                liste_rond.append(Fore.LIGHTWHITE_EX)
                solution_combinaison2[solution_combinaison2.index(int(combinaison2[i]))] = None

        ronds_couleurs = ""
        for i in liste_rond:
            ronds_couleurs += f"{i}{self.rond}  "

        print(ronds_couleurs)
        return ronds_couleurs, gagne

    def run(self):
        for i in range(self.tentatives):
            while True:
                combinaison_test = self.choisir_combinaison()
                combinaison = combinaison_test.replace(" ", "")
                if self.verifier(combinaison):
                    break
                else:
                    print(f"{Fore.LIGHTWHITE_EX}Votre saisie est incorrecte...")
            combinaison_couleurs = self.traduire_combinaison(combinaison)

            ronds_couleurs, gagne = self.comparer(combinaison)
            print(f"{combinaison_couleurs} {Fore.LIGHTWHITE_EX}Indicateurs : {ronds_couleurs}")

            if gagne:
                texte = "Bravo tu as gagné !"

                for i, char in enumerate(texte):
                    print(couleurs_arc_en_ciel[i % len(couleurs_arc_en_ciel)] + char, end='')
                print()
                break
        else:
            combinaison_secrete = self.traduire_combinaison(self.solution_combinaison)
            print(
                f"{Fore.LIGHTWHITE_EX}Vous avez utilisé vos {self.tentatives} tentatives. La combinaison secrète était : {combinaison_secrete}")



if __name__ == "__main__":
    game = Game()
    game.run()


