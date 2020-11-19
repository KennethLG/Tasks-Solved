game1, game2,game3 = [1,2,3], [4,5,6], [7,8,9]
def comp(L) :
    if (game1[0]==L and game2[1]==L and game3[2]==L) or (game1[2]==L and game2[1]==L and game3[0]==L) :
        return 1
    else :
        for i in range(3) :
            if (game1[i]==L and game2[i]==L and game3[i]==L) or (game1==[L]*3 or game2==[L]*3 or game3==[L]*3) :
                return 1
def add(n, turno) :
    global game1, game2, game3
    bol = 0
    if n <= 3 : game1[game1.index(n)] = turno
    if 4 <= n <= 6: game2[game2.index(n)] = turno
    if 7 <= n <= 9 : game3[game3.index(n)] = turno
    #comprobacion
    bol = comp(turno)
    return bol
cases = int(input())
for i in range(cases):
    game1, game2,game3 = [1,2,3], [4,5,6], [7,8,9]
    line, turno, move = [int(i) for i in input().split()], "O", 0
    for i in range(len(line)) :
        if turno == "O":
            turno = "X"
        else:
            turno = "O"
        move += 1
        if add(line[i], turno) == 1:
            print(move,"")
            break
        if move == 9:
            print(0,"")
            break
