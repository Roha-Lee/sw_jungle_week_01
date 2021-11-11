n, m = map(int, input().split())

def reverse(n):
    number = str(n)
    reverse_number = number[::-1]
    return int(reverse_number)

rev_n = reverse(n)
rev_m = reverse(m)

if rev_n > rev_m:
    print(rev_n)
else:
    print(rev_m)