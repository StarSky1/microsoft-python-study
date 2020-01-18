from dotenv import load_dotenv
import os

load_dotenv()
database=os.getenv('DATABASE')
print(database)

os_version=os.getenv('OS')
print(os_version)