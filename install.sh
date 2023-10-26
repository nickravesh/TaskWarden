#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

echo "UPDATING REPOSITORIES..."
sudo apt update
echo "UPDATING DONE!"

echo "INSTALLING PIP3..."
sudo apt install python3-pip
echo "INSTALLING PIP3... DONE!"

echo "INSTALLING REQUIREMENTS..."
pip install -r requirements.txt --no-warn-script-location
echo "INSTALLING REQUIREMENTS... DONE!"

echo "MOVING THE THE FILES..."
cp -r $SCRIPT_DIR ~/.local/bin/TaskWarden
cd ~/.local/bin/TaskWarden
echo "MOVING... DONE!"

echo "ONE MOMENT... SETTING THINGS UP..."
echo "alias todo='python3 ~/.local/bin/TaskWarden/TaskWarden.py'" >> ~/.bashrc
echo "alias tw='python3 ~/.local/bin/TaskWarden/TaskWarden.py'" >> ~/.bashrc
echo "alias TaskWarden='python3 ~/.local/bin/TaskWarden/TaskWarden.py'" >> ~/.bashrc
echo "alias taskwarden='python3 ~/.local/bin/TaskWarden/TaskWarden.py'" >> ~/.bashrc
echo "ALL DONE!"
echo "Now just type 'TaskWarden' or 'taskwarden' or 'tw' or 'todo' to get started."

cd $SCRIPT_DIR
bash