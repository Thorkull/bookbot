def get_num_words(book_text):
    return len(book_text.split())

def get_num_characters(book_text):
    characters = {}
    for i in book_text:
        if i.lower() in characters:
            characters[i.lower()] += 1
        else:
            characters[i.lower()] = 1
    return characters

def sort_character_counts(character_list):
    new_list = []
    sorted_list = []
    for c in character_list:
        char_count = character_list[c]
        temp_dict = {
            "char": c,
            "num": char_count
        }
        if c != " ":
            new_list.append(temp_dict)
    new_list.sort(key=lambda x: x['num'], reverse=True)
    return new_list