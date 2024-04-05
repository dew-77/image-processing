import os
from exceptions import IncorrectFilePathError, IncorrectImageExtensionError
from config import settings


class FileValidator:
    """Base class for validation of any files"""
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def validate_file_exists(self) -> None:
        if not os.path.exists(self.file_path):
            raise IncorrectFilePathError()


class ImageValidator(FileValidator):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def is_valid(self) -> None:
        self.validate_file_exists()
        self.validate_extension()

    def validate_extension(self) -> None:
        basename, extension = os.path.splitext(self.file_path)
        if extension[1:] not in settings.allowed_extensions:
            raise IncorrectImageExtensionError(extension)
