def totuple(arr):
    if arr.shape == ():
        return arr.item()
    else:
        return tuple(map(totuple, arr))