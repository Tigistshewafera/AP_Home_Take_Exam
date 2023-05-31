'''
Created on May 23, 2023

@author: Tigist shewafera
'''
import os


def number_of_let7(file_path):
  """Counts the number of let-7 miRNAs in a file.

  Args:
    file_path: The path to the file.

  Returns:
    The number of let-7 miRNAs in the file.
  """

  if not os.path.isfile(file_path):
    raise FileNotFoundError("The specified file does not exist.")

  species_codes = []
  species_frequency = {}

  with open(file_path, 'r') as file:
    for line in file:
      if line.startswith('>'):
        miRNA_identifier = line[1:].strip()
        if 'let-7' in miRNA_identifier:
          species_code = miRNA_identifier.split("-")[0]
          species_codes.append(species_code)
          species_frequency[species_code] = species_frequency.get(species_code, 0) + 1

  total_let7miRNA = len(species_codes)
  total_species = len(species_frequency)

  print("Total number of let-7 family of miRNAs:", total_let7miRNA)

  if total_species > 0:
    print("Total number of species codes with let-7 miRNA:", total_species)
  else:
    print("There are no species codes with let-7 miRNA in the file.")


if __name__ == '__main__':
  file_path = r"C:\Users\dbu\eclipse-workspace\Home_take_exam\src\mature.fa"
  number_of_let7(file_path)
