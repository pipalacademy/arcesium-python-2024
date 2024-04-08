import argparse
import datetime
import requests
from tabulate import tabulate

p = argparse.ArgumentParser()
p.add_argument("-c", "--currency", help="currency to list, default INR", default="INR")
p.add_argument("-b", "--base", help="base currency, default USD", default="USD")
p.add_argument("-d", "--date", help="starting date, default yesterday", type=datetime.date.fromisoformat)
p.add_argument("-n", "--days", help="number of days to display", type=int, default=10)

args = p.parse_args()

yday = datetime.date.today() - datetime.timedelta(days=1)
start_date = args.date or yday

date2 = start_date - datetime.timedelta(days=args.days)

url = f"https://api.frankfurter.app/{date2}..{start_date}"
params = {"base": args.base, "to": args.currency}

result = requests.get(url, params=params).json()

headers = ["Date", args.base, args.currency]
data = [[date, 1.0, value[args.currency]] for date, value in result['rates'].items()][::-1]

print(tabulate(data, headers=headers))