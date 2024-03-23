import pandas as pd
import fgsea

# Load results dataframe
results_df = pd.read_csv("results_with_names.csv")

# Sort dataframe by log2foldchange in descending order
results_df_sorted = results_df.sort_values(by='log2FoldChange', ascending=False)

# Read in the C2 gene sets
gmt_file = "/projectnb/bf528/materials/project_1_rnaseq/m2.all.v2023.2.Mm.symbols.gmt"
gene_sets = fgsea.gmtPathways(gmt_file)

# Get gene names and log2foldchange values
gene_names = results_df_sorted['gene_name'].tolist()
log2foldchange_values = results_df_sorted['log2FoldChange'].tolist()

# Perform GSEA analysis
gsea_results = fgsea.gsea(rank=log2foldchange_values, term=gene_sets, minSize=15, maxSize=500)

# Extract top twenty results with highest positive NES
top_positive_results = gsea_results.head(20)

# Extract top twenty results with most negative NES
top_negative_results = gsea_results.tail(20)

print("Top twenty results with highest positive NES:")
print(top_positive_results)

print("\nTop twenty results with most negative NES:")
print(top_negative_results)
