with open("day2/input.txt") as f:
    data = [x.rstrip("\n") for x in f.readlines()]
# XA for Rock, YB for Paper, and ZC for Scissors.

results = {
    "A X":3+1,
    "A Y":6+2,
    "A Z":0+3,
    "B X":0+1,
    "B Y":3+2,
    "B Z":6+3,
    "C X":6+1,
    "C Y":0+2,
    "C Z":3+3,
}
    
sum = 0
for el in data:
    sum += results[el]
print(sum)