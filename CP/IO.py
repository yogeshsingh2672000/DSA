import sys
input = sys.stdin.readline

def main():
    n = int(input())
    while n > 0:
        arr = list(map(int, input().split()))
        print(arr)
        n -= 1
    # Your solution here

if __name__ == "__main__":
    main()
