import os
from dotenv import load_dotenv 

load_dotenv()
try:
    URL = os.environ['URL']
except Exception as error:
    raise Exception(
        "Não foi possivel carregar variavel de ambiente:\n"\
        f"{error}"
    )