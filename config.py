from decouple import config

# Loading database configuration from the .env file
DATABASE_URL = config('DATABASE_URL')
