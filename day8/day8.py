#going horizontally first, arr_index = row; index = col

def check_visible(data,transposed,arr_index,index):
    hori_array = data[arr_index]
    vert_array = transposed[index]

    # horizontal
    target = hori_array[index]
    left = hori_array[0:index]
    right = hori_array[index+1:]
    left_not_visible = any(x >= target for x in left) 
    right_not_visible =  any(x >= target for x in right)

    # vertical
    goal = vert_array[arr_index]
    top = vert_array[0:arr_index]
    bottom = vert_array[arr_index+1:]
    top_not_visible = any(x >= goal for x in top) 
    bottom_not_visible =  any(x >= goal for x in bottom)

    # returns True = visible at least on one side, False = not visible (horizontally)
    return not(left_not_visible and right_not_visible and top_not_visible and bottom_not_visible)

def walk(arr,i):
    tmp = 0
    if arr:
        for x in arr:
            if x < i:
                tmp += 1
            else:
                tmp += 1
                break
        return tmp
    else:
        return 0

def check_score(data,transposed,arr_index,index):
    hori_array = data[arr_index]
    vert_array = transposed[index]

    # horizontal
    target = hori_array[index]
    left = hori_array[0:index]
    right = hori_array[index+1:]
    left_score = walk(left[::-1],target)
    right_score =  walk(right,target)

    # vertical
    goal = vert_array[arr_index]
    top = vert_array[0:arr_index]
    bottom = vert_array[arr_index+1:]
    top_score = walk(top[::-1],goal) 
    bottom_score = walk(bottom,goal)

    return left_score*right_score*top_score*bottom_score

with open('day8input.txt','r') as input:
    data = []
    for row in input:
        data.append([int(n) for n in row.strip('\n')])

    # create a transposed data for vertical
    transposed_tuples = list(zip(*data))
    transposed = [list(sublist) for sublist in transposed_tuples]
    
    ans1 = 0
    ans2 = 0
    for i,j in enumerate(data):
        for p in range(len(j)):
            # solution 1
            if check_visible(data,transposed,i,p):
                ans1+=1
            # solution 2
            if check_score(data,transposed,i,p) > ans2:
                ans2 = check_score(data,transposed,i,p)
                
    print(ans1)
    print(ans2)