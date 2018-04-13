import os


txt_file = os.path.join(os.getcwd(), 'kwayedza_data.txt')

with open(txt_file, 'r') as text_file:
	lines = text_file.read()

	new_file = os.path.join(os.getcwd(), 'kwayedza_data_clean.txt')
	cleaned_file = open(new_file, 'w+')

	for line in lines.split('.'):
		cleaned_file.write(line + ':' + '\n\n')

	cleaned_file.close()
		