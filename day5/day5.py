stack = {'a':["W","P","G","Z","V","S","B"],
        'b':["F","Z","C","B","V","J"],
        'c':["C","D","Z","N","H","M","L","V"],
        'd':["B","J","F","P","Z","M","D","L"],
        'e':["H","Q","B","J","G","C","F","V"],
        'f':["B","L","S","T","Q","F","G"],
        'g':["V","Z","C","G","L"],
        'h':["G","L","N"],
        'i':["C","H","F","J"]}

idx_dict = {}
for x,y in enumerate("abcdefghi",1):
    idx_dict[x] = y
print(idx_dict)

def cratemover9000(amount,src,dst):
    for i in range(amount):
        yeet = stack[idx_dict[src]].pop(0)
        stack[idx_dict[dst]].insert(0,yeet)
        print(f"moved {yeet} from {src} to {dst} ")
    return

def cratemover9001(amount,src,dst):
    yeet = stack[idx_dict[src]][:amount]
    print(yeet)
    stack[idx_dict[dst]] = yeet + stack[idx_dict[dst]]
    stack[idx_dict[src]] = stack[idx_dict[src]][amount:]
    print(f"moved {yeet} from {src} to {dst} ")
    return

with open ("day5input.txt", 'r') as input:
    for row in input:
        tmp = row.strip('\n').split()
        amount, src, dst =  int(tmp[1]),int(tmp[3]),int(tmp[5])

        # solution 1
        # cratemover9000(amount,src,dst)

        # solution 2
        cratemover9001(amount,src,dst)
    
    ans = []
    print(stack)
    for p in stack:
        try:
            ans.append(stack[p][0])
        except:
            continue
    print("".join(ans))

