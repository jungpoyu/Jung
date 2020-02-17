from google.cloud import bigquery
from google.cloud.exceptions import NotFound
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "PATH_TO_CERTIFICATION_FILE"


def is_dataset_exist(dataset_name):
    client = bigquery.Client()
    datasets = [item.dataset_id for item in client.list_datasets()]

    return True if dataset_name in datasets else False


def is_table_exist(target_dataset_name, table_name):
    client = bigquery.Client()
    dataset_ref = client.dataset(target_dataset_name)
    tables = [item.table_id for item in client.list_tables(dataset_ref)]

    return True if table_name in tables else False


def try_create_dataset(dataset_name):
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset_name)

    try:
        client.get_dataset(dataset_ref)
        return False
    except NotFound:
        dataset = bigquery.Dataset(dataset_ref)
        dataset = client.create_dataset(dataset)
        return True


def try_create_table(target_dataset_name, table_name, table_schema):
    client = bigquery.Client()
    dataset_ref = client.dataset(target_dataset_name)
    table_ref = dataset_ref.table(table_name)

    try:
        client.get_table(table_ref)
        return False
    except NotFound:
        schema = [
            bigquery.SchemaField(item["name"], item["type"], item["mode"])
            for item in table_schema
        ]
        table = bigquery.Table(table_ref, schema=schema)
        table = client.create_table(table)
        return True


def execute_query(query_sql):
    client = bigquery.Client()

    query_job = client.query(query_sql)
    results = query_job.result()

    return results
