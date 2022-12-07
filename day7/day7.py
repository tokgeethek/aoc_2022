from pathlib import Path
from collections import Counter

with open ("day7input.txt", 'r') as input:
    # create dict using Counter so that we can add new dir and their size counts
    size_dict = Counter()
    # use Path so that it's easy to add and remove from dir using .parent and /
    dir = Path('/')

    for row in input:
        data = row.strip('\n').split()
        if data[0] == '$':
            if data[1] == 'cd':
                if data[2] == '..':
                    dir = dir.parent
                else:
                    dir = dir/data[2]

        elif data[0] != 'dir':
            size_dict[dir] += int(data[0])
            for x in dir.parents:
                size_dict[x] += int(data[0])
            
    all_sizes = sorted(size_dict.values())

    # solution 1
    small = [i for i in all_sizes if i <= 100_000]
    print(sum(small))

    # solution 2
    # last item in all_sizes list is the size of the whole filesystem
    required_space = 3_000_0000 - (7_000_0000 - all_sizes[-1])
    for p in all_sizes:
        if p <= required_space:
            continue
        else:
            print(p)
            break
