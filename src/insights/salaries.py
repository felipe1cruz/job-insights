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
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    
    try:
        if int(job["max_salary"]) - int(job["min_salary"]) < 0:
            raise ValueError
        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    except (ValueError, KeyError, TypeError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except (ValueError):
            print(ValueError)
    return filtered_jobs
