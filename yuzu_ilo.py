
from re import fullmatch as flm
import re
import random
from string import capwords
from time import time as unix
from numpy import base_repr

random_2 = random.Random()


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


def dice_roll_2(x=1, y=6, z=0, seed=None): # XdY+Z anu XdY-Z en seed
	if int is type(x) is type(y) is type(z):
		if x < 0:
			raise ValueError('mute pi leko nanpa li nasa.')
		if y < 1:
			raise ValueError('leko nanpa li nasa.')
		if seed is not None:
			random_2.seed(seed)
		kulupu = [random_2.randint(1,y) for q in range(x)]
		return sum(kulupu,z), kulupu
	else:
		raise TypeError('nanpa ala li lon. o kepeken nanpa taso.')


def dice(open): # XdY+Z anu XdY-Z // tuple_dice en dice_roll
	ijo = tuple_dice(open)
	ijo = dice_roll(*ijo)
	return ijo[0]


def dice_2(open, seed=None): # XdY+Z anu XdY-Z en seed // tuple_dice en dice_roll_2
	ijo = tuple_dice(open)
	ijo = dice_roll_2(*ijo, seed)
	return ijo[0]



def efia_int(open=None): # unixtime
	if open is None:
		open = int(unix())
	elif type(open) is not int:
		raise TypeError('ni li nanpa ala.')
	efia = (open - 1632927600) // 86400
	return efia


def str_efia(open): # efia_int
	if type(open) is not int:
		raise TypeError('ni li nanpa ala.')
	pini = f'e{open:+05}'
	return pini


def efia(open=None): # unixtime // efia_int en str_efia
		return str_efia(efia_int(open))


def yuki_kekamu(efia=None, tuple=False): # efia_int
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



def prsk_pct_score(p, gr=0, go=0, b=0, m=0, *, p_pct=100, gr_pct=70, go_pct=50, b_pct=0, m_pct=0): # perfect-great-good-bad-miss
	if int is type(p) is type(gr) is type(go) is type(b) is type(m):
		max = (p+gr+go+b+m) * 100
		score = p * p_pct + gr * gr_pct + go * go_pct + b * b_pct + m * m_pct
		pct_score = score / max
		return pct_score
	else:
		raise TypeError('nanpa ala li lon. o kepeken nanpa taso.')


def prsk_vs_score(p, gr=0, go=0, b=0, m=0, *, vs_pct=False, p_score=3, gr_score=2, go_score=1, b_score=0, m_score=0): # perfect-great-good-bad-miss
	if int is type(p) is type(gr) is type(go) is type(b) is type(m):
		max = (p+gr+go+b+m) * p_score
		score = p * p_score + gr * gr_score + go * go_score + b * b_score + m * m_score
		minus_score = score - max
		if vs_pct == False:
			return score, minus_score
		else:
			vs_pct_score = score / max
			return score, minus_score, max, vs_pct_score
	else:
		raise TypeError('nanpa ala li lon. o kepeken nanpa taso.')


def prsk(p, gr=0, go=0, b=0, m=0, *, vs_pct=False):
	pct_score = prsk_pct_score(p, gr, go, b, m)
	vs_score = prsk_vs_score(p, gr, go, b, m, vs_pct=vs_pct)
	return pct_score, *vs_score



def list_int_kebab(open):
	if type(open) is not str:
		raise TypeError('ni li sitelen ala.')
	if flm(r'[0-9\-]+', open):
		ijo = open.split('-')
		pini = [int(q) for q in ijo]
		return pini
	else:
		raise ValueError('sitelen ni li ike.')


def str_pct(open):
	if type(open) is not float:
		raise TypeError('ni li nasin nanpa lili ala.')
	pini = f'{open:.4%}'
	return pini


def pascal_sneke(open): # Capitalized_Words_With_Underscores
	if type(open) is not str:
		raise TypeError('ni li sitelen ala.')
	ijo = capwords(open)
	ijo = ijo.replace(' ','_')
	return ijo


def base_convert(open, base=2, *, open_base=None, pini_namako=None):
	if type(open) is not str:
		raise TypeError('ni pi sitelen nanpa li sitelen ala.')
	if type(base) is not int:
		raise TypeError('ni pi nasin nanpa li nanpa ala.')
	if 1 < base < 37:
		ijo = open.upper()
		if re.search(r'^[\+\-]',ijo):
			pini_namako = re.search(r'^[\+\-]',ijo).group()
			ijo = re.sub(r'^[\+\-]','',ijo)
		if open_base is not None:
			nanpa = int(open, base=open_base)
		elif flm(r'[0-9_]+',ijo):
			nanpa = int(ijo)
		elif flm(r'(0[BOX])[0-9A-F_]+',ijo):
			nanpa = int(ijo, 0)
		elif flm(r'[0-9]+:[0-9A-Z_]*', ijo):
			open_base = int(re.search(r'^[0-9]+',ijo).group())
			if 1 < open_base < 37:
				ijo = re.sub(r'^[0-9]+:','',ijo)
				nanpa = int(ijo, open_base)
			else:
				raise ValueError('nasin nanpa pi sitelen ni li ike.')
		else:
			raise ValueError('sitelen ni li ike.')
		pini = base_repr(nanpa, base)
		if pini_namako:
			pini = pini_namako + pini
		return pini
	else:
		raise ValueError('nasin nanpa ni li ike')

























