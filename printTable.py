#! python3
# From chapter 6 of ATBS

def printtable(data):
	colWidths = [0] * len(data)

	for line in range(len(data)):
		for value in range(len(data[line])):
			if (len(data[line][value]) >= colWidths[line]):
				colWidths[line] = len(data[line][value])
			else:
				continue
	for i in range(len(data[0])):
		for j in range(len(data)):
				print((data[j][i]).rjust(colWidths[j]), end=' ')
		print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printtable(tableData)

