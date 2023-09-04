while True:
    flag = 0
    x, y, z = map(int, input().split())

    if x == 0 and y == 0 and z == 0:
        break

    if x*x + y*y == z*z:
        flag = 1
    elif x*x + z*z == y*y:
        flag = 1
    elif y*y + z*z == x*x:
        flag = 1

    if flag == 0:
        print("wrong")
    else:
        print("right")