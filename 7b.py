#Using Bio.pairwise2, perform pairwise sequence alignment of two DNA sequences. Print the 
#alignment result and the alignment score.








from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio import Entrez
from Bio.Align import PairwiseAligner
seq1="ATCGACTGACTCAGCTGCTG"
seq2="CTGATCATCATACATGGTAC"
aligner=PairwiseAligner()
alignment=aligner.align(seq1,seq2)
print(alignment)
print(alignment[0])
print(alignment[0].score)
