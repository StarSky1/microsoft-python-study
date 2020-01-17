# Install virtual environment
pip install virtualenv

# windows systems (normally,folder name is venv)
python -m venv <folder_name>

# OSX/Linux (bash)
virtualenv <folder_name>

# Using  virtual environments
# windows systems
# cmd.exe
<folder_name>\Scripts\Activate.bat

# powershell
<folder_name>\Scripts\Activate.ps1

# bash shell
../<folder_name>/Scripts/activate

# OSX/Linux (bash)
<fold_name>/bin/activate

# Installing packages in a virtual environment

# Install an individual package
pip install colorama

# Install from a list of packages
pip install -r requirements.txt

# requirements.txt
colorama