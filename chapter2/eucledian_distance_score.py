from math import *
def sim_score_between_persons(data,person1,person2):
    similar_items = {}
    distances = []
    for item in data[person1]:
        if(item in data[person2]):
            similar_items[item] = 1
            distances.append(pow(data[person2][item]-data[person1][item],2))
    if(len(distances) == 1):
        return 0
    distance = sum(distances)
    return 1/(1+(distance))
