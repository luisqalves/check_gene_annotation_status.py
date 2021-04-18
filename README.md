# check_gene_annotation_status.py

### Introduction

<br>

`check_gene_annotation_status.py` is a Python script that as output produces a matrix displaying the annotation status (annotated vs not annotated) of a set of target genes in a set of target species corresponding [NCBI](https://www.ncbi.nlm.nih.gov/)-available genomes (FASTA format). This script uses, on its basis, the NCBI Entrez API, making use of the latest annotation version of each target species genome.

<br>

### Dependencies

+ Python 3
+ [NCBI Entrez Programming Utilities](https://www.ncbi.nlm.nih.gov/home/tools/) 

<br>

### Usage 

`check_gene_annotation_status.py` requires a set of 3 arguments:
+ the input path to a .txt file containing the list of the species of interest (scientific name, separated by lines) (-target_species_list_file_path);
+ the input path to a .txt file containing the names of the genes of interest (separated by lines) (-target_genes_list_file_path);
+ the output path to a .csv file that will contain the produced matrix (-matrix_output_file_path).

<br>

	usage: check_gene_annotation_status.py
                                       -target_species_list_file_path
                                       -target_genes_list_file_path
                                       -matrix_output_file_path

<br>

### Example

Download the script available at `script/check_gene_annotation_status.py`. 

	python3 check_gene_annotation_status.py input_species.txt input_target_genes.txt output_matrix.csv
			
Using as `input` the above-mentioned arguments, as well as the `input_species.txt` and `input_target_genes.txt` files found in the `example` folder, the script should generate the output matrix file found within the same folder (`output_matrix.csv`).

<br>

>**Enjoy it and please let me know if you have any specific questions!**
