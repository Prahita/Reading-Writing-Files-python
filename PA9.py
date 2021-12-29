import operator
# Function to read text file and return a string
def read_file(filename): # takes in a file name, in this case hp.txt
	all_lines = '' # set empty string so we can add text to it
	with open(filename, 'r') as File: # create a variable that opens and reads hp.txt
		line_split = File.read().split('\n') # split the string by every newline to seperate lines of text
		for line in line_split: # for each line while the computer reads the text file and splits it by \n
			all_lines += line # we add every line split at a newline \n to the string
		File.close() # close this file
	return all_lines # we return the string

# Function to create a dictionary of word counts
def build_dictionary(text):
	text_clean = " " # we create an empty string
	text = text.upper() # we set our words to be all one case so we don't double count a word with a different case
	for char in text:
		if char.isalpha() or char == " ":
			text_clean += char
	w = text_clean.split(" ")
	dict = {}
	for words in w:
		if words in dict:
			dict[words]+=1

		else:
			dict[words]=1
	#sort the dictionary --> this function gets turned into a list but we fix it later
	d_sorted = sorted(dict.items(), key=operator.itemgetter(1), reverse = True)


	return d_sorted

# Function to write dictionary items into text file
def write_file(dictionary, filename):
	with open(filename,'w') as f:
		for k,v in dictionary.items():
			f.write('{}:\t{}\n'.format(k,v))

#define a function to calculate perctage of times word appears and write it onto a file
def select_stop_words(dictionary, percent): # take in dictio
	# get number of elements
	num_words = len(dictionary) * (percent/100)
	# to calculate the percentage we take the total words in dictionary and multiply it by decimal percentage
	dict_numwords = {}
	counter = 0
	for k,v in dictionary.items():
		dict_numwords[k] = v
		counter += 1
		if counter > num_words:
			break
	return dict_numwords

# Function call to get complete text of the text file as a string
all_text = read_file('hp.txt')
# Function call to get a word count dictionary that takes in a string
count_dict =dict( build_dictionary(all_text))
# Function call to write stop word dictionary items into text file
write_file(count_dict,'Wordcounts.txt')
# function to call select stop words
dict_stopwords = select_stop_words(count_dict,5)
write_file(dict_stopwords,"selectstopwords.txt")
