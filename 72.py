word1 = "horse"
word2 = "ros"

count = 0
min_len = min(len(word1), len(word2))

for i in range(min_len):
    if word1[i] != word2[i]:
        count += 1
    elif i > 0 and word1[i] == word2[i-1]:
        count -= 1

count += abs(len(word1) - len(word2))

print(count)
