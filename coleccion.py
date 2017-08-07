entrada1 = raw_input()
linea = entrada1.split(' ')
cantA = linea[0]
cantS = linea[1]
precioS = linea[2]
entrada2  = raw_input()

valoresCartas = entrada2.split(' ')
listSobre = []
for i in range(int(cantS)):
	sobre = []
	s = raw_input()
	sobre = s.split(' ')
	listSobre.append(sobre)
print listSobre
print listSobre.__sizeof__()
album = []
album.append(listSobre[0][0])
resg =  []
pare = []
pare.append(0)
pare.append(listSobre[0][0])
resg.append(pare)

for i in range(int(cantS)):
	for j in  range(5):
		if album.__contains__(listSobre[i][j]):
			continue
		else:
			album.append(listSobre[i][j])
			par = []
			par.append(i)
			par.append(listSobre[i][j])
			resg.append(par)

print album
print album.__sizeof__()
print resg
preTotal = int(cantS)*int(precioS)
pre2Total = 0
for i in range(int(cantA)):
	pre2Total = pre2Total + int(valoresCartas[i])

print preTotal
print pre2Total

