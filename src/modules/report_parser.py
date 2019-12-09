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

    def _get_case_information(self, key):
        return self.soup.find("td", text=key).find_next_sibling().find("div").text

    def get_investigator(self):
        return self._get_case_information("Investigator:")

    def get_subject_name(self):
        return self._get_case_information("Subject name:")

    def get_computer_name(self):
        return self._get_case_information("Computer name:")

    def get_case_number(self):
        return self._get_case_information("Case number:")

    def get_search_timestamp(self):
        return self._get_case_information("Search timestamp:")
