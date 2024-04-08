Write a program `frankfurter.py` to list the historical currency rate of a currency against a base currency using [Frankfurter Exchange Rate API][1].

[1]: https://www.frankfurter.app/docs/

The program should take the following command-line arguments.

```
  --currency CURRENCY target currency, default INR
  --base BASE  base currency, default USD
  --date DATE  First date to consider, default yesterday
  --days DAYS  number of days to display
```

The program should display the curreny rate between the base currency and the target currency for `n` days starting from yesterday. Optionally, the start date could be provided as a command-line argument.

Please note that there convertion data is not available on weekends. So the number of rows of data shown may be less than `n`.

## The Output Format

The output needs to be properly tabulated. Please use Python library `tabulate` for doing this.

Please refer to [Printing Tables with Tabulate][h2] in the Python Cookbook to learn how to the the `tabulate` library.


## Usage

```
$ python frankfurter.py
Date          USD    INR
----------  -----  -----
2023-10-18      1  83.25
2023-10-17      1  83.22
2023-10-16      1  83.25
2023-10-13      1  83.27
2023-10-12      1  83.24
2023-10-11      1  83.18
2023-10-10      1  83.24
2023-10-09      1  83.3
```

```
$ python frankfurter.py --days 2
Date          USD    INR
----------  -----  -----
2023-10-18      1  83.25
2023-10-17      1  83.22
```

```
$ python frankfurter.py --base GBP
Date          GBP     INR
----------  -----  ------
2023-10-18      1  101.55
2023-10-17      1  101.31
2023-10-16      1  101.37
2023-10-13      1  101.41
2023-10-12      1  102.47
2023-10-11      1  102.24
2023-10-10      1  101.96
2023-10-09      1  101.39
```

```
$ python frankfurter.py --base GBP --currency USD
Date          GBP     USD
----------  -----  ------
2023-10-18      1  1.2198
2023-10-17      1  1.2173
2023-10-16      1  1.2176
2023-10-13      1  1.2178
2023-10-12      1  1.231
2023-10-11      1  1.2292
2023-10-10      1  1.2249
2023-10-09      1  1.2172
```

```
$ python frankfurter.py --date 2023-01-31
Date          USD    INR
----------  -----  -----
2023-01-31      1  81.82
2023-01-30      1  81.53
2023-01-27      1  81.61
2023-01-26      1  81.53
2023-01-25      1  81.57
2023-01-24      1  81.62
2023-01-23      1  81.36
```

## Hints

* See [Working with dates][h1] in the Python Cookbook.
* See [Printing Tables with Tabulate][h2] in the Python Cookbook.

[h1]: https://notes.pipal.in/2023/perfios-python/cookbook/dates.html
[h2]: https://notes.pipal.in/2023/perfios-python/cookbook/tabulate.html
