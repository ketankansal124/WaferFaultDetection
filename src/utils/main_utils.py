import sys
from typing import Dict, Tuple
import os
import pandas as pd
import pickle
import yaml
import boto3

from src.constant import *
from src.exception import CustomException
from src.logger import logging

class MainUtils:
    def __init__(self) -> None:
        """
        Initializes the MainUtils class. Currently, it does not require any arguments 
        or perform any actions upon instantiation.
        """
        pass

    def read_yaml_file(self, filename: str) -> dict:
        """
        Reads a YAML file and returns its contents as a dictionary.

        Args:
            filename (str): Path to the YAML file.

        Returns:
            dict: Parsed contents of the YAML file.

        Raises:
            CustomException: If there is an error in reading the file.
        """
        try:
            with open(filename, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)

        except Exception as e:
            raise CustomException(e, sys) from e

    def read_schema_config_file(self) -> dict:
        """
        Reads the schema configuration YAML file located in the 'config' directory.

        Returns:
            dict: Parsed contents of the schema configuration file.

        Raises:
            CustomException: If there is an error in reading the schema file.
        """
        try:
            schema_config = self.read_yaml_file(os.path.join("config", "schema.yaml"))
            return schema_config

        except Exception as e:
            raise CustomException(e, sys) from e

    @staticmethod
    def save_object(file_path: str, obj: object) -> None:
        """
        Saves a Python object to a file using the pickle serialization.

        Args:
            file_path (str): Path to the file where the object will be saved.
            obj (object): The object to be saved.

        Raises:
            CustomException: If there is an error during the saving process.
        """
        logging.info("Entered the save_object method of MainUtils class")

        try:
            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj)

            logging.info("Exited the save_object method of MainUtils class")

        except Exception as e:
            raise CustomException(e, sys) from e

    @staticmethod
    def load_object(file_path: str) -> object:
        """
        Loads a Python object from a file using the pickle serialization.

        Args:
            file_path (str): Path to the file from which the object will be loaded.

        Returns:
            object: The loaded Python object.

        Raises:
            CustomException: If there is an error during the loading process.
        """
        logging.info("Entered the load_object method of MainUtils class")

        try:
            with open(file_path, "rb") as file_obj:
                obj = pickle.load(file_obj)

            logging.info("Exited the load_object method of MainUtils class")

            return obj

        except Exception as e:
            raise CustomException(e, sys) from e

    @staticmethod    
    def load_object(file_path):
        """
        Loads and returns a Python object from a file using the pickle serialization.

        Args:
            file_path (str): Path to the file from which the object will be loaded.

        Returns:
            object: The loaded Python object.

        Raises:
            CustomException: If there is an error during the loading process.
        """
        try:
            with open(file_path,'rb') as file_obj:
                return pickle.load(file_obj)
        except Exception as e:
            logging.info('Exception Occured in load_object function utils')
            raise CustomException(e, sys)
