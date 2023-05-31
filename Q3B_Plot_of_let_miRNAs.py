"""
Created on May 26, 2023
@author: Tigist Shewafera
"""

import matplotlib.pyplot as plt
import numpy as np
import os


def extract_let7_code(header):
    """Extracts the let-7 code from a FASTA header."""
    if 'let-7' in header:
        code = header.split('let-7')[1].split()[0]
        return f"let-7{code[0]}"
    return ""


def extract_species_code(header):
    """Extracts the species code from a FASTA header."""
    start_index = header.find('>') + 1
    end_index = header.find('-', start_index)
    if start_index < end_index:
        return header[start_index:end_index]
    return ""


def let7_family_presence(file_path):
    """Plots a bar chart showing the presence of let-7 family members in a FASTA file.

    Args:
      file_path: The path to the FASTA file.
    """
    if not os.path.isfile(file_path):
        print("The specified file does not exist.")
        return

    let7_species = {}

    with open(file_path, 'r') as file:
        current_species = ""
        for line in file:
            if line.startswith('>'):
                header = line[1:].strip()
                current_species = extract_species_code(header)
            else:
                let7_code = extract_let7_code(header)
                if let7_code:
                    let7_species.setdefault(current_species, {}).setdefault(let7_code, 0)
                    let7_species[current_species][let7_code] += 1

    # Filter species with frequency count less than 7
    let7_species_filtered = {species: counts for species, counts in let7_species.items() if sum(counts.values()) >= 7}

    # Get the list of species and let-7 codes
    species_list = list(let7_species_filtered.keys())
    let7_codes = list(set().union(*[d.keys() for d in let7_species_filtered.values()]))

    # Create a matrix to store the presence counts
    presence_matrix = np.zeros((len(species_list), len(let7_codes)))

    for i, species in enumerate(species_list):
        for j, let7_code in enumerate(let7_codes):
            presence_matrix[i, j] = let7_species_filtered[species].get(let7_code, 0)

    # Set the positions of the bars on the x-axis
    x = np.arange(len(species_list))

    # Set the width of the bars
    bar_width = 0.37

    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(10, 8))

    # Plot the stacked bars
    bottom = np.zeros(len(species_list))
    for i, let7_code in enumerate(let7_codes):
        ax.bar(x, presence_matrix[:, i], bottom=bottom, label=let7_code)
        bottom += presence_matrix[:, i]

    # Add labels and title
    ax.set_xlabel('Species')
    ax.set_ylabel('Presence Count')
    ax.set_title('Presence of let-7 Family in Species (Count >=7)')
    ax.set_xticks(x)
    ax.set_xticklabels(species_list, rotation=45, ha='right')

    # Add a legend
    ax.legend()

    # Display the plot
    plt.tight_layout()
    plt.show()


# File path
file_path = r"C:\Users\dbu\eclipse-workspace\Home_take_exam\src\mature.fa"
let7_family_presence(file_path)
