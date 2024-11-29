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
Featured on all pages as part of the base template, the footer contains information about me, the site creator and provides a way to get in contact.
By is styled in a minimalistic way to present the information clearly.

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

