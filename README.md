https://drive.google.com/drive/folders/1gYKBCxQHX_T_1oezFm3zb1BSjK1ecBZl?usp=sharing





https://drive.google.com/file/d/1ysxsG4dcdMzdcIa7vzuWuo2u5VgGVmD8/view?usp=sharing

https://drive.google.com/file/d/1JRmnIcCaFjTiw29vrA572R8ZUk1Tx2M2/view?usp=sharing

https://drive.google.com/file/d/1G-Fw6DEMrUPGS2s2XPSWJpCT2yXu4ow8/view?usp=sharing





#!/bin/bash
#SBATCH -N 1
#SBATCH -c 7
#SBATCH --mem 1gb
#SBATCH --time 00:30:00
#SBATCH --gres=gpu:1

module load python
module load CUDA

#trains the network - not interested in speeding up as it is a one time cost
python3 scripts/main.py --config configs/MyConfigProject.yaml

#makes a prediction on the full stack of images, hoping to distribute in the future to make it quicker
time python3 scripts/main.py --config configs/MyConfigProject.yaml --inference --checkpoint=trainOutput/checkpoint_50000.pth.tar

#an example of an array operation I may be able to make quicker
