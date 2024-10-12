import datetime
import time
import zoneinfo

from pony.orm import *

from khazeshgar import Emalls_Selenium

db = Database()

tehran_timezone = zoneinfo.ZoneInfo("Asia/Tehran")


class Users(db.Entity):
    name = Required(str)
    username = Required(str, unique=True)
    passwords = Required(str, nullable=False)
    super_user = Optional(bool, sql_default=False)
    times = Optional(datetime.datetime, auto=True)
    favorite = Optional("Favorite")


class Category(db.Entity):
    category_name = Required(str, unique=True)
    product = Set("Product")


class Product(db.Entity):
    product_name = Required(str, nullable=False)
    product_price = Required(int, nullable=False)
    product_shup = Required(str, nullable=False)
    times = Optional(datetime.datetime)
    product_url_pic = Optional(str)
    category = Required(Category)
    url = Optional("Urls")
    favorite = Optional("Favorite")


class Urls(db.Entity):
    urls = Required(str)
    product = Required("Product")


class Favorite(db.Entity):
    user = Set("Users")
    product = Set("Product")
    user_id = Required(int)
    product_id = Required(int)


db.bind(provider='postgres', user='postgres', password='1234', host='127.0.0.1', database='selenium')
db.generate_mapping(create_tables=False)


# user
class Create_User:
    def __init__(self, name, username, passwords, super_user=False, action="create"):
        self.name = name
        self.username = username
        self.passwords = passwords
        self.super_user = super_user
        self.action = action

    def __enter__(self):
        if self.action == "create":
            self.__class__.ste_user(self.name, self.username, self.passwords, self.super_user)

        elif self.action == "update":
            self.__class__.update_user(name=self.name, username=self.username, password=self.passwords)
        elif self.action == "login":
           return self.__class__.login_user(username=self.username,password=self.passwords)

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    @staticmethod
    @db_session
    def ste_user(name, username, passwords, super_user=False):
        user_validate = Users.get(username=username)
        if user_validate is None:
            Users(name=name, username=username, passwords=passwords, super_user=super_user,
                  times=datetime.datetime.now(tz=tehran_timezone))
            print("create")
        else:
            print('username in database')

    @staticmethod
    @db_session
    def update_user(name, password, username):
        user_query = Users.get(username=username)
        user_query.set(name=name, passwords=password, times=datetime.datetime.now(tz=tehran_timezone))
        print("update")

    @staticmethod
    @db_session
    def login_user(password, username):
        user_query = Users.get(username=username)
        if user_query is not None:
            if user_query.passwords == password:
                print('login')
                return user_query
            else:
                print('login22')
                return False
        else:
            print('login23')
            return False


class Create_Product:
    def __init__(self, product_name, product_price, product_shup, product_url_pic, category, url_shup):
        self.product_name = product_name
        self.product_price = product_price
        self.product_shup = product_shup
        self.product_url_pic = product_url_pic
        self.category = category,
        self.url_shup = url_shup

    def __enter__(self):
        self.__class__.ste_product(product_name=self.product_name,
                                   product_price=self.product_price,
                                   product_shup=self.product_shup,
                                   product_url_pic=self.product_url_pic,
                                   category=self.category,
                                   url_shup=self.url_shup)

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    @staticmethod
    @db_session
    def ste_product(product_name, product_price, product_shup, product_url_pic, category, url_shup):
        print(url_shup)
        categoryss1 = Category.get(category_name=category[0])
        p2 = Product(product_name=product_name, product_price=product_price, product_shup=product_shup,
                     category=categoryss1.id,
                     times=datetime.datetime.now(tz=tehran_timezone), product_url_pic=product_url_pic)
        Urls(urls=url_shup, product=p2)


# @db_session
#         def hamid():
#             data = Product.select(product_name=self.name)
#             if data != None:
#                 for e in Emalls_Selenium.bank:
#                     if e[0] == self.name:
#                         for i in data:
#                             print(i.product_name)
#                             print(i.product_shup)
#                             if self.name == i.product_name and e[1] == i.product_shup:
#                                 print("update")
#                                 i.product_price = e[2]
#                                 i.times = datetime.datetime.now(tz=tehran_timezone)
#             else:
#                 for e in Emalls_Selenium.bank:
#                     if e[0] == self.name:
@db_session
def set_category(category_names):
    Category(category_name=category_names)


# set_category('digital')

with Create_User(name="", passwords="dar12ya", username='mohamadk123', action='login')as a :
    print(a)
