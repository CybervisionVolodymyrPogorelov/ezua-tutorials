"""
This is an example dag for using the KubernetesPodOperator.
"""
import logging

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago

log = logging.getLogger(__name__)


default_args = {
    'owner': 'airflow',
    'start_date': days_ago(2)
}

with DAG(
        dag_id='example_kubernetes_operator',
        default_args=default_args,
        schedule_interval=None,
        tags=['example'],
        access_control={
            'role_hpedemo-user01': {
                'can_read',
                'can_edit'
            }
        }
) as dag:

    tolerations = [
        {
            'key': "key",
            'operator': 'Equal',
            'value': 'value'
        }
    ]

    k = KubernetesPodOperator(
        namespace='default',
        image="ubuntu:16.04",
        cmds=["bash", "-cx"],
        arguments=["echo hello here #1"],
        labels={"foo": "bar"},
        name="airflow-test-pod",
        task_id="task",
        get_logs=True,
        is_delete_operator_pod=False,
        tolerations=tolerations
    )