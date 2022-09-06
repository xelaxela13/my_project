import datetime
from typing import Union, Tuple

import requests


class Getter:
    URL = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange'
    HTTP_200_OK = 200
    ERROR_CURRENCY = 'Invalid currency name: {}'
    ERROR_DATE = 'Invalid date: {}'
    ERROR_SYSTEM = 'System Error'
    RESPONSE = '--------------\n{}\n=============='

    def __init__(self):
        self._currency = self._date = self._response = None

    def get_course(self, currency: str, date: str = None) -> str:
        self.__get_course(currency, date)
        rate, cc = self.__parse_response()
        if rate is None or cc is None:
            if self._date and datetime.datetime.strptime(
                    self._date,
                    '%Y-%m-%d'
            ) < datetime.datetime(1999, 1, 1):
                return self.RESPONSE.format(self.ERROR_DATE.format(self._date))
            if len(self._currency) == 3:
                return self.RESPONSE.format(
                    self.ERROR_CURRENCY.format(self._currency)
                )
            return self.RESPONSE.format(self.ERROR_SYSTEM)
        return self.RESPONSE.format('{}\n{}'.format(cc, rate))

    def __get_course(self, currency: str, date: str = None):
        params = {'valcode': currency.strip().upper(), 'json': True}
        if date:
            params.update({'date': date.strip().replace('-', '')})
        try:
            response = requests.get(self.URL, params=params)
        except requests.exceptions.RequestException:
            pass
        else:
            self._currency = currency
            self._date = date
            self._response = response.json()

    def __parse_response(self) -> Union[Tuple[str, str], Tuple[None, None]]:
        if self._response is not None:
            try:
                date = self._response[0]
                rate = date['rate']
                cc = date['cc']
            except (IndexError, KeyError):
                pass
            else:
                return rate, cc
        return None, None


course = Getter()
