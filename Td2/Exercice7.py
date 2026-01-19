import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def charger_image(path):
    img = Image.open(path).convert("L")  # L = grayscale
    pixels = np.array(img).flatten()
    return pixels




def histogramme(pixels):
    freqs = {}
    
    for p in pixels:
        if p in freqs:
            freqs[p] += 1
        else:
            freqs[p] = 1
    
    niveaux = list(freqs.keys())
    valeurs = list(freqs.values())

    plt.bar(niveaux, valeurs)
    plt.xlabel("Niveau de gris")
    plt.ylabel("Nombre de pixels")
    plt.title("Histogramme de l'image")
    plt.show()

    return freqs    




def probabilites(freqs):
    total = 0
    for i in freqs.values():
        total += i      
    probs = {}
    for caractere, nombre in freqs.items():
        probs[caractere] = nombre / total
        
    return probs
    
def information_propre(probas):
    info = {}
    for caractere, p in probas.items():
        info[caractere] = -math.log2(p)
    return info  

def entropie(probas):
    h = 0
    for p in probas.values():
        h += p * math.log2(p)

    return -h


def arbre_huffman(probas):
    noeuds = []
    for char, p in probas.items():
        noeuds.append([p, char])
    
    while len(noeuds) > 1:
        n = len(noeuds)
        for i in range(n):
            for j in range(0, n - i - 1):
                if noeuds[j][0] > noeuds[j + 1][0]:
                    temp = noeuds[j]
                    noeuds[j] = noeuds[j + 1]
                    noeuds[j + 1] = temp
        
        gauche = noeuds.pop(0)
        droite = noeuds.pop(0)
        
        fusion = [gauche[0] + droite[0], gauche, droite]
        noeuds.append(fusion)
        
    return noeuds[0]




def codes_huffman(noeud, prefixe="", codes=None):
    if codes is None:
        codes = {}

    if len(noeud) == 2:
        caractere = noeud[1]
        codes[caractere] = prefixe
    else:
        codes_huffman(noeud[1], prefixe + "0", codes)
        codes_huffman(noeud[2], prefixe + "1", codes)

    return codes         


def longueur_moyenne(probas, codes):
    total = 0
    
    for k in codes:
        contribution = probas[k] * len(codes[k])
        total += contribution
        
    return total

def efficacite_et_redondance(entropie, longueur):
    efficacite = entropie / longueur
    redondance = 1 - efficacite
    return efficacite, redondance



def main():
    pixels = charger_image("logo.png")  
    freqs = histogramme(pixels)
    probas = probabilites(freqs)

    infos = information_propre(probas)
    H = entropie(probas)

    racine = arbre_huffman(probas)
    codes = codes_huffman(racine)

    L = longueur_moyenne(probas, codes)
    efficacite, redondance = efficacite_et_redondance(H, L)

    print("Entropie H =", H)
    print("Longueur moyenne L =", L)
    print("Efficacité =", efficacite)
    print("Redondance =", redondance)

    print("\nCodes Huffman (niveau de gris : code) :")
    for k in (codes):
        print(k, ":", codes[k])

main()