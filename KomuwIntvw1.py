words = ["hello", "hell", "odelo"]

# print the letters that appear in each word in the array

# scan each list

# merge_strings
common = ""
distinct = []

for x in range(0, len(words)):
    common = common + words[x]

for chr in common:
    if chr not in distinct:
        distinct.append(chr)

for word in words:
    for char in distinct:
        if char not in word:
            distinct.remove(char)

print(distinct)