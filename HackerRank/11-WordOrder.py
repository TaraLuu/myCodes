from collections import OrderedDict

dict = OrderedDict()

for i in range(int(input())):
    word = input()
    if dict.get(word):
        dict[word] = int(dict.get(word)) + 1
    else:
        dict[word] = 1

print(len(dict))
print(' '.join([str(dict.get(x)) for x in dict]))