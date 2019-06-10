import csv
import sklearn
from sklearn.model_selection import train_test_split

DATA_FILE = "../Data/data_full_simple_short_2.csv"
PROTEIN_SEQUENCE_INDEX = 1
TM_INDEX = 0

MUTATED_SYNTHETIC_DATA_FILE_NAME = "synthetic_data_mutated.csv"
TEST_DATA_FOR_SYNTHETIC_DATA = "test_synthetic_data_mutated.csv"

AMINO_ACIDS = ['A', 'G', 'V', 'C', 'P', 'L', 'I', 'M', 'W', 'F', 'K', 'R', 'H', 'S', 'T', 'Y', 'N', 'Q', 'D', 'E']


def get_data(file_name, should_split):
    """
    :param file_name: the file name to be read
    :return: the data, where the TM_INDEX gives the index of the TM and PROTEIN_SEQUENCE_INDEX gives the index of the protein
    """
    with open(file_name, encoding='utf-8-sig') as f:
        csv_reader = csv.reader(f)
        two_d_arr = []
        for row in csv_reader:
            row_in_row = []
            for v in row:
                v = v.strip()
                if len(row_in_row) == PROTEIN_SEQUENCE_INDEX:
                    row_in_row.append(str(v))
                elif len(row_in_row) == TM_INDEX:
                    row_in_row.append(float(v))
            two_d_arr.append(row_in_row)
        if should_split:
            learning_data, test_data = train_test_split(two_d_arr)
            # Write test to file
            write_data(test_data, TEST_DATA_FOR_SYNTHETIC_DATA)
            # Return train
            return learning_data
        return two_d_arr


def mutate_data(data):
    count = 0
    old_data = data.copy()
    for tm, protein in old_data:
        for i in range(len(protein)):
            orig_aa = protein[i]
            for aa in AMINO_ACIDS:
                if aa == orig_aa: continue
                new_protein = ""
                for j in range(len(protein)):
                    if j == i:
                        new_protein += aa
                        continue
                    new_protein += protein[j]
                new_piece_of_data = [tm, new_protein]
            data.append(new_piece_of_data)
        count += 1
        print(count)
    return data


def write_data(data_to_write, filename):
    with open(filename, 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(data_to_write)


if __name__ == "__main__":
    data = get_data(DATA_FILE, True)
    data = mutate_data(data)
    write_data(data, "synthetic_data_mutated.csv")
    print(data)
