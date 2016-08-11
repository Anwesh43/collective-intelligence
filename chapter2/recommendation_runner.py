import sys
from recommendations import *
from eucledian_distance_score import *
import pearson_coefficent
names = []

for key,value in critics.items():
    names.append(key)

arguments = sys.argv[1:]
if len(arguments) == 3:
    if arguments[0] == "eucledian":
        if int(arguments[1])<len(names) and int(arguments[2])<len(names):
            print "comparing between {0} and {1}".format(names[int(arguments[1])],names[int(arguments[2])])
            print 'the similarity score is {0}'.format(sim_score_between_persons(critics,names[int(arguments[1])],names[int(arguments[2])]))
        else:
            print 'enter numbers less than {0}'.format(len(names))

    if arguments[0] == "pearson":
        if int(arguments[1])<len(names) and int(arguments[2])<len(names):
            print "comparing between {0} and {1}".format(names[int(arguments[1])],names[int(arguments[2])])
            print 'the similarity score is {0}'.format(pearson_coefficent.sim_score_between_persons(critics,names[int(arguments[1])],names[int(arguments[2])]))
        else:
            print 'enter numbers less than {0}'.format(len(names))
else:
    print "enter the method by which you want to evaluate score followed by the two indexes  of name of the person between whom you want to evaluate the score"
