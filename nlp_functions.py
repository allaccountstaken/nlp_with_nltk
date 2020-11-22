def run_imports():
    import re
    import string
    import nltk
    import pandas as pd


def clean_text(text):

    import re
    import string.punctuation
    import nltk
    from nltk.corpus import stopwords
    import pandas as pd

    stopwords = nltk.corpus.stopwords.words('english')

    text = "".join([char for char in text if char not in string.punctuation])
    tokens = re.split('\W+', text)
    tokenized_text = [word for word in tokens if word not in stopwords]
    return tokenized_text


def stemming(tokenized_text):
    """[summary]

    Args:
        tokenized_text ([type]): [description]

    Returns:
        [type]: [description]
    """

    import re
    import string
    import nltk
    import pandas as pd

    ps = nltk.PorterStemmer()

    stemmed_text = [ps.stem(word) for word in tokenized_text]
    return stemmed_text


def lemmatizing(tokenized_text):

    import re
    import string
    import nltk
    import pandas as pd
    wn = nltk.WordNetLemmatizer()

    lemmatized_text = [wn.lemmatize(word) for word in tokenized_text]
    return lemmatized_text
