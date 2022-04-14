#!/usr/bin/python3
import string
from collections import Counter
# from googletrans import Translator
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk import WordNetLemmatizer, LancasterStemmer, pos_tag, sent_tokenize, word_tokenize, ngrams
from nltk.corpus import stopwords

"""
Data source: [Kaggle - Verfied NFT Tweets](https://www.kaggle.com/datasets/adanai/verified-nft-tweets?select=verified_nft_tweets.csv)

Project overview: Preprocessing of verified NFT Tweets for machine learning (ML) training data

there will be several additional nltk downloads needing to be downloaded:

import nltk
nltk.download('stopwords')
"""


def get_ngrams(documents, size):
    """
    function to build out a new data frame composed of the top 5 ngrams and their count
    :param documents:
    :param size:
    :return: pandas data frame
    """
    ngrams_all = []
    # loop through the cleaned tweets
    for document in documents:
        tokens = document.split()
        if len(tokens) <= size:
            continue
        else:
            output = list(ngrams(tokens, size))
        for ngram in output:
            ngrams_all.append(" ".join(ngram))
    # create a collections counter for counting ngram instances
    cnt_ngram = Counter()
    for word in ngrams_all:
        cnt_ngram[word] += 1
    # create new data frame
    data_frame = pd.DataFrame.from_dict(cnt_ngram, orient='index').reset_index()
    # create two columns in data frame with data (cnt_ngram and ngrams_all
    data_frame = data_frame.rename(columns={'index': 'words', 0: 'count'})
    # sort them by decending count
    data_frame = data_frame.sort_values(by='count', ascending=False)
    # delete all but the top 5 ngrams from the data frame
    data_frame = data_frame.head(5)
    return data_frame


def plot_bigrams(document):
    """
    function to plat the ngrams build by get_ngrams()
    :param document:
    :return: None
    """
    # build bigrams from get_ngrams and document
    bigrams = get_ngrams(document, 2)
    print(bigrams)
    # create the matplotlib frame
    fig = plt.figure()
    plt.subplots_adjust(wspace=.5)
    ax = fig.add_subplot()
    # pass the data to the matplotlib frame
    ax.bar(bigrams['words'], bigrams['count'], align='center', alpha=.5)
    # format matplotlib frame
    ax.set_title('Bigrams in Dataset')
    plt.xlabel('Bigrams')
    plt.ylabel('Count')
    plt.rc('xtick', labelsize=6)
    plt.rc('ytick', labelsize=8)
    # save matplotlib frame to .png
    plt.savefig('bigrams.png')
    # plt.show()


def get_word_cloud(text, type):
    """
    function to create a word cloud from cleaned tweets
    :param text:
    :param type:
    :return: None
    """
    # pass the data to the matplotlib frame
    word_cloud = WordCloud(width=1024, height=1024, margin=0).generate(text)
    # format matplotlib frame
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.imshow(word_cloud, interpolation='bilinear')
    ax.axis("off")
    ax.margins(x=0, y=0)
    # save matplotlib frame to .png
    plt.savefig(f'wordcloud_{type}.png')
    # plt.show()


def get_stop_words(tokens):
    """
    function to clean the tweets of stop words

    *** Remove googletrans because of slow api calls and daily api requests ***

    :param tokens:
    :return: stringg
    """
    # translator = Translator()
    new_words = []
    # test_lang = ' '.join(tokens)
    # api call slows program, but this is the only effective means to remove non-english text
    # dec_lan = translator.detect(test_lang)
    # if dec_lan.lang == 'en':
    for word in tokens:
        # make word lowercase to run against nltk stop words list properly
        word = word.lower()
        # attempt to drop links
        if word.startswith('//t.co/'):
            # do nothing
            continue
        else:
            if word is not None:
                # strip punctuation from word
                word = word.strip('.,?:;#!@^%$&*<>-_+=`\'\"[]{}[0-9]')
                # check if word is in nltk.corpus stopwords
                if word not in stopwords.words('english'):
                    # check if word in supplemental list
                    if word not in ['RT', 'http', 'rt', 'timestamp', '.', '[video]', 'https', 'amp']:
                        # add 'cleaned' word to list
                        new_words.append(word)
            else:
                continue
    # create string from list
    results = ' '.join(new_words)
    # return back to create_meta()
    return results


def get_lemma(tokens):
    """
    function to lemmanize the words from the tweets using WordNetLemmatizer()
    :param tokens:
    :return: get_stop_words(lemmatized_tokens)
    """
    # call class
    lemma = WordNetLemmatizer()
    lemmatized_tokens = []
    # iterate through tokens and lemmatize token and add to list
    for token in tokens:
        temp_tokens = lemma.lemmatize(token)
        lemmatized_tokens.append(temp_tokens)
    return get_stop_words(lemmatized_tokens)


def get_stems(tokens):
    """
    function to stem the words in the tweets using LancasterStemmer()
    :param tokens:
    :return: get_lemma(stemmed_tokens)
    """
    # call class
    stemmer = LancasterStemmer()
    stemmed_tokens = []
    # iterate through tokens and lemmatize token and add to list
    for token in tokens:
        for word in token:
            if word[1] == 'DT' or word[1] == 'PRP' or word[1] == 'PRP$' or word[1] == 'NN' or word[1] == 'NNP' or word[1] == 'NNPS':
                temp_tokens = word[0]
            else:
                temp_tokens = stemmer.stem(word[0])
            stemmed_tokens.append(temp_tokens)
    return get_lemma(stemmed_tokens)


def get_pos_tag(tokens):
    """
    function to tag each word in the tweets as the part of speech it was used as in the tweet
    :param tokens:
    :return: get_stems(pos_tokens)
    """
    pos_tokens = [pos_tag(token) for token in tokens]
    return get_stems(pos_tokens)


def get_tokens(document):
    """
    function to tokenize each tweet using string and NLTK tokenizer functions
    :param document:
    :return: get_pos_tag(no_punctuation_seq_tokens)
    """
    document = str(document)
    if document is not None:
        # create tokens using NLTK
        sequences = sent_tokenize(document)
        seq_tokens = [word_tokenize(sequence) for sequence in sequences]
        no_punctuation_seq_tokens = []
        # iterate throuh tokens to remove punctuation
        for seq_token in seq_tokens:
            no_punctuation_seq_tokens.append([token for token in seq_token if token not in string.punctuation])
        return get_pos_tag(no_punctuation_seq_tokens)


def get_num_words(sentence):
    """
    function to count the number of words in each tweet
    :param tweet:
    :return: int
    """
    return len(sentence.split())


def append_col(frame):
    """
    function to append the two new columns to the pandas data frame
    :param frame:
    :return: pandas data frame
    """
    word_counts = []
    for index, row in frame.iterrows():
        word_counts.append(get_num_words(row['cleaned_tweets']))
    frame['cleaned_tweets_count'] = word_counts
    return frame


def create_meta(data_frame):
    """
    function to massage the pandas data frame for processing
    :param data_frame:
    :return: None
    """
    data_frame['cleaned_tweets'] = data_frame.iloc[:, 5].apply(
        lambda x: get_tokens(x))
    data_frame = append_col(data_frame)
    get_word_cloud(' '.join(data_frame.cleaned_tweets), 'cleaned_tweets')
    plot_bigrams(data_frame.cleaned_tweets)


if __name__ == '__main__':
    """
    open and read .csv and create panda data frame
    """
    DATA = 'data.csv'
    df = pd.read_csv(DATA)
    df = df.drop_duplicates(keep='first')
    df.reset_index(inplace=True)
    create_meta(df)
