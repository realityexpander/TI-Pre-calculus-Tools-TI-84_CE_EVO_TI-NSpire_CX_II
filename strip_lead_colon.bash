for file in dirty/*; do
    # Skip directories or non-existent matches
    [ -f "$file" ] || continue

    # Extract just the filename from the path
    filename=$(basename "$file")

    awk '{ sub(/^:/, ""); print }' "$file" > "cleaned/$filename"
done
