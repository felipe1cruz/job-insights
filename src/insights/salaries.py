from typing import Union, List, Dict
from jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    max_salarys = []
    for job in jobs:
        if job['max_salary'] not in max_salarys and job['max_salary'] != "":
            max_salarys.append(int(job['max_salary']))

    return min(max_salarys)


def get_min_salary(path: str) -> int:
    jobs = read(path)
    min_salarys = []
    for job in jobs:
        if job['min_salary'] not in min_salarys and job['min_salary'] != "":
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
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
