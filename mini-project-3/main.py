#!/usr/bin/python3
import string
from googletrans import Translator
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk import WordNetLemmatizer, LancasterStemmer, pos_tag, sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

"""
pip install google-cloud-translate

there will be several additional nltk downloads needing to be downloaded:

import nltk
nltk.download('stopwords')
"""


def plot_bigrams(total, bigrams):
    print(bigrams)
    fig = plt.figure()
    plt.subplots_adjust(wspace=.5)
    ax = fig.add_subplot()
    ax.barh(np.arange(total), total, align='center', alpha=.5)
    ax.set_title('Bigrams in Dataset')
    plt.yticks(np.arange(total), bigrams.iloc[19:28])
    plt.xlabel('Count')
    plt.savefig('bigrams.png')
    plt.plot()


def get_bigrams(train_data):
    bigram_vectorizer = CountVectorizer(analyzer='word', ngram_range=[2, 2])
    x = bigram_vectorizer.fit_transform(train_data.cleaned_tweets)
    bigram_total = bigram_vectorizer.get_feature_names_out()[:10]
    print(bigram_total)
    transformer = TfidfTransformer()
    mat = transformer.fit_transform(x)
    bigrams = pd.DataFrame(mat.todense(), index=train_data.index, columns=bigram_vectorizer.get_feature_names_out()[:10])
    train_data = pd.concat([train_data, bigrams], ignore_index=False, sort=False, axis=1, join="inner")
    plot_bigrams(len(bigram_total), train_data)
    return len(bigram_total), train_data


def get_word_cloud(text, type):
    """
    function to create a word cloud from cleaned tweets
    :param text:
    :param type:
    :return: None
    """
    word_cloud = WordCloud(width=1024, height=1024, margin=0).generate(text)
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    ax.imshow(word_cloud, interpolation='bilinear')
    ax.axis("off")
    ax.margins(x=0, y=0)
    plt.savefig(f'wordcloud_{type}.png')
    # plt.show()


def get_stop_words(tokens):
    """
    function to clean the tweets of stop words
    :param tokens:
    :return: stringg
    """
    translator = Translator()

    new_words = []
    test_lang = ' '.join(tokens)
    print(test_lang)
    # api call slows program, but this is the only effective means to remove non-english text
    dec_lan = translator.detect(test_lang)
    if dec_lan.lang == 'en':
        for word in tokens:
            # make word lowercase to run against nltk stop words list properly
            word = word.lower()
            # attempt to drop links
            if word.startswith('https //') or word.startswith('http //'):
                # do nothing
                continue
            elif word is None:
                continue
            else:
                # strip punctuation from word
                word = word.strip('.,?:;#!@^%$&*<>-_+=\'\"[]{}0123456789')
                # check if word is in nltk.corpus stopwords
                if word not in stopwords.words('english'):
                    # check if word in supplemental list
                    if word not in ['RT', 'http', 'rt', 'timestamp', '.', '[video]', 'https', 't', 'co', 'amp']:
                        # add 'cleaned' word to list
                        new_words.append(word)
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
    lemma = WordNetLemmatizer()
    lemmatized_tokens = []
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
    stemmer = LancasterStemmer()
    stemmed_tokens = []
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
    if document is not None:
        sequences = sent_tokenize(document)
        seq_tokens = [word_tokenize(sequence) for sequence in sequences]
        no_punctuation_seq_tokens = []
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
    get_bigrams(data_frame)


if __name__ == '__main__':
    DATA = 'data.csv'
    df = pd.read_csv(DATA)
    df = df.drop_duplicates(keep='first')
    df.reset_index(inplace=True)
    create_meta(df)

