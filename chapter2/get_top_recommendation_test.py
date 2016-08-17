from get_top_recommendations import *
from recommendations import critics
recommendationMap,recommendations = recommendSimilarItems(critics,{'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0,'You, Me and Dupree': 2.0})
recommendedMovies = []
for recommendation in recommendations:
    recommendedMovies.append(recommendationMap[recommendation])

print "the movies which we recommend is {0}".format(",".join(recommendedMovies))
