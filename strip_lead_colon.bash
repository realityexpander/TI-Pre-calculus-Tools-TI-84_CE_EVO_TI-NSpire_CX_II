# Purpose: Strips a leading colon (:) from every line in all files within the "dirty/"
#          directory while preserving all other leading/trailing whitespace formatting.
# Usage:   Run this script from the parent directory containing the "dirty/" folder.
#          Ensure a "cleaned/" directory exists prior to execution, or output will fail.

for file in dirty/*; do
    # Skip directories or non-existent matches
    [ -f "$file" ] || continue
    
    # Extract just the filename from the path
    filename=$(basename "$file")
    
    awk '{ sub(/^:/, ""); print }' "$file" > "cleaned/$filename"
done
