import datetime
import logging
import os

from airflow import DAG
from airflow.operators.python import PythonOperator


def start():
    logging.info("Hey fellow! This is our start task")


def current_time():
    logging.info(f"Another task at time: {datetime.datetime.now().isoformat()}")


def working_dir():
    logging.info(f"Current working directory: {os.getcwd()}")


def end():
    logging.info("The final task of our multitask DAG!!")


# TODO: Create a dag that runs every hour and its execution starts one day ago

dag = DAG()


# TODO: Create tasks and operators


# TODO: Configure task dependencies to have this dag
#
#                     -> current_time_task
#                   /                      \
# start_task -------                        ---> end_task
#                   \                     /
#                     -> working_dir_task
