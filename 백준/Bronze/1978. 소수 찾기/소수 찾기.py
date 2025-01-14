n = int(input())
l = map(int , input().split())
result = 0


for i in l:
    count =0
    if i > 1:
        for j in range(2 , i):
            if i % j == 0:
                count +=1
                break

        else:
            result += 1 

print(result)