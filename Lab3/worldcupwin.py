def world_cup():
    d = {1975:'WI', 1979:'WI', 1983:'IND', 1987:'AUS', 1992:'PAK', 1996:'SL', 1999:'AUS', 2003:'AUS', 2007:'AUS', 2011:'IND', 2015:'AUS', 2019:'ENG'}
    from collections import Counter
    c = Counter(d.values())
    print("Best:", c.most_common(1)[0][0])
    print("Winners:", set(d.values()))

world_cup()