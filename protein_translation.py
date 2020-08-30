import re

def proteins(strand):
    '''
    Codon	Protein
    AUG	                Methionine
    UUU, UUC	        Phenylalanine
    UUA, UUG	        Leucine
    UCU, UCC, UCA, UCG	Serine
    UAU, UAC	        Tyrosine
    UGU, UGC	        Cysteine
    UGG	                Tryptophan
    UAA, UAG, UGA	    STOP
    :param strand:
    :return:
    '''

    protein_translation = {"AUG":"Methionine",
                           "UUUUUC":"Phenylalanine",
                           "UUAUUG":"Leucine",
                           "UCUUCCUCAUCG": "Serine",
                           "UAUUAC": "Tyrosine",
                           "UGUUGC": "Cysteine",
                           "UGG": "Tryptophan",
                           "UAAUAGUGA": "STOP"}
    codons = list(protein_translation.keys())
    print(codons)
    to_return = []

    codon1 = f"{codons[0]}"
    print(codon1)

    matches = re.match(codon1, strand)
    print(matches)

    '''
    for condon in codons:
        matches = re.match(r"{codon}",strand)
        for match in matches:
            to_return.append(protein_translation[match])
            print(match)
    '''
    return to_return
    pass


value = "AUGUGGUAGUGG"

proteins(value)