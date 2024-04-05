from config import settings


class IncorrectFileExtensionError(Exception):
    """Base class for errors in file extension"""
    def __init__(self, extension: str) -> None:
        self.extension = extension
        super().__init__(f'Incorrect file extension: {extension}')


class IncorrectImageExtensionError(IncorrectFileExtensionError):
    """Exception for errors in image file extension"""
    def __init__(self, extension: str) -> None:
        super().__init__(extension)

    def __str__(self) -> str:
        allowed_extensions_str = ', '.join(settings.allowed_extensions)
        return f'Incorrect image extension: "{self.extension}". ' + \
            f'Must be one of: {allowed_extensions_str}'


class IncorrectFilePathError(BaseException):
    """Exception for error in path to file"""
    def __init__(self) -> None:
        super().__init__('File does not exists.')
