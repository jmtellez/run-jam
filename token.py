from dotenv import main
import os
main.load_dotenv()
print(os.getenv('CLIENT_ID'))

# # settings.py
# import os
# from os.path import join, dirname
# # from dotenv import load_dotenv
# import dotenv
# dv = dotenv()
# dotenv_path = join(dirname(__file__), '.env')
# dv.load_dotenv(dotenv_path)

# SECRET_KEY = os.environ.get("CLIENT_ID")
# print(SECRET_KEY)