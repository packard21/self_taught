import random
def hangman(word):
    wrong = 0 #miss回数
    stages = ["",
              "_____     ",
              "|    |    ",
              "|    |    ",
              "|    O    ",
              "|   /| ＼  ",
              "|   / ＼  ",
              "|         "
              ]
    rletters = list(word) #wordを一文字ずつに分解して保持
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    #以下制御
    while wrong < len(stages) -1:
        print("\n")
        msg = "1文字を予想してね: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$" #indexの仕様
        else:
            wrong += 1
        print(" ".join(board))
        print("\n".join(stages[:wrong+1]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))

words = ["cat", "car", "cow", "coffee", "company", "candy"]
hangman(words[random.randint(0, len(words)-1)])
