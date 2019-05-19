# Imports
import separasilabas
import re

def count_syllables(word):

	word = re.sub(r'\W+', '', word)
	syllables = separasilabas.silabizer()
	
	return(len(syllables(word)))

def count_all_syllables(text):

	syllables = [ count_syllables(w) for w in text ]

	return(syllables)

def get_sentences(text):

	sentence_end = re.compile('[.:;!?\)\()]')
	sentences = sentence_end.split(text)
	sentences = list(filter(None, sentences))
	
	return(sentences)

def flesch_szigriszt_index(P, S, F):

	FS_index = (206.835) - (62.3)*(S/P) - (P/F)

	return(FS_index)

def fernandez_huerda_readability(mean_P, mean_F):

	FH_read = 206.84 - (0.6)*(mean_P) - (1.02)*(mean_F)

	return(FH_read)

def gutierres_polini_comprehension(L, P, F):

	GP_com = 95.2 - ((9.7 * L) / P) - ((0.35 * P) / F)

	return(GP_com)

def munoz_munoz_read(n, x_hat, variance):

	mu = (n / (n - 1)) * (x_hat / variance) * (100)

	return(mu)

def crawford_age(OP, SP):

	A = (-0.205) * (OP) + (0.049)*(SP) - 3.407

	return(A)