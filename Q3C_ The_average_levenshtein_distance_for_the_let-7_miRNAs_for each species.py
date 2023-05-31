'''
Created on May 27, 2023

@author: Tigist Shewafera
'''
import os
import Levenshtein


def calculate_levenshtein_distance(file_path):
  """Calculates the Levenshtein distance between all pairs of let-7 miRNA sequences in a file.

  Args:
    file_path: The path to the file containing the let-7 miRNA sequences.

  Returns:
    A dictionary mapping species codes to average Levenshtein distances between all pairs of let-7 miRNA sequences in the species.
  """

  if not os.path.isfile(file_path):
    print("The specified file does not exist.")
    return {}

  species_let7_sequences = {}

  with open(file_path, 'r') as file:
    species_code = ""
    sequence = ""
    for line in file:
      if line.startswith('>'):
        if species_code and sequence:
          species_let7_sequences.setdefault(species_code, []).append(sequence)

        species_code = line[1:].strip().split("let-7")[0]
        sequence = ""
      else:
        sequence = line.strip()

    # Store the last species code and sequence outside the loop
    if species_code and sequence:
      species_let7_sequences.setdefault(species_code, []).append(sequence)

  average_distances = {}
  for species_code, sequences in species_let7_sequences.items():
    total_distance = 0
    total_sequences = len(sequences)

    if total_sequences < 2:
      continue

    for i in range(total_sequences - 1):
      for j in range(i + 1, total_sequences):
        total_distance += Levenshtein.distance(sequences[i], sequences[j])

    average_distance = total_distance / (total_sequences * (total_sequences - 1) / 2)
    average_distances[species_code] = average_distance

  return average_distances


# File path
file_path = r"C:\Users\dbu\eclipse-workspace\Home_take_exam\src\mature.fa"


# Calculate the Levenshtein distances
average_distances = calculate_levenshtein_distance(file_path)

# Print the results
for species_code, average_distance in average_distances.items():
  print(f"Average Levenshtein distance for let-7 miRNA in species '{species_code}': {average_distance:.2f}")
 