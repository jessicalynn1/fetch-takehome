import flask
from unittest import TestCase
import json
import server

client = app.test_client()


class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_add(self):
        """Test add function."""

        # assert that add function in Transcation class actually adds new data
        # wasn't sure how to test with no database or data to call
        
    def test_spend(self):
        """Test spend fucntion."""

        # assert that spend function in Spend class takes away points correctly
        # wasn't sure how to test with no database or data to call

    def test_balance(self):
            """Test check_balance fucntion."""

        # assert that check_balance function returns correct data
        # wasn't sure how to test with no database or data to call



if __name__ == "__main__":
    import unittest
    unittest.main()
