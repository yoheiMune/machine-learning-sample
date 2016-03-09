# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup







if __name__ == "__main__":

    # Amazonのジャンル一覧
    url = "http://www.amazon.co.jp/%E3%82%B8%E3%83%A3%E3%83%B3%E3%83%AB%E5%88%A5/b/ref=ed_book_seeallcategory?ie=UTF8&node=465610&pf_rd_m=AN1VRQENFRJN5&pf_rd_s=merchandised-search-leftnav&pf_rd_r=1BSD0T8CP0FCN0K8C0HB&pf_rd_t=101&pf_rd_p=291958249&pf_rd_i=465392"
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf-8")
    print(html)

    open("sample.html", "w").write(html)

    soup = BeautifulSoup(html, "html.parser")
    for div in soup.find_all(class_="acs-category-tile"):
        # genre_p = div.find(class_="acs-category-tile-header").find("a")["href"]
        # print(genre_p)
        elms = div.find(class_="acs-category-tile-header").find_all()
        print(elms)


    # ランキング
    # http://www.amazon.co.jp/gp/bestsellers/books/ref=zg_bs_nav_0 