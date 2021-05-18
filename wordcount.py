user_text = input()


word_count = 0

# Option 1 - Nesting loop that adds to word count each iteration.
for i in range(len(user_text)):
    if (user_text[i] != ' ') and (user_text[i] != ',') and (user_text[i] != '.'):
        word_count += 1


# Option 2 - A much simpler count of the length, minus the banned characters.
# I am guessing that as this is a chapter on loops, Option 1 is the preferred answer.
#word_count = (len(user_text) - (user_text.count(' ') + user_text.count(',') + user_text.count('.')))

print(word_count)
