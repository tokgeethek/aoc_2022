
lowercase = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

priority = {}
for i,c in enumerate(lowercase,1):
    priority[c] = i

# print(priority)
priority_sum = 0
priority_sum_2 = 0

with open("./day3input.txt") as input:
# solution for part 1 of question    
    # for row in input:
    #     data = row.strip('\n')
    #     midpoint = len(data)//2
        
    #     firstpart = [x for x in data[:midpoint]]
    #     secondpart = [y for y in data[midpoint:]]
    #     intersection = list(set(firstpart)&set(secondpart))

    #     for i in intersection:
    #         priority_sum += priority[i]
    
# print(priority_sum)

# solution for part 2 of question   
    group = [x.strip('\n') for x in input]
    grouped = [group[n:n+3] for n in range(0, len(group), 3)]
    for elves in grouped:
        badge = list(set(elves[0])&set(elves[1])&set(elves[2]))
        priority_sum_2 += priority[badge[0]]
    print(priority_sum_2)
