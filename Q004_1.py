N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sub_list= [x - y for x, y in zip(A, B)]
print(*sub_list)
