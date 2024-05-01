# Overview

Transcriptional Profile of Mammalian Cardiac Regeneration with mRNA-Seq

## Initialize the environment

The following packages must be installed: snakemake, pandas, fastqc, star, samtools, multiqc,
verse, bioconductor-deseq2, bioconductor-fgsea, jupyterlab

pip install snakemake-executor-plugin-cluster-generic <br>
or <br>
conda install -c conda-forge -c bioconda snakemake-executor-plugin-cluster-generic

snakemake -s weekX.snake --executor cluster-generic --cluster-generic-submit-cmd "qsub -P bf528 -pe omp {threads}" --jobs #ofjobs

## Pipeline files 

The pipeline's files are within week 1-4 snakemake files and they must be run in an organized manner. 
