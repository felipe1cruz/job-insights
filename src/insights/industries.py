from typing import List, Dict
from jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    unique_industries = []
    for job in jobs:
        if job['industry'] not in unique_industries:
            unique_industries.append(job['industry'])

    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
