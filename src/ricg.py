# check if there are any CLI arguments
import sys
if len(sys.argv) > 1:
    text = " ".join(sys.argv[1:])
else:
    text = input("Banned characters: ,/~\nEnter a string: ")

# space to ~
words = text.replace(" ", "~")

# make sure the length of the text is a multiple of 4
if len(words) % 4 != 0:
    words += "~" * (4 - len(words) % 4)

# split the text into two halves
wp1 = words[:int(len(words)/2)]
wp2 = words[int(len(words)/2):]

# generate a text that will be parsed by RIC
out = "=rule "
i = 0
for w in range(int(len(wp1) / 2)):
    out += wp1[w * 2] + wp1[w * 2 + 1] + "/" + wp2[w * 2] + wp2[w * 2 + 1] + " "

# print the generated text
print(out)