def check_contain(a,b):
    a1 = int(a.split('-')[0])
    a2 = int(a.split('-')[-1]) +1
    b1 = int(b.split('-')[0])
    b2 = int(b.split('-')[-1]) +1   
    
    if a1 != a2:
        arange = range(a1,a2)
    else:
        arange = [a1]
        print(arange)
    
    if b1 != b2:
        brange = range(b1,b2)
    else:
        brange = [b1]
        print(brange)

    # solution 1
    # return set(arange).issubset(brange) or set(brange).issubset(arange) or arange == brange
    # solution 2
    return any(list(set(arange)&set(brange)))

contain = 0
with open("./day4input.txt") as input:
    for row in input:
        elf_a, elf_b = row.strip('\n').split(",")
        # print(elf_a,elf_b)
    
        # print(check_contain(elf_a,elf_b))
        contain += check_contain(elf_a,elf_b)
    
    print(contain)

