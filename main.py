
print("welcome to my first game")
name=input("what is your name")
age=int(input("what is your age!?"))
print("hello",name,"your age is:",age,"years old")
health=10
print("you are starting with:",health,"health")
if age>=18:
    print("you are old enough to play this game")
    playy=input("do you want to play this game? ").lower()
    if playy=="yes":
        print("lets play")
        choice=input("first choice ..... Left or Right (Left / Right)?").lower()
        if choice=="left":
            ans=input("nice,you follow the path and reach a lake....... do you want to swim across or go around (across/around)?").lower()
            if ans==" around":
                print("you went around and reached the other side")

            elif ans== "across":
                print("you managed to get across,but you were bit by a fish and lost 5 health")
                health-=5
            ans=input(" you notice a house and a river.which do you want to go(river/house)?").lower()
            if ans=="house":
                print("you go to the house and are greeted by the owner ..... but he doesn't like you and you lose 5 health")
                health-=5


                if health<=0:
                    print("you now have zero health and lose the game")
                else:
                    print("you survive and you won")
            else:
                print("you fell in the river and lost")

        else:
            print("You fell down and lost")

    else :
        print("see you later")

elif age>=14:
    print("you can play with supervision")
else:
    print("you are not old enough to play this game")

