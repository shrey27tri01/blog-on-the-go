# blog-on-the-go

```blogonthego``` is a blogging web application made in Django. Users can view the blog posts when they visit the website.   
Users can also signup and login to the website and create new posts for others to see.

To run the website locally, type the following on the command line:
- git clone https://github.com/shrey27tri01/blog-on-the-go
- cd path/to/cloned/repository
- python -m venv VENV
- VENV\Scripts\activate.bat (or activate.ps1 on PowerShell)
- pip install -r requirements.txt
- python -m pip install django
- django-admin --version (check the installation of django)
- set SECRET_KEY = 'mysecret' (```export``` instead of ```set``` for macos) 
- python manage.py runserver    

Then visit localhost on port 8000(127.0.0.1:8000/ or localhost:8000/)

Or alternatively, you can visit the deployed website <a href="https://shrey27tri01.pythonanywhere.com/">here</a>.  
