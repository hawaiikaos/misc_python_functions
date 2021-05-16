def left_ex_join(a,b):
    # a left exclusionary join for two lists
    # subtract list b from list a
    for item in b:
        try:
            a.remove(item)
        except:
            pass
    
    return a
