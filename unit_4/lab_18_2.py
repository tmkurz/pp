def count_letters(string):
    stats = {}
    for c in string:
        if c in stats:
            stats[c] += 1
        else:
            stats[c] = 1
    return stats

print(count_letters("abecadło"))


