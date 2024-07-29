def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars_dict = get_chars_dict(text)
    report = get_book_report(book_path, word_count, chars_dict)
    print(report)



def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_chars_dict(text):
    text = text.lower()
    character_counts = {}
    for character in text:
        if character_counts.get(character):
            character_counts[character]+=1
        else:
            character_counts[character] = 1
    
    return character_counts

def get_book_report(book_path, word_count, chars_dict):
    sorted_chars_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    report = f"--- Begin report of {book_path} ---\n"
    report += f"{word_count} words found in the document\n"

    for c, count in sorted_chars_dict.items():
        if c.isalpha():
            report += f"\n The '{c}' character was found {count} times"
    
    report += "\n--- End report ---"

    return report


main()
