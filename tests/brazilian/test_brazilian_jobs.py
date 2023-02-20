from src.pre_built.brazilian_jobs import read_brazilian_file

result_index_zero = {'title': 'Maquinista',
                     'salary': '2000',
                     'type': 'trainee'}
path = 'tests/mocks/brazilians_jobs.csv'


def test_brazilian_jobs():
    brazilian_jobs = read_brazilian_file(path)
    assert brazilian_jobs[0] == result_index_zero
    for job in brazilian_jobs:
        keys = [job.keys()]
        assert keys == ['title', 'salary', 'type']
