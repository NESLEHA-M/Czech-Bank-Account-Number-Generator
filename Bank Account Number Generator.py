#CZ Bank Account Checker - Číslo účtu na přání


#Bank Codes
#0600 MONETA
#0300 CSOB
#0100 Komercni

bank_code="0600"
print("Vypisuji použitelná čísla účtů s kódem banky:",bank_code)

#X X X X X X X X X / X   X   X   X
#0 1 2 3 4 5 6 7 8 / 1   2   3   4

# "číslo" pro číslo na přání, "_" pro random číslo

    
for number in range(100000000, 900000000):

    number_pos=str(number)
    
    X0 ="_" #první číslo účtu
    X1 ="_"
    X2 ="_"
    X3 ="_"
    X4 ="_"
    X5 ="_"
    X6 ="_"
    X7 ="_"
    X8 ="_" #poslední číslo účtu

    if X0=="_":
        X0=number_pos[0]    
    if X1=="_":
        X1=number_pos[1]
    if X2=="_":
        X2=number_pos[2]      
    if X3=="_":
        X3=number_pos[3]
    if X4=="_":
        X4=number_pos[4]       
    if X5=="_":
        X5=number_pos[5]      
    if X6=="_":
        X6=number_pos[6]
    if X7=="_":
        X7=number_pos[7]     
    if X8=="_":
        X8=number_pos[8]

    #Modulo 11 - check s vahou různých čísel

    modulo11=number_pos[0]*3+number_pos[1]*7+number_pos[2]*9+number_pos[3]*10+number_pos[4]*5+number_pos[5]*8+number_pos[6]*4+number_pos[7]*2+number_pos[8]*1

    Div11=int(modulo11)
  

 
    if Div11%11==0\
       and number_pos[0]==X0\
       and number_pos[1]==X1\
       and number_pos[2]==X2\
       and number_pos[3]==X3\
       and number_pos[4]==X4\
       and number_pos[5]==X5\
       and number_pos[6]==X6\
       and number_pos[7]==X7\
       and number_pos[8]==X8:
        print(number,bank_code)
