import shutil


class ReportZipper:
    def __init__(self):
        pass

    def make_zip(self, folder_path, output_path):
        """
        Make zipped file from given folder path

        Arguments:
            folder_path {string} -- input folder path
            output_path {string} -- output zipped file path (without .zip extension)
        """
        shutil.make_archive(output_path, "zip", folder_path)
