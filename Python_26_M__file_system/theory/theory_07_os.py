import os

# get current work directory
print(os.getcwd())

# create the new directory
os.makedirs('new_dir', exist_ok=True)

# change current work directory -> new_dir
os.chdir('new_dir')
print(os.getcwd())

# change current work directory -> theory
os.chdir('..')
print(os.getcwd())

# delete directory new_dir
os.rmdir('new_dir')

# create nested directories
os.makedirs('new_dir/new_dir/new_dir/new_dir')

# os.rmdir('new_dir') !!!  can delete ONLY empty dirs

# delete not empty directory
import shutil
shutil.rmtree('new_dir')
