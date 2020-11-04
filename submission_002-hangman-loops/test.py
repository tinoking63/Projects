original_word = "yeet"
char = "y"
answer_word = "___t"
chosen = len(original_word)
place = original_word.find(char)

answer = answer_word[:c] + place + answer_word[chosen+1:]
print(answer)