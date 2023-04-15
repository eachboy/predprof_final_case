from turtle import *
# import serial
speed("fastest")
title('TEST 1')
setworldcoordinates (0, 0, 200, 200)
ht()
pensize(1)
for i in range(0, 41):
    color('black')
    goto(i*5, 200)
    pd()
    goto(i*5, 0)
    pu()

for i in range(0, 41):
    color('black')
    goto(200, i*5)
    pd()
    goto(0, i*5)
    pu()
pensize(5)
# uno = serial.Serial("com5", 9600)
# data = open("test.txt", "w")
# while True:
#     line = uno.readline().decode('utf-8').rstrip()
#     data.write(f'{line}\n')
#     if line == 'finish':
#         break
# data.close()
data = open("test.txt").readlines()
fin = open("final.txt", "w")
tests = []
cur_test = []
mx = []
g1 = []
g15 = []
g2 = []
g25 = []
g3 = []
g35 = []
g4 = []
g45 = []
g5 = []
g55 = []
g6 = []

for item in range(len(data)):
    if "\n" in data[item]:
        data[item] = data[item][:-1]

index = 0
cur = 0
for num in range(data.count("finish")):
    fin.write(f'Test{num+1}\n')
    mv = []
    mv_1 = []
    for item_d in range(index, len(data)):
        if data[item_d] == "finish":
            index += data.index(data[item_d]) + 1
            tests.append(cur_test)
            cur_test = []
            break
        else:
            cur_test.append(data[item_d])
            f = data[item_d].split(" ")
            x = [f[0], f[1], f[2]]
            mv_1.append(f[2])
            mv.append(x)
            x = []
            if f[3] == "1.0":
                a = [int(f[0]), int(f[1])]
                g1.append(a)
            elif f[3] == "1.5":
                a = [int(f[0]), int(f[1])]
                g15.append(a)
            elif f[3] == "2.0":
                a = [int(f[0]), int(f[1])]
                g2.append(a)
            elif f[3] == "2.5":
                a = [int(f[0]), int(f[1])]
                g25.append(a)
            elif f[3] == "3.0":
                a = [int(f[0]), int(f[1])]
                g3.append(a)
            elif f[3] == "3.5":
                a = [int(f[0]), int(f[1])]
                g35.append(a)
            elif f[3] == "4.0":
                a = [int(f[0]), int(f[1])]
                g4.append(a)
            elif f[3] == "4.5":
                a = [int(f[0]), int(f[1])]
                g45.append(a)
            elif f[3] == "5.0":
                a = [int(f[0]), int(f[1])]
                g5.append(a)
            elif f[3] == "5.5":
                a = [int(f[0]), int(f[1])]
                g55.append(a)
            elif f[3] == "6.0":
                a = [int(f[0]), int(f[1])]
                g6.append(a)
    mx = sorted(mv, key=lambda x: (x[2]))

    for i in range(len(tests[num])):
        fin.write(f'{tests[num][i]}\n')

    fin.write("Magnets found: 2\n")
    fin.write(f"Magnets XY: {mx[-1][0]} {mx[-1][1]}, {mx[-2][0]} {mx[-2][1]}\n")
   

    pencolor("#00008b") #тёмно-синий
    if len(g1)!=0:
        goto(g1[0][0], g1[0][1])
        pd()
        for i in range(1, len(g1)):
            goto(g1[i][0], g1[i][1])
        goto(g1[0][0], g1[0][1])
        pu()  

    pencolor("#0000ff") #синий_лайт
    if len(g15)!=0:
        goto(g15[0][0], g15[0][1])
        pd()
        for i in range(1, len(g15)):
            goto(g15[i][0], g15[i][1])
        goto(g15[0][0], g15[0][1])
        pu()

    pencolor("#1f75fe") #синий
    if len(g2)!=0:
        goto(g2[0][0], g2[0][1])
        pd()
        for i in range(1, len(g2)):
            goto(g2[i][0], g2[i][1])
        goto(g2[0][0], g2[0][1])
        pu()
    
    pencolor("#52a8ff") #светло-синий
    if len(g25)!=0:
        goto(g25[0][0], g25[0][1])
        pd()
        for i in range(1, len(g25)):
            goto(g25[i][0], g25[i][1])
        goto(g25[0][0], g25[0][1])
        pu()

    pencolor("#30d5c8") #бирюзовый
    if len(g3)!=0:
        goto(g3[0][0], g3[0][1])
        pd()
        for i in range(1, len(g3)):
            goto(g3[i][0], g3[i][1])
        goto(g3[0][0], g3[0][1])
        pu()

    pencolor("#99ff99") #зеленый
    if len(g35)!=0:
        goto(g35[0][0], g35[0][1])
        pd()
        for i in range(1, len(g35)):
            goto(g35[i][0], g35[i][1])
        goto(g35[0][0], g35[0][1])
        pu()

    pencolor("#ffff00") #жёлтый
    if len(g4)!=0:
        goto(g4[0][0], g4[0][1])
        pd()
        for i in range(1, len(g35)):
            goto(g4[i][0], g4[i][1])
        goto(g4[0][0], g4[0][1])
        pu()

    pencolor("#ffa500") #оранжевый
    if len(g45)!=0:
        goto(g45[0][0], g45[0][1])
        pd()
        for i in range(1, len(g35)):
            goto(g45[i][0], g45[i][1])
        goto(g45[0][0], g45[0][1])
        pu()

    pencolor("#ff4c5b") #светло-красный
    if len(g5)!=0:
        goto(g5[0][0], g5[0][1])
        pd()
        for i in range(1, len(g5)):
            goto(g5[i][0], g5[i][1])
        goto(g5[0][0], g5[0][1])
        pu()

    pencolor("#ff0000") #красный
    if len(g55)!=0:
        goto(g55[0][0], g55[0][1])
        pd()
        for i in range(1, len(g55)):
            goto(g55[i][0], g55[i][1])
        goto(g55[0][0], g55[0][1])
        pu()

    pencolor("#8b0000") #тёмно-красный
    if len(g6)!=0:
        goto(g6[0][0], g6[0][1])
        pd()
        for i in range(1, len(g6)):
            goto(g6[i][0], g6[i][1])
        goto(g6[0][0], g6[0][1])
        pu()
