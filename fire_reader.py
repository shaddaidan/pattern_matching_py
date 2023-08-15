import re

def extract_paragraphs(text):
    # Split the text into paragraphs
    paragraphs = re.split(r'\n\s*\n', text)
    return paragraphs

def find_fire_words(paragraph):
    # Find words with prefix "fire" (case-insensitive)
    fire_words = re.findall(r'\bfire\w*\b', paragraph, re.IGNORECASE)
    return fire_words

def create_new_file(paragraph, count):
    filename = f"fire_paragraph_{count}.txt"
    with open(filename, "w") as file:
        file.write(paragraph)

def main():
    with open("transcript.txt", "r") as file:
        transcript = file.read()

    paragraphs = extract_paragraphs(transcript)

    for count, paragraph in enumerate(paragraphs, start=1):
        fire_words = find_fire_words(paragraph)
        if fire_words:
            for _ in range(len(fire_words)):
                create_new_file(paragraph, count)

if __name__ == "__main__":
    main()


