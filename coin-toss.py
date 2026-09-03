import random
print("====Coin Tossing Game====")
times=int(input("How many times do you want to toss? "))
heads=0
tails=0
for i in range(times):
    coin=random.choice(["Heads,Tails"])
    print(f"Toss{i+1}:{coin}")
    if coin=="Heads":
        heads+=1
    else:
        tails+=1
print("\n====RESULTS====")
print("Heads:",heads)
print("Tails")