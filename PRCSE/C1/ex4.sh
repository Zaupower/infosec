#!/bin/bash
# Verify the number of command-line arguments passed, if not equal to 1 exit
if [ "$#" -ne 2 ]; then
        echo "Usage: $0 <path> <number_of_files>"
        exit 1
fi
#Get all .csv files in path
csv_files=$(ls $1/*.csv)
lines_to_output=$2
# Check if csv_files empty
if [ -z "csv_files" ]; then
       echo "No .csv files found in: $csv_files"
else
     echo "Csv files:"
     result=""
     for csv_file in $csv_files; do
             # Use wc to get the number of lines and awk
             num_lines=$(wc -l "$csv_file" | awk '{print $1}')
             # Extract file name
             filename=$(basename "$csv_file")
             # Append results to new variable
             result+="$filename $num_lines"$'\n'
             # Use sort to sort iteration result by the field separator(-t), by the key for 
             # sorting (-k<key number>) and use numerical sorting (n) in reverse order r() 
     done
     # Sort by second field key(k2) by numerical oreder (n) in reverse (r)
     sorted_result=$(echo -e "$result" | sort -k2,2nr)
     # Print the sorted result       
     IFS=$'\n'
     total_lines="$(echo "$sorted_result" | wc -l)"
     # If the total lines gathered are less or equal than the required to print, print all
     if [ "$total_lines" -le "$lines_to_output" ];then
             for line in "$sorted_result"; do
             echo "$line"
             done
     else
        new_variable=$(echo "$sorted_result" | awk -v num="$2" 'NR <= num {print}')
        echo "$new_variable"
     fi 
fi
