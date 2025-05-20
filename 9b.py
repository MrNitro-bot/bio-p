from Bio import Phylo, AlignIO 
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor 
import matplotlib.pyplot as plt 
# Load the sequence alignment 
alignment = AlignIO.read("aligned_sequences.aln", "clustal") 
# Compute distance matrix 
calculator = DistanceCalculator("identity") 
distance_matrix = calculator.get_distance(alignment) 
# Build the phylogenetic tree using UPGMA 
constructor = DistanceTreeConstructor() 
tree = constructor.upgma(distance_matrix) 
# Save tree 
Phylo.write(tree, "phylogenetic_tree.nwk", "newick") 
# Draw the tree 
fig = plt.figure(figsize=(8, 5)) # Set figure size 
ax = fig.add_subplot(1, 1, 1) # Ensure only one subplot is used 
Phylo.draw(tree, axes=ax) # Draw the tree on the specified axis 
plt.show() # Display the tree