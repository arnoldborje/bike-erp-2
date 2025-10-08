from dotenv import load_dotenv
import os

load_dotenv()

environment = os.getenv('APP_ENVIRONMENT', 'local')

if environment == 'production':
    from .production import *
else:
    from .local import *