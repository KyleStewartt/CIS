lastname = input("Enter player's last name: ")
hits = float(input("Enter number of hits: "))
atbats = float(input("Enter number of at bats: "))

def battingAverage(hits, atbats):
    return hits/atbats
    
print(f"Last Name: {lastname}")
print(f"Batting Average: {battingAverage(hits,atbats):.3f}")

