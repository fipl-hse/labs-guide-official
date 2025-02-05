"""
Checks the second lab calculate_cumulative_score_for_candidates function
"""

import unittest

import pytest

from lab_2_keywords_cooccurrence.main import calculate_cumulative_score_for_candidates


class CalculateCumulativeScoreForCandidatesTest(unittest.TestCase):
    """
    Tests calculate_cumulative_score_for_candidates function
    """

    @pytest.mark.lab_2_keywords_cooccurrence
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_calculate_cumulative_score_for_candidates_basic(self):
        """
        Ensure function calculates cumulative score for candidates correctly
        """
        candidate_keyword_phrases = [
            ("времена", "советского", "союза", "исследование", "космоса"),
            ("одной",),
            ("важнейших", "задач"),
            ("времена", "союза", "прошли"),
            ("важнейших", "задач"),
            ("времена", "союза", "прошли"),
        ]
        word_scores = {
            "времена": 4.0,
            "советского": 5.0,
            "союза": 4.0,
            "исследование": 5.0,
            "космоса": 5.0,
            "одной": 1.0,
            "важнейших": 2.0,
            "задач": 2.0,
            "прошли": 3.0,
        }
        expected = {
            ("времена", "советского", "союза", "исследование", "космоса"): 23,
            ("одной",): 1,
            ("важнейших", "задач"): 4,
            ("времена", "союза", "прошли"): 11,
        }
        actual = calculate_cumulative_score_for_candidates(candidate_keyword_phrases, word_scores)
        self.assertEqual(expected, actual)

    @pytest.mark.lab_2_keywords_cooccurrence
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_calculate_cumulative_score_for_candidates_scores_do_not_contain_all_words(self):
        """
        Ensure function returns None when scores don't contain all words
        """
        candidate_keyword_phrases = [
            ("времена", "советского", "союза", "исследование", "космоса"),
            ("одной",),
            ("важнейших", "задач"),
            ("времена", "союза", "прошли"),
        ]
        word_scores = {"времена": 4.0, "советского": 5.0, "союза": 4.0, "исследование": 5.0}
        expected = None
        actual = calculate_cumulative_score_for_candidates(candidate_keyword_phrases, word_scores)
        self.assertEqual(expected, actual)

    @pytest.mark.lab_2_keywords_cooccurrence
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_calculate_cumulative_score_for_candidates_candidates_do_not_contain_all_words(self):
        """
        Ensure function calculates cumulative score for candidates correctly
        when candidates don't contain all words
        """
        candidate_keyword_phrases = [
            ("времена", "советского", "союза", "исследование", "космоса"),
            ("одной",),
        ]
        word_scores = {
            "времена": 4.0,
            "советского": 5.0,
            "союза": 4.0,
            "исследование": 5.0,
            "космоса": 5.0,
            "одной": 1.0,
            "важнейших": 2.0,
            "задач": 2.0,
            "прошли": 3.0,
        }
        expected = {
            ("времена", "советского", "союза", "исследование", "космоса"): 23,
            ("одной",): 1,
        }
        actual = calculate_cumulative_score_for_candidates(candidate_keyword_phrases, word_scores)
        self.assertEqual(expected, actual)

    @pytest.mark.lab_2_keywords_cooccurrence
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_calculate_cumulative_score_for_candidates_empty_arguments(self):
        """
        Ensure function returns None for empty arguments
        """
        candidate_keyword_phrases = [
            ("времена", "советского", "союза", "исследование", "космоса"),
            ("одной",),
            ("важнейших", "задач"),
            ("времена", "союза", "прошли"),
        ]
        word_scores = {
            "времена": 4.0,
            "советского": 5.0,
            "союза": 4.0,
            "исследование": 5.0,
            "космоса": 5.0,
            "одной": 1.0,
            "важнейших": 2.0,
            "задач": 2.0,
            "прошли": 3.0,
        }
        expected = None
        actual = calculate_cumulative_score_for_candidates(candidate_keyword_phrases, {})
        self.assertEqual(expected, actual)
        actual = calculate_cumulative_score_for_candidates([], word_scores)
        self.assertEqual(expected, actual)

    @pytest.mark.lab_2_keywords_cooccurrence
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_calculate_cumulative_score_for_candidates_wrong_argument_types(self):
        """
        Ensure function returns None for wrong argument types
        """
        candidate_keyword_phrases = [
            ("времена", "советского", "союза", "исследование", "космоса"),
            ("одной",),
            ("важнейших", "задач"),
            ("времена", "союза", "прошли"),
        ]
        word_scores = {
            "времена": 4.0,
            "советского": 5.0,
            "союза": 4.0,
            "исследование": 5.0,
            "космоса": 5.0,
            "одной": 1.0,
            "важнейших": 2.0,
            "задач": 2.0,
            "прошли": 3.0,
        }
        expected = None

        wrong_inputs = [4, 4.0, False, {"dict": 0}]
        for wrong_input in wrong_inputs:
            actual = calculate_cumulative_score_for_candidates(wrong_input, word_scores)
            self.assertEqual(expected, actual)

        wrong_inputs = [4, 4.0, False, ["list"]]
        for wrong_input in wrong_inputs:
            actual = calculate_cumulative_score_for_candidates(
                candidate_keyword_phrases, wrong_input
            )
            self.assertEqual(expected, actual)
