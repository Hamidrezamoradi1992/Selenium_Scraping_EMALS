import datetime

from pony.orm import db_session
from selenium.common.exceptions import *

from databace_pony import Create_Product, Urls, Product, tehran_timezone, db
from khazeshgar import Emalls_Selenium


@db_session
def database_select():
    data = db.select("product_name FROM product group by product_name;")
    return data




while True:
    # da=database_select()
    da="ماشین لباسشویی دوقلوی پاکشوما (9.6 کیلویی) PWT-9654 AJ Pakshoma"
    for product in da:

        with Emalls_Selenium(product):
            dada=Emalls_Selenium.bank
        @db_session
        def data(name):
            data = Product.select()
            return data


        datasss = data(name="knjj")
        for i in dada:
            @db_session
            def hhhhh(data):
                print(data)

                try:
                    for d in data:
                        if d.product_name == i[0] and d.product_shup==i[1]:
                            d.set(product_price=i[2],times=datetime.datetime.now(tz=tehran_timezone), product_url_pic=i[4])
                            raise Exception
                except Exception as e:
                    print(e)
                else:
                    with Create_Product(product_name=i[0], product_price=i[2], product_shup=i[1], product_url_pic=i[4],
                                        category="digital", url_shup=i[3]):
                        print("acept" )
            hhhhh(datasss)
        print("*"*30,"request database")

        # database_select()
