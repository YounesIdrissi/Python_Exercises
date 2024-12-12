n = int(input())
arr = map(int, input().split())
    
max_val = max[arr]
    
max_val.remove(max[arr])
    
while max_val == max[arr]:
    max_val.pop(max[arr])
    
max_val = max[arr]
print(max_val)