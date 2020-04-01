# Token Based Authentication System in Django.

### API List:
>> (method: POST) (params: username, email, password, first_name, last_name)
* http://127.0.0.1:8000/api/sign-up/

>> (method: POST) (params: username, password)
* http://127.0.0.1:8000/api/login/ 

>> (method: GET) (accept headers token)
* http://127.0.0.1:8000/api/logout/ 

>> (method: GET) (accept headers token) (authentication decorator)
* http://127.0.0.1:8000/api/random/ 

### How to Run Faker Script:
* cd token-based-auth-system-django $> python django_faker.py

### How to Run Django Seeder Script:
* cd token-based-auth-system-django $> python manage.py seed practice_api --number=10
