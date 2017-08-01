global pareja #cantidad de parejas
m = [] #una lista mujeres
h = [] # una lista de hombres

pareja = input()

z = raw_input()
h = z.split(' ')
z = raw_input()
m = z.split(' ') 

m = sorted(m, reverse = True)
h = sorted(h, reverse = True)
apMujer = 0
for i in range(len(m)):
	if h[0] >= m[i]:
		apMujer = i
		break
k= 0
for j in range(apMujer, len(m)):
	print str(h[k])+" "+str(m[j])
	k = k + 1


