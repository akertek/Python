"""
https://www.imdb.com/find?q=matrix
https://www.imdb.com/find?q=matrix&s=tt
her filmin,
    + tam adini
    - turlerini ( Action, Sci-Fi )

    + yilini
    - ilk 5 (10?) oyuncusunu
    - puanini
    - suresini
Mert:
2020.07 anaconda bende
"""

import json
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# pylint: disable=missing-docstring

# su sayfadaki, ilk kac film gelecek?
# https://www.imdb.com/find?q=matrix&s=tt
# kac oyuncu bilgisini alacagiz?
# ilk 5 oyuncu gibi.
__SETTINGS = {
    "movie_count": 5,  # DRY
    "cast": 5,
    "base_url": "https://www.imdb.com",
}

__QUERY = "eternal sunshine of the spotless mind"
__QUERY = "matrix"
__QUERY = "lord of the rings"


class SearchResult:
    """
    <td class="result_text">
        <a href="/title/tt0133093/">The Matrix</a> (1999)
    </td>
    """

    def __init__(self, url, title, year, comments=""):
        self.url = url
        self.title = title
        self.year = year
        self.in_development = False
        self.comments = comments
        self.html = None
        self.soup = None
        self.genre = None
        self.actors = None
        self.rating = None

        if year in {"in development"}:
            self.in_development = True
            self.year = None

    def __str__(self):
        """
The Lord of the Rings: The Fellowship of the Ring
    year: 2001
    url: https://www.imdb.com/title/tt0120737/
    comments:
    genre: ['Action', 'Adventure', 'Drama', 'Fantasy']
    rating: 8.8
    actors: [{'@type': 'Person', 'url': '/name/nm0000704/', 'name': 'Elijah Wood'}, {'@type': 'Person', 'url': '/name/nm0005212/', 'name': 'Ian McKellen'}, {'@type': 'Person', 'url': '/name/nm0089217/', 'name': 'Orlando
Bloom'}, {'@type': 'Person', 'url': '/name/nm0000293/', 'name': 'Sean Bean'}]
        """
        result = f"""
{self.title}
    year: {self.year}
    url: {self.url}
    comments: {self.comments}
    genre: {self.genre}
    rating: {self.rating}
    actors: {self.actors}
"""
        return result

    def __repr__(self):
        return str(self)

    def _get_html(self):
        """
        requests ile sayfanın HTML halini alalım.
        """
        raw_html = requests.get(self.url)
        self.html = raw_html.text

    def _collect_more_like_this(self):
        """
        Bu film gibi olan 6+6 filmin URL'lerini bir listeye toplar.
        hepsini içeren div:
        rec_const_picker
        <img class="loadlate hidden rec_poster_img"
    <div class="rec_item" data-info="" data-spec="p13nsims:tt6133424" data-tconst="tt0486419">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>
        </div>
        <a href="/title/tt0486419/?ref_=tt_sims_tti">
            <img alt="A Look Inside 'Eternal Sunshine of the Spotless Mind'" title="A Look Inside 'Eternal Sunshine of the Spotless Mind'"
                src="https://m.media-amazon.com/images/M/MV5BYjQ1ZWFlZDQtZDhjOS00NjdmLTg1MzEtYjM0MzM0MGIxYTU5XkEyXkFqcGdeQXVyMTEyMDcwNw@@._V1_UX76_CR0,0,76,113_AL_.jpg"
                class="loadlate rec_poster_img" width="76" height="113"><br>
        </a>
    </div>
        """
        # self.html
        # self.soup
        dev_picker = self.soup.find("div", attrs={"class":"rec_const_picker"})
        # TODO: sayfa dinamik yuklendigi için, bu t zamanında,
        # bu div burada yer almiyor.
        # bu sebeple, dev_picker, None değeri alıyor.
        # ne yapacağımıza bakacağız.
        # assert dev_picker is not None


    def fill(self):
        """
        sayfanın HTML halini bs4 ile tarayalim.
        """
        self._get_html()
        soup = BeautifulSoup(self.html, 'html.parser')
        self.soup = soup

        script_tag = soup.find("script", attrs={"type": "application/ld+json"})
        assert script_tag is not None, "script_tag is None"
        script_tag: Tag

        json_data = script_tag.string
        assert isinstance(json_data, str), "json_data str değil."
        assert len(json_data) > 20, "json_data boş gelmiş."

        # print(json_data[:100])
        json_data2 = json.loads(json_data)

        self.genre = json_data2.get("genre", None)
        self.actors = json_data2.get("actor", None)

        key1 = "aggregateRating"
        rating = None
        aggregate_rating = json_data2.get(key1, None)
        if aggregate_rating:
            key2 = "ratingValue"
            rating = aggregate_rating.get(key2, None)
        self.rating = rating

        self._collect_more_like_this()
        print("done100")
        return None


def build_search_result_url(query):
    # the matrix aranirsa:
    query = query.replace(" ", "+")
    result = "https://www.imdb.com/find?q={}&s=tt".format(query)
    return result


def get_n_films_head(html_soup, movie_count):
    """
    return n movies
    return type list!
    """
    list_movies_head = html_soup.find_all(
        'td', attrs={"class": "result_text"}, limit=movie_count)
    return list_movies_head


def get_title_search_results(query, settings):  # pylint: disable=R0914
    """
    # film adi, link
    The Matrix (1999), https://www.imdb.com/title/  tt0133093/?ref_=fn_tt_tt_1
    ustteki satir gibi n tane dondurelim.
    :return:
    """
    url = build_search_result_url(query)
    # https://www.imdb.com/find?q=matrix&s=tt

    # download html
    # TODO: 7 değerini _SETTINGS'e taşı.R
    raw_html = requests.get(url, timeout=7)
    raw_html = raw_html.text
    soup = BeautifulSoup(raw_html, 'html.parser')
    head_n = get_n_films_head(soup, settings["movie_count"])
    # head_n içinde, asagidakinin bir listesi var:
    # <td class="result_text">
    #   <a href="/title/tt0133093/">The Matrix</a> (1999)
    # </td>

    # head_n = head_n[:2]  # TODO: 3 remove this

    search_results = []

    # first = head_n[0]  # <class 'bs4.element.Tag'>
    # from bs4.element import Tag
    for tag in head_n:
        tag: Tag

        # <td class="result_text">
        #   <a href="/title/tt7631058/">The Lord of the Rings</a>
        #   (TV Series)
        # </td>

        # <td class="result_text">
        # <a href="/title/tt6482606/">Lord of the Rings (By Spring)</a>
        # (2017) (Short)
        # </td>

        link = tag.find('a')
        # <a href="/title/tt0133093/">The Matrix</a>

        # <td class="result_text">
        #     <a href="/title/tt0106062/">Matrix</a> (1993) (TV Series)
        # </td>

        # https://www.imdb.com/title/tt0468569/?ref_=fn_tt_tt_4
        #                     /title/tt0106062/

        href_link = link.get("href")  # /title/tt0106062/
        href_link = settings["base_url"] + href_link
        title = link.text

        # The Matrix title
        # The Matrix (1993) (TV Series)  # td.text
        # (1993) (TV Series)  # td.text
        # "TV Series"

        details = tag.text  # (1993) (TV Series)
        details = details.replace(title, "")
        position = details.find(")")
        comments = details[position+1:].strip()
        details = details[:position]
        details = details.strip(" ()")   # "1993" / "TV Series"

        # Omer
        # try:
        #     year_text = int(year_text)
        # except:
        #     comments = year_text
        #     year_text = None
        # finally:
        #     sr1 = SearchResult(href_link, title, year_text, comments)

        # Cihat
        # import re
        # year_text = re.search("([0-9][0-9][0-9][0-9])", year_text)
        # 0000 .. 9999

        # Mert
        if details.isnumeric():
            year_text = details
        else:
            comments += details
            year_text = None

        # Oguzhan
        # year_test = int(year_test) if year_test.isnumeric() else None

        sr1 = SearchResult(href_link, title, year_text, comments)
        search_results.append(sr1)

    # print("done100")
    return search_results


def main():
    print("\n\n\n")
    query = __QUERY
    settings = __SETTINGS
    search_results = get_title_search_results(query, settings)
    # print(search_results)  # list
    for sr1 in search_results:
        sr1: SearchResult
        sr1.fill()
        print(sr1)
    # print(search_results[2])  # SearchResult instance


if __name__ == "__main__":
    main()