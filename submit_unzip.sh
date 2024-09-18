#!/bin/sh 

#SBATCH -A 16cores 
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=1 
##SBATCH --nodes=1
##SBATCH --tasks-per-node=1 
#SBATCH --job-name=UNIT_cp
#SBATCH --output=/home/arnes/Sbatch_Slurm/Basurero/UNIT/decompress/out.unzip%j 
#SBATCH --error=/home/arnes/Sbatch_Slurm/Basurero/UNIT/decompress/err.unzip%j
##SBATCH --mem=600000 
#SBATCH --partition=all 
#SBATCH --nodelist=miclap
#SBATCH --time=03-00:00:00 
# 
##export OMP_NUM_THREADS=16

# Loop to decompress files from out_0p.list.bz2 to out_128p.list.bz2
for i in $(seq 127 128); do
    pbzip2 -d /home/arnes/UNIT/conf_UNIT/1Gpc_4096_fixedAmp_001_ROCKSTAR/out_${i}p.list.bz2
done
