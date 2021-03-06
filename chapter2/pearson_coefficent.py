from math import *
def sim_score_between_persons(data,person1,person2):
    similar_items = []
    for item,value in data[person1].items():
        if item in data[person2]:
            similar_items.append(item)
    sum1 = sum([data[person1][item] for item in similar_items])
    sum2 = sum([data[person2][item] for item in similar_items])
    sum1Sq = sum([pow(data[person1][item],2) for item in similar_items])
    sum2Sq = sum([pow(data[person2][item],2) for item in similar_items])
    psum = sum([data[person2][item]*data[person1][item] for item in similar_items])
    n = len(similar_items)
    num = psum - (sum1*sum2)/n
    den = sqrt(sum1Sq- pow(sum1,2)/n)*sqrt(sum2Sq -pow(sum2,2)/n)
    return num/den

def pearson_score(itemDictionary1,itemDictionary2):
    similar_items = []
    for item,value in itemDictionary1.items():
        if(item in itemDictionary2):
            similar_items.append(item)
    sum1 = sum([itemDictionary1[item] for item in similar_items])
    sum2 = sum([itemDictionary2[item] for item in similar_items])
    sum1Sq = sum([pow(itemDictionary1[item],2) for item in similar_items])
    sum2Sq = sum([pow(itemDictionary2[item],2) for item in similar_items])
    psum = sum(itemDictionary1[item]*itemDictionary2[item] for item in similar_items)
    n = len(similar_items)
    num = psum-(sum1*sum2)/n
    dem = (sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n)
    return num/dem
