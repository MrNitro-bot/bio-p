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