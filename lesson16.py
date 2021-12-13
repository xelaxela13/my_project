import json

import requests
from bs4 import BeautifulSoup


class BS:
    parser_type = 'html.parser'
    domain = 'https://rozetka.com.ua'
    ERRORS = {
        1: 'Something wrong with BS object'
    }

    def __init__(self, start_url: str):
        self._start_url = f'{self.domain}{start_url}'
        self._storage = []
        self._request_count = 0
        self._results = []
        self._urls_list = [self._start_url]

    def parse(self, to_file=False) -> list:
        for url in self._urls_list:
            html = self._get_page(url)
            if html:
                self._store_result(html, to_file=to_file)
                self._parse_results(html, to_file=to_file)
        return self._results

    def _pagination(self, soup):
        next_page = soup.find('a', class_='pagination__direction--forward', href=True)
        self._urls_list.append(f'{self.domain}{next_page["href"]}')

    def _get_page(self, url: str, params: dict = None) -> str:
        try:
            response = requests.get(url, params=params)
        except requests.exceptions.ConnectionError as err:
            print(f'ERROR: {err}')
        else:
            self._request_count += 1
            print(f'REQUEST: {self._request_count} {url}, '
                  f'RESPONSE: {response.status_code}')
            return response.content
        return ''

    def _store_result(self, data: str = None, to_file=False):
        if data is not None:
            self._storage.append(data)
            if to_file:
                self._save_result(f'catalog/page{self._request_count}.html', data)

    def _parse_results(self, html: str, to_file=False):
        soup = BeautifulSoup(html, self.parser_type)
        if soup:
            # self._pagination(soup)
            self._results.extend(self._parse_result(soup))
            if to_file:
                self._save_result(
                    f'catalog/results.json', self._results, as_json=True, append=True)
        else:
            print(f'ERROR {self.ERRORS[1]}')

    @staticmethod
    def _parse_result(soup) -> list:
        tags = soup.find_all('li', {'class': 'catalog-grid__cell'})
        data_list = []
        if tags:
            for tag in tags:
                data_list.append({
                    'title': tag.find('span',
                                      class_='goods-tile__title').text.strip(),
                    'price': {
                        'old': tag.find('div',
                                        class_="goods-tile__price--old").text,
                        'actual': tag.find('span',
                                           class_="goods-tile__price-value").text
                    },
                    'description': tag.find('p',
                                            class_="goods-tile__description_type_text").text
                })
        return data_list

    def _save_result(self, filename, data, as_json=False, append=False):
        with open(filename, 'a+' if append else 'w+') as f:
            f.write(json.dumps(data, ensure_ascii=False) if as_json else str(data))


def main():
    start_url = '/notebooks/c80004/'
    bs = BS(start_url)
    data_list = bs.parse(to_file=True)
    print(data_list)


if __name__ == '__main__':
    main()
