import datetime
import logging

from airflow import DAG
from airflow.operators.python import PythonOperator


def log_details(*args, **kwargs):
    #
    # TODO: Extract ds, run_id, prev_ds, and next_ds from the kwargs, and log them
    #

    logging.info(f"Execution date is {ds}")
    logging.info(f"My run id is {run_id}")
    if previous_ds:
        logging.info(f"My previous run was on {previous_ds}")
    if next_ds:
        logging.info(f"My next run will be {next_ds}")


# TODO: Create a dag that runs on a daily manner and its execution date starts two days ago


# TODO: Create the operator to execute the task
