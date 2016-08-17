from recommendations import critics
from pearson_coefficent import pearson_score

def getSimilarItems(data,person,n = 3):
    similarties = []
    similartiesMap = {}
    for other,value in data.items():
        similarties.append(pearson_score(person,data[other]))
        similartiesMap[pearson_score(person,data[other])] = other
    similarties.sort()
    similarties.reverse()
    topSimilarties = similarties[0:n]
    similarTopItemsMap = {}
    for similarity in topSimilarties:
        similarTopItemsMap[similartiesMap[similarity]] = similarity
    return similarTopItemsMap
def recommendSimilarItems(data,person,n=5):
    similarItemsMap = getSimilarItems(data,person,n)
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
    if(len(recomendations) < n):
        return (recommendMap,recomendations[0:len(recomendations)])
    return (recommendMap,recomendations[0:n])

def getTopMatches(data,itemName):
    return getSimilarItems(data,data[itemName])
