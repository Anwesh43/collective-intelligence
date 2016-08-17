from recommendations import critics
from productMatching import ProductMatcher
movie = 'Superman Returns'
productMatcher = ProductMatcher(critics)
similarMovies = productMatcher.getTopMatches(movie)
print "movies similar to {0} is {1}".format(movie,",".join(similarMovies))
