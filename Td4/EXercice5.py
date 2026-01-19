import math
message = "institut supérieur du numérique"

def frequences_caracteres():
    frequences = {}
    for caractere in message:
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

def entropie(probas):
    h = 0
    for p in probas.values():
        h += p * math.log2(p)
    return -h

def shannon_fano_rec(liste, prefixe, codes):
    if len(liste) == 1:
        caractere = liste[0][0]
        codes[caractere] = prefixe
        return

    total = 0
    for element in liste:
        total += element[1]
        
    somme_partielle = 0
    split_index = 0
    diff_min = total

    for i in range(len(liste)):
        somme_partielle += liste[i][1]
        diff = abs((total - somme_partielle) - somme_partielle)
        if diff < diff_min:
            diff_min = diff
            split_index = i + 1
        else:
            break

    shannon_fano_rec(liste[:split_index], prefixe + "0", codes)
    shannon_fano_rec(liste[split_index:], prefixe + "1", codes)

def generer_codes_sf(probas):
    liste_probas = []
    for char, p in probas.items():
        liste_probas.append([char, p])
    
    n = len(liste_probas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste_probas[j][1] < liste_probas[j + 1][1]:
                temp = liste_probas[j]
                liste_probas[j] = liste_probas[j + 1]
                liste_probas[j + 1] = temp
                
    codes = {}
    shannon_fano_rec(liste_probas, "", codes)
    return codes

def coder_message(message, codes):
    resultat = ""
    for caractere in message:
        resultat += codes[caractere]
    return resultat

def main():
    
    freqs = frequences_caracteres()
    probas = probabilites(freqs)
    h_source = entropie(probas)

    print("Entropie :", h_source)

    codes = generer_codes_sf(probas)

    message_code = coder_message(message, codes)
    
    longueur_bits = len(message_code)
    longueur_moyenne = longueur_bits / len(message)
    taux = (1 - (longueur_bits / (len(message) * 8))) * 100
    efficacite = h_source / longueur_moyenne
 
    print("Codes Shannon-Fano :", codes)
    print("Longueur compressée :", longueur_bits)
    print("Taux de compression :", taux, "%")
    print("Efficacité :", efficacite)

main()