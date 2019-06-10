from nltk.tokenize import RegexpTokenizer
# from gensim import corpora, models
# import gensim
import csv

tokenizer = RegexpTokenizer(' ')
TEST_DATA_SET = []

def get_lda_data(two_d_arr):
    texts = []
    for i in two_d_arr:
        amino_acid = i.upper()
        tokens = tokenizer.tokenize(amino_acid)
        texts.append(tokens)

    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=20)


def get_data(file_name):
    with open(file_name) as f:
        csv_reader = csv.reader(f)
        two_d_arr = []
        for row in csv_reader:
            row_in_row = []
            for v in row:
                row_in_row.append(float(v))
            two_d_arr.append(row_in_row)
        return two_d_arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(arr[int(len(arr) / 5):])
    print(arr[:int(len(arr) / 5)])
    # break
    # data = get_data('data/full_data.csv')
    # # Add to topics in dictionary
    # # Then get topics
    # # If you get similar topics for test set, choose that
    # print(len(data))
    # print(data)