# `scrapy` Unit Tests

## Description 🖼️

This repository holds (toy) **`pytest` unit tests for `scrapy`**, a Python library for scrapping and crawling websites. It was created for a course from Faculty of Automatic Control and Computers, University POLITEHNICA of Bucharest, namely "Cybersecurity Incidents Management".

In total, there are **52 tests** that are passing with the frozen versions of libraries. All **78 asserts** have a **suggestive message**. Each test has a **timeout** attached: `0.1` seconds for offline tests and more for those that requires Internet connection (for example, those scrapping a website).

Each test method is accompanied by a short **documentation** explaining what it checks and what principles respects. These principles come from a pool made by combining **Right-BICEP** and **CORRECT**.

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

The tests are split into **test suites** by using `pytest`'s **marks** for the followings aspects:
- Internet connection requirements: `online`, `offline`; and
- High-level concept testing: `sitemap_testing`, `robotstxt_testing`, and `crawlers_testing`.

In addition, the source files were formatted with **Black** and **isort**, linted with **Flake8** (including the requirement of asserts to have a message) and type-checked with **MyPy**.

# Setup 🔧

1. Install [Poetry](https://python-poetry.org).
2. Install the Python dependencies using Poetry: `poetry install`.

# Usage 🧰

Just run `PYTHONPATH="tests" .venv/bin/pytest tests`. To use only tests from a suite, add `-m <mark>` to the previous command.