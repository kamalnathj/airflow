import os
import airflow
from datetime import datetime
from airflow import DAG
from pathlib import Path
from airflow import models
from airflow.operators import bash_operator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator

