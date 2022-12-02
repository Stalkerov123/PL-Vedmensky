def main():
    n = int(input())
    if n == 0:
        return 0
    else:
        return max(n, main())
    
print(main())
