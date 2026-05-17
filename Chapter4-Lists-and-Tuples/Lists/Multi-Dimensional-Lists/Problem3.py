"""
SHOWROOM MANAGEMENT SYSTEM
STEP 1 : STORE AT-LEAST 5 CARS FOR AT-LEAST 3 COMPANIES IN MULTI-DIMENSIONAL LIST.
STEP 2 : CREATE A MENU FOR THE USER AND ASK FOR SELL OR BUY THE CAR.
         MENU :
               1. BUY
               2. SELL
               0. EXIT
              ENTER YOUR SELECTION :
STEP 3 : FOR BUY OPTION SHOW USER ANOTHER MENU FOR THE CAR COMPANIES.
        MENU:
             1. TOYOTA
             2. SUZUKI
             ENTER YOUR SELECTION :
STEP 4 : IF THE USER SELECTS THE COMPANY THAN SHOW THEM ALL CARS THAT ARE AVAILABLE FOR SELL ON YOUR SHOWROOM.
        MENU:
             1. COROLLA
             2. YARIS
             ENTER YOUR SELECTION :
STEP 5 : IF THE USER SELECTS ANY CAR SHOW THEM ALL DETAILS ABOUT THAT CAR AND THANKS FOR SHOPPING MESSAGE.
"""

data = [
    [
        ["TOYOTA","COROLLA","XLI","2026",6100000],
        ["TOYOTA","COROLLA","GLI","2026",6700000],
        ["TOYOTA","FORTUNER","SIGMA 4","2024",20200000],
        ["TOYOTA","YARIS","ATIV X","2023",6500000],
        ["TOYOTA","HILUX","REVO V","2022",14200000],
    ],
    [
        ["HONDA","CIVIC","ORIEL","2026",9000000],
        ["HONDA","CIVIC","RS TURBO","2025",9800000],
        ["HONDA","CITY","ASPIRE","2024",6200000],
        ["HONDA","BR-V","i-VTEC S","2023",6700000],
        ["HONDA","ACCORD","1.5L TURBO","2022",20000000],
    ],
    [
        ["KIA","SPORTAGE","ALPHA","2026",7300000],
        ["KIA","SPORTAGE","AWD","2025",8470000],
        ["KIA","PICANTO","AT","2024",4090000],
        ["KIA","STONIC","EX","2023",4862000],
        ["KIA","SORENTO","2.4 FWD","2022",8999000],
    ],
]

print("*"*10,"MENU","*"*10)
selection = int(input("1. BUY\n2. SELL\n0. EXIT\nENTER YOUR SELECTION : "))
if (selection == 1):
    print("*"*10,"MENU","*"*10)
    for i in range(len(data)):
        print( (i+1), ". ", data[i][0][0],sep="")
    selection = int(input("ENTER YOUR SELECTION : "))
    if (selection > 0 and selection <= len(data)):
        company = data[selection-1]
        print("*"*10,"MENU","*"*10)
        for i in range(len(company)):
            print( (i+1), ". ", company[i][1], " ", company[i][2], sep="")
        selection2 = int(input("ENTER YOUR SELECTION : "))
        if (selection2 > 0 and selection2 <= len(company)):
            car = company[selection2-1]
            print("CAR COMPANY :",car[0])
            print("CAR NAME :",car[1])
            print("CAR MODEL :",car[2])
            print("CAR MODEL YEAR :",car[3])
            print("CAR PRICE :",car[4])
            print("THANKS FOR BUYING SIR...")
        else:
            print("WRONG SELECTION")
    else:
        print("WRONG SELECTION")

elif (selection == 2):
    pass
elif (selection == 0):
    print("THANKS FOR VISITING")
    exit(0)
else:
    print("WRONG SELECTION")
