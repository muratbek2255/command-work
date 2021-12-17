def change_to_star(text):
    text = text
    words = text.split()
    new_text = '*'.join(words)
    return new_text

print(change_to_star(input("Enter text: ")))
