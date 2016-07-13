#to reset a value in scale1 to the proportional value in scale2
#from sc1 to sc2
#sc1min === sc2min, and sc1max ===sc2max

def scaleLinear(val, sc1min,sc1max,sc2min,sc2max):
	scaledval = ((sc2max-sc2min)*(val-sc1min))/(sc1max-sc1min)+sc2min
	return scaledval