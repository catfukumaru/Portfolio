import unittest
from unittest.mock import patch #to simulate user input. This allows you to provide predefined inputs without requiring actual user interaction during the test.
import io
from main import *

class Test_ask_pl_name(unittest.TestCase):
    @patch('builtins.input', side_effect=['Alice'])
    def test_type(self, mock_input):
        result = ask_pl_name()
        self.assertEqual(type(result), str)  # add assertion here

    @patch('builtins.input', side_effect=['', 'John'])
    def test_emptiness(self, mock_input):
        result = ask_pl_name()
        self.assertEqual(result, 'John')  # add assertion here

    @patch('builtins.input', side_effect=['134', ':@[[[]]', '1jamie2', '                             ', '12jamie', 'Anna'])
    def test_invalid_characters(self, mock_input):
        result = ask_pl_name()
        self.assertEqual(result, 'Anna')  # add assertion here

## ask black box ai the right way to test .input() cause i need to keep inserting the asnwer to test

class Test_add_player(unittest.TestCase):
    def setUp(self):
        """Reset the global variable before each test."""
        player_names.clear()  # Reset to initial state

    # testing that the list gets changed

    def test_modify_global_variable(self):
        """Test that the global variable is modified correctly."""
        add_player('Amie')  # Call the function to modify the global variable
        self.assertEqual(player_names, ['Amie'])  # Check if the global variable is now 10

    def test_modify_global_list_multiple(self):
        """Test that the global list can be modified multiple times."""
        add_player('Trixie')
        add_player('Mikayla')
        self.assertEqual(player_names, ['Trixie', 'Mikayla'])

    # testing that ask_pl_name gets called
    @patch('main.ask_pl_name')  # Patch ask_pl_name in the main module
    def test_add_player_calls_ask_pl_name(self, mock_ask_pl_name):
        add_player('Trixie')
        add_player('Trixie')
        # if the same name is inputted twice in the function then on the second time then the ask_pl_name should be called
        mock_ask_pl_name.assert_called_once()  # Assert that ask_pl_name was called exactly once

    @patch('main.ask_pl_name')  # Patch ask_pl_name in the main module
    def test_add_player_calls_ask_pl_name_last(self, mock_ask_pl_name):
        '''
        checks 2 conditions at the same time. What the list contains and that ask_pl_name was called once
        :param mock_ask_pl_name: replacement for the ask_pl_name function
        :return:
        '''
        add_player('Trixie')
        add_player('Valerie')
        add_player('Trixie')
        add_player('George')
        self.assertEqual(player_names, ['Trixie', 'Valerie', 'George'])  # Check if the collected names are correct
        mock_ask_pl_name.assert_called_once()  # Assert that ask_pl_name was called exactly once

class Test_choose_where_is_carrot(unittest.TestCase):
    def test_return_value_range(self):
        for _ in range(100):  # Test the function multiple times
            testing_box = choose_where_is_carrot()
            self.assertIn(testing_box, [0, 1], "The function should return either 0 or 1.")

class Test_print_carrot(unittest.TestCase):
    def setUp(self):
        # Code to set up test environment
        self.mock_player_name = ["Alice", "Beatrix"]

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_carrot_carrot_first_player(self, mock_stdout):
        print_carrot(True, self.mock_player_name[0])

        # Get the printed output
        output = mock_stdout.getvalue()
        # Assert that the output is as expected
        self.assertEqual(output.strip(), "Alice has the carrot")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_carrot_no_carrot_first_player(self, mock_stdout):
        print_carrot(False, self.mock_player_name[0])

        # Get the printed output
        output = mock_stdout.getvalue()
        # Assert that the output is as expected
        self.assertEqual(output.strip(), "Alice doesn\'t have the carrot")


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_carrot_carrot_second_player(self, mock_stdout):
        print_carrot(True, self.mock_player_name[1])

        # Get the printed output
        output = mock_stdout.getvalue()
        # Assert that the output is as expected
        self.assertEqual(output.strip(), "Beatrix has the carrot")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_carrot_no_carrot_second_player(self, mock_stdout):
        print_carrot(False, self.mock_player_name[1])

        # Get the printed output
        output = mock_stdout.getvalue()
        # Assert that the output is as expected
        self.assertEqual(output.strip(), "Beatrix doesn\'t have the carrot")

class TestLieInput(unittest.TestCase):

    @patch('builtins.input', side_effect=['T'])
    def test_truth_response(self, mock_input):
        result = lie_input()
        self.assertEqual(result, 'T')

    @patch('builtins.input', side_effect=['L'])
    def test_lie_response(self, mock_input):
        result = lie_input()
        self.assertEqual(result, 'L')

    @patch('builtins.input', side_effect=['A', 'B', 'T'])
    def test_invalid_inputs_then_truth(self, mock_input):
        result = lie_input()
        self.assertEqual(result, 'T')

    @patch('builtins.input', side_effect=['X', 'Y', 'L'])
    def test_invalid_inputs_then_lie(self, mock_input):
        result = lie_input()
        self.assertEqual(result, 'L')

    @patch('builtins.input', side_effect=['A', 'B', 'C', 'D', 'T'])
    def test_multiple_invalid_inputs_then_truth(self, mock_input):
        result = lie_input()
        self.assertEqual(result, 'T')

    @patch('builtins.input', side_effect=['A', 'B', 'C', 'D', 'L'])
    def test_multiple_invalid_inputs_then_lie(self, mock_input):
        result = lie_input()
        self.assertEqual(result, 'L')

class Test_lie_about_carrot(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lie_about_carrot_lie_carrot(self, mock_stdout):
        lie_about_carrot(True, 'T')

        # Get the printed output
        output = mock_stdout.getvalue()
        # Assert that the output is as expected
        self.assertEqual(output.strip(), "I have the carrot")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lie_about_carrot_not_lie_carrot(self, mock_stdout):
        lie_about_carrot(True, 'L')

        # Get the printed output
        output = mock_stdout.getvalue()
        # Assert that the output is as expected
        self.assertEqual(output.strip(), "I don't have the carrot")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lie_about_no_carrot_lie_no_carrot(self, mock_stdout):
        lie_about_carrot(False, 'T')

        # Get the printed output
        output = mock_stdout.getvalue()
        # Assert that the output is as expected
        self.assertEqual(output.strip(), "I don't have the carrot")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_lie_about_no_carrot_lie_carrot(self, mock_stdout):
        lie_about_carrot(False, 'L')

        # Get the printed output
        output = mock_stdout.getvalue()
        # Assert that the output is as expected
        self.assertEqual(output.strip(), "I have the carrot")

class Test_second_player_route(unittest.TestCase):
    @patch('builtins.input', side_effect=['Y'])
    def test_swap_boxes(self, mock_input):
        box1, box2 = second_player_route(True, False)
        self.assertEqual(box1, False)
        self.assertEqual(box2, True)

    @patch('builtins.input', side_effect=['N'])
    def test_no_swap_boxes(self, mock_input):
        box1, box2 = second_player_route(True, False)
        self.assertEqual(box1, True)
        self.assertEqual(box2, False)

    @patch('builtins.input', side_effect=['A', 'Y'])
    def test_invalid_input_then_swap(self, mock_input):
        box1, box2 = second_player_route(True, False)
        self.assertEqual(box1, False)
        self.assertEqual(box2, True)

    @patch('builtins.input', side_effect=['A', 'N'])
    def test_invalid_input_then_no_swap(self, mock_input):
        box1, box2 = second_player_route(True, False)
        self.assertEqual(box1, True)
        self.assertEqual(box2, False)

    @patch('builtins.input', side_effect=['A', 'B', 'Y'])
    def test_multiple_invalid_inputs_then_swap(self, mock_input):
        box1, box2 = second_player_route(True, False)
        self.assertEqual(box1, False)
        self.assertEqual(box2, True)

    @patch('builtins.input', side_effect=['A', 'B', 'N'])
    def test_multiple_invalid_inputs_then_no_swap(self, mock_input):
        box1, box2 = second_player_route(True, False)
        self.assertEqual(box1, True)
        self.assertEqual(box2, False)

if __name__ == '__main__':
    unittest.main()