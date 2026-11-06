t = int(input())
for _ in  range(t):
    num = list(map(int, input().split()))
    num_sum = sum(num)
    avg_sum = num_sum/len(num)
    print( f"{num_sum} {avg_sum}")