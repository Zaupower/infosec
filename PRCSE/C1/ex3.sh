#!/bin/bash
# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi
directory="$1"
# Check if the specified directory exists
if [ ! -d "$directory" ]; then
    echo "Error: Directory '$directory' does not exist."
    exit 1
fi

# Check if the script has read permission for the specified directory
if [ ! -r "$directory" ]; then
    echo "Error: No read permission for directory '$directory'."
    exit 1
fi
# Loop through files in the directory with group read permission
echo "Files with group read permission in '$directory':"
for file in "$directory"/*; do
    if [ -f "$file" ] && [ -r "$file" ] && [ -r "$file" ]; then
        echo "$file"
    fi
done
