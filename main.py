from dice_roll import roll, check

def game_2001():
    player1 = 0
    player2 = 0
    wynik = 1
    turn = 1
    dice = ""
    temp = []
    input("Wciśnij Enter aby rozpocząć grę\n")

    while player1 < 2001 and player2 < 2001:
        temp = []
        while len(temp) < 2:
            dice = input("Dostępne opcje: D3, D4, D6, D8, D10, D12, D20, D100.\n"
                         f"{len(temp)+1}/2 - Spośród dostępnych opcji wybierz pierwszą kość jaką kością chcesz rzucić: \n")
            dice = dice.upper()
            if check(dice):
                temp.append(roll(dice))
            else:
                print("Niewłaściwy typ kości! wybierz jeszcze raz.\n")
                continue
        rzut = int(temp[0]) + int(temp[1])
        if rzut == 7 and turn != 1:
            player1 = player1 // 7
            print("wyrzucono 7, wynik gracza dzieli się przez 7")
            print(f"Gracz rzucił {temp[0]} oraz {temp[1]} = {rzut}. Stan punktów: {player1}", end="\n\n")
        elif rzut == 11 and turn != 1:
            player1 = player1*11
            print("wyrzucono 11, wynik gracza mnoży się przez 11")
            print(f"Gracz rzucił {temp[0]} oraz {temp[1]} = {rzut}. Stan punktów: {player1}", end="\n\n")
        else:
            player1 += rzut
            print(f"Gracz rzucił {temp[0]} oraz {temp[1]} = {rzut}. Stan punktów: {player1}", end="\n\n")

        rzut = roll("2D6")
        if rzut == 7 and turn != 1:
            player2 = player2 // 7
            print("wyrzucono 7, wynik gracza dzieli się przez 7")
            print(f"Komputer rzucił {rzut}. Stan punktów: {player2}", end="\n")
            input("Gracz wciska enter aby rzucić kością.\n")
        elif rzut == 11 and turn != 1:
            player2 = player2*11
            print("wyrzucono 11, wynik gracza mnoży się przez 11")
            print(f"Komputer rzucił {rzut}. Stan punktów: {player2}", end="\n")
            input("Gracz wciska enter aby rzucić kością.\n")
        else:
            player2 += rzut
            print(f"Komputer rzucił {rzut}. Stan punktów: {player2}", end="\n")
            input("Gracz wciska enter aby rzucić kością.\n")

        turn += 1
    return f"Koniec gry. Wyniki:\nGracz 1: {player1}, Gracz 2:{player2}"


print(game_2001())
