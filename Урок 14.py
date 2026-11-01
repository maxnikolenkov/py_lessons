spisok1 = [100, -211, -2, 233, -614, -5, 1, 127, -187, -319]
spisok = ["А", "в", "т", "о", "м", "о", "б", "и", "л", "ь"]
print(spisok)
#print(spisok[0])
#print(spisok[1])
#print(spisok[2])
#print(spisok[3])
#print(spisok[4])
#print(spisok[5])
#print(spisok[6])
#print(spisok[7])
#print(spisok[8])
#print(spisok[9])
for i in spisok1:
    if i % 2 != 0:
        print(i)
        
if spisok1[1] % 2 == 0:
    print(spisok1[1])
if spisok1[2] % 2 == 0:
    print(spisok1[2])
if spisok1[3] % 2 == 0:
    print(spisok1[3])
if spisok1[4] % 2 == 0:
    print(spisok1[4])
if spisok1[5] % 2 == 0:
    print(spisok1[5])
if spisok1[6] % 2 == 0:
    print(spisok1[6])
if spisok1[7] % 2 == 0:
    print(spisok1[7])
if spisok1[8] % 2 == 0:
    print(spisok1[8])
if spisok1[9] % 2 == 0:
    print(spisok1[9])
counter = 0
negative = 0
for i in spisok1:
    if i > 0:
        print(f"Число {i} положительное")
        counter = counter + 1
    if i < 0:
        print(f"Число {i} отрицательное")
        negative = negative + 1
print(f"Положительных чисел: {counter}")
print(f"Отрицательных чисел: {negative}")
