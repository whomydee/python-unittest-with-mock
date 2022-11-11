import unittest
from unittest.mock import patch, Mock

from my_utility_class import MyUtilityClass


class TestMyUtilityClass(unittest.TestCase):
	def mock_get_first_name(self):
		return "Abdul"

	def mock_get_last_name(self):
		return "Latif"

	@patch('my_utility_class.NameService')
	def test__get_name__return_correct_name__given_a_name(self, mock_name_service: Mock):
		another_mock_name_service = Mock()
		another_mock_name_service.get_first_name.return_value = "Christian"
		another_mock_name_service.get_last_name.return_value = "Bale"

		mock_name_service.return_value = another_mock_name_service

		my_class = MyUtilityClass(name="Johnny Depp")

		full_name = my_class.get_name()

		assert full_name == "Christian Bale"

		another_mock_name_service.get_first_name.assert_called_once()
		another_mock_name_service.get_last_name.assert_called_once()


if __name__ == '__main__':
	unittest.main()
