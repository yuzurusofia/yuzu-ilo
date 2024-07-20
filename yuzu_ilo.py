
from re import fullmatch as flm
import re
import random
import math
from string import capwords
from time import time as unix

import regex
import numpy as np

random_2 = random.Random()


# ale li 42.


def tuple_dice(open, *, x=1, y=6, z=0): # XdY+Z anu XdY-Z // tuple dice notation
	if type(open) is not str:
		raise TypeError('ni li sitelen ala.')
	m = flm(r'([0-9]+(?=d))?d?([0-9]+|%)?([+-]?[0-9]+)?',open)
	if m is None:
		raise ValueError('sitelen ni li ike. o kepeken XdY+Z anu XdY-Z. (X en Y en Z li nanpa.)')
	tmp_x, tmp_y, tmp_z = m.groups()
	if tmp_x is not None:
		x = int(tmp_x)
	if tmp_y is not None:
		if tmp_y == '%':
			y = 100
		else:
			y = int(tmp_y)
	if tmp_z is not None:
		z = int(tmp_z)
	return x, y, z


def dice_roll(x=1, y=6, z=0): # XdY+Z anu XdY-Z
	if not (int is type(x) is type(y) is type(z)):
		raise TypeError('nanpa ala li lon. o kepeken nanpa taso.')
	if x < 0:
		raise ValueError('mute pi leko nanpa li nasa.')
	if y < 1:
		raise ValueError('leko nanpa li nasa.')
	
	kulupu = [random.randint(1,y) for q in range(x)]
	return sum(kulupu,z), kulupu


def dice_roll_2(x=1, y=6, z=0, seed=None): # XdY+Z anu XdY-Z en seed
	if not (int is type(x) is type(y) is type(z)):
		raise TypeError('nanpa ala li lon. o kepeken nanpa taso.')
	if x < 0:
		raise ValueError('mute pi leko nanpa li nasa.')
	if y < 1:
		raise ValueError('leko nanpa li nasa.')
	
	if seed is not None:
		random_2.seed(seed)
	kulupu = [random_2.randint(1,y) for q in range(x)]
	return sum(kulupu,z), kulupu


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
		open = math.floor(unix())
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
		rosa -= 1
	if F == 1460:
		neka = 2
		rosa = 13
		ipa -= 1
	
	if tuple == False:
		pini = str(ipa) + 'i:' + str(rosa) + 'r:' + str(neka) + 'n'
	else:
		pini = (ipa, rosa, neka)
	return pini



# A1 B1 C1 D1
# A2 B2 C2 D2
# A3 B3 C3 D3
# A4 B4 C4 D4

def magic_square_4(A1, B1, C1, D1, *, min=0, max=None):
	if not (int is type(A1) is type(B1) is type(C1) is type(D1)):
		raise TypeError('nanpa ala li lon. o kepeken nanpa taso.')
	
	list = [A1, B1, C1, D1]
	sum = A1 + B1 + C1 + D1
	if max is None:
		max = sum - (min + 1) * 3
	nanpa = range(min, max+1)
	pini = []
	
	for A4 in nanpa:
		if A4 in list:
			continue
		list.append(A4)
		D4 = sum - (A1 + D1 + A4)
		if D4 in list or D4 not in nanpa:
			del list[-1:]
			continue
		list.append(D4)
		
		for A2 in nanpa:
			if A2 in list:
				continue
			list.append(A2)
			A3 = sum - (A1 + A2 + A4)
			if A3 in list or A3 not in nanpa:
				del list[-1:]
				continue
			list.append(A3)
			
			for B2 in nanpa:
				if B2 in list:
					continue
				list.append(B2)
				C3 = sum - (A1 + B2 + D4)
				if C3 in list or C3 not in nanpa:
					del list[-1:]
					continue
				list.append(C3)
				
				for C2 in nanpa:
					if C2 in list:
						continue
					list.append(C2)
					D2 = sum - (A2 + B2 + C2)
					if D2 in list or D2 not in nanpa:
						del list[-1:]
						continue
					list.append(D2)
					
					C4 = sum - (C1 + C2 + C3)
					if C4 in list or C4 not in nanpa:
						del list[-2:]
						continue
					list.append(C4)
					
					D3 = sum - (D1 + D2 + D4)
					if D3 in list or D3 not in nanpa:
						del list[-3:]
						continue
					list.append(D3)
					
					B3 = sum - (A3 + C3 + D3)
					if B3 in list or B3 not in nanpa:
						del list[-4:]
						continue
					list.append(B3)
					
					B4 = sum - (A4 + C4 + D4)
					if B4 in list or B4 not in nanpa:
						del list[-5:]
						continue
					list.append(B4)
					
					tmp1 = B1 + B2 + B3 + B4
					tmp2 = D1 + C2 + B3 + A4
					if sum == tmp1 == tmp2:
						tmp = [
							[A1,B1,C1,D1],
							[A2,B2,C2,D2],
							[A3,B3,C3,D3],
							[A4,B4,C4,D4],
							]
						pini.append(tmp)
					del list[-6:]
				del list[-2:]
			del list[-2:]
		del list[-2:]
	return pini


def is_square(kulupu):
	if type(kulupu) in (list, tuple):
		kulupu = np.array(kulupu)
	elif type(kulupu) is not np.ndarray:
		raise TypeError('ni li kulupu ala.')
	if kulupu.ndim != 2:
		return False
	tmp = kulupu.shape
	if tmp[0] != tmp[1]:
		return False
	return True


def is_semimagic_square(kulupu):
	if type(kulupu) in (list, tuple):
		kulupu = np.array(kulupu)
	elif type(kulupu) is not np.ndarray:
		raise TypeError('ni li kulupu ala.')
	if not is_square(kulupu):
		return False
	sum_0 = kulupu.sum(axis=0)
	if np.any(sum_0 != sum_0[0]):
		return False
	sum_1 = kulupu.sum(axis=1)
	if np.any(sum_1 != sum_0[0]):
		return False
	return True


def is_magic_square(kulupu):
	if type(kulupu) in (list, tuple):
		kulupu = np.array(kulupu)
	elif type(kulupu) is not np.ndarray:
		raise TypeError('ni li kulupu ala.')
	if not is_square(kulupu):
		return False
	sum_0 = kulupu.sum(axis=0)
	if np.any(sum_0 != sum_0[0]):
		return False
	sum_1 = kulupu.sum(axis=1)
	if np.any(sum_1 != sum_0[0]):
		return False
	sum_2 = kulupu.diagonal().sum()
	if sum_0[0] != sum_2:
		return False
	kulupu_tmp = np.flipud(kulupu)
	sum_3 = kulupu_tmp.diagonal().sum()
	if sum_0[0] != sum_3:
		return False
	return True


def is_panmagic_square(kulupu):
	if type(kulupu) in (list, tuple):
		kulupu = np.array(kulupu)
	elif type(kulupu) is not np.ndarray:
		raise TypeError('ni li kulupu ala.')
	if not is_square(kulupu):
		return False
	sum_0 = kulupu.sum(axis=0)
	if np.any(sum_0 != sum_0[0]):
		return False
	sum_1 = kulupu.sum(axis=1)
	if np.any(sum_1 != sum_0[0]):
		return False
	for q in kulupu:
		sum_2 = kulupu.diagonal().sum()
		if sum_0[0] != sum_2:
			return False
		kulupu_tmp = np.flipud(kulupu)
		sum_3 = kulupu_tmp.diagonal().sum()
		if sum_0[0] != sum_3:
			return False
		kulupu = np.roll(kulupu, (1,0), (0,1))
	return True



def is_alpha(open):
	if type(open) is not str:
		raise TypeError('ni li sitelen ala.')
	return bool(regex.fullmatch(r'(\p{Lu}|\p{Ll}|\p{Lt})+', open))


def is_alnum(open):
	if type(open) is not str:
		raise TypeError('ni li sitelen ala.')
	return bool(regex.fullmatch(r'(\p{Lu}|\p{Ll}|\p{Lt}|\p{Nd})+', open))



def prsk_pct_score(p, gr=0, go=0, b=0, m=0, *, p_pct=100, gr_pct=70, go_pct=50, b_pct=0, m_pct=0): # perfect-great-good-bad-miss
	if not (int is type(p) is type(gr) is type(go) is type(b) is type(m)):
		raise TypeError('nanpa ala li lon. o kepeken nanpa taso.')
	max = (p+gr+go+b+m) * 100
	score = p * p_pct + gr * gr_pct + go * go_pct + b * b_pct + m * m_pct
	pct_score = score / max
	return pct_score


def prsk_vs_score(p, gr=0, go=0, b=0, m=0, *, vs_pct=False, p_score=3, gr_score=2, go_score=1, b_score=0, m_score=0): # perfect-great-good-bad-miss
	if not (int is type(p) is type(gr) is type(go) is type(b) is type(m)):
		raise TypeError('nanpa ala li lon. o kepeken nanpa taso.')
	max = (p+gr+go+b+m) * p_score
	score = p * p_score + gr * gr_score + go * go_score + b * b_score + m * m_score
	minus_score = score - max
	if vs_pct == False:
		return score, minus_score
	else:
		vs_pct_score = score / max
		return score, minus_score, max, vs_pct_score


def prsk(p, gr=0, go=0, b=0, m=0, *, vs_pct=False):
	pct_score = prsk_pct_score(p, gr, go, b, m)
	vs_score = prsk_vs_score(p, gr, go, b, m, vs_pct=vs_pct)
	return pct_score, *vs_score



def list_int_kebab(open):
	if type(open) is not str:
		raise TypeError('ni li sitelen ala.')
	if not flm(r'[0-9\-]+', open):
		raise ValueError('sitelen ni li ike.')
	
	ijo = open.split('-')
	pini = [int(q) for q in ijo]
	return pini


def str_pct(open):
	if type(open) is not float:
		raise TypeError('ni li nasin nanpa lili ala.')
	pini = f'{open:.4%}'
	return pini


def pascal_snake(open): # Capitalized_Words_With_Underscores
	if type(open) is not str:
		raise TypeError('ni li sitelen ala.')
	ijo = capwords(open)
	ijo = ijo.replace(' ','_')
	return ijo


def base_convert(open, base=2, *, open_base=10, pini_namako=None):
	if type(open) is not str:
		raise TypeError('ni pi sitelen nanpa li sitelen ala.')
	if type(base) is not int:
		raise TypeError('ni pi nasin nanpa li nanpa ala.')
	if not 2 <= base <= 36:
		raise ValueError('nasin nanpa ni li ike')
	ijo = open.upper()
	tmp = flm(r'([+-])([0-9A-Z_:]+)', ijo)
	if tmp:
		pini_namako, ijo = tmp.groups()
	if flm(r'(0[BOX])[0-9A-F_]+',ijo):
		open_base = 0
	elif m := flm(r'([0-9]+):([0-9A-Z_]+)', ijo):
		tmp, ijo = m.groups()
		open_base = int(tmp)
	elif not flm(r'[0-9A-Z_]+',ijo):
		raise ValueError('sitelen ni li ike.')
	if not(2 <= open_base <= 36 or open_base == 0):
		raise ValueError('nasin nanpa pi sitelen ni li ike.')
	nanpa = int(ijo, open_base)
	pini = np.base_repr(nanpa, base)
	if pini_namako:
		pini = pini_namako + pini
	return pini

























