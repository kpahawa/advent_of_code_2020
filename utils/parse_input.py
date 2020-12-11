from os.path import join
from typing import List


_file_path = '/utils/parse_input.py'
f = __file__.split(_file_path)[0]


_base_path = join(f, 'inputs')


def fetch_input_raw(file_name: str, base_path=_base_path) -> str:
    with open(join(base_path, file_name), 'r') as f:
        return f.read()


def fetch_input(file_name: str, base_path=_base_path, delim="\n") -> List[str]:
    raw_input = fetch_input_raw(file_name, base_path)

    contents = raw_input.split(delim)
    return list(filter(lambda x: not not x, contents))  # filter out empty strings


def fetch_input_ints(file_name: str, base_path=_base_path, delim="\n", sort=True) -> List[int]:
    raw_input = fetch_input_raw(file_name, base_path)

    contents = raw_input.split(delim)
    l = [int(i) for i in contents if i]
    return l if not sort else sorted(l)
