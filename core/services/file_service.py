import os
import json

class FileService:
    @staticmethod
    def ensure_dir(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    @staticmethod
    def read_json(file_path, default=None):
        if not os.path.exists(file_path):
            return default if default is not None else {}
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading JSON from {file_path}: {e}")
            return default if default is not None else {}

    @staticmethod
    def write_json(file_path, data, indent=2):
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=indent)
            return True
        except Exception as e:
            print(f"Error writing JSON to {file_path}: {e}")
            return False

    @staticmethod
    def read_file(file_path):
        if not os.path.exists(file_path):
            return ""
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    @staticmethod
    def write_file(file_path, content):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    @staticmethod
    def get_size(file_path):
        if not os.path.exists(file_path):
            return 0
        return os.path.getsize(file_path)
