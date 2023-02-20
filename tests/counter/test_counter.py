from src.pre_built.counter import count_ocurrences
import pytest


def test_counter():
    assert count_ocurrences('data/jobs.csv', 'systems') == 3176
    assert count_ocurrences('data/jobs.csv', 'Marketing') == 1259

    with pytest.raises(AttributeError):
        count_ocurrences('data/jobs.csv', 156156)
