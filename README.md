# Bet Tracker

Bet Tracker is a full-stack, responsive website built for football supports who enjoy betting on matches. The site is for bet tracking purposes only and all monetary amounts on the site are for documentation purposes only. 
<br>
It provides users with the opportunity to share their upcoming bets with the website community, and see how their results fare against other like-minded bettors. 

View the live website [here][https://track-my-bets-1ee4e00d237a.herokuapp.com/]
____

## Overview

Bet Tracker is a responsive website compatible with all current major browers. It is built for educational purposes using Bootstarp and the Django Framework. It consists of user authentication and permission logic, with full CRUD functionality on bets entered on the site. 

The site is aimed at betting and football enthusiasts who want to add an extra element to their betting by sharing and comparing with others. Part of responsible gambling is to keep a track of all betting, successful or not, and this site helps to achieve this 

## User Expectations

- The app should be easy to navigate and all betting information displayed intelligently.
- The user should be able to create, read, update and delete any football bets they want to track.
- The user should be able to compare their betting success with other users.
- The user should be able to view bets places by other users on the site.
- The app should be fully tested and run without bugs.

## Agile Methodology

## Wireframes


## Website Structure

### Homepage
The homepage welcomes users to the site and gives them a clear overview of the sites purpose. For visitors unfamiliar with betting, a clear description of football betting and how odds work is provided.

### View Bets
The View Bets page gives users a complete one-page view of all bets on the site. Bets are split into categories, "Open" and "Settled". Open bets are for upcoming matches and users are sharing their bets and predictions with each other. Users can gain insight and inspiration by knowing how other successful bettors are thinking about a certain match. The "Settled Bet" list is a historical record of all bets that have been settled.

### Add a Bet
An logged in user can add a new bet to the site at any time. The site allows up to 6 matches (lines) to be combined into a single bet.

### Update a Bet
While a bet is still open, the user can edit all details their bet. This can either be to correct a mistake, remove a cancelled fixture, or to enter the match result and update the bet status after the match(es) has been played.

### Money List
THe money list page allows users to see the ranking of their account balance compared to other users on the site. 

## Administration

## Database structure

<table>
<thead>
  <tr>
    <th>Field Name</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>

## Styling

## Features

**Header and Navigation**

The header and navigtaion bar are contained within the base template so that all pages on the site inherit the same design. The Bet Tracker brand name is an anchor tag which brings the user back to the home page whenever clicked.
The Navigation bar contains links to the "View Bets", "Add Bet", "Money List", "Login", "Logout" and "Register".
On smaller screens, the navigation bar condenses into a hamburger button, which when pressed, displays the navigation options vertically. 
The links have an active class assigned to them, styling the active-page link differently so the user always knows where within the site they are.
The links for "Registration", "Login" and "Logout are displayed dynamically and respond to the status of the current user. 
At the right hand side of the header is a statement confirming the username of the user currently logged in. This is visible on every page to rassure the user they are both logged in, and under which account.

<details>
<summary>Click to view screenshots of Navigation</summary>
</summary>
<details>

**Footer**
Featured on all pages as part of the base template, the footer contains information about me as the site creator and provides a way to get in contact. Links to my email and to my github page are both included.
The footer is styled in a minimalistic way to present the information clearly and concisely. All links are labelled for enhanced accessibility. 

**Home Page**
The home page welcomes the user or vistor and explains the purpose of the website. A photo of a football match is displayed as an instant prompt to the user as to what the website is focussed on. 
A section for how to use the website is included, which details the process of adding a bet, updating a bet, deleting a bet and settling a bet. 
For users or guest unfamiliar with betting, a short introductory guide offers them an explanation for how betting works, and what the terminolgy of the site means. 
This information makes the site acccessible to all visitors. 

**Add A Bet**
One of the main reasons for visiting the site is to track the success of your own football bets, and this page is where the user is able to add their bets to the site. 
The page is intentionally kept very clean so that the the important information is clearly visible and the user is not distracted. The user can add up to 6 matches (lines) in a single bet.
The details required for each line are:
 - Home Team: The team playing at home in the fixture
 - Away Team: The team playing away in the fixture
 - Your prediction: Choose from "Home" (Home team wins), "Away" (Away team wins), "Draw" (The teams draw)
 - Odds: The user enters the odds of their selection, taken from the betting site where they placed the bet.

By default, the match prediction of each line is set to "Home".
<b>Validation</b>
Any bet must have a valid stake amount before the bet is saved. Minimum stake is 0.01. 
If a line has any team or odds data entered, it will be validated as a completed line. 
Home Team, Away Team and Odds must all be valid, or all be empty for the bet to save.

The "Save Bet" button is lablled clearly.

Once saved successfully, the betting form is cleared and a confirmation message is displayed to the user.

I decided to allow bets with no lines to pass validation and be saved, to allow users the abilty to track their betting balance with non-football related bets. 

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



**Delete Bet**

**View Bets**
All open bets are 


**Money List**
The money list page presents the user with an ordered list of all user's bank balances, ordered with the highest balance at the top.

## Technologies

## Testing

## Deployment


### How to clone the project

1. Log into Github
2. Go to the project repository at (https://github.com/bmays9/bet-tracker)
3. Click on the Code button and copy your preferred link.
4. Open the terminal in your code editor and change the working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal, paste the link you copied and hit enter.


### How to fork the repository

1. Login to Github.
2. Go to the project repository at (https://github.com/bmays9/bet-tracker)
3. Click the 'Fork' button.



## Bugs



## References

