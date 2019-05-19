def get_num2text:

	for index, row in data.iterrows():
		aux = []
		for w in row['text_process'].split(' '):
			try:
				num_name = num2words(float(w), lang='es')
				aux.append(num_name)
			except:
				aux.append(w)
		print(' '.join(aux))
		print('uwu' * 30)