# -*- coding: utf-8 -*-

"""
pandas_web.py

web scraping

cimri.com

asus g07 ROG laptop
hb->100
n11->92
x->FIRSAT*** 112

n11.com/urunler/laptop/asus/g07/&referrer=cimri.com

https://www.cimri.com/offer/430289880?platformName=CIMRI_DESKTOP&productId=616747467&pageType=PRODUCT&offerOrder=1&offerSponsored=false&priceOrder=1&minPrice=17894&minPriceMerchant=10109&commentCount=0&photoCount=10&offerCount=7
https://www.trendyol.com/asus/rog-strix-g17-g712lws-ev028-intel-core-i7-10750h-16gb-ram-512gb-ssd-8gb-rtx2070-super-17-3-fhd-144hz-p-42804328?boutiqueId=527772&adjust_tracker=1xed9e_u72in2&adjust_campaign=cimri_urun_listeleme

"""
#%%
import pandas as pd
# 0.25.1
print(pd.__version__)
# pd.show_versions()


#%%
url = "https://www.turkiye.gov.tr/doviz-kurlari"
# uniform resource locator

tables = pd.read_html(url)
assert isinstance(tables, list)

df_dovizler = tables[0]
df_capraz = tables[1]

# veri geldikten sonra, DF işlemleri.

# EDA

print("done100")


#%% df_capraz icinde bos bir satir var. onu drop edelim.
df_capraz = df_capraz.dropna(how="all")
# default: "any"
# tum satir na ise drop eder.
# eger satirda tek 1 na varsa, o satir kalir.


#%% doviz cinsini ayiralim.
df_dovizler[["miktar", "doviz_cinsi"]] = df_dovizler["Döviz Cinsi"].str.split(" ", expand=True, n=1)

df_capraz[["miktar1", "doviz_cinsi1"]] = df_capraz["Döviz Cinsi"].str.split(" ", expand=True, n=1)
df_capraz[["miktar2", "doviz_cinsi2"]] = df_capraz["Döviz Cinsi.1"].str.split(" ", expand=True, n=1)

# df_dovizler["Döviz Cinsi"].str.split(" ", expand=True, n=1)
# 1 Amerikan Dollari

# "1 SUUDİ ARABİSTAN RİYALİ" -> "1", "SUUDI ARAB R"
# "100 JAPON YENİ" -> "100", "JAPON YENI"


#%% eski "Döviz Cinsi" kolonunu silelim.
df_dovizler1 = df_dovizler.copy()
df_dovizler = df_dovizler.drop(columns=["Döviz Cinsi"])
df_capraz = df_capraz.drop(columns=["Döviz Cinsi","Döviz Cinsi.1"])


# https://codeshare.io/a3drnv

#%% dtypes: EDA
ser_types = df_dovizler.dtypes  # VSCode bizi üzdü. [object, object]
# df_dovizler.info()


#%% miktar kolonu string görünüyor, cevirelim.
df_dovizler["miktar"] = df_dovizler["miktar"].astype(int)
df_capraz['miktar1'] = df_capraz['miktar1'].astype(float)
df_capraz['miktar2'] = df_capraz['miktar2'].astype(float)
# df_dovizler.info()


#%% Kolon isimlerinde Türkçe ve boşluk karakterlerini atalım.
# rename column yapmamız lazım.
dict_rename = {
    'Döviz Alış':'doviz_alis',
    'Döviz Satış':'doviz_satis',
    'Efektif Alış':'efektif_alis',
    'Efektif Satış':'efektif_satis',
}
df_dovizler = df_dovizler.rename(columns = dict_rename)



#%% Doviz cinsi kolonunu index yapalım.
# TODO: 7 bu degeri dinamik alsin.



#%% bitcoin satırı ekleyelim.
# df_capraz icine, 1 bitcoin x amerikan dollari gibi bir satir ekleyelim.


def get_1_bitcoin_amount():
    """
    1 bitcoin'in amerikan dollari oalrak karsiligini dondurur.
    """
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    dataj = pd.read_json(url)
    dict_btc = dataj["bpi"]["USD"]
    btc_rate_float = dict_btc["rate_float"]
    return btc_rate_float


#%% 1 bitcoin icin USD degerini al
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
dataj = pd.read_json(url)
dict_btc = dataj["bpi"]["USD"]
btc_rate_float = dict_btc["rate_float"]


#%% 2 df'e ekle.
dic_capraz = {
        'miktar1':1,
        'doviz_cinsi1':'Bitcoin',
        'miktar2':get_1_bitcoin_amount(),
        # 'miktar2':btc_rate_float,
        'doviz_cinsi2':'AMERIKAN DOLARI',
}
df_capraz = df_capraz.append(dic_capraz, ignore_index=True)


