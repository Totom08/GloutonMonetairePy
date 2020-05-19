# Algorithme glouton de résolution de monnaie à rendre
# A CORRIGER
# NF.NSI

# montant de la monnaie a rendre
montant = float(input("Montant à rendre ? (Sous forme XX.XX)"))

# valeur des pieces disponibles en euro trié dans l'ordre décroissant
pieces = [ 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 ]
billets = [500, 200, 100, 50, 20, 10, 5 ]

## exemple de cas non optimal
## montant = 21
## pieces = [ 18, 7, 1 ]

def Monnaie(somme, ListeMontantP, ListeMontantB) :

    # tableaux de nombre de pieces et billets max a rendre selon le tableau de pieces/billets
    ListeNbPieces=[-1 for k in ListeMontantP]
    ListeNbBillets=[-1 for k in ListeMontantB]

    # parcours de la liste des billets
    for k in range(len(ListeMontantB)):

        # recupere le nombre de billets selon le quotient (entier //)
        ListeNbBillets[k]=somme//ListeMontantB[k]

        # somme restante a deduire du montant
        somme=round(somme%ListeMontantB[k], 2)

    # parcours de la liste des pieces
    for k in range(len(ListeMontantP)):

        # recupere le nombre de piece selon le quotient (entier //)
        ListeNbPieces[k]=somme//ListeMontantP[k]

        # somme restante a deduire du montant
        somme=round(somme%ListeMontantP[k], 2)



    return somme,ListeNbBillets,ListeNbPieces

print(Monnaie(montant, pieces, billets),"(",montant,")")
