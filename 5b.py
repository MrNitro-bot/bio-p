
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
dna_sequence=Seq("ATCGCTAGCTAGCTG")
print(dna_sequence)
record=SeqRecord(dna_sequence,id="1",name="shello",description="adhjqjf")
record.annotations["gene"]="example"
record.annotations["molecule_type"]="round"
record.annotations["function"]="ok"
from Bio.SeqFeature import SeqFeature, FeatureLocation
gene_feature=SeqFeature(FeatureLocation(0,21),type="gene",qualifiers={"typeof":"Example"})
record.features.append(gene_feature)
print(f"Id:{record.id}")
print(f"name:{record.name}")
print(f"description:{record.description}")
print(f"Annotations:{record.annotations}")
print(f"Features:{record.features}")
Create a SeqRecord object for a DNA sequence and add annotations for a gene (start, end position, 
description). Modify the annotations and print the updated SeqRecord.
