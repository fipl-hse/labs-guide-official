"""
Checks the second lab getting language profiles function
"""

import unittest
from unittest.mock import patch

import pytest

from lab_2_classify_by_knn.main import get_freq_dict, get_language_profiles


class GetLanguageProfilesTest(unittest.TestCase):
    """
    Tests getting language profiles function
    """

    @pytest.mark.lab_2_classify_by_knn
    @pytest.mark.mark4
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_get_language_profiles_ideal(self):
        """
        Ideal getting language profiles scenario
        """
        corpus = [
            ["the", "boy", "is", "playing", "football"],
            ["der", "junge", "der", "fussball", "spielt"],
        ]
        labels = ["en", "de"]
        expected = {
            "en": {"the": 0.2, "boy": 0.2, "is": 0.2, "playing": 0.2, "football": 0.2},
            "de": {"der": 0.4, "junge": 0.2, "fussball": 0.2, "spielt": 0.2},
        }
        actual = get_language_profiles(corpus, labels)
        self.assertEqual(expected, actual)

    @patch("lab_2_classify_by_knn.main.get_freq_dict", side_effect=get_freq_dict)
    @pytest.mark.lab_2_classify_by_knn
    @pytest.mark.mark4
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_get_freq_dict_called(self, mock):
        """
        Get language profiles call getting frequency dictionary function check
        """
        corpus = [
            ["the", "boy", "is", "playing", "football"],
            ["der", "junge", "der", "fussball", "spielt"],
        ]
        labels = ["en", "de"]
        get_language_profiles(corpus, labels)
        self.assertTrue(mock.called)

    @pytest.mark.lab_2_classify_by_knn
    @pytest.mark.mark4
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_get_language_profiles_bad_input(self):
        """
        Get language profiles invalid input corpus or labels check
        """
        bad_inputs = ["string", {}, (), None, 9, 9.34, True, [None]]
        expected = None
        for bad_input in bad_inputs:
            actual = get_language_profiles(bad_input, bad_input)
            self.assertEqual(expected, actual)

    @pytest.mark.lab_2_classify_by_knn
    @pytest.mark.mark4
    @pytest.mark.mark6
    @pytest.mark.mark8
    @pytest.mark.mark10
    def test_get_language_profiles_return_values(self):
        """
        Get frequency dictionary return values check
        """
        corpus = [
            ["the", "boy", "is", "playing", "football"],
            ["der", "junge", "der", "fussball", "spielt"],
        ]
        labels = ["en", "de"]
        expected = 2
        actual = get_language_profiles(corpus, labels)
        self.assertEqual(expected, len(actual))
        for label in labels:
            self.assertTrue(actual[label])
        self.assertTrue(isinstance(actual[labels[0]], dict))
