#!/bin/bash

module load python
module load CUDA
mkdir projectFolder
cd projectFolder
git clone https://github.com/zudi-lin/pytorch_connectomics.git
git clone https://github.com/brookho8/CMSE401Project.git
cd pytorch_connectomics
python3 -m venv projectEnvironment
source projectEnvironment/bin/activate
pip3 install -r requirements.txt
pip3 install --editable .
pip install torch torchvision torchaudio
cp ../CMSE401Project/submission.sb submission.sb
cp ../CMSE401Project/example.py example.py
cp ../CMSE401Project/config.yaml configs/MyConfigProject.yaml