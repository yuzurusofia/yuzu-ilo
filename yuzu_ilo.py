
from re import fullmatch as flm
import re
import random
from time import time as unix


# ale li 42.


def tuple_dice(open, *, x=1, y=6, z=0): # XdY+Z anu XdY-Z // tuple dice notation
	if type(open) is not str:
		raise TypeError('ni li sitelen ala.')
	if flm(r'[0-9]*d?([0-9]*|%)[\+\-]?[0-9]*',open):
		if re.search(r'[-\+][0-9]+$',open):
			z = int(re.search(r'[-\+][0-9]+$',open).group())
			open = re.sub(r'[-\+][0-9]+$','',open)
		if re.search(r'[0-9]+d',open):
			x = int(re.search(r'[0-9]+d',open).group()[:-1])
			open = re.sub(r'[0-9]+d','',open)
		if re.search(r'[0-9]+',open):
			y = int(re.search(r'[0-9]+',open).group())
		if re.search(r'%',open):
			y = 100
		return x, y, z
	else:
		raise ValueError('sitelen ni li ike. o kepeken XdY+Z anu XdY-Z. (X en Y en Z li nanpa.)')


def dice_roll(x=1, y=6, z=0): # XdY+Z anu XdY-Z
	if int is type(x) is type(y) is type(z):
		if x < 0:
			raise ValueError('mute pi leko nanpa li nasa.')
		if y < 1:
			raise ValueError('leko nanpa li nasa.')
		kulupu = [random.randint(1,y) for q in range(x)]
		return sum(kulupu,z), kulupu
	else:
		raise TypeError('nanpa ala li lon. o kepeken nanpa taso.')


def dice(open): # XdY+Z anu XdY-Z // tuple_dice en dice_roll
	ijo = tuple_dice(open)
	ijo = dice_roll(*ijo)
	return ijo[0]



def efia_int(open=None): # unixtime
	if open is None:
		open = int(unix())
	elif type(open) is not int and open:
		raise TypeError('ni li nanpa ala.')
		open = int(unix())
	efia = (open - 1632927600) // 86400
	return efia


def str_efia(open): # efia_int
	if type(open) is not int:
		raise TypeError('ni li nanpa ala.')
	if open < 0:
		pini = 'e-' + str(open)[1:].zfill(4)
		return pini
	else:
		pini = 'e+' + str(open).zfill(4)
		return pini


def efia(open=None): # unixtime // efia_int en str_efia
	if open is None:
		pini = str_efia(efia_int())
		return pini
	else:
		pini = str_efia(efia_int(open))
		return pini


def yuki_kekamu(efia=None, tuple=False): # efia
	if efia is None:
		 efia = efia_int()
	elif type(efia) is not int:
		raise TypeError('ni li nanpa ala.')
		
	ijo = efia + 7883
	A = ijo // 146097
	B = ijo % 146097
	C = B // 36524
	D = B % 36524
	E = D // 1461
	F = D % 1461
	G = F // 365
	H = F % 365
	I = H // 91
	J = H % 91
	K = J // 30
	L = J % 30
	
	ipa = A * 400 + C * 100 + E * 4 + G + 1
	rosa = I * 3 + K + 1
	neka = L + 1
	
	if J == 90:
		neka = 31
		rosa = rosa - 1
	if F == 1460:
		neka = 2
		rosa = 13
		ipa = ipa - 1
	
	if tuple == False:
		pini = str(ipa) + 'i:' + str(rosa) + 'r:' + str(neka) + 'n'
	else:
		pini = (ipa, rosa, neka)
	return pini







