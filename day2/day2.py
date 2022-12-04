# A = Rock
# B = Paper
# C = Scissors

my_score = {"X":1,
"Y":2,
"Z":3}

win = {"A":"Y", "B":"Z", "C":"X"}
draw = {"A":"X", "B":"Y", "C":"Z"}
lose = {"A":"Z", "B":"X", "C":"Y"}

def check_win(oppo,me):
    #draw
    if (oppo == "A" and me == "X") or (oppo == "B" and me == "Y") or (oppo == "C" and me == "Z"):
        return 3
    #win
    elif (oppo == "A" and me == "Y") or (oppo == "B" and me == "Z") or (oppo == "C" and me == "X"):
        return 6
    #lose
    elif (oppo == "A" and me == "Z") or (oppo == "B" and me == "X") or (oppo == "C" and me == "Y"):
        return 0

def show_hand(oppo,me):
    if me == "X":
        return lose[oppo]
    elif me == "Y":
        return draw[oppo]
    elif me == "Z":
        return win[oppo]


total_score = 0
second_total_score = 0

with open("./day2input.txt") as input:
    for row in input:
        data = row.strip('\n').split(" ")
        oppo = data[0]
        me = data[-1]

        #score
        shape_score = my_score[me]
        round_score = check_win(oppo,me) + shape_score
        total_score += round_score

        #result
        #X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
        hand = show_hand(oppo,me)
        second_round_score = check_win(oppo,hand) + my_score[hand]
        second_total_score += second_round_score

    print(total_score)
    print(second_total_score)