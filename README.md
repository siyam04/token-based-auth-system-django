# Token Based Authentication System in Django.

### API List:
* (method: POST) (params: username, email, password, first_name, last_name)
* http://127.0.0.1:8000/api-drf/sign-up/
* image
![sign-up](https://user-images.githubusercontent.com/23103980/78637727-c57a2780-78cc-11ea-9873-350a8aac5262.PNG)

* (method: POST) (accept headers token) (params: username, password)
* http://127.0.0.1:8000/api-drf/login/ 
* image-1
![login (1)](https://user-images.githubusercontent.com/23103980/78638072-72ed3b00-78cd-11ea-92c0-620b042dd1c7.PNG)
* image-2
![login (2)](https://user-images.githubusercontent.com/23103980/78638109-87313800-78cd-11ea-9051-f2526555522b.PNG)
* image-3
![login (3)](https://user-images.githubusercontent.com/23103980/78638119-8a2c2880-78cd-11ea-8d2a-47c77890e606.PNG)

* (method: GET) (accept headers token)
* http://127.0.0.1:8000/api-drf/logout/ 
* image
![logout](https://user-images.githubusercontent.com/23103980/78638150-9dd78f00-78cd-11ea-908d-75b8a46798fb.PNG)

* (method: GET) (accept headers token) (authentication decorator)
* http://127.0.0.1:8000/api/random/ 

### How to Run Faker Script:
* cd token-based-auth-system-django $> python django_faker.py

### How to Run Django Seeder Script:
* cd token-based-auth-system-django $> python manage.py seed practice_api --number=10
