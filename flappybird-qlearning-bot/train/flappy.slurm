#!/bin/bash
#SBATCH --partition=normal
#SBATCH --exclusive
#SBATCH --ntasks=20
#SBATCH --ntasks-per-node=20
#SBATCH --mem=0
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#SBATCH --time=10:00:00
#SBATCH --job-name=flappybird

parallel --workdir ${SLURM_SUBMIT_DIR} --progress -P 20 ./run.sh ::: `seq -f"%02g" 0 19`
