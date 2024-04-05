import os

from PIL import Image

from config import settings, ResolutionPreset


class ImageHandler:
    """Class for operations with images."""
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.basename, self.extension = os.path.splitext(self.file_path)
        self.image = Image.open(self.file_path)

    def change_resolution(
        self, resolution_preset: ResolutionPreset
    ) -> str:
        """
        Function to change image resolution and save new image.
        Returns path to modified file.
        """
        new_height = resolution_preset.resH
        new_weight = resolution_preset.resW
        new_size = resolution_preset.name
        resized_img = self.image.resize(
            (new_height, new_weight), Image.LANCZOS
        )

        self.check_path_exists(settings.directory_to_save)
        absolute_basename = self.basename.split("/")[-1]
        new_filename = f'{absolute_basename}_{new_size}{self.extension}'
        new_path = f'{settings.directory_to_save}{new_filename}'

        if resolution_preset.quality is not None:
            resized_img.save(
                new_path, quality=resolution_preset.quality)
        else:
            resized_img.save(new_path)

        return new_path

    def check_path_exists(self, directory: str) -> None:
        if not os.path.exists(directory):
            os.makedirs(directory)
