def ci(s, b):
    """Возвращает истину, 
    если сумма цифр чила s равна сумме цифр числа b"""
    if sum(int(i) for i in str(s)) == sum(int(j) for j in str(b)):
        return True
    return False


for A in range(1, 300):
    for x in range(300):
        if ((x + A < 145) <= (ci(A, 71) and (A % 11 == 0))) == False:
            break
    else:
        print(A)
        break
