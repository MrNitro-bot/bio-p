
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
def convert_fasta_to_genbank(fasta_file,genbank_file):
    records=[]
    for record in SeqIO.parse(fasta_file,"fasta"):
        sequence=record.seq
        description=record.description

    genbank_record=SeqRecord(id="1",name="hello",description="sfbajfaj",annotations={
        "molecule_type":"safafvja",
        "gene":"function",
        "function":"Hypothetical protein"

    })
    records.append(genbank_record)

    with open(genbank_file,"w") as output_handle:
        SeqIO.write(records,output_handle,"genbank")
    
    fasta_file="fasta_1.fasta"
    genbank_file="genbank_1.gb"

    convert_fasta_to_genbank(fasta_file,genbank_file)
Using a SeqRecord object, write the DNA sequence along with its annotations (e.g., gene name, 
function) to a GenBank file format

