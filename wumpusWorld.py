from itertools import product

###
# Wumpus World Problem
# Suppose the agent has progressed to the point shown in Figure 7.4(a), 
# having perceived nothing in [1,1], a breeze in [2,1], and a stench in 
# [1,2], and is now concerned with the contents of [1,3], [2,2], and [3,1]. 
# Each of these can contain a pit, and at most one can contain a wumpus. 
# Following the example of Figure 7.5, construct the set of possible worlds. 
# (You should find 32 of them.) Mark the worlds in which the KB is true and 
# those in which each of the following sentences is true:
# α2 = “There is no pit in [2,2].” 
# α3 = “There is a wumpus in [1,3].” 
# Hence show that KB⊨α2 and KB⊨α3
###

# wumpus might be in 1,3, 2,2, 3,1, or nowhere (not valid but still include).
# we know [1,1] is safe, so not possible include
whereCouldTheWumpusBe = ["1,3", "2,2", "3,1", "No Wumpus"]

# generate all possible combinations of pits with 3 squares
pitCombinations = list(product(["No Pit", "Pit"], repeat=3))

# If valid world by the Knowledge Base
def isValidWorldByKB(pit13, pit22, pit31, wumpusLocation):
    # Mapping of square to pit presence
    world = {
        "1,3": pit13,
        "2,2": pit22,
        "3,1": pit31,
        "Wumpus": wumpusLocation
    }
    
    # Breeze in [2,1] implies at least one pit in [1,1], [3,1], or [2,2]
    # if there is no pit then the world is invalid
    if world["3,1"] != "Pit" and world["2,2"] != "Pit":
        return False
    
    # Stench in [1,2] implies Wumpus in [1,3] or [2,2] or [1,1]
    # no wumpus in [1,3] or [2,2] is invalid world
    if world["Wumpus"] not in ["1,3", "2,2"]:
        return False
    
    return True

# List all possible worlds. There should be 32
allWorlds = []
for pits in pitCombinations:
    for wumpusLocation in whereCouldTheWumpusBe:
        world = {
            "1,3": pits[0],
            "2,2": pits[1],
            "3,1": pits[2],
            "Wumpus": wumpusLocation,
            "Valid": isValidWorldByKB(pits[0], pits[1], pits[2], wumpusLocation)
        }
        allWorlds.append(world)

# Print all possible worlds
print("All Possible Worlds:")
for i, world in enumerate(allWorlds):
    print(f"World {i+1}: {world}")

# Filter and print valid worlds based on KB
validWorlds = [world for world in allWorlds if world["Valid"]]
print("\nValid Worlds (according to KB):")
for i, world in enumerate(validWorlds):
    print(f"World {i+1}: {world}")

print(f"\nTotal valid worlds: {len(validWorlds)}")

# Further check all possible worlds for α2 and α3
# α2 = “There is no pit in [2,2].” 
# α3 = “There is a wumpus in [1,3].” 
alpha2Valid = [world for world in allWorlds if world["2,2"] == "No Pit"]
alpha3Valid = [world for world in allWorlds if world["Wumpus"] == "1,3"]

print("\nWorlds where α2 (No pit in [2,2]) is true:")
for i, world in enumerate(alpha2Valid):
    print(f"World {i+1}: {world}")

print("\nWorlds where α3 (Wumpus in [1,3]) is true:")
for i, world in enumerate(alpha3Valid):
    print(f"World {i+1}: {world}")
