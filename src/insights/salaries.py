from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    max_salarys = []
    for job in jobs:
        # if len(job['max_salary']) != 0:
        if job['max_salary'].isdigit():
            max_salarys.append(int(job['max_salary']))

    return max(max_salarys)


def get_min_salary(path: str) -> int:
    jobs = read(path)
    min_salarys = []
    for job in jobs:
        if job['min_salary'].isdigit():
            min_salarys.append(int(job['min_salary']))

    return min(min_salarys)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        for job_salary in job:
            if job_salary["min_salary"] < salary < job_salary["max_salary"]:
                return True
            else:
                return False
    except ValueError:
        print("Invalid Values!")


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    valid_jobs = matches_salary_range(jobs, salary)
    filtered_jobs = []
    if valid_jobs:
        for job in jobs:
            if job["min_salary"] < salary < job["max_salary"]:
                filtered_jobs.append(job)

    return filtered_jobs
