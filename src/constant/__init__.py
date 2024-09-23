from dotenv import load_dotenv
import os

load_dotenv()

AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")
MONGO_DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME")
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")

TARGET_COLUMN = "quality"
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder = os.getenv("ARTIFACT_FOLDER", "artifacts")
