def aminoacid_to_codons(aminoacid_seq):
    aminoacid_to_codon = {
        'F': ['UUU', 'UUC'], 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
        'I': ['AUU', 'AUC', 'AUA'], 'M': ['AUG'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'],
        'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'P': ['CCU', 'CCC', 'CCA', 'CCG'],
        'T': ['ACU', 'ACC', 'ACA', 'ACG'], 'A': ['GCU', 'GCC', 'GCA', 'GCG'],
        'Y': ['UAU', 'UAC'], '*': ['UAA', 'UAG', 'UGA'], 'H': ['CAU', 'CAC'],
        'Q': ['CAA', 'CAG'], 'N': ['AAU', 'AAC'], 'K': ['AAA', 'AAG'],
        'D': ['GAU', 'GAC'], 'E': ['GAA', 'GAG'], 'C': ['UGU', 'UGC'],
        'W': ['UGG'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'G': ['GGU', 'GGC', 'GGA', 'GGG']
    }
    
    codons_list = []
    for aa in aminoacid_seq:
        codons_list.extend(aminoacid_to_codon[aa])
    
    return codons_list

def codon_frequencies(mrna_seq, codons_list):
    frequencies = {}
    for codon in codons_list:
        frequencies[codon] = mrna_seq.count(codon)
    return frequencies

def main_codon_frequency():
    aminoacid_seq = input("Enter the amino acid sequence: ")
    mrna_seq = input("Enter the mRNA sequence: ")

    possible_codons = aminoacid_to_codons(aminoacid_seq)
    
    frequencies = codon_frequencies(mrna_seq, possible_codons)
    
    for codon, freq in frequencies.items():
        print(f"Codon {codon}: {freq} occurrences")

main_codon_frequency()