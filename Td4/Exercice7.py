def lz78_compression(texte):
    dictionnaire = {}      
    index = 1
    i = 0
    resultat = []

    while i < len(texte):
        courant = ""
        j = i

        while j < len(texte) and courant + texte[j] in dictionnaire:
            courant += texte[j]
            j += 1

        if j < len(texte):
            caractere = texte[j]
        else:
            caractere = ""

        indice = dictionnaire.get(courant, 0)
        resultat.append((indice, caractere))

        dictionnaire[courant + caractere] = index
        index += 1
        i = j + 1

    return resultat



def lz78_decompression(code):
    dictionnaire = {0: ""}
    index = 1
    texte = ""

    for indice, caractere in code:
        chaine = dictionnaire[indice] + caractere
        texte += chaine
        dictionnaire[index] = chaine
        index += 1

    return texte


def test_lz78():
    message = "ABAABABAABBBBBBBBBBA"

    print("Texte original :")
    print(message)

    code = lz78_compression(message)
    print("\nTexte compressé (index, caractère) :")
    for c in code:
        print(c)

    texte_decompresse = lz78_decompression(code)
    print("\nTexte décompressé :")
    print(texte_decompresse)
test_lz78()