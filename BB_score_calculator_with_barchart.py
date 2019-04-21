import time

gp = int(input("How many games did you play? "))
tot_shots = 0
tot_makes = 0
for j in range(gp):
    print("Let's talk about game",j+1,".")
    if int(j) < gp:
        counter = 0
        no_shots = int(input('How many shots did you take in the game? '))
        print("You took", no_shots, "shots. Let's review them.")
        for i in range(no_shots):
            if int(i) < no_shots:
                print()
                print("Let's talk about shot #",i+1,".")
                make = input("Did you make it? Answer y or n. Be honest. ")
                if make == "y":
                    counter = counter + 1
            elif int(i) >= no_shotps:
                break
        misses = no_shots - counter
        print()
        #print("You made", counter, "out of", no_shots, "shots. That is", 100*round(counter/no_shots,2), "percent.")
        print()
        print("Game#", "\tFG", "\tFGA", " \tPCT")
        print("****", "\t**", "\t***", " \t***")
        if no_shots > 0:
            pct = round(100*(counter/no_shots),3)
            print(j+1, "\t",counter, "\t",no_shots,"\t",pct)
        else:
            print(j+1, "\t",counter, "\t",no_shots,"\t",0)    
        print()
        tot_shots = tot_shots + no_shots
        tot_makes = tot_makes + counter
    elif int(j) >= gp:
                break
if tot_shots > 0:
    tot_pct = round(100*(tot_makes/tot_shots),2)
else:
    tot_pct = 0
print()
print("Here are your summary stats.")
print()
# Wait for 5 seconds
time.sleep(1)
print('Thinking...')
print()
time.sleep(2)
print("Games", "\tFG", "\tFGA", "  \tPCT")
print("*****", "\t**", "\t***", "  \t***")
print("  ",gp, "\t",tot_makes, "\t",tot_shots,"\t",tot_pct)
print()
