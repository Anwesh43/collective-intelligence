from recommendations import critics
from pearson_coefficent import pearson_score

def getSimilarPeople(data,person,n = 3):
    similarties = []
    similartiesMap = {}
    for other,value in data.items():
        similarties.append(pearson_score(person,data[other]))
        similartiesMap[pearson_score(person,data[other])] = other
    similarties.sort()
    similarties.reverse()
    print similarties
    topSimilarties = similarties[0:n]
    similarTopItemsMap = {}
    for similarity in topSimilarties:
        similarTopItemsMap[similartiesMap[similarity]] = similarity
    return similarTopItemsMap
def recommendMovies(data,person):
    similarItemsMap = getSimilarPeople(data,person)
    totalMap = {}
    simSumMap = {}
    for name,similarity in similarItemsMap.items():
        for item,value in data[name].items():
            if not(item in person):
                if item not in totalMap:
                    totalMap[item] = 0
                    simSumMap[item] = 0
                totalMap[item] += value*similarity
                simSumMap[item] += similarity

    recomendations = []
    recommendMap = {}
    for item,total in totalMap.items():
        recomendations.append(total/simSumMap[item])
        recommendMap[total/simSumMap[item]] = item
    recomendations.sort()
    recomendations.reverse()
    print recomendations[0]
    return recommendMap[recomendations[0]]



print recommendMovies(critics,{'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0,'You, Me and Dupree': 2.0})
