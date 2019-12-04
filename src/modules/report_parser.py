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

    def get_investigator(self):
        return (
            self.soup.find("td", text="Investigator:")
            .find_next_sibling()
            .find("div")
            .text
        )

    def get_subject_name(self):
        return (
            self.soup.find("td", text="Subject name:")
            .find_next_sibling()
            .find("div")
            .text
        )

    def get_computer_name(self):
        return (
            self.soup.find("td", text="Computer name:")
            .find_next_sibling()
            .find("div")
            .text
        )

    def get_case_number(self):
        return (
            self.soup.find("td", text="Case number:")
            .find_next_sibling()
            .find("div")
            .text
        )
