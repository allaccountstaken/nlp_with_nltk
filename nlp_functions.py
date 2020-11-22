def clean_text(text):
    """Cleans text string removing punctuation, spliting to tokens, and removing stopwords

    Args:
        text ([str]): [String, ex sentences in panda columns]

    Returns:
        [list]: [List of cleaned strings separated by comma]
    """

    text = "".join([char for char in text if char not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [word for word in tokens if word not in stopwords]
    return text
