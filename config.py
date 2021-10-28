import os

class Config:

	def __init__(self):

		self.DB_PLATFORM = "postgresql"
		self.DB_SERVER = "localhost"
		self.DB_NAME = "noteapp"
		self.DB_USERNAME = "postgres"
		self.DB_PASSWORD = "juice"

		self.SECRET_KEY = 'Ini Harusnya Rahasia'

		self.DB_URL=f"{self.DB_PLATFORM}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_SERVER}/{self.DB_NAME}" #WINDOWS
		#self.DB_URL=f"{self.DB_PLATFORM}://{self.DB_SERVER}/{self.DB_NAME}"

	def check_env(self):
		print(self.DB_USERNAME, self.DB_PASSWORD)

if __name__ == '__main__':
	myConfig = Config()
	myConfig.check_env()
