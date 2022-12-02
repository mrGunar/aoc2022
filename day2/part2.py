with open("day2/input.txt") as f:
    data = [x.rstrip("\n") for x in f.readlines()]
# XA for Rock 1, YB for Paper 2, and ZC for Scissors 3.
# X lose, Y draw, and Z means you need to win. Good luck!"

results = {
    "A X":0+3,
    "A Y":3+1,
    "A Z":6+2,
    "B X":0+1,
    "B Y":3+2,
    "B Z":6+3,
    "C X":0+2,
    "C Y":3+3,
    "C Z":6+1,
}
    
sum = 0
for el in data:
    sum += results[el]
print(sum)