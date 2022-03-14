def get_middle(s):
    if len(s) % 2 == 0:
        return s[int(len(s)/2)-1] + s[int(len(s)/2)]
    else:
        x = int(len(s) / 2)
        return s[x]