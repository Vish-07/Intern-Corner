# INTERN CORNER
* Made By:   
* Velpucherla Pavithra(BT19CSE117)
* Vikharankar Vishakha Chandrakant(BT19CSE118)

###  Techstack Used
            Django Framework
            HTML,CSS,Bootstrap Framework
            Postgresql

###  SETUP
* Type python from your shell, then at python prompt
* >>> import django
* Install pgAdmin and postgresql 
* Create a database with name 'Intern'
* Accordingly update username and password same as your postgresql id-password in settings.py
* From the command line, move into InternCorner directory, and run following commands
* $ python manage.py makemigrations
* $ python manage.py migrate
* $ python manage.py runserver

* Note: Make the changes in settings.py according to your id-passowrd created during postgres and pgAdmin installation. 
* To approve the experiences/gain admin rights, create a superuser, via following command:
* $ python manage.py createsuperuser
* And then browse to 'http://127.0.0.1:8000/admin'and login via superuser credentials, to make the changes/ approve experiences.

### RUN APP
* Run the server using            python manage.py runserver
* In Navbar, click on Register, enter the details and create your account
* Then, Login by entering created username and password
* Then, click on 'Experiences' tab in navbar and surf through all the experiences ;)
* For adding the experience, click on 'Add Experience' tab, and enter the data.
* For editing or deleting the experience, move to home page and scroll in 'Your Experience' part and choose the option you want.
* For logging out, click on 'Logout' tab in navbar