#!/bin/bash


# Save the current directory
current_dir=$(pwd)

# Change to the directory where the files are located
cd /home/kidscripto/Documents

# Get a list of all files in the directory
files=$(ls)

# Loop through the list of files
counter=1
for file in $files; do
	counter=$((counter+1))
	new_file_name="file$counter"
	mv $file $new_file_name
done

# Change back to the original directory
cd $current_dir



