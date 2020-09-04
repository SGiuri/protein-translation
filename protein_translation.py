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
    :param strand: a string containing Codon to be matched
    :return: a list of proteins
    '''

    # a dictionary containing codon-protein association
    codons_translation = {"AUG": "Methionine",
                          "UUU": "Phenylalanine", "UUC": "Phenylalanine",
                          "UUA": "Leucine", "UUG": "Leucine",
                          "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
                          "UAU": "Tyrosine", "UAC": "Tyrosine",
                          "UGU": "Cysteine", "UGC": "Cysteine",
                          "UGG": "Tryptophan"}

    # reserved dictionary for stop codons
    stop_codons = ["UAA", "UAG", "UGA"]

    # 3 char splitting of the string
    strand_splitted = [strand[j-3:j] for j in range(3,len(strand)+1,3)]

    # searching stop codons and deleting codons after the stop
    for j in range(len(stop_codons)):

        if stop_codons[j] in strand_splitted:
            k = strand_splitted.index(stop_codons[j])
            strand_splitted = strand_splitted[0:k]

    # creating the list of protiens
    proteins = [codons_translation[x] for x in strand_splitted]

    return proteins
