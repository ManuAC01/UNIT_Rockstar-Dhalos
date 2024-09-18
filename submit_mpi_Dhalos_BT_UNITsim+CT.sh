#!/bin/bash

#SBATCH -A 16cores
#SBATCH --job-name=BT_UNIT_1Gpc_4096_CT
#SBATCH --output=/home/arnes/Sbatch_Slurm/Basurero/UNIT/out_%x.txt
#SBATCH --error=/home/arnes/Sbatch_Slurm/Basurero/UNIT/error_%x.txt
#SBATCH --ntasks=1
#SBATCH --nodes=2
#SBATCH --cpus-per-task=1
#SBATCH --tasks-per-node=1
#SBATCH --time=5-00:00:00
#SBATCH --nodelist=miclap,brutus
#SBATCH --mem=0

mpirun -np 1 ./build/build_trees /home/arnes/UNIT/conf_UNIT/UNITsim+CT.txt
