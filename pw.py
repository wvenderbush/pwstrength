#Winston Venderbush
#Constantine Athanitis
import math

def pwCheck(password):
	pwlist = list(password)
	lowers = [ x for x in pwlist if x.islower() ]
	uppers = [ x for x in pwlist if x.isupper() ]
	numbers = [x for x in pwlist if x.isdigit() ]
	if (len(lowers) > 0 and len(uppers) > 0 and len(numbers) > 0):
		return True
	return False


#print(pwCheck("hellothere"))
#print(pwCheck("Winston1"))

def rRestrict(n, minN, maxN):
	return max(min(maxN, n), minN)


def pwStrength(password):
	symlist = ". ? ! & $ # , ; : - _ *".split()
	pwlist = list(password)
	lowers = [ x for x in pwlist if x.islower() ]
	uppers = [ x for x in pwlist if x.isupper() ]
	numbers = [x for x in pwlist if x.isdigit() ]
	symbols = [x for x in pwlist if x in symlist ]
	strength = math.sqrt((math.fabs((len(lowers) - len(uppers) + len(numbers) - len(symbols)))  *  math.fabs((len(lowers) + len(uppers) - len(numbers) + len(symbols))) * 4) * len(symbols) * len(lowers) * len(uppers) * len(numbers))
	rating = round(rRestrict(math.sqrt(strength), 0, 10))
	return rating


#print(pwStrength("Winston12#*"))
#print(pwStrength("W1nston*"))
#print(pwStrength("winston12#*"))



