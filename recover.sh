#!/bin/bash

# Usage: ./run_command_with_args.sh command text_file
# Example: ./run_command_with_args.sh echo args.txt

# Check if correct number of arguments is provided
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <text_file>"
    exit 1
fi

# Assign variables to the arguments
text_file=$1

# Check if the text file exists
if [[ ! -f $text_file ]]; then
    echo "Error: File '$text_file' not found."
    exit 1
fi

# Read the arguments from the file and store them in an array
args=()
while IFS= read -r line; do
    args+=("$line")
done < "$text_file"

# Run the command with the arguments
git checkout d142490b022900ecd511f36143b6860311e3fb41 "${args[@]}"