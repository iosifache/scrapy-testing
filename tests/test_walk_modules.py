"""Unit tests for scrapy.utils.misc.walk_modules

Method type: Returning a list
"""

import typing
from inspect import ismodule

import pytest
from scrapy.utils.misc import walk_modules


def __check_valid_module(module: typing.Any, parent_module: str) -> bool:
    return ismodule(module) and module.__name__.startswith(parent_module)


@pytest.mark.timeout(0.1)
def test_zero_submodules() -> None:
    """Tests if a module containing no submodule is correctly walked.

    Testing principles: right, cardinality with 0 elements, performance,
        conformance, inverse relationship
    """
    modules = walk_modules("modules.zero")

    assert (
        len(modules) - 1 == 0
    ), "The lack of submodules was not correctly reported."


@pytest.mark.timeout(0.1)
def test_one_submodule() -> None:
    """Tests if a module containing one submodule is correctly walked.

    Testing principles: right, cardinality with 1 element, performance,
        conformance, inverse relationship
    """
    target_module = "modules.one"
    modules = walk_modules(target_module)

    assert len(modules) - 1 == 1, "The single submodule was not returned."
    assert __check_valid_module(
        modules[1], target_module
    ), "The returned submodule is not a correct sub-module."


@pytest.mark.timeout(0.1)
def test_multiple_submodules() -> None:
    """Tests if a module containing one submodule is correctly walked.

    Testing principles: right, cardinality with N elements, performance,
        conformance, inverse relationship
    """
    target_module = "modules.two"
    modules = walk_modules(target_module)

    assert len(modules) - 1 == 2, "The two submodules were not returned."
    for module in modules:
        assert __check_valid_module(
            module, target_module
        ), "A returned object is not a correct sub-module."


@pytest.mark.timeout(0.1)
def test_invalid_module() -> None:
    """Tests if an error is raised when walking an invalid module.

    Testing principles: right, error, performance
    """
    try:
        walk_modules("doublethink")
    except ModuleNotFoundError:
        pass
    else:
        assert False, "No error was raised when walking an invalid module."


@pytest.mark.timeout(0.1)
def test_local_module() -> None:
    """Tests if an error is raised when walking a local module.

    Testing principles: right, error, performance
    """
    try:
        walk_modules(".crimethought")
    except TypeError:
        pass
    else:
        assert False, "No error was raised when walking a local module."
