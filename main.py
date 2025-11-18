"""
Module permettant de générer la suite de Syracuse d'une valeur initiale,
d'en extraire différentes grandeurs caractéristiques, et de produire un
graphique via Plotly.

Fonctions implémentées :
- syracuse_l(n) : génère la suite de Syracuse sous forme de liste
- temps_de_vol(l) : retourne le temps de vol
- temps_de_vol_en_altitude(l) : retourne le temps de vol en altitude
- altitude_maximale(l) : retourne l'altitude maximale atteinte
"""

from plotly.graph_objects import Scatter, Figure


### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Affiche la suite de Syracuse sous forme graphique (NE PAS MODIFIER)."""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure(
        {
            "layout": {
                "title": {"text": title},
                "xaxis": {"title": {"text": "x"}},
                "yaxis": {"title": {"text": "y"}},
            }
        }
    )

    x = list(range(len(lsyr)))
    trace = Scatter(
        x=x, y=lsyr, mode="lines+markers", marker_color="blue"
    )
    fig.add_trace(trace)
    fig.show()
#######################


def syracuse_l(n):
    """
    Retourne la suite de Syracuse sous forme de liste.

    Args:
        n (int): valeur initiale de la suite

    Returns:
        list: liste des valeurs de la suite jusqu'à 1
    """
    suite = [n]
    while suite[-1] != 1:
        u = suite[-1]
        if u % 2 == 0:
            suite.append(u // 2)
        else:
            suite.append(3 * u + 1)
    return suite


def temps_de_vol(liste):
    """
    Retourne le temps de vol d'une suite de Syracuse.

    Args:
        liste (list): suite de Syracuse

    Returns:
        int: temps de vol (longueur - 1)
    """
    if not liste:
        return 0

    return len(liste) - 1


def temps_de_vol_en_altitude(liste):
    """
    Retourne le temps de vol en altitude d'une suite de Syracuse.

    Le calcul s'arrête dès que la suite descend sous la valeur initiale.

    Args:
        liste (list): suite de Syracuse

    Returns:
        int: temps passé strictement au-dessus du niveau initial
    """
    if not liste:
        return 0

    n0 = liste[0]
    count = 0

    for u in liste[1:]:
        if u < n0:
            break
        if u > n0:
            count += 1

    return count


def altitude_maximale(liste):
    """
    Retourne l'altitude maximale atteinte dans la suite de Syracuse.

    Args:
        liste (list): suite de Syracuse

    Returns:
        int: valeur maximale atteinte
    """
    if not liste:
        return 0

    return max(liste)


def main():
    """Fonction principale de démonstration des fonctions secondaires."""
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
