# UMU Baseball Twitter Application
**A Twitter API application that is used to post tweets from the @umubaseball twitter page during games.**<br><br>
![Home screen](https://github.com/schrotbe2021/UMU-Baseball-Twitter-Application/blob/master/images/HomeScreen.PNG)

## Problem to be solved
Acting as the social media manager for the University of Mount Union baseball team, I wanted a solution for making consistent, formatted tweets during games.

## How I solved the problem
My solution was to build an application using the Twitter API that can Tweet from a set of predefined set of templates.
What I used to build the project:
* **Python**
  * I had never worked with Python and saw this project as a good way to learn Python.
* **TKinter**
  * GUI Library used to style the application.
* **Python Twitter**
  * Wrapper used to work with the Twitter API (https://github.com/sixohsix/twitter)

## Features of application
* Ability to Tweet from a set of predefined, formatted Tweets:
  * **Start of Game**
  * **Lineup**
  * **Scoring Change**
  * **End Game**
  * **Substitution**
  * **Custom Tweet**
* Attach image, video, or gif to any Tweet.
* After Tweet is made a check screen shows the most recent Tweet on the account to verify the success of the Tweet.
  * If a change is needed to the Tweet this page also allows to delete the Tweet <br><br>
![Tweets](https://github.com/schrotbe2021/UMU-Baseball-Twitter-Application/blob/master/images/Tweets.PNG)

## Example Tweet (Scoring Change)
To make a Tweet the user fills in the input areas. This input will be used to fill in fields of the predefined Tweet.<br><br>
![Scoring change](https://github.com/schrotbe2021/UMU-Baseball-Twitter-Application/blob/master/images/ScoringChangeTweet.PNG)

When the user presses `Send Tweet` they are prompted if they want to post media with it. After the Tweet is made the user is taken to a screen that shows if the Tweet has been posted to the @umubaseball Twitter page. This page also gives the option to delete the tweet.<br><br>
![Example Tweet](https://github.com/schrotbe2021/UMU-Baseball-Twitter-Application/blob/master/images/ScoreChange.PNG)

## Future Improvements
* Develop the application using Electron (JS, HTML, and CSS)
  * Would make distributing the app easier. Python is dificult to build desktop applications for all Operating Sytems. It was good for personal use but for future development a different solution would need to be developed.
* There is a lot of redundancy in the input fields of the app. I would like to store the opponent and score so that it would not have to be filled in every time a Tweet is made.
* Make the application have the  ability to Tweet from different accounts.
  * Generalize the UI more so that it could be distributed to other teams.
