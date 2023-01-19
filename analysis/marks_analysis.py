# /usr/bin/env python3

import ast
import os
import typing
from collections import defaultdict
from dataclasses import dataclass

from tabulate import tabulate


@dataclass
class UnitTest:
    name: str
    decorators: typing.List[str]


def main():
    marks = get_marks()

    print_table(marks)


def print_table(marks: dict) -> None:
    table = create_markdown_table(marks)

    print(table)


def create_markdown_table(marks: dict) -> str:
    formatted_keys = [f"`{mark}`" for mark in marks.keys()]

    table = tabulate(
        {"Mark": formatted_keys, "Count": marks.values()},
        ["Mark", "Count"],
        tablefmt="github",
    )

    return table


def get_marks() -> dict:
    marks_count: typing.Dict[str, int] = defaultdict(int)
    for test in get_all_tests():
        for decorator in test.decorators:
            marks_count[decorator] += 1

    sorted_marks_count = dict(sorted(marks_count.items()))

    return sorted_marks_count


def get_all_tests() -> typing.Generator[UnitTest, None, None]:
    for unit_filename in iterate_folder():
        yield from get_tests_from_file(unit_filename)


def iterate_folder() -> typing.Generator[str, None, None]:
    yield from [
        os.path.join("tests", filename)
        for filename in os.listdir("tests")
        if is_unit_test_file(filename)
    ]


def is_unit_test_file(filename: str) -> bool:
    return filename.startswith("test_") and filename.endswith(".py")


def get_tests_from_file(
    filename: str,
) -> typing.Generator[UnitTest, None, None]:
    with open(filename) as file:
        node = ast.parse(file.read())

    for node in node.body:  # type: ignore [assignment]
        if isinstance(node, ast.FunctionDef) and is_unit_test(node.name):
            decorators = []
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Call):
                    decorator_name = (
                        decorator.func.attr
                        if isinstance(decorator.func, ast.Attribute)
                        else decorator.func.id  # type: ignore [attr-defined]
                    )
                else:
                    decorator_name = (
                        decorator.attr
                        if isinstance(decorator, ast.Attribute)
                        else decorator.id  # type: ignore [attr-defined]
                    )

                if is_valid_mark(decorator_name):
                    decorators.append(decorator_name)

            yield UnitTest(node.name, decorators)


def is_unit_test(function_name: str) -> bool:
    return function_name.startswith("test_")


def is_valid_mark(decorator_name: str) -> bool:
    return decorator_name != "timeout"


if __name__ == "__main__":
    main()
