def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):     
        print(''.join(set(list(string[i: i + k]))))