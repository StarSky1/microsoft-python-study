Using dotenv
# install python-dotenv
pip install python-dotenv

Store environment variables in text file
Don't hard code
Don't check sensitive values into source control
# .env file
DATABASE=Sample_Connection_String

# app.py
from dotenv import load_dotenv
import os

load_dotenv()
database=os.getenv('DATABASE')
print(databse)

Final  notes

Don't hard code sensitive information ever
Use dotenv for a simple solution
Add .env to .gitignore
Consider full encryption options
Azure key Vault