# kara
## How to run


1. Clone the project from `https://github.com/MohsenZarein/kara.git`.
  ```bash
  $ git clone https://github.com/MohsenZarein/kara && cd kara
  ```
2. create a virtual env and activate it
```bash
  $ python3 -m venv ./.venv && source .venv/bin/active
  ```
3. install requirements
```bash
  $ pip install -r requirements.txt
  ```
4. apply migrations for django defualt models
  ```bash
  $ python manage.py migrate
  ```
5. run development server

  ```bash
  $ python manage.py runserver
  ```
6. install and config rabbitmq as message broker for the celery app

7. start celery worker (in root directory of projetc)
```bash
  $ celery -A app worker
  ```



## How to use

   #### top 10 trade streams based on quantity
   Navigate to browser and enter http://127.0.0.1:8000/main-api/top-trade-streams/btcusdt in url to see top trades on Bitcoin or you
   can use curl in terminal to see the results:
 ```bash
    $ curl  localhost:8000/main-api/top-trade-streams/btcusdt
   ```
   * In order to get data on other coins, just change the symbol at the end of the url  
   
