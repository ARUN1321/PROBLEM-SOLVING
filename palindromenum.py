def main(n):
    n = str(n)
    if n == n[::-1]:
        return "true"
    else: return "false"

n = int(input())
print(main(n))
