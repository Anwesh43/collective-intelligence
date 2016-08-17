from recommendations import critics
from get_top_recommendations import getTopMatches
class ProductMatcher:
    def __init__(self,data):
        self.data = data
    def reverseTransform(self):
        reverseDict = {}
        for person,personRatingsMap in self.data.items():
            for item,rating in personRatingsMap.items():
                if(item not in reverseDict):
                    reverseDict[item] = {}
                reverseDict[item][person] = rating
        return reverseDict
    def getTopMatches(self,item):
        reversedDict = self.reverseTransform()
        similarItemMap = getTopMatches(reversedDict,item)
        similarItems = []
        for similarItem,similarity in similarItemMap.items():
            if(not(similarItem == item)):
                similarItems.append(similarItem)
        return similarItems
