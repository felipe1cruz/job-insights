from src.pre_built.brazilian_jobs import read_brazilian_file

path = 'tests/mocks/brazilians_jobs.csv'


def test_brazilian_jobs():
    brazilian_jobs = read_brazilian_file(path)
    for job in brazilian_jobs:
        keys = list(job.keys())
        assert keys == ['title', 'salary', 'type']
