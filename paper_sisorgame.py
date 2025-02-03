import random as  rm
l1=["rock","scissor","paper"]
while True:
    ccount=0
    ucount=0
    usr_choice=int(input('''Game start
1 play
2 exit'''))
 
    if usr_choice==1:
        for a in range(1,6):
           usr_input=int(input('''
1 Rock 
2 Scissor
3 Paper '''))

        if usr_input==1:
            uc="Rock"
        elif usr_input==2:
            uc="Scissor"
        elif usr_input==3:
            uc="Paper"
        machine=rm.choice(l1)
        if machine==uc:
            print("computer values",machine)
            print("user value",uc)
            print("Game over")
            ucount=ucount+1
            ccount=ccount+1
        elif(uc=="Rock" and machine=="Scissor")or (uc=="Paper" and machine=="Rock") or (uc=="Scissor" and machine=="Paper"):
            print("computer value",machine)
            print("user value",uc)
            print("you win")
            ucount=ucount+1
        else:
            print("computer value",machine)
            print("usr choice",uc)
            print("computer win")
            cccount=ccount+1



