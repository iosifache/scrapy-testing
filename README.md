# `scrapy` Unit Tests

## Description 🖼️

This repository holds (toy) **`pytest` unit tests for `scrapy`**, a Python library for scrapping and crawling websites. It was created for a course from Faculty of Automatic Control and Computers, University POLITEHNICA of Bucharest, namely "Cybersecurity Incidents Management".

### Overview

In total, there are **52 tests** that are passing with the frozen versions of libraries. All **78 asserts** have a **suggestive message**. Each test has a short **documentation** explaining what it checks, and a **timeout** attached: `0.1` seconds for offline tests and more for those that requires Internet connection (for example, those scrapping a website).

In addition, the source files were formatted with **Black** and **isort**, linted with **Flake8** (including the requirement of asserts to have a message) and type-checked with **MyPy**.

### Test Suites

The tests are split into **test suites** by using `pytest`'s **marks** for the followings aspects:
- Internet connection requirements: `online`, `offline`;
- Unit testing principles: `principle_*`;
- Unit testing techniques: `technique_*`; and
- High-level concept testing: `sitemap_testing`, `robotstxt_testing`, and `crawlers_testing`.

The above principles come from a pool made by combining **Right-BICEP** and **CORRECT**.

<details>
    <summary><b>Right-BICEP and CORRECT Principles</b></summary>
    <ul>
        <li>Are the returned results <strong>right</strong>?</li>
        <li>Are the results at <strong>boundaries</strong> correct? The boundaries can be identified by following these aspects (CORRECT):
            <ul>
                <li><strong>Conformance</strong>: Compliance with a formal definition of the type</li>
                <li><strong>Ordering</strong> (for example, of an ordered list)</li>
                <li><strong>Range</strong></li>
                <li><strong>References</strong> (to external objects or methods) </li>
                <li><strong>Existence</strong> (of a method, parameter)</li>
                <li><strong>Cardinality</strong>: Tests with 0, 1 and N elements</li>
                <li><strong>Time</strong></li>
            </ul>
        </li>
        <li>Check for <strong>inverse</strong> relationships, where the operations support it.</li>
        <li><strong>Cross-check</strong> results using other means.</li>
        <li>Force <strong>error</strong> condition to happen.</li>
        <li>Are <strong>performance</strong> characteristics verified?</li>
    </ul>
</details>

The marks distribution (generated with `analysis/marks_analysis.py`) is listed in the following table:

| Mark                      | Count |
| ------------------------- | ----- |
| `crawlers_testing`        | 1     |
| `offline`                 | 51    |
| `online`                  | 1     |
| `principle_cardinality_0` | 4     |
| `principle_cardinality_1` | 4     |
| `principle_cardinality_n` | 4     |
| `principle_conformance`   | 9     |
| `principle_error`         | 7     |
| `principle_existence`     | 4     |
| `principle_inverse`       | 10    |
| `principle_performance`   | 52    |
| `principle_range_lower`   | 12    |
| `principle_right`         | 46    |
| `principle_time`          | 52    |
| `robotstxt_testing`       | 3     |
| `sitemap_testing`         | 8     |
| `technique_fake`          | 6     |
| `technique_monkey`        | 5     |

## Setup 🔧

1. Install [Poetry](https://python-poetry.org).
2. Install the Python dependencies using Poetry: `poetry install`.

## Usage 🧰

Just run `PYTHONPATH="tests" .venv/bin/pytest tests`. To use only tests from a suite, add `-m <mark>` to the previous command.

## Resources 📚

The used resources are only the libraries specified in Poetry's `pyproject.toml` file.