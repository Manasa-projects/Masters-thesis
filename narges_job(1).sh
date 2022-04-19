#!/bin/bash
##ENVIRONMENT SETTINGS; CHANGE WITH CAUTION
#SBATCH --export=NONE                #Do not propagate environment
#SBATCH --get-user-env=L             #Replicate login environment

##NECESSARY JOB SPECIFICATIONS
#SBATCH --job-name=JobExample4       #Set the job name to "JobExample4"
#SBATCH --time=010:30:00              #Set the wall clock limit to 1hr and 30min
#SBATCH --ntasks=1                   #Request 1 task
#SBATCH --mem=8000M                  #Request 25600MB (2.5GB) per node
#SBATCH --output=Example4Out.%j      #Send stdout/err to "Example4Out.[jobID]"
#SBATCH --gres=gpu:2                 #Request 1 GPU per node can be 1 or 2
#SBATCH --partition=gpu              #Request the GPU partition/queue

##OPTIONAL JOB SPECIFICATIONS
##SBATCH --account=123456             #Set billing account to 123456
#SBATCH --mail-type=ALL              #Send email on all job events
#SBATCH --mail-user=nzarnaghi@tamu.edu    #Send all emails to email_address

module load SciPy-bundle/2019.10-fosscuda-2019b-Python-3.7.4
module load scikit-learn/0.21.3-fosscuda-2019b-Python-3.7.4
module load TensorFlow/1.15.0-fosscuda-2019b-Python-3.7.4
module load matplotlib/3.1.1-fosscuda-2019b-Python-3.7.4
module load PyTables/3.6.1-fosscuda-2019b-Python-3.7.4
module load NLTK/3.5-fosscuda-2019b-Python-3.7.4
module load h5py/2.10.0-fosscuda-2019b-Python-3.7.4
module load progressbar33/2.4-fosscuda-2019b-Python-3.7.4
module load ViennaRNA/2.3.5-fosscuda-2019b-Python-3.7.4
##module load Theano/1.0.4-fosscuda-2019b-Python-3.7.4


##python make_RNA_dataset_grammar_py3.py
##python train_RNA.py
##python train_zinc_py3.py
python generate_latent_features_and_targets.py

