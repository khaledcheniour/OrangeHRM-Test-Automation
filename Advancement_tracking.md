# Week 1
## Install Python, VS Code, Git, dependencies, browsers
-The virtual envirenment is working perfctly


<img width="652" height="762" alt="image" src="https://github.com/user-attachments/assets/a72fb746-9900-4ed2-b86c-ce6132005dd0" />


## Run all the example tests; make them pass
- Under the folder Tests there is login_tests.py containing login tests :

  (test_login_with_empty_credentials / test_login_with_invalid_credentials / test_login_with_valid_credentials )


- Using the command : python -m pytest C:\Users\User\Desktop\summer_internship\OrangeHRM-Test-Automation_Khaled\tests\test_login.py --headed --slowmo 1000 

the test passed and the website was opened and I so the tests happening one aby one and a report was created 

<img width="740" height="567" alt="image" src="https://github.com/user-attachments/assets/add12121-787e-489d-90e9-f7cc02de30b6" />

## Log into OrangeHRM manually; explore PIM, Admin, Recruitment
✔ Done

## Read login_page.py and test_login.py line by line
✔ Done

## Use playwright codegen to record a login
### 1. I recorded 3 login attempts :
- Login with valid credentials
- Login with invalid credentials
- check if the login is successful when adding spaces at the end of the  username
### 2. Acces the PIM page and add a new employee

<img width="811" height="347" alt="image" src="https://github.com/user-attachments/assets/41fba74f-ec99-41c6-bb18-4c8abe7e4e2c" />
<img width="841" height="821" alt="image" src="https://github.com/user-attachments/assets/6a102d88-4fc7-4810-8d63-b77cd4df175a" />

## Write a tiny new test: assert the login page title is shown

For testing whether the page is loaded and the title appeares as expected "Login" I added a method called login-title that fetches the title shown and returns it as a String 

<img width="664" height="178" alt="image" src="https://github.com/user-attachments/assets/c6553eac-4632-4d00-9886-0656a51ec48f" />

Then I created a test file named test_title_week1.py where I wrote the test function to check if the page is loaded using the existing is_loaded method and to check if the title is shown correctly using the method I created 

<img width="975" height="426" alt="image" src="https://github.com/user-attachments/assets/ab1048f6-0f2a-4957-993c-ec2a96747385" />

## Create a feature branch and push your first commit
✔ Done

## what a page object is

The Page Object Model (POM) is a design pattern where each page in the UI is represented as a class. This class contains the locators (objects) and methods (actions) specific to that page, which are then used in the test scripts. This pattern drastically simplifies updates and maintenance because any UI changes only need to be modified in one single place.
