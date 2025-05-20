# Create a SeqRecord object for a DNA sequence and add annotations for a gene (start, end position, 
#description). Modify the annotations and print the updated SeqRecord.






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
