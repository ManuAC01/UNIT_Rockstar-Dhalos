#!/usr/bin/env python

import os
from datetime import datetime
import numpy as np

def mkdir_p(dir):
    '''make a directory (dir) if it doesn't exist'''
    if not os.path.exists(dir):
        os.mkdir(dir)

# Executable

range = range(1)

jobnames = ['FD_UNIT'.format(i) for i in range]
    
# Job description
ncores = '16cores'
partition = 'all'  # test/compute 
time = '05-00:00:00'  #Format: d-hh:mm:ss
nodelist = 'miclap,brutus'
nodes = 1
ntasks = 2
nodetaks = 1
cputask = 1
mem = 600000

# Logs output directory
log_dir = '/home/arnes/Sbatch_Slurm/Basurero/UNIT/Dhalos/' #'/home/arnes/Sbatch_Slurm/Basurero'
submit_dir = '/home/arnes/Sbatch_Slurm/sub_dhalos_UNIT/'
mkdir_p(log_dir)


# For checking if the module is loaded
#script_content1 = 'module_to_check="apps/anaconda3/2023.03/bin"'
#script_content2 = 'if [[ $module_list_output != *"$module_to_check"* ]]; then'

# Submission script
for i, jobname in enumerate(jobnames):
    #now = datetime.now()
    #script = log_dir+jobname+now.strftime('_%Y%m%d_%H%M')+'.sh'
    script = submit_dir + jobname + '.sh'
    
    with open(script,'w') as fh:
        fh.write("#!/bin/sh \n")
        fh.write("\n")
        fh.write("#SBATCH -A {} \n".format(str(ncores)))
        fh.write("#SBATCH --ntasks={} \n".format(str(ntasks)))
        fh.write("#SBATCH --cpus-per-task={} \n".format(str(cputask)))
        fh.write("##SBATCH --nodes={} \n".format(str(nodes)))
        fh.write("##SBATCH --tasks-per-node={} \n".format(str(nodetaks)))
        fh.write("#SBATCH --job-name={} \n".format(jobname))
        fh.write("#SBATCH --output={}out.{} \n".format(log_dir,jobname))
        fh.write("#SBATCH --error={}err.{} \n".format(log_dir,jobname))
        fh.write("##SBATCH --mem={} \n".format(str(mem)))
        fh.write("#SBATCH --partition={} \n".format(partition))
        fh.write("#SBATCH --nodelist={} \n".format(nodelist))
        fh.write("#SBATCH --time={} \n".format(time))
        fh.write('# \n')
        fh.write('##export OMP_NUM_THREADS=16')
        fh.write('\n')
        fh.write("\n")
        fh.write("mpirun -np 1 ./build/find_descendants /home/arnes/UNIT/conf_UNIT/UNITsim_ROCKSTAR.txt \n".format(range[i]))  # Assuming shark_executable is present
        
        #fh.write("#SBATCH --mail-type=END,FAIL \n")         #Not working
        #fh.write("#SBATCH --mail-user=violetagp@protonmail.com \n")
        #fh.write("\n")
        #fh.write("flight env activate gridware \n")
        #fh.write("\n")
        #fh.write("{} \n".format(script_content1))
        #fh.write("module_list_output=$(module list 2>&1) \n")
        #fh.write("{} \n".format(script_content2))
        #fh.write("  module load $module_to_check \n")
        #fh.write("fi \n")
        #fh.write("\n")    
        #fh.write("python3 {} \n".format(path2program))
    
    print("Run {}".format(script))
    os.system("sbatch {}".format(script))
