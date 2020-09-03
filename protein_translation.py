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
    # test of git
    codons_translation = {"AUG": "Methionine",
                          "UUU": "Phenylalanine", "UUC": "Phenylalanine",
                          "UUA": "Leucine",
                          "UUG": "Leucine",
                          "UCU": "Serine",
                          "UCC": "Serine",
                          "UCA": "Serine",
                          "UCG": "Serine",
                          "UAU": "Tyrosine",
                          "UAC": "Tyrosine",
                          "UGU": "Cysteine",
                          "UGC": "Cysteine",
                          "UGG": "Tryptophan"}
    stop_codons = ["UAA", "UAG", "UGA"]
    print(strand)
    for stop_codon in stop_codons:
        if strand.find(stop_codon) > 0:
            strand = strand[:strand.find(stop_codon)]
        print(strand)
    codons = codons_translation.keys()

    matches = []
    for codon in codons:
        match = strand.find(codon)
        if match >= 0:
            matches.append(codons_translation[codon])
    print(matches)
    return matches
    pass


value = "UGGUGUUAUUAAUGGUUU"

proteins(value)
