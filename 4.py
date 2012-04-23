def is_palindrome(n):
    n_str = str(n)

    tam = int(len(n_str)/2 + 0.5)

    for x in xrange(0, tam):
        if (n_str[x] != n_str[len(n_str) - x - 1]):
            return False

    return True

max = 0
for i in xrange(999, 100, -1):
    for j in xrange(999, 100, -1):
        prod = j * i
        if (is_palindrome(prod)):
            if (max < prod):
                max = prod

print "%d" % (max)