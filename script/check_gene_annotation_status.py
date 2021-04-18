import argparse
import os
import time


def check_target_gene_annotation_status():
    global species_data
    data = os.popen(
        'esearch -db gene -query "'
        + gene_name
        + "[GENE] AND "
        + species
        + '[Organism]"'
    ).read()
    if "<Count>0" in data:
        species_data += ",Not Annotated"
        print(str(i + 1) + " - " + gene_name + ": NOT ANNOTATED")
    else:
        species_data += ",Annotated"
        print(str(i + 1) + " - " + gene_name + ": ANNOTATED")


parser = argparse.ArgumentParser()
parser.add_argument(
    "target_species_list_file_path",
    metavar="-target_species_list_file_path",
    type=str,
    help="Target Species List File Path (.txt)",
)
parser.add_argument(
    "target_genes_list_file_path",
    metavar="-target_genes_list_file_path",
    type=str,
    help="Target Genes List File Path (.txt)",
)
parser.add_argument(
    "matrix_output_file_path",
    metavar="-matrix_output_file_path",
    type=str,
    help="Output Matrix File Path (.csv)",
)
args = parser.parse_args()
print("\nCheck Gene Annotation Status Script\n")
file_species = open(args.target_species_list_file_path, "r")
file_genes = open(args.target_genes_list_file_path, "r")
file_output = open(args.matrix_output_file_path, "w")
genes = []
for gene in file_genes:
    gene_name = gene.replace("\n", "").upper()
    genes.append(gene_name)
header = "Species\Gene Name"
for i in genes:
    header += "," + i
file_output.write(header + "\n")
for species in file_species:
    species = species.strip().replace("\n", "")
    print("Current Species:", species + "\n")
    species_data = species
    for i in range(len(genes)):
        time.sleep(0.3)
        gene_name = genes[i]
        check_target_gene_annotation_status()
    file_output.write(species_data + "\n")
    print("\n----------------------------------------\n")
file_genes.close()
file_species.close()
file_output.close()
print("\nDone.")
