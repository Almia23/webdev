def top_words(fname):
    from collections import Counter
    with open(fname) as f:
        words = f.read().split()
    for w,c in Counter(words).most_common(10): print(w,c)

top_words("file.txt")