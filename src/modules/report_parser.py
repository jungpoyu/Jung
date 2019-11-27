from bs4 import BeautifulSoup

CHUNK_SIZE = 4096


class ReportParser:
    def __init__(self, folder_path):
        content_path = f"{folder_path}/_meta/content.html"
        with open(content_path, encoding="utf-8") as f:
            data = ""
            for chunk in iter(lambda: f.read(CHUNK_SIZE), f""):
                data += chunk

        self.soup = BeautifulSoup(data, "html.parser")
