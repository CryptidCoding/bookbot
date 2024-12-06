def sort_on(dict_item):
    return dict_item["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
        print(f"{num_words} words found in this document")
        
        lowercase_words = file_contents.lower()
        lowercase_chars = list(lowercase_words)
        char_dict = {}
        
        for lowercase_char in lowercase_chars:
            if lowercase_char.isalpha():
                if lowercase_char in char_dict:
                    char_dict[lowercase_char] += 1
                else:
                    char_dict[lowercase_char] = 1
        
        # Transform the dictionary into a list of dictionaries
        list_char_dict = [{"char": k, "num": v} for k, v in char_dict.items()]
        
        # Sort the list based on the frequency of characters
        list_char_dict.sort(reverse=True, key=sort_on)
        
        # Print the sorted report
        for item in list_char_dict:
            char = item["char"]
            num = item["num"]
            print(f"The '{char}' character was found {num} times")

main()
