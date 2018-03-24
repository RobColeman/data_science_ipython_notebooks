import sys



def main(args):
	""" Skeleton of python app"""
	if len(args) < 1:
		print("Inpute filepath required")
		return 1
	if len(args) < 2:
		print("Output filepath required")
		return 1
	input_file = open(args[0], 'r')
	output_path = args[1]

	word_count = {}
	stop_chars = ['.',',',';',':']
	for line in input_file.readlines():
		line = line.replace('\n', '').replace('\t',' ')

		if len(line) < 1:
			continue

		for word in line.split(' '):
			for ch in stop_chars:
				word = word.replace(ch,'') # regex is faster here

			if not word in word_count:
				word_count[word] = 1
			else:
				word_count[word] += 1

	input_file.close()

	if len(word_count) < 1:
		print("No words found")
		output_file = open(output_path, 'w')
		output_file.close()
		return 0

	output_file = open(output_path, 'w')
	word_count = sorted(word_count.items())
	for word, count in word_count[:-1]:
		output_file.write("{}\t{}\n".format(word, count))
	# last line
	output_file.write("{}\t{}".format(word_count[-1][0], word_count[-1][1]))

	output_file.close()

	return 0
	

if __name__ == "__main__":
	""" >python run.py <input_file> <output_path> """
	main(sys.argv[1:])