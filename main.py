import random
#CNP= S AA LL ZZ JJ NNN
def CNP():
    Lista_S = [1, 2, 5, 6]
    S = random.choice(Lista_S)
    if (S == 5 or S == 6):
        AA = random.randint(0, 21)
    else:
        AA = random.randint(0, 99)
    LL = random.randint(1, 12)
    if (LL == 2):
        ZZ = random.randint(1, 28)
    else:
        if (LL % 2 == 0 and LL > 2):
            ZZ = random.randint(1, 30)
        else:
            ZZ = random.randint(1, 31)
    JJ = random.randint(1, 52)
    NNN = random.randint(1, 999)
    Const = 279146358279
    C = ((S * 2) + ((AA // 10) * 7) + ((AA % 10) * 9) + ((LL // 10) * 1) + ((LL % 10) * 4) + ((ZZ // 10) * 6) + ((ZZ % 10) * 3) + ((JJ // 10) * 5) + ((JJ % 10) * 8) + ((NNN // 100) * 2) + ((NNN // 10) * 7)+ ((NNN % 10) * 9)) % 11
    if (C == 10):
        C = 1
    cnp = str(S) + str(AA).zfill(2) + str(LL).zfill(2) + str(ZZ).zfill(2) + str(JJ).zfill(2) + str(NNN).zfill(3) + str(C)
    return cnp
if __name__ == "__main__":
    NumeF = [' Ana' , ' Stefania' , ' Beatrice' , ' Claudia' , ' Maria' , ' Sophia' , ' Emma' , ' Isabella' , ' Olivia' , ' Ava' ,' Giulia' , ' Martina' , ' Giorgia' , ' Sara' , ' Aurora' , ' Alice' , ' Amelia' , ' Jessica' , ' Sophia' , ' Melisa' ,' Alexandra' ]
    NumeM = [' Alesio' , ' Albert' , ' Arthur' , ' Andy' , ' Carol' , ' Cosmin' , ' Oliver' , ' David' , ' Darius' , ' Felix' , ' Eric' ,' Iustin' , ' Edward' , ' Luca' , ' Louis' , ' Martin' , ' Matei' , ' Rares' , ' Tudor' , ' Victor' , ' Sebastian' ,' Vladimir' , ' Boris' , ' Carol' ]
    NumeFam = [' Popescu' , ' Ionescu' , ' Popa' , ' Pop' , ' Stan' , ' Constantinescu' , ' Stanciu' , ' Dumitrescu' , ' Dima' ,' Gheorghiu' , ' Barbu' , ' Nistor' , ' Florea' , ' Dinu' , ' Dinescu' , ' Georgescu' , ' Stoica' , ' Diaconu' , ' Diaconescu' , ' Mocanu' , ' Mocanu' , ' Albu' ]
    Lista_nume_cnp = []
    for numar in range(1, 1000001):
        cnp = CNP()
        if (cnp[0] == '2' or cnp[0] == '6'):
            Lista_nume_cnp.append(cnp)
            Lista_nume_cnp.append(random.choice(NumeF) + random.choice(NumeFam))
        else:
            Lista_nume_cnp.append(cnp)
            Lista_nume_cnp.append(random.choice(NumeM) + random.choice(NumeFam))
    for i in range(0, 1000):
        print(Lista_nume_cnp[i])



