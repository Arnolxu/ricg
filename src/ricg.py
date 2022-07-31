text = input("Banned characters: ,/~\nEnter a string: ")

out = "=rule "

words = text.replace(" ", "~")

if len(words) % 4 != 0:
    words += "~" * (4 - len(words) % 4)

wp1 = words[:int(len(words)/2)]
wp2 = words[int(len(words)/2):]

i = 0
for w in range(int(len(wp1) / 2)):
    out += wp1[w * 2] + wp1[w * 2 + 1] + "/" + wp2[w * 2] + wp2[w * 2 + 1] + " "

print(out)