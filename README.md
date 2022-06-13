## Author
> [Faith Kwamboka Okong'o](https://github.com/FaithKwamboka)

# Awwwards
This is an app that allows users to post a project he/she has created and get it reviewed by his/her peers.

## Screenshot of Landing Page
![awards](https://user-images.githubusercontent.com/100117264/173208417-0fb749f1-3f40-492a-917d-ebd0767b0c84.png)

##  Screenshot of Sites Display
![awwards](https://user-images.githubusercontent.com/100117264/173208425-39c54973-3cc7-4ebf-8339-5d35c2c1b493.png)

## User Stories
As a user of the application, I would like to:
* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Admin Authentication | **On demand, verify emails before proceeding** | Access Admin dashboard |
| Display all projects | **Home page** | Clickable links to open live projects in different sites |
| To add a project  | **Through Admin dashboard and homepage** | Click on add and upload respectively|
| To edit a project  | **Through Admin dashboard** | Redirected to the  project form details and editing happens|
| To delete a project  | **Through Admin dashboard** | click on project object and confirm by delete button|
| To search projects by title | **Enter text in search bar** | Users can search by Project Title|
| Rate projects | **Through the projects page** | Users can rate projects based on Design, Usability and Content|

## Technologies used
* Python3
* Django & postresql
* Html5
* Css3
* Bootstrap4


## Installations

The following command installs all the application requirements
>``pip freeze -r requirements.txt``

## Setup
Run 
``https://github.com/FaithKwamboka/Awwwards-Clone.git``

or download the zip file from github.

After extracting the files, 

1. Navigate to the project folder
>`` cd name_of_folder`` 

2. Creating a virtual environment
>``virtualenv virtual``

3. Activating the virtual environment
>``source virtual/bin/activate``

4. Running the application
>``python3 manage.py runserver``

5. Running tests

 > ``python3 manage.py test.``

## [License]()

## Collaborate
For any collaborations, reach me on [okongofaith3@gmail.com]()