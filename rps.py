p1_score: int = 0
cpu_score: int = 0


def game():

    from random import randint
    wins = "You won! \n"
    lose = " You loose! \n"
    global p1_score
    global cpu_score

    ai = randint(0, 2)
    if ai == 0:
        ai = "Rock"
    elif ai == 1:
        ai = "Paper"
    else:
        ai = "Scissor"
    # 0 = rock, 1 = paper, 2 = scissor

    p1 = input("Make your move:")
    p1 = p1.title()
    if p1 == "Rock" and ai == "Scissor":
        print(wins)
        if wins:
            p1_score += 1
            print(f"User: {p1_score} CPU: {cpu_score}")
    elif p1 == "Paper" and ai == "Rock":
        print(wins)
        if wins:
            p1_score += 1
            print(f"User: {p1_score} CPU: {cpu_score}")
    elif p1 == "Scissor" and ai == "Paper":
        print(wins)
        if wins:
            p1_score += 1
            print(f"User: {p1_score} CPU: {cpu_score}")
    elif p1 == ai:
        print("Draw")
    else:
        cpu_score += 1
        print(ai + "," + lose)
        print(f"User: {p1_score} CPU: {cpu_score}")

    game()


game()
