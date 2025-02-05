"""
Checks the second lab predicting language score function
"""

import unittest
from unittest.mock import patch

import pytest

from lab_2_classify_by_knn.main import calculate_distance, predict_language_score


class PredictLanguageScoreTest(unittest.TestCase):
    """
    Tests predicting language score function
    """

    @pytest.mark.lab_2_classify_by_knn
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_predict_language_score_ideal(self):
        """
        Ideal predicting language score scenario
        """
        first_text_vector = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        second_text_vectors = [
            [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0],
            [0.1, 0, 0.4, 0.1, 0, 0, 0.34, 0.3, 0],
            [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0.35],
        ]
        language_labels = ["en", "de", "en"]
        expected = ["de", 0.45782]
        actual = predict_language_score(first_text_vector, second_text_vectors, language_labels)
        self.assertEqual(expected, actual)

    @pytest.mark.lab_2_classify_by_knn
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    @patch("lab_2_classify_by_knn.main.calculate_distance", side_effect=calculate_distance)
    def test_calculate_distance_called(self, mock):
        """
        Predict language score call calculating distance function check
        """
        first_text_vector = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        second_text_vectors = [
            [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0],
            [0.1, 0, 0.4, 0.1, 0, 0, 0.34, 0.3, 0],
            [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0.35],
        ]
        language_labels = ["en", "de", "en"]
        predict_language_score(first_text_vector, second_text_vectors, language_labels)
        self.assertTrue(mock.called)

    @pytest.mark.lab_2_classify_by_knn
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_predict_language_score_bad_input(self):
        """
        Predict language score invalid input vectors check
        """
        bad_inputs = ["hello", None, 6, True, [None], {}, (), 1.65]
        expected = None
        for bad_input in bad_inputs:
            actual = predict_language_score(bad_input, bad_input, bad_input)
            self.assertEqual(expected, actual)

    @pytest.mark.lab_2_classify_by_knn
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_predict_language_score_incorrect_labels(self):
        """
        Predict language score invalid number of language labels check
        """
        first_text_vector = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        second_text_vectors = [
            [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0],
            [0.1, 0, 0.4, 0.1, 0, 0, 0.34, 0.3, 0],
            [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0.35],
        ]
        language_labels = ["en", "de"]
        expected = None
        actual = predict_language_score(first_text_vector, second_text_vectors, language_labels)
        self.assertEqual(expected, actual)

    @pytest.mark.lab_2_classify_by_knn
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_predict_language_score_return_value(self):
        """
        Predict language score return values check
        """
        first_text_vector = [0.2, 0, 0.2, 0, 0.2, 0, 0.2, 0, 0]
        second_text_vectors = [
            [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0],
            [0.1, 0, 0.4, 0.1, 0, 0, 0.34, 0.3, 0],
            [0, 0.2, 0, 0.1, 0, 0.49, 0, 0.3, 0.35],
        ]
        language_labels = ["en", "de", "en"]
        actual = predict_language_score(first_text_vector, second_text_vectors, language_labels)
        self.assertTrue(isinstance(actual, list))
        self.assertTrue(isinstance(actual[0], str))
        self.assertTrue(isinstance(actual[1], float))
