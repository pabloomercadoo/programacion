from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv(root)
password = os.getenv(root)
host = os.getenv(localhost)
database = os.getenv(Taller_Mecanico)

DATABASE_CONNECTION_URI = f"mysql+pymysql://{root},{root},{localhost},{Taller_Mecanico}"