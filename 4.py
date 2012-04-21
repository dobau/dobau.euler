def is_palindrome(n):
    n_str = str(n)

    tam = int(len(n_str)/2 + 0.5)

    for x in xrange(0, tam):
        if (n_str[x] != n_str[len(n_str) - x - 1]):
            return False

    return True

print "%r" % is_palindrome(121)
print "%r" % is_palindrome(111)
print "%r" % is_palindrome(1221)
print "%r" % is_palindrome(11)
print "%r" % is_palindrome(98)
print "%r" % is_palindrome(9)
print "%r" % is_palindrome(900)
print "%r" % is_palindrome(998899)
print "%r" % is_palindrome(9987899)
print "%r" % is_palindrome(99877899)
print "%r" % is_palindrome(998767899)
print "%r" % is_palindrome(9987667899)
print "%r" % is_palindrome(99876567899)

max = 0
for i in xrange(999, 100, -1):
    for j in xrange(999, 100, -1):
        prod = j * i
        if (is_palindrome(prod)):
            if (max < prod):
                max = prod
                print "%d %d = %d" % (j, i, max)

print "%d" % (max)