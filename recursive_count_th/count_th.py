'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    if "th" in word:
        return count_th(word.replace("th", "1", 1)) + 1
    else:
        return 0


print(count_th("thisthisthis"))
