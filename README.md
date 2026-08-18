# Investor Project

## Project setup

1- Clone the repo by typing the following command on terminal 
```bash
git clone https://github.com/AfnanBq/malaa-project.git
```
2- Install all requried libraires 
```
Package                Version
---------------------- --------
AMQPStorm              2.10.7
cockroachdb            0.3.5
fastapi                0.109.2
httpx                  0.26.0
pika                   1.3.2
psycopg2-binary        2.9.9
pydantic               2.6.1
pydantic_core          2.16.2
pydantic-settings      2.2.0
python-dotenv          1.0.1
SQLAlchemy             2.0.27
sqlalchemy-cockroachdb 2.0.2
uvicorn                0.27.1
asgiref                3.7.2
celery                 5.3.6
```
3- Run docker containers by typing the following command on terminal
```bash
make up
```
4- Run fastapi server
```bash
export PYTHONPATH="$(pwd)/investor_bulletin" && python investor_bulletin/api/main.py
```
5- Run celery worker 
```bash
export PYTHONPATH="$(pwd)/investor_bulletin" && celery -A worker.app worker --loglevel=INFO
```
6- Run celery beat
```bash
export PYTHONPATH="$(pwd)/investor_bulletin" && celery -A worker.app beat --loglevel=INFO
```
### Phase 1 Results
- Get markets
<img width="1262" alt="Screenshot 1445-08-13 at 3 07 57 PM" src="https://github.com/AfnanBq/malaa-project/assets/44619363/5b5bcc7a-b41f-41c8-852d-69973e895fac">
<img width="1262" alt="Screenshot 1445-08-13 at 3 08 16 PM" src="https://github.com/AfnanBq/malaa-project/assets/44619363/71229721-4452-4669-adcb-a8646780d45b">
- Get alert rules
<img width="1262" alt="Screenshot 1445-08-13 at 3 09 18 PM" src="https://github.com/AfnanBq/malaa-project/assets/44619363/373390e3-7a74-4b28-8ffe-6154a71d5b62">
- Create alert rule
<img width="1262" alt="Screenshot 1445-08-13 at 3 10 29 PM" src="https://github.com/AfnanBq/malaa-project/assets/44619363/83db7160-4a27-48b9-93e8-1d98997e51fa">
- Update alert rule
<img width="1262" alt="Screenshot 1445-08-13 at 3 12 27 PM" src="https://github.com/AfnanBq/malaa-project/assets/44619363/d9480601-548d-4f6b-85dd-029793bb5325">
- Delete alert rule
<img width="1262" alt="Screenshot 1445-08-13 at 3 28 52 PM" src="https://github.com/AfnanBq/malaa-project/assets/44619363/46360fef-c500-4f76-8674-82d26be0a244">
- Get alerts
<img width="1262" alt="Screenshot 1445-08-13 at 3 54 57 PM" src="https://github.com/AfnanBq/malaa-project/assets/44619363/75f88524-0b1d-4e4b-be56-097d9f92f2f9">

#### Phase 2 Results
<img width="1099" alt="Screenshot 1445-08-13 at 4 11 05 PM" src="https://github.com/AfnanBq/malaa-project/assets/44619363/b502484a-ab65-4b98-8a0d-eadc34ac60b0">
<img width="1099" alt="Screenshot 1445-08-13 at 4 11 14 PM" src="https://github.com/AfnanBq/malaa-project/assets/44619363/b4955e36-ee72-45ce-a8e9-6ec406ff3ac1">

### Phase 3 Results
<img width="1099" alt="Screenshot 1445-08-14 at 10 58 27 AM" src="https://github.com/AfnanBq/malaa-project/assets/44619363/2c8c4b75-3596-4b0d-9fd2-eb75054ed7b1">
