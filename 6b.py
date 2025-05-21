
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio import Entrez
Entrez.email="example@gmail.com"
accession_number="NM_001301717"
handle=Entrez.efetch(db="nucleotide",id=accession_number,rettype="gb",retmode="text")
gen_record=SeqIO.read(handle,"genbank")
print(f"id:{gen_record.id}")
print(f"description:{gen_record.description}")
print(f"annotations:{gen_record.annotations}")
print(f"features:{gen_record.features}")
Write a script that uses Entrez to fetch a nucleotide sequence from the NCBI database by using a 
known accession number, and print out the sequence and the related metadata.
