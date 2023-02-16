from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        file_reader = csv.DictReader(file)
        jobs_list = []
        for row in file_reader:
            jobs_list.append(row)
    return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    unique_jobs = []
    for job in jobs:
        if job['job_type'] not in unique_jobs:
            unique_jobs.append(job['job_type'])

    return unique_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    job_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_list.append(job)

    return job_list
