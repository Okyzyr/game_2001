from dice_roll import roll

def game_2001():
    player1 = 0
    player2 = 0
    wynik = 1
    turn = 1
    while player1 < 2001 and player2 < 2001:

        rzut = roll("2D6")
        if rzut == 7 and turn != 1:
            player1 = player1 % 7
            print("wyrzucono 7, wynik gracza dzieli się przez 7")
            print(f"P1 rzucił {rzut}. Stan punktów: {player1}", end="\n")
            input("Kolejny gracz wciska enter.\n")
        elif rzut == 11 and turn != 1:
            player1 = player1*11
            print("wyrzucono 11, wynik gracza mnoży się przez 11")
            print(f"P1 rzucił {rzut}. Stan punktów: {player1}", end="\n")
            input("Kolejny gracz wciska enter.\n")
        else:
            player1 += rzut
            print(f"P1 rzucił {rzut}. Stan punktów: {player1}", end="\n")
            input("Kolejny gracz wciska enter.\n")

        rzut = roll("2D6")
        if rzut == 7 and turn != 1:
            player2 = player2 % 7
            print("wyrzucono 7, wynik gracza dzieli się przez 7")
            print(f"P2 rzucił {rzut}. Stan punktów: {player2}", end="\n")
            input("Kolejny gracz wciska enter.\n")
        elif rzut == 11 and turn != 1:
            player2 = player2*11
            print("wyrzucono 11, wynik gracza mnoży się przez 11")
            print(f"P2 rzucił {rzut}. Stan punktów: {player2}", end="\n")
            input("Kolejny gracz wciska enter.\n")
        else:
            player2 += rzut
            print(f"P2 rzucił {rzut}. Stan punktów: {player2}", end="\n")
            input("Kolejny gracz wciska enter.\n")


        turn += 1
    return player1, player2


print(game_2001())
