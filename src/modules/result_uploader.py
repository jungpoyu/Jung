import utils.bigquery_util as bq_util


class ResultUploader:
    _dataset = "Jung"
    _table = "Evidence_V1"
    _schema = [
        {"name": "CaseID", "type": "STRING", "mode": "REQUIRED"},
        {"name": "EvidenceType", "type": "STRING", "mode": "REQUIRED"},
        {"name": "EvidenceID", "type": "INTEGER", "mode": "REQUIRED"},
        {"name": "SeizureLocation", "type": "STRING", "mode": "REQUIRED"},
        {"name": "Perpetrator", "type": "STRING", "mode": "REQUIRED"},
        {"name": "EvidenceDescription", "type": "STRING", "mode": "REQUIRED"},
        {"name": "EvidenceHash", "type": "STRING", "mode": "REQUIRED"},
        {"name": "Quantity", "type": "INTEGER", "mode": "REQUIRED"},
        {"name": "Investigator", "type": "STRING", "mode": "REQUIRED"},
        {"name": "SearchTimestamp", "type": "STRING", "mode": "REQUIRED"},
        {"name": "TimeZone", "type": "STRING", "mode": "REQUIRED"},
        {"name": "ZipHash", "type": "STRING", "mode": "REQUIRED"},
        {"name": "IsTransferred", "type": "BOOLEAN", "mode": "REQUIRED"},
    ]

    def __init__(self):
        if bq_util.is_dataset_exist(self._dataset) == False:
            bq_util.try_create_dataset(self._dataset)
            print(f'create dataset "{self._dataset}"')

        if bq_util.is_table_exist(self._dataset, self._table) == False:
            bq_util.try_create_table(self._dataset, self._table, self._schema)
            print(f'create table "{self._table}" under dataset "{self._dataset}"')

    def _get_new_evidence_id(self, case_id):
        sql = f'SELECT EvidenceID FROM {self._dataset}.{self._table} WHERE CaseID = "{case_id}" AND EvidenceType = "D"'
        results = bq_util.execute_query(sql)

        return max([row.EvidenceID for row in results], default=0) + 1

    def upload_result(
        self,
        case_id,
        perpetrator,
        evidence_description,
        investigator,
        search_timestamp,
        time_zone,
        zip_hash,
    ):
        data = {
            "CaseID": f"{case_id}",
            "EvidenceType": "D",
            "EvidenceID": self._get_new_evidence_id(case_id),
            "SeizureLocation": "computer",
            "Perpetrator": f"{perpetrator}",
            "EvidenceDescription": f"{evidence_description}",
            "EvidenceHash": "",
            "Quantity": 1,
            "Investigator": f"{investigator}",
            "SearchTimestamp": f"{search_timestamp}",
            "TimeZone": f"{time_zone}",
            "ZipHash": f"{zip_hash}",
            "IsTransferred": False,
        }

        columns = data.keys()
        values = [f'"{v}"' if isinstance(v, str) else str(v) for v in data.values()]

        sql = f"INSERT INTO {self._dataset}.{self._table} ({','.join(columns)}) VALUES ({','.join(values)})"
        bq_util.execute_query(sql)
