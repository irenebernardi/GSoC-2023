#!/bin/bash

#$ -N test
#$ -cwd
#$ -pe smp 5
#$ -l h_vmem=128G

# see the submission script
cat $SGE_O_WORKDIR/submit.sh

source ~/.bashrc
time mpiexec $ (hostname) -n $NSLOTS nrniv -python -mpi CA3batch.py

