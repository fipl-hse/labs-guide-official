"""
Lab 2.

Language classification
"""


def tokenize(text: str) -> list[str] | None:
    """
    Remove punctuation, cast to lowercase, split into tokens.

    Args:
        text (str): Original text

    Returns:
        list[str] | None: A sequence of lowercase tokens with no punctuation

    In case of corrupt input arguments, None is returned
    """
    pass


def remove_stop_words(tokens: list[str], stop_words: list[str]) -> list[str] | None:
    """
    Exclude stop words from the token sequence.

    Args:
        tokens (list[str]): Original token sequence
        stop_words (list[str]): Tokens to exclude

    Returns:
        list[str] | None: Token sequence that does not include stop words

    In case of corrupt input arguments, None is returned
    """
    pass


def get_freq_dict(tokens: list) -> dict | None:
    """
    Calculate frequencies of given tokens.

    Args:
        tokens (list): A list of tokens

    Returns:
        dict | None: A dictionary with frequencies
    """
    pass


def get_language_profiles(texts_corpus: list, language_labels: list) -> dict | None:
    """
    Compute language profiles for texts and add appropriate language label for each text.

    Args:
        texts_corpus (list): A list of given texts
        language_labels (list): A list of given language labels

    Returns:
        dict | None: A dictionary of dictionaries - language profiles
    """
    pass


def get_language_features(language_profiles: dict) -> list | None:
    """
    Get all unique words from language profiles and sort them in alphabetical order.

    Args:
        language_profiles (dict): A dictionary of dictionaries - language profiles

    Returns:
        list | None: List of all unique words
    """
    pass


def get_text_vector(original_text: list, language_profiles: dict) -> list | None:
    """
    Build a vector representation of a given text using dictionary with language profiles.

    Args:
        original_text (list): Any tokenized text
        language_profiles (dict): A dictionary of dictionaries - language profiles

    Returns:
        list | None: Frequency vector
    """
    pass


def calculate_distance(
    unknown_text_vector: list[float], known_text_vector: list[float]
) -> float | None:
    """
    Calculate distance between two vectors using euclid metric.

    Args:
        unknown_text_vector (list[float]): Vector for unknown text
        known_text_vector (list[float]): Vector for known text

    Returns:
        float | None: Distance between vectors
    """
    pass


def predict_language_score(
    unknown_text_vector: list, known_text_vectors: list, language_labels: list
) -> list | None:
    """
    Predict unknown text label and its distance to the closest known text.

    Args:
        unknown_text_vector (list): Vector for unknown text
        known_text_vectors (list): A list of vectors for known texts
        language_labels (list): Language labels for each known text

    Returns:
        list | None: A list where 1st element is the predicted label
            for the unknown text, 2nd element is the minimum distance between texts
    """
    pass


def calculate_distance_manhattan(
    unknown_text_vector: list, known_text_vector: list
) -> float | None:
    """
    Calculate distance between two vectors using manhattan metric.

    Args:
        unknown_text_vector (list): Vector for unknown text
        known_text_vector (list): Vector for known text

    Returns:
        float | None: Distance between vectors
    """
    pass


def predict_language_knn(
    unknown_text_vector: list,
    known_text_vectors: list,
    language_labels: list,
    k: int = 1,
    metric: str = "manhattan",
) -> list | None:
    """
    Predict unknown text label and its distance to the closest known text.

    Use knn based algorithm and specific metric.

    Args:
        unknown_text_vector (list): Vector for unknown text
        known_text_vectors (list): A list of vectors for known texts
        language_labels (list): Language labels for each known text
        k (int): The number of neighbors to choose label from
        metric (str): Specific metric to use while calculating distance

    Returns:
        list | None: A list with a language label and the minimum distance to the nearest neighbor
    """
    pass


def get_sparse_vector(
    original_text: list[str], language_profiles: dict[str, dict[str, float]]
) -> list | None:
    """
    Build a sparse vector representation of a given text.

    Use dictionary with language profiles

    Args:
        original_text (list[str]): Any tokenized text
        language_profiles (dict[str, dict[str, float]]):
            A dictionary of dictionaries - language profiles

    Returns:
        list | None: Sparse vector
    """
    pass


def calculate_distance_sparse(
    unknown_text_vector: list[list[int | float]], known_text_vector: list[list[int | float]]
) -> float | None:
    """
    Calculate distance between two vectors using euclid metric.

    Args:
        unknown_text_vector (list[list[int | float]]): Sparse vector for unknown text
        known_text_vector (list[list[int | float]]): Sparse vector for known text

    Returns:
        float | None: Distance between vectors
    """
    pass


def predict_language_knn_sparse(
    unknown_text_vector: list, known_text_vectors: list, language_labels: list, k: int = 1
) -> list | None:
    """
    Predict unknown text label and its distance to the closest known text.

    Use knn based algorithm.

    Args:
        unknown_text_vector (list): Sparse vector for unknown text
        known_text_vectors (list): A list of sparse vectors for known texts
        language_labels (list): Language labels for each known text
        k (int): The number of neighbors to choose label from

    Returns:
        list | None: A list with text label and its distance to the closest known text
    """
    pass
