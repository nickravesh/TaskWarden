#!/bin/bash

# Define ANSI color codes
RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
RESET="\033[0m"  # Reset color

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Update repositories
echo -e "${YELLOW}UPDATING REPOSITORIES...${RESET}"
if sudo apt update; then
  echo -e "${GREEN}UPDATING DONE!${RESET}"
else
  echo -e "${RED}Failed to update repositories. Aborting installation.${RESET}"
  exit 1
fi

# Install PIP3
echo -e "${YELLOW}INSTALLING PIP3...${RESET}"
if sudo apt install python3-pip; then
  echo -e "${GREEN}INSTALLING PIP3... DONE!${RESET}"
else
  echo -e "${RED}Failed to install PIP3. Aborting installation.${RESET}"
  exit 1
fi

# Install Python requirements
echo -e "${YELLOW}INSTALLING REQUIREMENTS...${RESET}"
if pip install -r requirements.txt --no-warn-script-location; then
  echo -e "${GREEN}INSTALLING REQUIREMENTS... DONE!${RESET}"
else
  echo -e "${RED}Failed to install Python requirements. Aborting installation.${RESET}"
  exit 1
fi

# Define the target directory path
TARGET_DIR="$HOME/.local/bin/TaskWarden"

# Check if the directory already exists
if [ -d "$TARGET_DIR" ]; then
  echo -e "${YELLOW}Directory already exists: $TARGET_DIR${RESET}"
else
  # Create the directory and its parent directories
  if mkdir -p "$TARGET_DIR"; then
    echo -e "${GREEN}Directory created: $TARGET_DIR${RESET}"
  else
    echo -e "${RED}Failed to create directory: $TARGET_DIR${RESET}"
    exit 1
  fi
fi

# Move files to the target directory
echo -e "${YELLOW}MOVING THE FILES...${RESET}"
if cp -r "$SCRIPT_DIR"/* "$TARGET_DIR"; then
  cd "$TARGET_DIR"
  echo -e "${GREEN}MOVING... DONE!${RESET}"
else
  echo -e "${RED}Failed to move files. Aborting installation.${RESET}"
  exit 1
fi

# Configure aliases
echo -e "${YELLOW}ONE MOMENT... SETTING THINGS UP...${RESET}"
{
  echo "alias todo='python3 $HOME/.local/bin/TaskWarden/TaskWarden.py'"
  echo "alias tw='python3 $HOME/.local/bin/TaskWarden/TaskWarden.py'"
  echo "alias TaskWarden='python3 $HOME/.local/bin/TaskWarden/TaskWarden.py'"
  echo "alias taskwarden='python3 $HOME/.local/bin/TaskWarden/TaskWarden.py'"
} >> ~/.bashrc

echo -e "${GREEN}ALL DONE!${RESET}"
echo "Now just type 'TaskWarden' or 'taskwarden' or 'tw' or 'todo' to get started."

# Return to the original directory
cd "$SCRIPT_DIR"
bash