from name_service import NameService


class MyUtilityClass:
	def __init__(self, name: str):
		self.name = name
		self.__name_service = NameService()

	def get_name(self) -> str:

		first_name = self.__name_service.get_first_name(self.name)
		print(f"[Log] First Name: {first_name}")

		second_name = self.__name_service.get_last_name(self.name)
		print(f"[Log] Last Name: {second_name}")

		full_name = first_name + " " + second_name

		print(f"[Log] Returning Name: {full_name}")

		return full_name
