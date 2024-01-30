#Поле
field=[[" "] * 3 for i in range(3)]

#Игровое поле
def playing_field():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")


#Проверки+ввод
def ask():
    while True:
        cords = (input("Ваш ход: ")).split()
        if len(cords)!=2:
            print("Введите 2 координаты!!")
            continue
        x,y=cords

        if not(x.isdigit()) or not (y.isdigit()):
            print("Введите числа!")
            continue

        x,y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона!")
            continue

        if field [x] [y] !=" ":
            print("Клетка занята!")
            continue
        return x,y
def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field [i] [j])
        if symbols == ["Х","Х","Х"]:
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field [j] [i])
        if symbols == ["Х","Х","Х"]:
            return True

        symbols = []
        for i in range(3):
            symbols.append(field [i] [i])
        if symbols == ["Х","Х","Х"]:
            return True

        symbols = []
        for i in range(3):
            symbols.append(field [i] [2-i])
        if symbols == ["Х","Х","Х"]:
            return True
        return False
#Игровой процес
num = 0
while True:
    num+=1

    playing_field()

    if num % 2 ==1:
        print("Ходит Х")
    else:
        print("Ходит 0")
    x,y=ask()

    if num % 2 ==1:
        field [x] [y] = "X"
    else:
        field [x] [y] = "0"

    if check_win():
        break

    if num ==9:
        print("Ничья")
        break
        
#Проверка победы
