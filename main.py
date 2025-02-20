def main():
    filename = input("Enter the path and file name to your text: ")
    text = get_book_text(filename)
    num_words = get_num_words(text)
    characters = get_character_count(text)
    report = get_report(text, filename, num_words, characters)

def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_character_count(text):
    lower_text = text.lower()
    character_dict = {}
    for character in lower_text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_report(text, filename, num_words, characters):
    descending_order = dict(sorted(characters.items(), key=lambda x: x[1], reverse=True))
    include_list = "abcdefghijklmnopqrstuvwxyz"
    print(f"--- Begin report of {filename} ---")
    print(f"{num_words} words found in the document"'\n')
    for character, count in descending_order.items():
        if character in include_list:
            print(f"The '{character}' character was found {count} times")

    
main()