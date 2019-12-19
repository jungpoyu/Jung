from bs4 import BeautifulSoup
from datetime import datetime

CHUNK_SIZE = 4096


class ReportParser:
    def __init__(self, folder_path):
        content_path = f"{folder_path}/_meta/content.html"
        with open(content_path, encoding="utf-8") as f:
            data = ""
            for chunk in iter(lambda: f.read(CHUNK_SIZE), f""):
                data += chunk

        self.soup = BeautifulSoup(data, "html.parser")

    def get_triage_program(self):
        return self.soup.find("h1").text.rsplit(" ", 1)[0]

    def _get_case_information(self, key):
        return (
            self.soup.find("div", text=key).parent.find_next_sibling().find("div").text
        )

    def get_investigator(self):
        return self._get_case_information("Investigator:")

    def get_subject_name(self):
        return self._get_case_information("Subject name:")

    def get_computer_name(self):
        return self._get_case_information("Computer name:")

    def get_case_number(self):
        return self._get_case_information("Case number:")

    def _get_datetime_obj(self):
        datetime_str = self._get_case_information("Search timestamp:")

        word_conversion = {"上午": "AM", "下午": "PM"}

        for k, v in word_conversion.items():
            datetime_str = datetime_str.replace(k, v)

        return datetime.strptime(datetime_str, "%Y/%m/%d %p %I:%M:%S %z")

    def get_search_timestamp(self):
        return self._get_datetime_obj().strftime("%Y-%m-%d %H:%M:%S")

    def get_time_zone(self):
        return self._get_datetime_obj().tzinfo
