"""
Lab 1.

Extract keywords based on frequency related metrics
"""


def is_dict_valid(
    dictionary: dict,
    key_types: tuple = (str,),
    value_types: tuple = (int, float),
    can_be_empty: bool = False,
) -> bool:
    """
    Verify that dictionary meets expectations.

    Args:
        dictionary (dict): Object to test
        key_types (tuple): Acceptable types for keys
        value_types (tuple): Acceptable types for values
        can_be_empty (bool): Indicator whether it is acceptable that the dictionary has no content

    Returns:
        bool: Indicator whether the dictionary satisfies all the requirements presented
    """
    pass


def clean_and_tokenize(text: str) -> list[str] | None:
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


def calculate_frequencies(tokens: list[str]) -> dict[str, int] | None:
    """
    Compose a frequency dictionary from the token sequence.

    Args:
        tokens (list[str]): Token sequence to count frequencies for

    Returns:
        dict[str, int] | None: A dictionary where key - token,
            value - number of occurrences in the token sequence

    In case of corrupt input arguments, None is returned
    """
    pass


def get_top_n(frequencies: dict[str, int | float], top: int) -> list[str] | None:
    """
    Extract a certain number of most frequent tokens.

    Args:
        frequencies (dict[str, int | float]): A dictionary with tokens
            and its corresponding frequency values
        top (int): Number of token to extract

    Returns:
        list[str] | None: Sequence of specified length
            consisting of tokens with the largest frequency

    In case of corrupt input arguments, None is returned
    """
    pass


def calculate_tf(frequencies: dict[str, int]) -> dict[str, float] | None:
    """
    Calculate TF score for each word in a token sequence based on the raw frequency.

    Args:
        frequencies (dict[str, int]): Raw number of occurrences for each of the tokens

    Returns:
        dict[str, float] | None: A dictionary with tokens
            and corresponding term frequency score

    In case of corrupt input arguments, None is returned
    """
    pass


def calculate_tfidf(term_freq: dict[str, float], idf: dict[str, float]) -> dict[str, float] | None:
    """
    Calculate TF-IDF score for each of the tokens based on its TF and IDF scores.

    Args:
        term_freq (dict[str, float]): A dictionary with tokens
            and its corresponding TF values
        idf (dict[str, float]): A dictionary with tokens
            and its corresponding IDF values

    Returns:
        dict[str, float] | None: A dictionary with tokens
            and its corresponding TF-IDF values

    In case of corrupt input arguments, None is returned
    """
    pass


def calculate_expected_frequency(
    doc_freqs: dict[str, int], corpus_freqs: dict[str, int]
) -> dict[str, float] | None:
    """
    Calculate expected frequency for each of the tokens.

    Calculation based on its TF score for both target document and general corpus

    Args:
        doc_freqs (dict[str, int]): A dictionary with tokens
            and its corresponding number of occurrences in document
        corpus_freqs (dict[str, int]): A dictionary with tokens
            and its corresponding number of occurrences in corpus

    Returns:
        dict[str, float] | None: A dictionary with tokens
            and its corresponding expected frequency

    In case of corrupt input arguments, None is returned
    """
    pass


def calculate_chi_values(
    expected: dict[str, float], observed: dict[str, int]
) -> dict[str, float] | None:
    """
    Calculate chi-squared value for the tokens.

    Calculation based on their expected and observed frequency rates

    Args:
        expected (dict[str, float]): A dictionary with tokens
            and its corresponding expected frequency
        observed (dict[str, int]): A dictionary with tokens
            and its corresponding observed frequency

    Returns:
        dict[str, float] | None: A dictionary with tokens
            and its corresponding chi-squared value

    In case of corrupt input arguments, None is returned
    """
    pass


def extract_significant_words(
    chi_values: dict[str, float], alpha: float
) -> dict[str, float] | None:
    """
    Select those tokens from the token sequence.

    Tokens have a chi-squared value smaller than the criterion.

    Args:
        chi_values (dict[str, float]): A dictionary with tokens
            and its corresponding chi-squared value
        alpha (float): Level of significance that controls
            critical value of chi-squared metric

    Returns:
        dict[str, float] | None: A dictionary with significant tokens
            and its corresponding chi-squared value

    In case of corrupt input arguments, None is returned
    """
    pass
