def main():
  with open("books/frankenstein.txt") as book:
    file_contents = book.read()
    count_words(file_contents)
    count_chars(file_contents)

def count_words(text):
  words = text.split()
  word_count = len(words)

def count_chars(text):
  character_dict = {}
  text_lower = text.lower()
  for char in text_lower:
    character_dict[char] = character_dict.get(char, 0) + 1

  dict_to_list(character_dict)

def on_sort(dict):
  return dict["count"]

def dict_to_list(dict):
  new_list = []
  for item in dict:
    if item.isalpha():
      new_list.append({ "char": item, "count": dict[item] })
  new_list.sort(reverse=True, key=on_sort)
  print(new_list)

main()