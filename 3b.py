from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

dna_sequence=Seq("ATGCGTACGTACGTA")
print(dna_sequence)

record=SeqRecord(dna_sequence,id="seq1",name="ExampleSequence",description="hello world",annotations={
    "molecule_type":"DNA",
    "gene":"ExampleGene",
    "function":"Hypothetical protein"
})
output_file_path="genbank_1.gb"
with open(output_file_path,"w") as output_file:
    SeqIO.write(record, output_file,"genbank")
print("Genbank written successfully")

with open(output_file_path,"r") as input_file:
    record_read=SeqIO.read(input_file,"genbank")
    print("Contents of the GenBank")
    print(record_read)