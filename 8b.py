#Explain the steps to perform a multiple sequence alignment using MUSCLE in Biopython. Write 
#a script to align three sequences of your choice and save the results to a file.







import subprocess
from Bio import AlignIO

muscle_exe = r"C:\Users\UMAR\Documents\muscle-win64.v5.3.exe"

try:
    subprocess.run([muscle_exe, "-align", "fasta_1.fasta", "-output", "aligned_sequences.fasta"], check=True)
    alignment = AlignIO.read("aligned_sequences.fasta", "fasta")
    print(alignment)

except FileNotFoundError:
    print("Error: MUSCLE executable not found")

except subprocess.CalledProcessError as e:
    print("Error: Running MUSCLE failed")

--------
import subprocess
from Bio import AlignIO


muscle_exe = r"C:\Users\UMAR\Documents\muscle3.8.31_win32.exe"

try:
    subprocess.run([muscle_exe, "-in", "fasta_1.fasta", "-out", "aligned_sequences.fasta"], check=True)
    alignment = AlignIO.read("aligned_sequences.fasta", "fasta")
    print("Alignment done using MUSCLE v3/v4:")
    print(alignment)
except FileNotFoundError:
    print("Error: MUSCLE executable not found")
except subprocess.CalledProcessError:
    print("Error: Failed running MUSCLE")
