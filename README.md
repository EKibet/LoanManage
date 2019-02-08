# SortLoan


Loan application app
## Versioning

 -V1.0 

## Author

* **Edgar**

## Features


As a user, You will:

1. Sign in with the application to start using.
2. A profile will be automatically set.
3. Fill a progressive multi step loan form.
4. Edit loan application.
5. Cancel loan application.
6. view loan application.


### Installing

*** To view the app.Visit -> [SortLoan](https://github.com/EKibet/LoanManage.git)

1. Clone this repo: git clone https://github.com/EKibet/LoanManage.git.
2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to LoanManage then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
3. To run the app, you'll have to run the following commands in your terminal
    
    
       pip install -r requirements.txt
4. On your terminal,Create database loans using the command below.


       CREATE DATABASE loans; 
       **if you opt to use your own database name, replace instaclone your preferred name, then also update settings.py variable DATABASES > NAME

5. Migrate the database using the command below


       python3.6 manage.py migrate
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below


       python manage.py runserver
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

## Running the tests

Use the command given below to run automated tests.


        python manage.py test




## Built With

* [Django](https://www.djangoproject.com/) - web framework used
* Javascript - For DOM(Document Object Manipulation) scripts
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

