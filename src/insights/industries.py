from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    unique_industries = []
    for job in jobs:
        if job['industry'] != "" and job['industry'] not in unique_industries:
            unique_industries.append(job['industry'])

    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    job_industry_list = []
    for job in jobs:
        if job["industry"] == industry:
            job_industry_list.append(job)

    return job_industry_list
