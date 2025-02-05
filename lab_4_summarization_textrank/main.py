"""
Lab 4.

Summarize text using TextRank algorithm
"""

from typing import Union

from lab_3_keywords_textrank.main import TextEncoder, TextPreprocessor

PreprocessedSentence = tuple[str, ...]
EncodedSentence = tuple[int, ...]


class Sentence:
    """
    An abstraction over the real-world sentences.
    """

    #: a text
    _text: str

    #: a position
    _position: int

    #: preprocessed
    _preprocessed: tuple

    #: encoded
    _encoded: tuple

    def __init__(self, text: str, position: int) -> None:
        """
        Initialize an instance of Sentence.

        Args:
            text (str): A text
            position (int): A position
        """
        pass

    def get_position(self) -> int:
        """
        Return the attribute.

        Returns:
            int: The position of the sentence in the text
        """
        pass

    def set_text(self, text: str) -> None:
        """
        Set the attribute.

        Args:
            text (str): The text
        """
        pass

    def get_text(self) -> str:
        """
        Return the attribute.

        Returns:
            str: The text
        """
        pass

    def set_preprocessed(self, preprocessed_sentence: PreprocessedSentence) -> None:
        """
        Set the attribute.

        Args:
            preprocessed_sentence (PreprocessedSentence): The preprocessed
                sentence (a sequence of tokens)
        """
        pass

    def get_preprocessed(self) -> PreprocessedSentence:
        """
        Return the attribute.

        Returns:
            PreprocessedSentence: The preprocessed sentence (a sequence of tokens)
        """
        pass

    def set_encoded(self, encoded_sentence: EncodedSentence) -> None:
        """
        Set the attribute.

        Args:
            encoded_sentence (EncodedSentence): The encoded sentence (a sequence of numbers)
        """
        pass

    def get_encoded(self) -> EncodedSentence:
        """
        Return the attribute.

        Returns:
            EncodedSentence: The encoded sentence (a sequence of numbers)
        """
        pass


class SentencePreprocessor(TextPreprocessor):
    """
    Class for sentence preprocessing.
    """

    #: capitals
    _capitals: str

    #: sentence delimiters
    _sentence_delimiters: str

    def __init__(self, stop_words: tuple[str, ...], punctuation: tuple[str, ...]) -> None:
        """
        Initialize an instance of SentencePreprocessor.

        Args:
            stop_words (tuple[str, ...]): Stop words
            punctuation (tuple[str, ...]): Punctuation
        """
        pass

    def _split_by_sentence(self, text: str) -> tuple[Sentence, ...]:
        """
        Split the provided text by sentence.

        Args:
            text (str): The raw text

        Returns:
            tuple[Sentence, ...]: A sequence of sentences
        """
        pass

    def _preprocess_sentences(self, sentences: tuple[Sentence, ...]) -> None:
        """
        Enriche the instances of sentences with their preprocessed versions.

        Args:
            sentences (tuple[Sentence, ...]): A tuple of sentences
        """
        pass

    def get_sentences(self, text: str) -> tuple[Sentence, ...]:
        """
        Extract the sentences from the given text & preprocesses them.

        Args:
            text (str): The raw text

        Returns:
            tuple[Sentence, ...]:
        """
        pass


class SentenceEncoder(TextEncoder):
    """
    A class to encode string sequence into matching integer sequence.
    """

    #: idx
    _idx: int

    def __init__(self) -> None:
        """
        Initialize an instance of SentenceEncoder.
        """
        pass

    def _learn_indices(self, tokens: tuple[str, ...]) -> None:
        """
        Fill attributes mapping words and integer equivalents to each other.

        Args:
            tokens (tuple[str, ...]): A sequence of string tokens
        """
        pass

    def encode_sentences(self, sentences: tuple[Sentence, ...]) -> None:
        """
        Enriche the instances of sentences with their encoded versions.

        Args:
            sentences (tuple[Sentence, ...]): A sequence of sentences
        """
        pass


def calculate_similarity(sequence: Union[list, tuple], other_sequence: Union[list, tuple]) -> float:
    """
    Calculate similarity between two sequences using Jaccard index.

    Args:
        sequence (Union[list, tuple]): A sequence of items
        other_sequence (Union[list, tuple]): A sequence of items

    Returns:
        float: Similarity score
    """
    pass


class SimilarityMatrix:
    """
    A class to represent relations between sentences.
    """

    #: a matrix
    _matrix: list[list[float]]

    #: vertices
    _vertices: dict[Sentence, int]

    def __init__(self) -> None:
        """
        Initialize an instance of SimilarityMatrix.
        """
        pass

    def get_vertices(self) -> tuple[Sentence, ...]:
        """
        Return a sequence of all vertices present in the graph.

        Returns:
            tuple[Sentence, ...]: A sequence of vertices
        """
        pass

    def _extend_matrix_by_one(self) -> None:
        """
        Add one dimension to the matrix, increasing number of rows and number of columns by one.
        """
        pass

    def _add_vertex(self, vertex: Sentence) -> None:
        """
        Record information about a new vertex and assigns a sequence number to it.

        Args:
            vertex (Sentence): A sentence to add as a vertex
        """
        pass

    def _get_vertex_index(self, vertex: Sentence) -> int:
        """
        Retrieve a sequence number of the specified vertex.

        Args:
            vertex (Sentence): A vertex to search for

        Returns:
            int: The vertex's index
        """
        pass

    def calculate_inout_score(self, vertex: Sentence) -> int:
        """
        Retrieve a number of vertices that are similar to the input one.

        Args:
            vertex (Sentence): vertex

        Returns:
            int:
        """
        pass

    def add_edge(self, vertex1: Sentence, vertex2: Sentence) -> None:
        """
        Add or overwrite an edge in the graph between the specified vertices.

        Args:
            vertex1 (Sentence): Vertex 1
            vertex2 (Sentence): Vertex 2
        """
        pass

    def get_similarity_score(self, sentence: Sentence, other_sentence: Sentence) -> float:
        """
        Get the similarity score for two sentences from the matrix.

        Args:
            sentence (Sentence):
            other_sentence (Sentence):

        Returns:
            float: The similarity score
        """
        pass

    def fill_from_sentences(self, sentences: tuple[Sentence, ...]) -> None:
        """
        Update graph instance with vertices and edge extracted from sentences.

        Args:
            sentences (tuple[Sentence, ...]): Sentences
        """
        pass


class TextRankSummarizer:
    """
    TextRank for summarization.
    """

    #: a graph
    _graph: SimilarityMatrix

    #: damping factor
    _damping_factor: float

    #: convergence threshold
    _convergence_threshold: float

    #: max iter
    _max_iter: int

    #: scores
    _scores: dict[Sentence, float]

    def __init__(self, graph: SimilarityMatrix) -> None:
        """
        Initialize an instance of TextRankSummarizer.

        Args:
            graph (SimilarityMatrix): The filled instance of the similarity matrix
        """
        pass

    def update_vertex_score(
        self, vertex: Sentence, incidental_vertices: list[Sentence], scores: dict[Sentence, float]
    ) -> None:
        """
        Change vertex significance score using algorithm-specific formula.

        Args:
            vertex (Sentence): A sentence
            incidental_vertices (list[Sentence]): Vertices with similarity score > 0 for vertex
            scores (dict[Sentence, float]): Current vertices scores
        """
        pass

    def train(self) -> None:
        """
        Compute iteratively significance scores for vertices.
        """
        pass

    def get_top_sentences(self, n_sentences: int) -> tuple[Sentence, ...]:
        """
        Retrieve top n most important sentences in the encoded text.

        Args:
            n_sentences (int): Number of sentence to retrieve

        Returns:
            tuple[Sentence, ...]: A sequence of sentences
        """
        pass

    def make_summary(self, n_sentences: int) -> str:
        """
        Construct summary from the most important sentences.

        Args:
            n_sentences (int): Number of sentences to include in the summary

        Returns:
            str: Summary
        """
        pass


class IncorrectQueryError(Exception):
    """
    Exception for IncorrectQuery.
    """


class NoRelevantTextsError(Exception):
    """
    Exception for NoRelevantTexts.
    """


class Buddy:
    """
    (Almost) All-knowing entity.
    """

    #: paths to texts
    _paths_to_texts: list[str]

    #: stop words
    _stop_words: tuple[str, ...]

    #: punctuation
    _punctuation: tuple[str, ...]

    #: idf values
    _idf_values: dict[str, float]

    #: knowledge database
    _knowledge_database: dict

    #: text preprocessor
    _text_preprocessor: TextPreprocessor

    #: sentence encoder
    _sentence_encoder: SentenceEncoder

    #: sentence preprocessor
    _sentence_preprocessor: SentencePreprocessor

    def __init__(
        self,
        paths_to_texts: list[str],
        stop_words: tuple[str, ...],
        punctuation: tuple[str, ...],
        idf_values: dict[str, float],
    ) -> None:
        """
        Initialize an instance of Buddy.

        Args:
            paths_to_texts (list[str]): Paths to the texts from which to learn
            stop_words (tuple[str, ...]): A sequence of stop words
            punctuation (tuple[str, ...]): A sequence of punctuation symbols
            idf_values (dict[str, float]): Pre-computed IDF values
        """
        pass

    def _populate_database_from_texts(self) -> None:
        """
        Populate the database from the provided texts.
        """
        pass

    def add_text_to_database(self, path_to_text: str) -> None:
        """
        Add the given text to the existing database.

        Args:
            path_to_text (str): A path to text
        """
        pass

    @staticmethod
    def _reconstruct_text_from_sentences(sentences: tuple[Sentence, ...]) -> str:
        """
        Restore the text from the given sentences.

        Args:
            sentences (tuple[Sentence, ...]): A sequence of sentences

        Returns:
            str: The text
        """
        pass

    def _extract_keywords_from_sentences(self, sentences: tuple[Sentence, ...]) -> tuple[str, ...]:
        """
        Extract the keywords from the given sentences.

        Args:
            sentences (tuple[Sentence, ...]): A sequence of sentences

        Returns:
            tuple[str, ...]: A sequence of keywords
        """
        pass

    def _find_texts_close_to_keywords(
        self, keywords: tuple[str, ...], n_texts: int
    ) -> tuple[str, ...]:
        """
        Find texts that are similar (i.e. contain the same keywords) to the given keywords.

        Args:
            keywords (tuple[str, ...]): A sequence of keywords
            n_texts (int): Number of texts to find

        Returns:
            tuple[str, ...]: The texts' ids
        """
        pass

    @staticmethod
    def _summarize_text(sentences: tuple[Sentence, ...]) -> str:
        """
        Summarize text.

        Args:
            sentences (tuple[Sentence, ...]): A sequence of sentences

        Returns:
            str: The summary
        """
        pass

    def reply(self, query: str, n_summaries: int = 3) -> str:
        """
        Reply to the query.

        Args:
            query (str): The query
            n_summaries (int): The number of summaries to include in the answer

        Returns:
            str: The answer
        """
        pass
