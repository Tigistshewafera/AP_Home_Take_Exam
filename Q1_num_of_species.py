'''
Created on May 23, 2023

@author: Tigist Shewafera
'''
import matplotlib.pyplot as plt
import seaborn as sns


def count_species_from_mirna(file_path):
    """Counts the number of species in a miRNA file.

    Args:
      file_path: The path to the miRNA file.

    Returns:
      A tuple of (species_dict, total_species).
      species_dict is a dictionary mapping species codes to their counts.
      total_species is the total number of species in the file.
    """

    species_dict = {}
    total_species = 0

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>'):
                species_code = line.split('>')[1].split('-')[0]
                species_dict[species_code] = species_dict.get(species_code, 0) + 1
                total_species += 1

    sorted_species = sorted(species_dict.items(), key=lambda x: x[1])
    total_species = len(species_dict)

    return sorted_species, total_species


def main():
    """The main function."""

    # Provide the path to your mature.fa file
    file_path = r"C:\Users\dbu\eclipse-workspace\Home_take_exam\src\mature.fa"

    # Count the number of species
    sorted_species, total_species = count_species_from_mirna(file_path)

    # Print the number of total species found in the mature.fa file
    print("Number of total species found in the mature.fa file:", total_species)
    # #print("The frequency of species codes from lowest to highest")
    # for species, frequency in sorted_species:
    #     print(species, ":", frequency)

    # Extract species codes and corresponding frequencies
    species_codes = [species[0] for species in sorted_species]
    frequencies = [species[1] for species in sorted_species]

    # Filter species codes and frequencies for counts > 300
    filtered_species = [code for code, freq in zip(species_codes, frequencies) if freq > 250]
    filtered_frequencies = [freq for freq in frequencies if freq > 250]

    # Plotting with Seaborn
    sns.set(style="whitegrid")

    plt.figure(figsize=(12, 6))

    ax = sns.barplot(x=filtered_species, y=filtered_frequencies)

    ax.set_xlabel('Species Code')
    ax.set_ylabel('Frequency')
    ax.set_xticklabels(filtered_species, rotation=90)
    ax.set_title('Number of miRNA Sequences per Species from Lowest to Highest (Count > 250)')

    plt.tight_layout()

    plt.show()


if __name__ == '__main__':
    main()
