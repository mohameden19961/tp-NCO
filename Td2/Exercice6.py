import math

def saisir():
    message = input("Saisir un texte(message) : ")
    fichier = open("msg.txt", "w" , encoding="utf-8")
    fichier.write(message)
    fichier.close()

def frequences_caracteres():
    fichier = open("msg.txt", "r", encoding = 'utf-8')
    text=fichier.read()
    fichier.close()    
    
    frequences = {}
    for caractere in text:
        if caractere in frequences:
            frequences[caractere] += 1
        else:
            frequences[caractere] = 1
            
    return frequences


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


def probabilite_totale(probas):
    total = 0
    for p in probas.values():
        total += p
        
    return total

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

def coder_message(message, codes):
    resultat = ""
    for caractere in message:
        resultat += codes[caractere]
    return resultat







def main():
    saisir()

    freqs = frequences_caracteres()
    probas = probabilites(freqs)

    print("Fréquences :", freqs)
    print("Probabilités :", probas)
    print("Information propre :", information_propre(probas))
    print("Probabilité totale :", probabilite_totale(probas))
    print("Entropie :", entropie(probas))

    racine = arbre_huffman(probas)
    codes = codes_huffman(racine)

    fichier = open("msg.txt", "r", encoding = 'utf_8')
    message=fichier.read()
    fichier.close()      

    message_code = coder_message(message, codes)
 
    print("Codes Huffman :", codes)
    print("Message codé :", message_code)

    
main()
