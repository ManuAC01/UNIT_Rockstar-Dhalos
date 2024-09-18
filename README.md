The main goal of this project is trying to run Rockstar halo catalogs on Dhalos in order to generate new merger trees with different initial redshifts. In order to do this, one needs to run find_descendants and build_trees. There are two python files created to run these using the Slurm queues. The config files that have been used to run this unsuccessfully are "UNITsim+ROCKSTAR". There is an original repository with more information about the Rockstar+Dhalos problem [https://github.com/angel-chandro/DHalos_ROCKSTARhalos.git]

The data used is located in "/home/arnes/UNIT/1Gpc_4096_fixedAmp_001_ROCKSTAR/". This data is already decompressed (using the submit_unzip.sh) and already contains the "pid" column (it is the last column). The compressed data and the Rockstar+ConsistentTrees data is located in "/data5/UNITSIM/1Gpc_4096/fixedAmp_001/ROCKSTAR/tree/".

The "UNITsim+CT" files are the ones used to run the ConsistentTrees files. There should be no problem on running build_trees on these merger trees and the run Shark.

Both redshift lists are the same but redshit_list.txt contains the scale factor in the third column. This file is the one I have used when I tried to run Dhalos on the Rockstar catalogues.
