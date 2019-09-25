# #!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from threading import Thread


class FileHandler(Thread):
    """FileHandler takes care of reading
        and writing data to files."""

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, msg):
        """Write new data to file."""
        success = False
        try:
            with open(self.file_path, 'w') as f:
                f.write(msg)
            success = True
        except FileNotFoundError:
            print("File does not exits.")
        finally:
            return success

    def read(self):
        """Read everything from file."""
        content = ''
        try:
            with open(self.file_path, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print("File does not exits.")
        finally:
            return content

    def append(self, msg):
        """Append new data to file."""
        success = False
        try:
            with open(self.file_path, 'rb') as f:
                f.write(msg)
            success = True
        except FileNotFoundError:
            print("File does not exits.")
        finally:
            return success


# Example of usage
if __name__ == "__main__":
    jsonc = FileHandler(
        "C:\\Users\\Magnus\\Documents\\Pick-And-Sort-Robot\\resources\\Objects\\objects.json")
    print(jsonc.read())
