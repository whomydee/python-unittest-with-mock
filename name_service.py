class NameService:

	def get_first_name(self, name: str) -> str:
		return name.split()[0]

	def get_last_name(self, name: str) -> str:
		return name.split()[-1]
