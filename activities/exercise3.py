import datetime
import logging

from airflow import DAG
from airflow.operators.python import PythonOperator


# TODO Complete the functions body
def hello_world():
    logging.info("Hello World")


def addition():
    logging.info(f"46 + 27 = {46 + 27}")


def subtraction():
    pass


def division():
    pass


def completed_task():
    pass


# TODO: Create a dag that runs every hour and its execution starts one day ago


# TODO: Create tasks and operators


# TODO: Configure task dependencies to have this dag
#
#                    ->  addition_task
#                   /                 \
# hello_world_task  -> division_task-> completed_task
#                   \                 /
#                    -> subtraction_task
