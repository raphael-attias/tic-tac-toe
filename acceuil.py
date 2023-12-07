import pygame
import sys
from random import randint

pygame.init()

width, height = 300, 300
cell_size = width // 3

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Couleurs
BLEU_TURQUOISE_FONCE = (0, 102, 102)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)

# Paramètres de la fenêtre d'accueil
largeur_fenetre_accueil = 400
hauteur_fenetre_accueil = 300

# Fenêtre d'accueil
fenetre_accueil = pygame.display.set_mode((largeur_fenetre_accueil, hauteur_fenetre_accueil))
pygame.display.set_caption('Tic Tac Toe - Accueil')

police = pygame.font.Font(None, 36)

def afficher_texte(texte, x, y, couleur, surface):
    texte_surface = police.render(texte, True, couleur)
    texte_rect = texte_surface.get_rect(center=(x, y))
    surface.blit(texte_surface, texte_rect)

def page_accueil():
    while True:
        fenetre_accueil.fill(BLEU_TURQUOISE_FONCE)

        afficher_texte('Tic Tac Toe', largeur_fenetre_accueil // 2, hauteur_fenetre_accueil // 4, BLANC, fenetre_accueil)

        # Bouton "Jouer avec un ami"
        pygame.draw.rect(fenetre_accueil, BLANC, (50, 150, 300, 50))
        afficher_texte('Jouer avec un ami', largeur_fenetre_accueil // 2, 175, BLEU_TURQUOISE_FONCE, fenetre_accueil)

        # Bouton "Jouer contre l'ordinateur"
        pygame.draw.rect(fenetre_accueil, BLANC, (50, 225, 300, 50))
        afficher_texte("Jouer contre l'ordinateur", largeur_fenetre_accueil // 2, 250, BLEU_TURQUOISE_FONCE, fenetre_accueil)

        pygame.display.flip()

        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:
                x, y = evenement.pos
                if 50 <= x <= 350 and 150 <= y <= 200:
                    return "2_joueurs"
                elif 50 <= x <= 350 and 225 <= y <= 275:
                    return "vs_ordi"

def fin_de_partie(resultat):
    while True:
        screen.fill((255, 255, 255))
        afficher_texte(resultat, width // 2, height // 8, ROUGE, screen)

        # Bouton "Rejouer"
        pygame.draw.rect(screen, BLANC, (50, 200, 100, 50))
        afficher_texte('Rejouer', 100, 225, BLEU_TURQUOISE_FONCE, screen)

        # Bouton "Arrêter"
        pygame.draw.rect(screen, BLANC, (200, 200, 100, 50))
        afficher_texte('Arrêter', 250, 225, BLEU_TURQUOISE_FONCE, screen)

        pygame.display.flip()

        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evenement.type == pygame.MOUSEBUTTONDOWN and evenement.button == 1:
                x, y = evenement.pos
                if 50 <= x <= 150 and 200 <= y <= 250:
                    return "rejouer"
                elif 200 <= x <= 300 and 200 <= y <= 250:
                    return "arreter"

def jouer_coup_ia(grid):
    while True:
        position = randint(1, 9)
        row, col = divmod(position - 1, 3)
        if grid[row][col] == 0:
            return row, col

def jeu_2_joueurs():
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    joueur_actuel = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                row = y // cell_size
                col = x // cell_size
                if grid[row][col] == 0:
                    grid[row][col] = joueur_actuel
                    joueur_actuel = 3 - joueur_actuel  # Alterne entre les joueurs 1 et 2

        screen.fill((255, 255, 255))

        for row in range(3):
            for col in range(3):
                pygame.draw.rect(screen, (0, 0, 0), (col * cell_size, row * cell_size, cell_size, cell_size), 1)
                if grid[row][col] == 1:
                    pygame.draw.line(screen, (255, 0, 0), (col * cell_size, row * cell_size), ((col + 1) * cell_size, (row + 1) * cell_size), 2)
                    pygame.draw.line(screen, (255, 0, 0), ((col + 1) * cell_size, row * cell_size), (col * cell_size, (row + 1) * cell_size), 2)
                elif grid[row][col] == 2:
                    pygame.draw.circle(screen, (0, 0, 255), (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), cell_size // 2 - 5, 2)

        pygame.display.flip()

        # Vérification de la victoire ou match nul
        victoire = False
        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2] != 0 or grid[0][i] == grid[1][i] == grid[2][i] != 0:
                victoire = True
                break
        if grid[0][0] == grid[1][1] == grid[2][2] != 0 or grid[0][2] == grid[1][1] == grid[2][0] != 0:
            victoire = True

        if victoire:
            resultat = f"Joueur {joueur_actuel} a gagné!"
            choix = fin_de_partie(resultat)
            if choix == "rejouer":
                jeu_2_joueurs()
            elif choix == "arreter":
                break
        elif all(all(cell != 0 for cell in row) for row in grid):
            resultat = "Match nul!"
            choix = fin_de_partie(resultat)
            if choix == "rejouer":
                jeu_2_joueurs()
            elif choix == "arreter":
                break

#ia
def jeu_ia():
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    joueur_actuel = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                row = y // cell_size
                col = x // cell_size
                if grid[row][col] == 0:
                    grid[row][col] = joueur_actuel
                    joueur_actuel = 3 - joueur_actuel  # Alterne entre les joueurs 1 et 2

        if joueur_actuel == 2:
            # Tour de l'IA
            row, col = jouer_coup_ia(grid)
            grid[row][col] = joueur_actuel
            joueur_actuel = 1  # Passer au tour du joueur

        screen.fill((255, 255, 255))

        for row in range(3):
            for col in range(3):
                pygame.draw.rect(screen, (0, 0, 0), (col * cell_size, row * cell_size, cell_size, cell_size), 1)
                if grid[row][col] == 1:
                    pygame.draw.line(screen, (255, 0, 0), (col * cell_size, row * cell_size), ((col + 1) * cell_size, (row + 1) * cell_size), 2)
                    pygame.draw.line(screen, (255, 0, 0), ((col + 1) * cell_size, row * cell_size), (col * cell_size, (row + 1) * cell_size), 2)
                elif grid[row][col] == 2:
                    pygame.draw.circle(screen, (0, 0, 255), (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), cell_size // 2 - 5, 2)

        pygame.display.flip()

        # Vérification de la victoire ou match nul
        victoire = False
        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2] != 0 or grid[0][i] == grid[1][i] == grid[2][i] != 0:
                victoire = True
                break
        if grid[0][0] == grid[1][1] == grid[2][2] != 0 or grid[0][2] == grid[1][1] == grid[2][0] != 0:
            victoire = True

        if victoire:
            resultat = f"Joueur {joueur_actuel} a gagné!"
            choix = fin_de_partie(resultat)
            if choix == "rejouer":
                jeu_ia()
            elif choix == "arreter":
                break
        elif all(all(cell != 0 for cell in row) for row in grid):
            resultat = "Match nul!"
            choix = fin_de_partie(resultat)
            if choix == "rejouer":
                jeu_ia()
            elif choix == "arreter":
                break

# Boucle principale
mode_jeu = page_accueil()

# Choix du mode de jeu
if mode_jeu == "2_joueurs":
    jeu_2_joueurs()
elif mode_jeu == "vs_ordi":
    jeu_ia()

pygame.quit()
sys.exit()
