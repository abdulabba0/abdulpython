# from statModel import a, mean, median, mode
# from statModel import mean
# import statModel
# importing children in the model as an alias
# from statModel import mean as m
#import model as an alias
import statModel as stat

me = stat.mean([8,9,9,9])

print(dir(stat))
print(me.__doc__)