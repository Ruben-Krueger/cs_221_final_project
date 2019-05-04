import csv
import re

PDB_NAME_INDEX = 1
TM_INDEX = 3
PH_INDEX = 6
PROTEIN_NAME_INDEX = 7
SPECIES_NAME_INDEX = 8
SPECIES_BODY_ENV = 9

INDICES_ORDER = [PDB_NAME_INDEX, PROTEIN_NAME_INDEX, PH_INDEX, SPECIES_NAME_INDEX, SPECIES_BODY_ENV, TM_INDEX]


# The main method
def main():
	data = loadCsvData('222Data.csv')
	printData(data)
	writeData(data)

# Reads a files
def loadCsvData(fileName):
	matrix = []
	# open a file
	with open(fileName) as f:
		reader = csv.reader(f)

		# loop over each row in the file
		for row in reader:

			if len(row) > 0:
				extractedData = re.split("\s{2,}", row[0])
				# extractedData = row[0].split()
				if len(extractedData) > 1:

					if extractedData[1] == 'x':
						# store the row into our matrix
						newRow = []
						for i in INDICES_ORDER:
							newRow.append(extractedData[i + 1])
						matrix.append(newRow)
					else:
						# store the row into our matrix
						newRow = []
						for i in INDICES_ORDER:
							newRow.append(extractedData[i])
						matrix.append(newRow)
	print(len(matrix))
	return matrix


# Prints out a 2d array
def printData(matrix):
	for row in matrix:
		print(row)


def writeData(matrix):
	with open('people.csv', 'w') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerows(matrix)

# This if statement passes if this
# was the file that was executed
if __name__ == '__main__':
	main()