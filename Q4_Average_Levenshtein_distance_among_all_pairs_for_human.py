'''
Created on May 27, 2023

@author: Tigist Shewafera
'''
import Levenshtein
import matplotlib.pyplot as plt

let7a_mirnas = []

with open(r"C:\Users\dbu\eclipse-workspace\Home_take_exam\src\mature.fa", "r") as file:
    miRNA_name = ""
    sequence = ""
    for line in file:
        if line.startswith(">"):
            if miRNA_name != "":
                if miRNA_name.startswith("hsa-let-7"):
                    let7a_mirnas.append((miRNA_name, sequence))
            miRNA_name = line.strip()[1:]
            sequence = ""
        else:
            sequence += line.strip()

    if miRNA_name.startswith("hsa-let-7"):
        let7a_mirnas.append((miRNA_name, sequence))

print("let-7 miRNA codes:")
for mirna, _ in let7a_mirnas:
    print(mirna)

# Calculate pairwise Levenshtein distance
distances = []
for mirna, seq in let7a_mirnas:
    print("Pairwise Levenshtein distances for", mirna)
    for other_mirna, other_seq in let7a_mirnas:
        if mirna != other_mirna:
            distance = Levenshtein.distance(seq, other_seq)
            print(f"Levenshtein distance between {mirna} and {other_mirna}: {distance}")
            distances.append(distance)

# Plotting a histogram of the Levenshtein distances
plt.figure(figsize=(8, 6))
plt.hist(distances, bins=10, edgecolor='black')
plt.xlabel("Levenshtein Distance")
plt.ylabel("Frequency")
plt.title("Histogram of Levenshtein Distances for hsa let-7 miRNAs")
plt.tight_layout()
plt.show()
