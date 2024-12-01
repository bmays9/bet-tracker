# Bet Tracker

Bet Tracker is a full-stack, responsive website built for football supports who enjoy betting on matches. The site is for bet tracking purposes only and all monetary amounts on the site are for documentation purposes only. 
<br>
It provides users with the opportunity to share their upcoming bets with the website community, and see how their results fare against other like-minded bettors. 

View the live website [here](https://track-my-bets-1ee4e00d237a.herokuapp.com/)
____

## Overview

Bet Tracker is a responsive website compatible with all current major browsers. It is built for educational purposes using Bootstrap and the Django Framework. It consists of user authentication and permission logic, with full CRUD functionality on bets entered on the site. 

The site is aimed at betting and football enthusiasts who want to add an extra element to their betting by sharing and comparing with others. Part of responsible gambling is to keep a track of all betting, successful or not, and this site helps to achieve this 

## User Expectations

- The app should be easy to navigate and all betting information displayed intelligently.
- The user should be able to create, read, update and delete any football bets they want to track.
- The user should be able to compare their betting success with other users.
- The user should be able to view bets places by other users on the site.
- The app should be fully tested and run without bugs.

## Agile Methodology

The workflow for planning and implementing this project was carried out using Agile Methodology. I created a Project within GitHub and used GitHub Issues to record the Epics and User Stories. Milestones were used to manage iterations of development, and labels were used to categorise the user stories and structure the prioritisation of work. 

Each User Story contains Acceptance Criteria which sometimes was adjusted throughout the process of completing the user story. This flexibility benefitted the project by constantly ensuring the acceptance criteria were tailored towards the goal of the user story.

Estimating the effort behind each user story was a challenge, so the workload of each milestone was varied.

The MoSCoW Method of Prioritisation was used, classifying each User Story as a 'Must Have', 'Should Have' or 'Could Have'. All 'Must Have' stories were successfully completed, while there were some remaining user stories labelled 'Could Have' that were not implemented. These User Stories (#15, #16, #29) remain in the Optional list of tasks to be implemented in a future iteration. 

### Epics
#1 As a superuser I want to add a bet via the admin page and view it on the site.
#9 This Epic covers all the user stories required for the features associated with the Bet app functionality
#17 Epic to cover all User Stories for the Bank App features
#18 Epic to cover all user stories linked to account registration and login / logout process


### User Stories

#2 As a developer, I want to create a Django Project in the IDE, so that I have the framework for the Bet Tracker project
#3 As a developer, I want to have a Bet app created in the Django project to facilitate the bet tracking element of the project
#4 As a developer, I want to have a Bank app in the Django project to facilitate the money tracking and user ranking elements of the project
#5 As a project, I want to be deployed to Heroku, so that I am available to all potential users.
#6 As a developer, I want to set up and configure my database and Bet app models, so that data can be added via the admin page
#7 As a superuser I want to have an admin page that is customised to the project, so that the data and admin functions are presented in an intelligent way
#8 As a user, I want to view all open bets so that I can see what other users bets are upcoming
#10 As a user, I want to have consistent styling across all pages so that the site is accessible and familiar
#11 As a user, I want to view all settled bets so that I can review all previous betting activity
#12 As a user, I want to add a bet to the site so that share with others and track my success
#13 As a user, I want to edit my open bets so that update the result, status and make any necessary corrections
#14 As a user, I want to delete an open bet so that the bet details are removed from the database
#19 As a visitor, I want to register to the site so that i can use the site and track my bets
#20 As a user, I want to login to the site so that I can make changes to my bets, and make new bets
#21 As a user, I want to logout of the site so that my account is not logged in when i am not using the site
#22 As a user, I want to **view all user bank amounts so that I can see where I rank in the community
#23 As a user, I want to see information presented intelligently and cleanly on the site so that the site is easy to read
#24 As a user, I want to see my account balance on the homepage so that i know how successful my bets are
#25 As a user, I want to see the deployed project with intended styling so that I view the site as intended
#26 As a user I want to add multiple lines to my new bet so that I can place accumulator bets on more than one match at a time.
#27 As a tester, I want to automate tests to the bet form function so that i can ensure the functions work as expected
#28 As a user, I want to track my betting account balance so that I can see how profitable my bets are
#30 As a user, I want to view a home page that explains how to use the site so that a casual viewer unfamiliar with betting can use the site
#31 As a user, I want to view a responsive and consistently styled site so that the user experience is a good one when using the site

## Wireframes


## Website Structure

### Homepage
The homepage welcomes users to the site and gives them a clear overview of the sites purpose. For visitors unfamiliar with betting, a clear description of football betting and how odds work is provided.

### View Bets
The View Bets page gives users a complete one-page view of all bets on the site. Bets are split into categories, "Open" and "Settled". Open bets are for upcoming matches and users are sharing their bets and predictions with each other. Users can gain insight and inspiration by knowing how other successful bettors are thinking about a certain match. The "Settled Bet" list is a historical record of all bets that have been settled.

### Add a Bet
An logged in user can add a new bet to the site at any time. The site allows up to 6 matches (lines) to be combined into a single bet.

### Update a Bet
While a bet is still open, the user can edit all details of their bet. This can either be to correct a mistake, remove a cancelled fixture, or to enter the match result and update the bet status after the match(es) has been played.

### Money List
The money list page allows users to see the ranking of their account balance compared to other users on the site. 

## Administration
The administration pages all the site administrator a convenient and intuitive way to manage the database, and in turn the datadisplayed on the site. The administrator can amend individual bets, lines, or user's bank balance and search for each on the site in an intelligent way.

## Database structure

### **User**

(Django Model)

| Field Name  | Field Type   | Key         |
|-------------|--------------|-------------|
| id          | Integer      | Primary Key |
| username    | CharField    | -           |
| email       | EmailField   | -           |

---

### **Bet**

| Field Name      | Field Type    | Key            |
|------------------|---------------|----------------|
| id              | UUIDField     | Primary Key    |
| punter          | ForeignKey    | Foreign Key (to User) |
| created_on      | DateTimeField | -              |
| updated_on      | DateTimeField | -              |
| stake           | DecimalField  | -              |
| status          | IntegerField  | -              |
| settled_amount  | DecimalField  | -              |

---

### **Line**

| Field Name     | Field Type    | Key            |
|----------------|---------------|----------------|
| id             | AutoField     | Primary Key    |
| bet            | ForeignKey    | Foreign Key (to Bet) |
| home_team      | CharField     | -              |
| away_team      | CharField     | -              |
| prediction     | IntegerField  | -              |
| odds           | DecimalField  | -              |
| match_result   | IntegerField  | -              |
| status         | IntegerField  | -              |
| created_on     | DateTimeField | -              |
| updated_on     | DateTimeField | -              |

---

### **Bank**

| Field Name  | Field Type    | Key            |
|-------------|---------------|----------------|
| id          | AutoField     | Primary Key


## Styling

The website is designed with minimalist intent to keep the pages clean and with the important data clearly visible. 

### Fonts
I used Google fonts to source the two fonts I used for this website.
Anton was chosen for the brand name in the heading, making it stand out from the other text.
Poppins was chosen as the font for all other text as it is a sans-serif font that displays numbers in a clear style. The site contains a lot of numbers so it was important to choose the font accordingly. 

### Colours

I chose the colour pallete using the [Coolers](https://coolors.co/) to give the site a modern and professional look. 


## Features

**Header and Navigation**

The header and navigation bar are contained within the base template so that all pages on the site inherit the same design. The Bet Tracker brand name is an anchor tag which brings the user back to the home page whenever clicked.
The Navigation bar contains links to the "View Bets", "Add Bet", "Money List", "Login", "Logout" and "Register".
On smaller screens, the navigation bar condenses into a hamburger button, which when pressed, displays the navigation options vertically. 
The links have an active class assigned to them, styling the active-page link differently so the user always knows where within the site they are.
The links for "Registration", "Login" and "Logout are displayed dynamically and respond to the status of the current user. 
At the right hand side of the header is a statement confirming the username of the user currently logged in. This is visible on every page to rassure the user they are both logged in, and under which account.

<details>
<summary>Click to view screenshots of Navigation</summary>
</details>

**Footer**
Featured on all pages as part of the base template, the footer contains information about me as the site creator and provides a way to get in contact. Links to my email and to my Github page are both included.
The footer is styled in a minimalistic way to present the information clearly and concisely. All links are labelled for enhanced accessibility. 

<details>
<summary>Click to view screenshots of the Footer</summary>
</summary>
</details>


**Home Page**
The home page welcomes the user or visitor and explains the purpose of the website. A photo of a football match is displayed as an instant prompt to the user as to what the website is focussed on. 
A section for how to use the website is included, which details the process of adding a bet and updating a bet.
For users or guest unfamiliar with betting, a short introductory guide offers them an explanation for how betting works, and what the terminology of the site means. 
This information makes the site accessible to all visitors, whatever their betting experience and knowledge. 

**Add A Bet**
One of the main reasons for visiting the site is to track the success of your own football bets, and this page is where the user is able to add their bets to the site. 
The page is intentionally kept very clean so that the important information is clearly visible and the user is not distracted. The user can add up to 6 matches (lines) in a single bet.
The details required for each line are:
 - Home Team: The team playing at home in the fixture
 - Away Team: The team playing away in the fixture
 - Your prediction: Choose from "Home" (Home team wins), "Away" (Away team wins), "Draw" (The teams draw)
 - Odds: The user enters the odds of their selection, taken from the betting site where they placed the bet.

By default, the match prediction of each line is set to "Home". 
<b>Validation</b>
 - Any bet must have a valid stake amount before the bet is saved. Minimum stake is 0.01.
 - Minimum odds for any line is 1.00. This is stated at the bottom of the page to assist the user. 
 - If a line has any team or odds data entered, it will be validated as a completed line. 
 - Home Team, Away Team and Odds must all be valid, or all be empty for the bet to save.

The "Save Bet" button is labelled clearly and is the only button on the page, so the user is guided with how to proceed.

Once saved successfully, the betting form is cleared and a confirmation message is displayed to the user.

I decided to allow bets with no lines to pass validation and be saved. This allows users the ability to update their betting balance (on the site) for any reason, without having to reference a football match.

**View Bets**

At the top of the page are links for the user to switch between two views. Open Bets and Settled Bets. Open bets 

All open bets are displayed on this page. This includes bets placed by the user, and other users on the site. The username of the bettor is distinctly displayed in the bet header. The bets are ordered by their modified date to keep the new additions and the newly modified as the most prominent at the top.
To keep the page from being too busy on the eye, I have implemented an accordion element for each bet so that the individual line detail can be hidden or displayed. The top five bets on the page are expanded by default - the rest are initially collapsed.

From this 'open bets' page, a user is presented with two buttons for each of their bets - Update and Delete. This is part of the CRUD functionality solution to allow a user to update or delete their bets. 
At the top of the page, the user's current bank balance is permanently displayed so there is no action for the user to search for it.



**Update Bet**

From the View Bets page, the user is presented with all open bets on the site. The bets are displayed in a single list with no pagination. This allows the user to easily scroll though to find what they are looking for. 
The Update Button is clearly visible on bets that the user has placed themselves. 
If clicked, the user is presented with the Update Bet screen.
Here the user can edit all fields associated with the bet. 
 - Stake: To correct an error with the stake previously entered.
 - Status: While the status is pending the bet remains open. The user will update the status to reflect whether the bet was a winner or loser after the matches have been played. If the status is not pending, the bet will be considered 'settled'.
  - For a winning bet, the settled amount should be greater than the stake.
  - For a losing bet, the settled amount should be less than the stake.
 - Settled Amount: When the bet is settled, the user enters the amount that the bet returned. 

The text at the bottom of the page is dynamic and responds to changes in the bet status field, informing the user what will happen when they save the changes.

Validation:
There is Javascript validation to check the status of the bet correctly reflects the settled amount compared to the stake.
- For a bet to win, the settled amount must not be lower than the stake amount
- For a bet to lose, the settled amount must not be lower than the stake amount

**Delete Bet**
From the View Bets > Open Bets page, the user is able to delete any of their own bets. This feature is only available on open bets. Once the bet is settled it can only be deleted by the site administator. This is to ensure the settled bets page records a full history of settled bets. 

**Money List**
The money list page presents the user with an ordered list of all user's bank balances, ordered with the highest balance at the top.
The leader at the top of the table is highted in green, and the user row is highlighted in blue (if not the leader).


## Technologies Used

### Languages

- HTML5
- CSS
- Javascript
- Python

### Libraries & Frameworks

* [Django 3.2.18](https://www.djangoproject.com/) - Free and open source Python Web Framework
* [Gunicorn 20.1.0](https://gunicorn.org/) - A Python WSGI HTTP server compatible with Django and used to run the project on Heroku
* [PostgreSQL 0.5.0](https://www.postgresql.org/) - A powerful, open-source object-relational database system
* [Pyscopg2 2.9.5](https://www.psycopg.org/docs/) - A PostgreSQL database adapter for Python
- [Heroku](https://www.heroku.com) - A cloud platform as a service
- [SQLite3](https://docs.python.org/3/library/sqlite3.html) - The database provided by Django
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Integrated set of Django applications addressing authentication and registration
- [Bootstrap 4.6.2]

### Tools

- [GitPod](https://www.gitpod.io/) - Cloud development environment used
- [GitHub](https://github.com/) - Cloud based git repository used
- [W3C Validator](https://validator.w3.org/) - A validator which checks the markup validity of Web documents in HTML, XHTML, SMIL, MathML, etc.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - A validator which checks the validity of CSS code
- [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) - Highlights syntactical and stylistic problems in Python source code
- [Chrome DevTools and Lighthouse](https://developer.chrome.com/docs/devtools/) - Web Developer Tools
- [Autoprefixer CSS Online](https://autoprefixer.github.io/) - A PostCSS plugin which parses CSS and adds vendor prefixes 
- [Am I responsive](https://ui.dev/amiresponsive) - For responsive visuals of the website
- [CanIUse](https://caniuse.com/) - Browser support tables for modern web technologies
- TinyPNG(https://tinypng.com/) - Compresses images to reduce the file size
- TinyURL(https://tinyurl.com/app/) - Shortens links
- [Pexels](https://www.pexels.com/) - Stock Photos
- [Google Fonts](https://fonts.google.com/) - Fonts
- [Font Awesome](https://fontawesome.com/) - Icons
- [Balsamiq](https://balsamiq.com/wireframes/) - Low Fidelity Wireframes
- [BrowserStack](https://www.browserstack.com/) - App and Browser Testing


## Technologies

## Testing
All testing information is documented in TESTING.md

## Deployment

### How to clone the project
<details>
<summary>Details</summary>

1. Log into Github
2. Go to the project repository at (https://github.com/bmays9/bet-tracker)
3. Click on the Code button and copy your preferred link.
4. Open the terminal in your code editor and change the working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal, paste the link you copied and hit enter.
</details>

### How to fork the repository
<details>
<summary>Details</summary>

1. Login to Github.
2. Go to the project repository at (https://github.com/bmays9/bet-tracker)
3. Click the 'Fork' button.
</details>

### Code Institute PostgreSQL Database

<details>
<summary>Details</summary>

1. Create a [Code Institute PostgreSQL](https://dbs.ci-dbs.net/manage/KeeMR5RVAMT6WX8k/) account.
2. Create a new instance.
3. Copy the database URL.
4. Add database to the settings.py-file in Django.

</details>

---
  

### Deploying to Heroku

<details>

<summary> Deploying to Heroku </summary>

To install the Django framework installed and deploy to Heroku I followed the Code institutes [Django Blog cheatsheet](docs/django-blog-cheatsheet.pdf)


</details>

## Bugs

Code Validation Bugs

Homepage
On the HTML page, the fonts were not loading correctly due to splitting the code across two lines. This was rectified during code validation phase.

unclosed elements

On View Bets Page, main issue was an unclosed span element within the line element that repeated for each bet.


## References

## Credits
