import os


PARENT_FOLDER = r'/Users/parsa/Daneshgah/Arshad/2/NLP/Ponzi'
DATA_FOLDER  = os.path.join(PARENT_FOLDER, 'data')

unigram_path = os.path.join(DATA_FOLDER, 'unigrams.csv')
vocab_path = os.path.join(DATA_FOLDER, 'vocab.txt')

train_specifier = os.path.join
test_specifier = os.path.join

train_list = get_urls_from_file(train_specifier)
test_list = get_urls_from_file(test_specifier)

for url in train_list:
    extract_text_from_url(url, save_path)

create_vocab_file(vocab_path, unigram_path)