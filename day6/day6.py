def check_duplicate(string):
    lst = [x for x in string]
    return sorted(lst) == sorted(list(set(lst)))

with open ('day6input.txt','r') as input:
    data = input.readline()
    marker = [data[n:n+4] for n in range(0, len(data))]
    message = [data[n:n+14] for n in range(0, len(data))]
    for i in marker:
        if check_duplicate(i):
            x = data.index(i)
            ans1 = x+4
            break
    for i in message:
        if check_duplicate(i):
            y = data.index(i)
            ans2 = y+14
            break        
    print(ans1)
    print(ans2)
    
