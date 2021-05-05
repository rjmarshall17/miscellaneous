#!/usr/bin/env python3

import json
from datetime import datetime, timedelta
import sys
from argparse import ArgumentParser
from sqlalchemy import create_engine
import logging

sys.path.append('/home/rob/workspace/stocks')
import stock_option_updates

DATE_CHOICES = [
    '2021-04-30',
    '2021-05-03',
    '2021-05-04',
]

SKIP_EXPIRATION_FOR = []
EXPIRATION_DATES_TO_SKIP = []
SKIP_BAD_TICKERS = []


def main():
    parser = ArgumentParser('Update the options DB from results JSON files')
    parser.add_argument('--verbose',dest='verbose',help='Enable verbose logging',default=False,action='store_true')
    parser.add_argument('--debug',dest='debug',help='Enable debug logging',default=False,action='store_true')
    parser.add_argument(dest='date',help='The date to use', choices=DATE_CHOICES)
    args = parser.parse_args()

    logging.basicConfig()
    log = logging.getLogger('sqlalchemy.engine')
    log.setLevel(logging.WARN)
    if args.verbose:
        log.setLevel(logging.INFO)
    if args.debug:
        log.setLevel(logging.DEBUG)

    today = datetime.strptime(args.date, '%Y-%m-%d')

    if today.strftime('%Y-%m-%d') == '2021-04-30':
        results = json.load(open('/home/rob/tmp/all_options.json','r'))
    elif today.strftime('%Y-%m-%d') == '2021-05-03':
        SKIP_BAD_TICKERS.append('TROW')
        results = json.load(open('/home/rob/tmp/all_options_20210503.json','r'))
    elif today.strftime('%Y-%m-%d') == '2021-05-04':
        SKIP_EXPIRATION_FOR.append('AAPL')
        EXPIRATION_DATES_TO_SKIP.append(datetime(2021, 5, 7, 0, 0))
        results = json.load(open('/home/rob/tmp/all_options_20210504.json', 'r'))

    su = stock_option_updates.UpdateStockOptions(verbose=args.verbose, debug=args.debug)
    engine = create_engine('mariadb+mariadbconnector://rob:Ultim8!@127.0.0.1/options')

    for j,result in enumerate(results):
        ticker = result[0][0][0]
        if ticker in SKIP_BAD_TICKERS:
            print("Skipping bad ticker symbol: %s" % (ticker))
            continue
        print('Expiration dates for %s: %s' % (ticker, result[0][0][1]['optionChain']['result'][0]['expirationDates']))
        for i, ts in enumerate(result[0][0][1]['optionChain']['result'][0]['expirationDates']):
            expiration = datetime.utcfromtimestamp(ts)
            if ticker in SKIP_EXPIRATION_FOR and expiration in EXPIRATION_DATES_TO_SKIP:
                print("Skipping expiration date: %s for %s" % (expiration, ticker))
                continue
            try:
                print('For ticker %s and expires on %s: calls: %4d puts: %4d' % (ticker,
                    expiration,
                    len(result[0][i][1]['optionChain']['result'][0]['options'][0]['calls']),
                    len(result[0][i][1]['optionChain']['result'][0]['options'][0]['puts'])))
            except Exception as e:
                raise RuntimeError("Error on ticker %s (%d) at expiration %s and index %d" % (ticker, j, expiration, i))
            for otype in ('calls','puts'):
                print("Starting %s (%d) for %s number: %d" % (otype, i, ticker, len(result[0][i][1]['optionChain']['result'][0]['options'][0][otype])))
                df = su.convert_options_to_df(result[0][i][1]['optionChain']['result'][0]['options'][0][otype],
                        otype, date=today, expiration=expiration)
                print("Converted to dataframe")
                df.to_sql(ticker, engine, if_exists='append')
