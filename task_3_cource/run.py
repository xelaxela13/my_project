import argparse

from services import course


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("currency", action="store", help="Currency")
    parser.add_argument("date", action="store", help='Date', nargs='?')
    args = parser.parse_args()
    return args.currency, args.date


def run():
    currency, date = parse_args()
    res = course.get_course(currency, date)
    print(res)


if __name__ == '__main__':
    run()
