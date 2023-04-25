# ratio

This is **ratio**, an application for University of Helsinki's _Ohjelmistotekniikka_ course.

## Documentation

* [Software Requirements Specification](https://github.com/jobatabs/ratio/blob/main/doc/software_requirements_specification.md)
* [Architecture description](https://github.com/jobatabs/ratio/blob/main/doc/architecture.md)
* [Hours tracking](https://github.com/jobatabs/ratio/blob/main/doc/hours.md)
* [Changelog](https://github.com/jobatabs/ratio/blob/main/doc/changelog.md)

## Installation

Install dependencies using ````poetry````:

    poetry install

Run program:

    poetry run invoke start

## Command line functions

### Run tests

You can run tests using poetry and invoke:

    poetry run invoke test

### Run linter

You can run the linter using poetry and invoke:

    poetry run invoke lint

### Autopep8

Autopep8 formatting is available using poetry and invoke

    poetry run invoke autopep

### Generate coverage report

You can generate a test coverage report using poetry and invoke:

    poetry run invoke coverage-report

The report appears under ````htmlcov/````