from utils.parse_input import fetch_input_raw
from typing import List, Callable
from utils.timer import time_me, benchmark


class Field:
    def __init__(self, field_name, value, validator: Callable, required=True):
        self.field_name = field_name
        self.value = value
        self.required = required
        self.validator = validator

    def validate(self) -> bool:
        if self.value is None:
            return False

        return self.validator(self.value)


def _validate_years(min_year, max_year) -> Callable:
    def _inner(x):
        try:
            x = int(x)
            return min_year <= x <= max_year
        except:
            return False
    return _inner


def _validate_height(x) -> bool:
    if len(x) < 2:
        return False
    units = x[-2:]
    if len(x[:-2]) == 0:
        return False

    measurement = int(x[:-2])
    if units == 'cm':
        return 150 <= measurement <= 193

    if units == 'in':
        return 59 <= measurement <= 76

    return False


def _validate_haircolor(x) -> bool:
    if len(x) != 7 or x[0] != '#':
        return False

    for i in x[1:]:
        if not (48 <= ord(i) <= 57 or 97 <= ord(i) <= 102):
            return False
    return True


def _validate_pid(x: str) -> bool:
    if len(x) != 9:
        return False
    return x.isdigit()


class Passport:
    _required_fields = {
        'byr': _validate_years(1920, 2002),
        'iyr': _validate_years(2010, 2020),
        'eyr': _validate_years(2020, 2030),
        'hgt': _validate_height,
        'hcl': _validate_haircolor,
        'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': _validate_pid,
    }

    _optional_fields = {
        'cid': lambda _: True,
    }

    def __init__(self, **kwargs):
        self.required_fields = []
        self.optional_fields = []

        for i, t in self._required_fields.items():
            value = None
            if i in kwargs:
                value = kwargs[i]

            f = Field(field_name=i, value=value, validator=t)
            self.required_fields.append(f)

        for i, t in self._optional_fields.items():
            value = None
            if i in kwargs:
                value = kwargs[i]

            f = Field(field_name=i, value=value, required=False, validator=t)
            self.optional_fields.append(f)

    def __tostr(self):
        s = []
        for f in self.required_fields:
            s.append('{}: ({}, {})'.format(f.field_name, f.value, f.validate()))
        fields = "\t".join(s)
        return f"<{fields}>"

    def __str__(self):
        return self.__tostr()

    def __repr__(self):
        return self.__tostr()

    def validate_p1(self) -> bool:
        for i in self.required_fields:
            if i.value is None:
                return False

        return True

    def validate_p2(self) -> bool:
        for i in self.required_fields:
            if not i.validate():
                return False

        return True


@time_me
def part1(passport_fields: List[str]) -> int:
    """
    find all valid passports
    """
    passports = []
    curr_pass = {}
    for line in passport_fields:
        if line == '':
            passports.append(Passport(**curr_pass))
            curr_pass = {}
            continue
        for item in line.split():
            k, v = item.split(':')
            curr_pass[k] = v

    if len(curr_pass) > 0:
        passports.append(Passport(**curr_pass))

    return len(list(filter(lambda p: p.validate_p2(), passports)))


def test_input() -> str:
    return"""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""


def main():
    problem_input = fetch_input_raw('day4-input.txt')
    print("part 1 solution: {}".format(part1(problem_input.splitlines())))


if __name__ == '__main__':
    main()
