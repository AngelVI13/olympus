import os
import re
from main import get_files_from_dir, compute_elevation


def test_get_files_from_dir():
    file_pattern = r".*\.py"
    files = get_files_from_dir(pattern=file_pattern, directory=".")

    assert all(re.search(file_pattern, f) for f in files)


def test_compute_elevation():
    input = """
    x = 5
    for i in range(x):
        print(i)
    """
    input_lines = input.split(os.linesep)
    print(input_lines)
    elevation = compute_elevation(input_lines)
    expected_elevation = [0, 4, 4, 8, 4]
    assert expected_elevation == list(elevation)
