import csv
import matplotlib.pyplot as plt
import numpy as np
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews


def extract_features(word_list):
    return dict([(word, True) for word in word_list])


if __name__ == '__main__':
    # 输入训练集
    positive_fileids = movie_reviews.fileids('pos')
    negative_fileids = movie_reviews.fileids('neg')

    features_positive = [(extract_features(movie_reviews.words(fileids=[f])),
                          'Positive') for f in positive_fileids]
    features_negative = [(extract_features(movie_reviews.words(fileids=[f])),
                          'Negative') for f in negative_fileids]

    # 使用八二分，训练集为百分之八十
    threshold_factor = 0.8
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))

    features_train = features_positive[:threshold_positive] + features_negative[:threshold_negative]
    features_test = features_positive[threshold_positive:] + features_negative[threshold_negative:]
    print("\nNumber of training datapoints:", len(features_train))
    print("Number of test datapoints:", len(features_test))

    # 训练分类器
    classifier = NaiveBayesClassifier.train(features_train)
    print("\nAccuracy of the classifier:", nltk.classify.util.accuracy(classifier, features_test))

    print(")\nTop 10 most informative words:")
    for item in classifier.most_informative_features()[:10]:
        print(item[0])

    # Sample input reviews
    """input_reviews = [
        "It is an amazing movie", 
        "This is a dull movie. I would never recommend it to anyone.",
        "The cinematography is pretty great in this movie", 
        "The direction was terrible and the story was all over the place" 
    ]"""

    # Importing datetime.
    from datetime import datetime

    with open("F:/programing/Python/201602_tweets/output.csv", "r", encoding="utf-8-sig", ) as f:
        datadict = csv.DictReader(f)
        for dict1 in datadict:
            dd = datetime.strptime(dict1['TIME'], "%Y-%m-%d %H:%M:%S")
            time.append(dd)
            text.append(dict1['TEXT'])

    emotion_polarity_number = []
    time_number = []
    positive = 0
    negative = 0
    # print ("\nPredictions:")
    for review in text:
        # print("\nTime:",type(time[count]))
        # print("\nTime:", time[count])
        # print ("\nText:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
        # print ("Predicted sentiment:", pred_sentiment )
        if pred_sentiment == 'Negative':
            negative = negative + 1  # emotion_polarity_number.append(round(probdist.prob(pred_sentiment), 2)*(-1))
        else:
            positive = positive + 1
        # print ("Probability:", round(probdist.prob(pred_sentiment), 2))
        # emotion_polarity_number.append(round(probdist.prob(pred_sentiment), 2))
        count = count + 1
        print(count)
        # if count == 500: break




