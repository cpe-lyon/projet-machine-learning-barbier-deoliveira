#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Error: Directory $1 does not exist."
    exit 1
fi

mkdir user_input

for file in "$1"/*; do
    if [ -f "$file" ]; then
        ffplay -x 400 -y 400 -alwaysontop -exitonkeydown $file &
        echo
        echo -n "Enter a string for $file: "
        read user_input

        base_file=$(basename "$file")
        txt_file="user_input/${base_file%.*.}.txt"
        echo "$user_input" > "$txt_file"
    fi
done
