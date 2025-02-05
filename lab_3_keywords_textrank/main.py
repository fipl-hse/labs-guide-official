"""
Lab 3.

Extract keywords based on TextRank algorithm
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).parent
ASSETS_PATH = PROJECT_ROOT / "assets"


class TextPreprocessor:
    # pylint: disable=too-few-public-methods
    """
    Preprocess raw text.
    """

    #: Insignificant words to remove from tokens
    _stop_words: tuple[str, ...]

    #: Punctuation symbols to remove during text cleaning
    _punctuation: tuple[str, ...]

    # 4
    def __init__(self, stop_words: tuple[str, ...], punctuation: tuple[str, ...]) -> None:
        """
        Initialize an instance of TextPreprocessor.

        Args:
            stop_words (tuple[str, ...]): Insignificant words to remove from tokens
            punctuation (tuple[str, ...]): Punctuation symbols to remove during text cleaning
        """
        pass

    def _clean_and_tokenize(self, text: str) -> tuple[str, ...]:
        """
        Remove punctuation, cast to lowercase, split into tokens.

        Args:
            text (str): Raw text

        Returns:
            tuple[str, ...]: Clean lowercase tokens
        """
        pass

    def _remove_stop_words(self, tokens: tuple[str, ...]) -> tuple[str, ...]:
        """
        Filter tokens, removing stop words.

        Args:
            tokens (tuple[str, ...]): Tokens containing stop-words

        Returns:
            tuple[str, ...]: Tokens without stop-words
        """
        pass

    def preprocess_text(self, text: str) -> tuple[str, ...]:
        """
        Produce filtered clean lowercase tokens from raw text.

        Args:
            text (str): Raw text

        Returns:
            tuple[str, ...]: Clean lowercase tokens with no stop-words
        """
        pass


class TextEncoder:
    """
    Encode string sequence into matching integer sequence.
    """

    #: a string -> number dictionary
    _word2id: dict

    #: a number -> string dictionary
    _id2word: dict

    def __init__(self) -> None:
        """
        Initialize an instance of TextEncoder.
        """
        pass

    def _learn_indices(self, tokens: tuple[str, ...]) -> None:
        """
        Fill attributes mapping words and integer equivalents to each other.

        Args:
            tokens (tuple[str, ...]): Sequence of string tokens
        """
        pass

    def encode(self, tokens: tuple[str, ...]) -> tuple[int, ...] | None:
        """
        Encode input sequence of string tokens to sequence of integer tokens.

        Args:
            tokens (tuple[str, ...]): Sequence of string tokens

        Returns:
            tuple[int, ...] | None: Sequence of integer tokens

        In case of empty tokens input data, None is returned
        """
        pass

    def decode(self, encoded_tokens: tuple[int, ...]) -> tuple[str, ...] | None:
        """
        Decode input sequence of integer tokens to sequence of string tokens.

        Args:
            encoded_tokens (tuple[int, ...]): Sequence of integer tokens

        Returns:
            tuple[str, ...] | None: Sequence of string tokens

        In case of out-of-dictionary input data, None is returned
        """
        pass


def extract_pairs(
    tokens: tuple[int, ...], window_length: int
) -> tuple[tuple[int, ...], ...] | None:
    """
    Retrieve all pairs of co-occurring words in the token sequence.

    Args:
        tokens (tuple[int, ...]): Sequence of tokens
        window_length (int): Maximum distance between co-occurring tokens.
            Tokens are considered co-occurring if they appear in the same window of this length

    Returns:
        tuple[tuple[int, ...], ...] | None: Pairs of co-occurring tokens

    In case of corrupt input data, None is returned.
    Tokens must not be empty, window lengths must be integer, window lengths cannot be less than 2.
    """
    pass


class AdjacencyMatrixGraph:
    """
    Represent graph as matrix of adjacency.
    """

    #: a matrix
    _matrix: list[list[int]]

    #: vertices
    _vertices: dict[int, int]

    #: positions
    _positions: dict[int, list[int]]

    #: position weights
    _position_weights: dict[int, float]

    def __init__(self) -> None:
        """
        Initialize an instance of AdjacencyMatrixGraph.
        """
        pass

    def get_vertices(self) -> tuple[int, ...]:
        """
        Return a sequence of all vertices present in the graph.

        Returns:
            tuple[int, ...]: A sequence of vertices present in the graph
        """
        pass

    def _extend_matrix_by_one(self) -> None:
        """
        Add one dimension to the matrix, increasing number of rows and number of columns by one.
        """
        pass

    def _add_vertex(self, vertex: int) -> None:
        """
        Record information about a new vertex and assign a sequence number to it.

        Args:
            vertex (int): Vertex to add
        """
        pass

    def _get_vertex_index(self, vertex: int) -> int:
        """
        Retrieve a sequence number of the specified vertex.

        Args:
            vertex (int): A vertex for which to retrieve a sequence number

        Returns:
            int: Sequence number of the specified vertex

        In case of corrupt input data, None is returned
        """
        pass

    def add_edge(self, vertex1: int, vertex2: int) -> int:
        """
        Add or overwrite an edge in the graph between the specified vertices.

        Args:
            vertex1 (int): The first vertex incidental to the added edge
            vertex2 (int): The second vertex incidental to the added edge

        Returns:
            int: 0 if edge was added successfully, otherwise -1

        In case of vertex1 being equal to vertex2, -1 is returned as loops are prohibited
        """
        pass

    def is_incidental(self, vertex1: int, vertex2: int) -> int:
        """
        Retrieve information about whether the two vertices are incidental.

        Args:
            vertex1 (int): The first vertex incidental to the edge sought
            vertex2 (int): The second vertex incidental to the edge sought

        Returns:
            int: 1 if vertices are incidental, otherwise 0

        If either of vertices is not present in the graph, -1 is returned
        """
        pass

    def calculate_inout_score(self, vertex: int) -> int:
        """
        Retrieve a number of incidental vertices to a specified vertex.

        Args:
            vertex (int): A vertex to calculate inout score for

        Returns:
            int: Number of incidental vertices

        If vertex is not present in the graph, -1 is returned
        """
        pass

    def fill_from_tokens(self, tokens: tuple[int, ...], window_length: int) -> None:
        """
        Update graph instance with vertices and edge extracted from tokenized text.

        Args:
            tokens (tuple[int, ...]): Sequence of tokens
            window_length (int): Maximum distance between co-occurring tokens.
                Tokens are considered co-occurring if they appear in the same window of this length
        """
        pass

    def fill_positions(self, tokens: tuple[int, ...]) -> None:
        """
        Save information about all positions of each vertex in the token sequence.

        Args:
            tokens (tuple[int, ...]): Sequence of tokens
        """
        pass

    def calculate_position_weights(self) -> None:
        """
        Compute position weights for all tokens in text.
        """
        pass

    def get_position_weights(self) -> dict[int, float]:
        """
        Retrieve position weights for all vertices in the graph.

        Returns:
            dict[int, float]: Position weights for all vertices in the graph
        """
        pass


class EdgeListGraph:
    """
    Represent graph as a list of edges.
    """

    #: edges
    _edges: dict

    #: positions
    _positions: dict

    #: position weights
    _position_weights: dict

    def __init__(self) -> None:
        """
        Initialize an instance of EdgeListGraph.
        """
        pass

    def get_vertices(self) -> tuple[int, ...]:
        """
        Return a sequence of all vertices present in the graph.

        Returns:
            tuple[int, ...]: A sequence of vertices present in the graph
        """
        pass

    def add_edge(self, vertex1: int, vertex2: int) -> int:
        """
        Add or overwrite an edge in the graph between the specified vertices.

        Args:
            vertex1 (int): The first vertex incidental to the added edge
            vertex2 (int): The second vertex incidental to the added edge

        Returns:
            int: 0 if edge was added successfully, otherwise -1

        In case of vertex1 being equal to vertex2, -1 is returned as loops are prohibited
        """
        pass

    def is_incidental(self, vertex1: int, vertex2: int) -> int:
        """
        Retrieve information about whether the two vertices are incidental.

        Args:
            vertex1 (int): The first vertex incidental to the edge sought
            vertex2 (int): The second vertex incidental to the edge sought

        Returns:
            int: 1 if vertices are incidental, otherwise 0

        If either of vertices is not present in the graph, -1 is returned
        """
        pass

    def calculate_inout_score(self, vertex: int) -> int:
        """
        Retrieve a number of incidental vertices to a specified vertex.

        Args:
            vertex (int): A vertex to calculate inout score for

        Returns:
            int: Number of incidental vertices

        If vertex is not present in the graph, -1 is returned
        """
        pass

    def fill_from_tokens(self, tokens: tuple[int, ...], window_length: int) -> None:
        """
        Update graph instance with vertices and edge extracted from tokenized text.

        Args:
            tokens (tuple[int, ...]): Sequence of tokens
            window_length (int): Maximum distance between co-occurring tokens.
                Tokens are considered co-occurring if they appear in the same window of this length
        """
        pass

    def fill_positions(self, tokens: tuple[int, ...]) -> None:
        """
        Save information on all positions of each vertex in the token sequence.

        Args:
            tokens (tuple[int, ...]): Sequence of tokens
        """
        pass

    def calculate_position_weights(self) -> None:
        """
        Compute position weights for all tokens in text.
        """
        pass

    def get_position_weights(self) -> dict[int, float]:
        """
        Retrieve position weights for all vertices in the graph.

        Returns:
            dict[int, float]: Position weights for all vertices in the graph
        """
        pass


class VanillaTextRank:
    """
    Basic TextRank implementation.
    """

    #: a graph
    _graph: AdjacencyMatrixGraph | EdgeListGraph

    #: damping factor
    _damping_factor: float

    #: convergence threshold
    _convergence_threshold: float

    #: max iter
    _max_iter: int

    #: scores
    _scores: dict[int, float]

    def __init__(self, graph: AdjacencyMatrixGraph | EdgeListGraph) -> None:
        """
        Initialize an instance of VanillaTextRank.

        Args:
            graph (AdjacencyMatrixGraph | EdgeListGraph): A graph representing the text
        """
        pass

    def update_vertex_score(
        self, vertex: int, incidental_vertices: list[int], scores: dict[int, float]
    ) -> None:
        """
        Change vertex significance score using algorithm-specific formula.

        Args:
            vertex (int): A vertex which significance score is updated
            incidental_vertices (list[int]): Vertices incidental to the scored one
            scores (dict[int, float]): Scores of all vertices in the graph
        """
        pass

    def train(self) -> None:
        """
        Compute iteratively significance scores for vertices.
        """
        pass

    def get_scores(self) -> dict[int, float]:
        """
        Retrieve importance scores of all tokens in the encoded text.

        Returns:
            dict[int, float]: Importance scores of all tokens in the encoded text
        """
        pass

    def get_top_keywords(self, n_keywords: int) -> tuple[int, ...]:
        """
        Retrieve top n most important tokens in the encoded text.

        Args:
            n_keywords (int):

        Returns:
            tuple[int, ...]: Top n most important tokens in the encoded text
        """
        pass


class PositionBiasedTextRank(VanillaTextRank):
    """
    Advanced TextRank implementation: positions of tokens in text are taken into consideration.
    """

    #: position weights
    _position_weights: dict[int, float]

    def __init__(self, graph: AdjacencyMatrixGraph | EdgeListGraph) -> None:
        """
        Initialize an instance of PositionBiasedTextRank.

        Args:
            graph (AdjacencyMatrixGraph | EdgeListGraph): A graph representing the text
        """
        pass

    def update_vertex_score(
        self, vertex: int, incidental_vertices: list[int], scores: dict[int, float]
    ) -> None:
        """
        Change vertex significance score using algorithm-specific formula.

        Args:
            vertex (int): A vertex which significance score is updated
            incidental_vertices (list[int]): Vertices incidental to the scored one
            scores (dict[int, float]): Scores of all vertices in the graph
        """
        pass


BENCHMARK_MATERIAL_PATH = ASSETS_PATH / "benchmark_materials"
IDF_PATH = BENCHMARK_MATERIAL_PATH / "IDF.json"
ENG_STOP_WORDS_PATH = BENCHMARK_MATERIAL_PATH / "eng_stop_words.txt"


class TFIDFAdapter:
    """
    Unify the interface of TF-IDF keywords extractor with TextRank algorithms.
    """

    #: tokens
    _tokens: tuple[str, ...]

    #: idf
    _idf: dict[str, float]

    #: scores
    _scores: dict[str, float]

    def __init__(self, tokens: tuple[str, ...], idf: dict[str, float]) -> None:
        """
        Initialize an instance of TFIDFAdapter.

        Args:
            tokens (tuple[str, ...]): Sequence of tokens from which to extract keywords
            idf (dict[str, float]): Inverse Document Frequency scores for tokens
        """
        pass

    def train(self) -> int:
        """
        Compute importance scores for all tokens.

        Returns:
            int: 0 if importance scores were calculated successfully, otherwise -1
        """
        pass

    def get_scores(self) -> dict[str, float]:
        """
        Retrieve importance scores for each of the tokens.

        Returns:
            dict[str, float]: Dictionary with importance scores calculated
        """
        pass

    def get_top_keywords(self, n_keywords: int) -> tuple[str, ...]:
        """
        Retrieve a requested number of the most important tokens.

        Args:
            n_keywords (int): Requested number of keywords to extract

        Returns:
            tuple[str, ...]: A requested number tokens with the highest importance scores
        """
        pass


class RAKEAdapter:
    """
    Unify the interface of RAKE keywords extractor with TextRank algorithms.
    """

    #: a text
    _text: str

    #: stop words
    _stop_words: tuple[str, ...]

    #: scores
    _scores: dict[str, float]

    def __init__(self, text: str, stop_words: tuple[str, ...]) -> None:
        """
        Initialize an instance of RAKEAdapter.

        Args:
            text (str): A text from which to extract keywords
            stop_words (tuple[str, ...]): A sequence of stop-words
        """
        pass

    def train(self) -> int:
        """
        Compute importance scores for all tokens.

        Returns:
            int: 0 if importance scores were calculated successfully, otherwise -1
        """
        pass

    def get_scores(self) -> dict[str, float]:
        """
        Retrieve importance scores for each of the tokens.

        Returns:
            dict[str, float]: Dictionary with importance scores calculated
        """
        pass

    def get_top_keywords(self, n_keywords: int) -> tuple[str, ...]:
        """
        Retrieve a requested number of the most important tokens.

        Args:
            n_keywords (int): Requested number of keywords to extract

        Returns:
            tuple[str, ...]: A requested number tokens with the highest importance scores
        """
        pass


def calculate_recall(predicted: tuple[str, ...], target: tuple[str, ...]) -> float:
    """
    Compute recall metric.

    Args:
        predicted (tuple[str, ...]): Keywords predictions of an algorithm to estimate
        target (tuple[str, ...]): Ground truth keywords

    Returns:
        float: Recall value
    """
    pass


class KeywordExtractionBenchmark:
    """
    Compare 4 different algorithms of keywords extraction.
    """

    #: stop words
    _stop_words: tuple[str, ...]

    #: punctuation
    _punctuation: tuple[str, ...]

    #: idf
    _idf: dict[str, float]

    #: materials path
    _materials_path: Path

    #: themes
    themes: tuple[str, ...]

    #: a report
    report: dict

    def __init__(
        self,
        stop_words: tuple[str, ...],
        punctuation: tuple[str, ...],
        idf: dict[str, float],
        materials_path: Path,
    ) -> None:
        """
        Initialize an instance of KeywordExtractionBenchmark.

        Args:
            stop_words (tuple[str, ...]): A sequence of stop-words
            punctuation (tuple[str, ...]): Symbols of punctuation
            idf (dict[str, float]): Inverse Document Frequency scores for the words in materials
            materials_path (Path): A path to materials to use for comparison
        """
        pass

    def retrieve_text(self, theme: str) -> str:
        """
        Retrieve the text from which to extract keywords by the theme requested.

        Args:
            theme (str): Theme

        Returns:
            str: The text from which to extract keywords
        """
        pass

    def retrieve_keywords(self, theme: str) -> tuple[str, ...]:
        """
        Retrieve the ground truth keywords by the theme requested.

        Args:
            theme (str): Theme

        Returns:
            tuple[str, ...]: A sequence of ground truth keywords
        """
        pass

    def run(self) -> dict[str, dict[str, float]] | None:
        # pylint: disable=too-many-locals
        """
        Create a report.

        Returns:
            dict[str, dict[str, float]] | None: Comparison report
        """
        pass

    def save_to_csv(self, path: Path) -> None:
        """
        Save comparison report to csv.

        Args:
            path (Path): A path where to save the report file
        """
        pass
