## Overview

Python Package Index (PyPI) maintains an index of all the third-party python packages. It also provides an API to look at all the releases of a package.

Write a command line program ``pypi-releases.py` to list all the releases of a given package using the PyPI API.

The program should take the package name as argument and list all the releases along with the release time and filename uploaded for that release, in the reverse chronological order of the release time. By default, it should show the recent 5 releases.

The program should accept the following optional command-line arguments.

```
-n --count     number of releases to show
-b --before    only show release on or before this date
-a --after     only show releases that are on or after this date
-r --reverse   show the release in the reverse order - old releases first
```

You can use the  `upload_time` as an approximation for the release time. Typically, there would multiple files uploaded for each release and all of them will be listed in the response of the API. Please use first entry where the `packagetype` is `sdist`. If a release does not have an entry with `packagetype` with value `sdist`, please ignore that release.

## The PyPI API

The [PYPI API documentation][1] has two endpoints. The first one is to fecth the information about all releases of a project or a package. The second one is to get information about one particular release. We are only interested in the first one.

The following is the URL for getting information about releases of python package `Flask`. You can replace `Flask` with any package name to get information about that package.

<https://pypi.org/pypi/Flask/json>

You'll have to explore the API response and figure out which part of the data that you need to take.

Hint: You just need to focus on the `releases` part of the response.

## The Output Format

The output needs to be properly tabulated. Please use Python library `tabulate` for doing this.

Please refer to [Printing Tables with Tabulate][h2] in the Python Cookbook to learn how to the the `tabulate` library.

[h2]: https://notes.pipal.in/2023/perfios-python/cookbook/tabulate.html

## Hints for typer options

for having short and long option -n/--name here is sample code for typer

```
%%file short-long.py
import typer
from typing_extensions import Annotated


def main(user_name: Annotated[str, typer.Option("--name", "-n")]):
    print(f"Hello {user_name}")


if __name__ == "__main__":
    typer.run(main)
```
This when run from commandline will show options as given below

```
$ python short-long.py --help
Usage: short-long-options.py [OPTIONS]                                                                                                                       
                                                                                                                                                              
 Options
    --name  -n      TEXT  [default: None] [required]
    --help                Show this message and exit.
```

## Sample Usage

```
$ python pypi-releases.py Flask
Package    Version    Release Date         Filename
---------  ---------  -------------------  ------------------
Flask      3.0.0      2023-09-30T14:36:12  flask-3.0.0.tar.gz
Flask      2.3.3      2023-08-21T19:52:35  flask-2.3.3.tar.gz
Flask      2.2.5      2023-05-02T14:42:36  Flask-2.2.5.tar.gz
Flask      2.3.2      2023-05-01T15:42:12  Flask-2.3.2.tar.gz
Flask      2.3.1      2023-04-25T21:20:31  Flask-2.3.1.tar.gz
```

```
$ python pypi-releases.py Flask -b 2022-06
Package    Version    Release Date         Filename
---------  ---------  -------------------  ------------------
Flask      2.1.2      2022-04-28T17:47:40  Flask-2.1.2.tar.gz
Flask      2.1.1      2022-03-30T21:38:32  Flask-2.1.1.tar.gz
Flask      2.1.0      2022-03-28T19:15:15  Flask-2.1.0.tar.gz
Flask      2.0.3      2022-02-14T20:01:09  Flask-2.0.3.tar.gz
Flask      2.0.2      2021-10-04T14:34:54  Flask-2.0.2.tar.gz
```

```
$ python pypi-releases.py Flask -a 2022-06 -r
Package    Version    Release Date         Filename
---------  ---------  -------------------  ------------------
Flask      2.1.3      2022-07-13T20:56:00  Flask-2.1.3.tar.gz
Flask      2.2.0      2022-08-02T00:14:12  Flask-2.2.0.tar.gz
Flask      2.2.1      2022-08-03T23:52:25  Flask-2.2.1.tar.gz
Flask      2.2.2      2022-08-08T23:26:33  Flask-2.2.2.tar.gz
Flask      2.2.3      2023-02-15T22:43:57  Flask-2.2.3.tar.gz
```

