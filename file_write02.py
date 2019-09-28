my_letters = "Python is very funny language"
max_index = len(my_letters)
output_file = "alpha.txt"
filewriter = open(output_file, 'w')
for index_value in range (max_index):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print("Output written to file")
