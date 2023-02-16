Как запустить проект
----
```
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl

sudo -u postgres psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv

git clone git@github.com:Agahan14/django-stripe.git

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Ендпоинты
----------------------------
* `/index/` - главная страница
* `admin/` - админка
* `buy/<item_id>` - купить товар
* `item/<item_id>` - страница товара
* `order/<order_id>` - страница заказа
* `buy_order/<order_id>/` - купить заказ

Удаленный сервис - поднял в google cloud
----------------------------
* `[http://34.159.42.97/admin/](http://34.159.42.97/admin/)` - админка
* `[http://34.159.42.97/item/4](http://34.159.42.97/item/4)` - товары
* `[http://34.159.42.97/order/4](http://34.159.42.97/order/4)` - купить заказ


Создание заказов делается все через админки, подумал, что так будет легче
