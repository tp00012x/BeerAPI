# BeerAPI

This is a web application that let users create their own beer and reviews.

1. Download project to desired location and 'cd' into the BeerAPI folder

2. It's recommended to create a virtual environment before installing all the requirements from step 3.

    To create environment with anaconda run:
    - conda create --name myenv

3. Install requirements:
    - pip install -r requirements.txt

4. Run server
    - python manage.py runserver
    
----------------------

After you have the application running, please register as new user.

5. To login into the admin page: http://127.0.0.1:8000/admin/ , create a super user by running:

   - python manage.py create super user
  
Note: To view the reviews and beers using Django REST framework, go to:

   - http://127.0.0.1:8000/home/rates/ to see rates
   - http://127.0.0.1:8000/home/reviews/ to see reviews
