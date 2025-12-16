word = "hello there bro"
words = ""
reversed_words = ""
for i in range(0, len(word)):
    if word[i-1] == " ":
        reversed_words += words[::-1] + word[i]
        words = ""
    else:
        words += word[i]

print(reversed_words)