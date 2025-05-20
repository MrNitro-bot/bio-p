#Explain the steps to perform a multiple sequence alignment using MUSCLE in Biopython. Write 
#a script to align three sequences of your choice and save the results to a file.


import subprocess 
from Bio import AlignIO 
muscle_exe=r"C:\Users\WELCOME\Downloads\muscle3.8.31_i86win32.exe" 
try: 
subprocess.run([muscle_exe,"-in","lab4.fasta","
out","aligned_sequences.fasta"],check=True) 
alignment=AlignIO.read("aligned_sequences.fasta","fasta") 
print(alignment) 
except FileNotFoundError: 
print("error muscle executable not found") 
except subprocess.CalledProcessError as e: 
print("error running muscle") 
