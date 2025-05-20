#Using the Seq class from Biopython, create a DNA sequence object and: i. Slice the sequence to 
#extract a specific region (e.g., from index 3 to 10). ii. Concatenate this sequence with another 
#sequence. iii. Transcribe and translate the concatenated sequence into RNA and protein sequences.


from Bio.Seq import Seq

dna_sequence=Seq("ATGCTAGCTAGCTAGCTG")
print(dna_sequence)

sliced_sequence=dna_sequence[3:11]
print(sliced_sequence)

other_sequence=Seq("ATGCCTG")
concatenated_sequence=sliced_sequence+dna_sequence
print(concatenated_sequence)

rna_sequence=sliced_sequence.transcribe()
print(rna_sequence)

protein_sequence=sliced_sequence.translate()
print(protein_sequence)
