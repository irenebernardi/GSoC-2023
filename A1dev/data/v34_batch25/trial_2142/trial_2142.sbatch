#!/bin/bash
#SBATCH --job-name=trial_2142
#SBATCH -A default
#SBATCH -t 24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=80
#SBATCH -o data/v34_batch25/trial_2142/trial_2142.run
#SBATCH -e data/v34_batch25/trial_2142/trial_2142.err
#SBATCH --mail-user=salvadordura@gmail.com
#SBATCH --mail-type=end


source ~/.bashrc
cd /home/ext_salvadordura_gmail_com/A1_layers/
mpirun -n 80 nrniv -mpi -python init.py simConfig=data/v34_batch25/trial_2142/trial_2142_cfg.json netParams=data/v34_batch25/v34_batch25_netParams.py 
wait
        