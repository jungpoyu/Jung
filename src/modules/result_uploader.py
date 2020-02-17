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
