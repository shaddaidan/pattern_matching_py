# FIRE READER

Here's how this code works:

The extract_paragraphs function splits the transcript into paragraphs based on empty lines.
The find_fire_words function uses a regular expression to find words with the prefix "fire" (case-insensitive) in a paragraph.
The create_new_file function creates a new text file with a unique filename and writes the given paragraph into it.
In the main function, the script reads the transcript from the "transcript.txt" file.
It then extracts paragraphs from the transcript and checks each paragraph for "fire" words.
If "fire" words are found, the script creates a new text file for each paragraph and writes the paragraph into the file multiple times, based on the number of "fire" words found.
To use this script, save your transcript in a file named "transcript.txt" in the same directory as the script. Run the script, and it will create new text files containing paragraphs with "fire" words. Make sure to modify the regular expression and file naming conventions as needed for your specific use case.