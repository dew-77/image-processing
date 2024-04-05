from config import settings
from exceptions import IncorrectFilePathError, IncorrectImageExtensionError
from handlers import ImageHandler
from validators import ImageValidator


class ImageInterface:
    """Class for user interaction and passing data to other objects."""
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.validator = ImageValidator
        self.handler = ImageHandler

    def change_resolution(self) -> None:
        self.validate()
        resolution = self._get_resolution()

        new_file_path = self.handler(self.file_path).change_resolution(
            resolution
        )
        print(f'New image saved at {new_file_path}')

    def validate(self) -> None:
        """
        Function to catch errors from validator before handling.
        If errors are caught, the input occurs again.
        """
        try:
            self.validator(self.file_path).is_valid()
        except IncorrectFilePathError as e:
            print(e)
            self._retry_input('Try again with correct filename: ')
        except IncorrectImageExtensionError as e:
            print(e)
            self._retry_input('Try again with correct file extension: ')

    def _retry_input(self, msg: str) -> None:
        file_path = input(msg)
        self.file_path = file_path
        self.validate()

    def _get_resolution(self, msg='\nChoose number from list below.') -> dict:
        """
        Dialog to let user choose resolution for image.
        Returns resolution preset (dict).
        """

        print(msg)
        existing_presets = []
        for preset in settings.resolution_presets:
            print(
                f"({preset.index}) - {preset.name}: " +
                f"{preset.resW}x{preset.resH}")
            existing_presets.append(preset.index)

        # Validate answer
        error_msg = '\nTry again with correct number!'

        preset_index = input(": ")
        if preset_index.isdigit():
            preset_index = int(preset_index)
            if preset_index not in existing_presets:
                return self._get_resolution(error_msg)
        else:
            return self._get_resolution(error_msg)

        for preset in settings.resolution_presets:
            if preset.index == preset_index:
                return preset


if __name__ == '__main__':
    user_file = input('Enter the path to the image: ')
    interface = ImageInterface(user_file)
    interface.change_resolution()
