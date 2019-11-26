import shutil


class ReportZipper:
    def __init__(self):
        pass

    def make_zip(self, folder_path, output_path):
        shutil.make_archive(output_path, "zip", folder_path)
