"""
Lab 2.

Extract keywords based on co-occurrence frequency
"""

from pathlib import Path
from typing import Mapping, Sequence, Union


KeyPhrase = tuple[str, ...]
KeyPhrases = Sequence[KeyPhrase]


def extract_phrases(text: str) -> list[str] | None:
    """
    Split the text into separate phrases using phrase delimiters.

    Args:
        text (str): An original text

    Returns:
        list[str] | None: A list of phrases

    In case of corrupt input arguments, None is returned
    """
    pass


def extract_candidate_keyword_phrases(
    phrases: list[str], stop_words: list[str]
) -> KeyPhrases | None:
    """
    Create a list of candidate keyword phrases by splitting the given phrases by the stop words.

    Args:
        phrases (list[str]): A list of the phrases
        stop_words (list[str]): A list of the stop words

    Returns:
        KeyPhrases | None: The candidate keyword phrases for the text

    In case of corrupt input arguments, None is returned
    """
    pass


def calculate_frequencies_for_content_words(
    candidate_keyword_phrases: KeyPhrases,
) -> dict[str, int] | None:
    """
    Extract the content words and compute their frequencies.

    Args:
        candidate_keyword_phrases (KeyPhrases): A list of the candidate keyword phrases

    Returns:
        dict[str, int] | None: A dictionary with the content words
            and corresponding frequencies

    In case of corrupt input arguments, None is returned
    """
    pass


def calculate_word_degrees(
    candidate_keyword_phrases: KeyPhrases, content_words: list[str]
) -> dict[str, int] | None:
    """
    Calculate the word degrees based on the candidate keyword phrases list.

    Degree of a word is equal to the total length of all keyword phrases the word is found in

    Args:
        candidate_keyword_phrases (KeyPhrases): The candidate keyword phrases for the text
        content_words (list[str]): The content words from the candidate keywords

    Returns:
        dict[str, int] | None: The words and their degrees

    In case of corrupt input arguments, None is returned
    """
    pass


def calculate_word_scores(
    word_degrees: dict[str, int], word_frequencies: dict[str, int]
) -> dict[str, float] | None:
    """
    Calculate the word score based on the word degree and word frequency metrics.

    Args:
        word_degrees (dict[str, int]): A mapping between the word and the degree
        word_frequencies (dict[str, int]): A mapping between the word and the frequency

    Returns:
        dict[str, float] | None: A dictionary with key - word, value - word_score

    In case of corrupt input arguments, None is returned
    """
    pass


def calculate_cumulative_score_for_candidates(
    candidate_keyword_phrases: KeyPhrases, word_scores: dict[str, float]
) -> dict[KeyPhrase, float] | None:
    """
    Calculate cumulative score for each candidate keyword phrase.

    Cumulative score for a keyword phrase equals to
    the sum of the word scores of each keyword phrase's constituent

    Args:
        candidate_keyword_phrases (KeyPhrases): A list of candidate keyword phrases
        word_scores (dict[str, float]): Word scores

    Returns:
        dict[KeyPhrase, float] | None: A dictionary containing the mapping
            between the candidate keyword phrases and respective cumulative scores

    In case of corrupt input arguments, None is returned
    """
    pass


def get_top_n(
    keyword_phrases_with_scores: dict[KeyPhrase, float], top_n: int, max_length: int
) -> list[str] | None:
    """
    Extract the top N keyword phrases based on their scores and lengths.

    Args:
        keyword_phrases_with_scores (dict[KeyPhrase, float]): A dictionary
            containing the keyword phrases and their cumulative scores
        top_n (int): The number of the keyword phrases to extract
        max_length (int): Maximal length of a keyword phrase to be considered

    Returns:
        list[str] | None: A list of keyword phrases
            sorted by their scores in descending order

    In case of corrupt input arguments, None is returned
    """
    pass


def extract_adjoining_keyword_phrases(
    candidate_keyword_phrases: KeyPhrases,
) -> Sequence[tuple[KeyPhrase, KeyPhrase]] | None:
    """
    Extract the keyword phrases that are found at least twice together.

    Args:
        candidate_keyword_phrases (KeyPhrases): A list of candidate keyword phrases

    Returns:
        Sequence[tuple[KeyPhrase, KeyPhrase]] | None: Pairs of keyword phrases
            that are found together at least twice
    """
    pass


def extract_candidate_keyword_phrases_with_adjoining(
    candidate_keyword_phrases: KeyPhrases, phrases: list[str]
) -> KeyPhrases | None:
    # pylint: disable=too-many-locals
    """
    Extract the adjoining keyword phrases and build new candidate keywords with stop words.

    Adjoining keywords: such pairs that are found at least twice
    in the candidate keyword phrases list one after another

    To build a new keyword phrase the following is required:
        1. Find the first constituent of the adjoining keyword phrase in the phrases followed by:
           a stop word and the second constituent of the adjoining keyword phrase
        2. Combine these three pieces in the new candidate keyword phrase, i.e.:
           new_candidate_keyword = [first_constituent, stop_word, second_constituent]

    Args:
        candidate_keyword_phrases (KeyPhrases): A list of candidate keyword phrases
        phrases (list[str]): A list of phrases

    Returns:
        KeyPhrases | None: A list containing the pairs of candidate keyword phrases
            that are found at least twice together

    In case of corrupt input arguments, None is returned
    """
    pass


def calculate_cumulative_score_for_candidates_with_stop_words(
    candidate_keyword_phrases: KeyPhrases, word_scores: dict[str, float], stop_words: list[str]
) -> dict[KeyPhrase, float] | None:
    """
    Calculate cumulative score for each candidate keyword phrase.

    Cumulative score for a keyword phrase equals to
    the sum of the word scores of each keyword phrase's constituent except for the stop words

    Args:
        candidate_keyword_phrases (KeyPhrases): A list of candidate keyword phrases
        word_scores (dict[str, float]): Word scores
        stop_words (list[str]): A list of stop words

    Returns:
        dict[KeyPhrase, float] | None: A dictionary containing the mapping
            between the candidate keyword phrases and respective cumulative scores

    In case of corrupt input arguments, None is returned
    """
    pass


def find_subsequence_position(
    subsequence: Union[Sequence[str], tuple[str, ...]],
    sequence: Union[Sequence[str], tuple[str, ...]],
    start: int,
) -> int:
    """
    Find the starting position of a subsequence in a sequence.

    Args:
        subsequence (Union[Sequence[str], tuple[str, ...]]): A subsequence
            for which the function searches
        sequence (Union[Sequence[str], tuple[str, ...]]): A sequence in which
            the function searches
        start (int): Starting position of the search

    Returns:
        int: Position from which the subsequence starts,
            -1 returned if the subsequence is not found
    """
    pass


def find_ceil_of_value(value: float) -> int:
    """
    Find the ceiling value (closes int x that is >= value) of the given value.

    Helper function

    Args:
        value (float): The value for which the ceiling value should be found

    Returns:
        int: The ceiling value
    """
    pass


def find_percentile(data: Union[Sequence[int], tuple[int, ...]], percentage: int) -> int:
    """
    Find the percentile value.

    Helper function

    Args:
        data (Union[Sequence[int], tuple[int, ...]]): An array of values
        percentage (int): Required percentile

    Returns:
        int: The percentile
    """
    pass


def generate_stop_words(text: str, max_length: int) -> list[str] | None:
    """
    Generate the list of stop words from the given text.

    Args:
        text (str): The text
        max_length (int): Maximum length (in characters) of an individual stop word

    Returns:
        list[str] | None: A list of stop words
    """
    pass


def load_stop_words(path: Path) -> dict[str, list[str]] | None:
    """
    Load stop word lists from the file.

    Args:
        path (Path): Path to the file with stop word lists

    Returns:
        dict[str, list[str]] | None: A dictionary containing the language names
            and corresponding stop word lists
    """
    pass
