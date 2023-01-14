# Testing
Back to [README.MD](https://github.com/AlexSmall96/Connect-Four/blob/main/README.md).
## Table of Contents
 - [Testing](#testing)
  * [Table of Contents](#table-of-contents)
  * [Manual Testing](#manual-testing)
    + [Game Setup](#game-setup)
    + [Screenshots where applicable for Game Setup](#screenshots-where-applicable-for-game-setup)
    + [Game Play - Single Player Mode](#game-play---single-player-mode)
    + [Screenshots where applicable for Game Play - Single Player Mode](#screenshots-where-applicable-for-game-play---single-player-mode)
    + [Game Play - Two Player Mode](#game-play---two-player-mode)
    + [Screenshots where applicable for Game Play - Two Player Mode](#screenshots-where-applicable-for-game-play---two-player-mode)
    + [Win Detection](#win-detection)
    + [Screenshots where applicable for Win Detection](#screenshots-where-applicable-for-win-detection)
    + [Replay and Exiting Game](#replay-and-exiting-game)
    + [Screenshots where applicable for Replay and Exiting Game](#screenshots-where-applicable-for-replay-and-exiting-game)
  * [User Stories Testing](#user-stories-testing)
  * [Validation Testing](#validation-testing)
## Manual Testing
Throughout this section, tests have been divided into sections based on each stage of the game sequence, and marked as a certain category. The expected and actual results are given, along with a pass/fail indicator. Each test has a unique reference number and, where applicable, these numbers are matched to screenshots of the test results below each table.
 
### Game Setup
 
| Test | Category         | Expected Result                     | Actual Result                                              | Pass/Fail |
|------|------------------|-------------------------------------|------------------------------------------------------------|-----------|
|1.1   |Loading Information | Home screen with title and welcome message appears upon pressing run program button | Full screen loads as expected |Pass|
|1.2   |Loading Information| Pressing Enter loads Instructions, with a further prompt to press enter to set up game at bottom of screen | Instructions loads as expected, prompt message appears after instructions |Pass|
|1.3   |Loading Information| Pressing Enter after instructions are given results in number of players selection stage | Upon pressing enter a message asking user to select number of players appears as expected  |Pass|
|1.4   |Input Validation| Entering a non numerical symbol at number of players selection stage results in warning message and user is asked to retry| 'd' is inputted and a message stating input must be either 1 or 2 appears, user is promted to reselct number of players |Pass|
|1.5   |Input Validation| Entering a number other than 1 or 2 at number of players selection stage results in warning message and user is asked to retry| '3' is inputted and a message stating input must be either 1 or 2 appears, user is promted to reselct number of players |Pass|
|1.6   |Input Validation| Entering 1 results in a message to allow the user to choose username | '1' is inputted and a username input message appears as expected |Pass|
|1.7   |Input Validation| User is able to enter username consisting of any symbol | Username consisting of letters, numbers and special characters is entered and input is accepted |Pass|
|1.8   |Loading Information| Entering username results in prompt message asking user to select their color, with username appearing at start of message  | Prompt message appears with username and color selection as expected |Pass|
|1.9   |Input Validation| Entering anything other than 'red' or 'yellow' results in message asking user to select from available colors  |'blue' is entered, feedback appears as expected and user is asked to reselect colors |Pass|
|1.10   |Input Validation| Entering 'red' takes the user to the game play screen |'red' is entered and game screen loads as expected  |Pass|
|1.11   |Input Validation| Entering 'yellow' takes the user to the game play screen |'yellow' is entered and game screen loads as expected  |Pass|
|1.12   |Loading Information| Entering 'red' at color selection results in red counter appearing during gameplay prompts|'red' is entered gameplay input message appears with red counter  |Pass|
|1.13   |Loading Information| Entering 'yellow' at color selection results in yellow counter appearing during gameplay prompts|'red' is entered and gameplay input message appears with red counter  |Pass|
|1.14   |Loading Information| Entering 2 at select number of players stage results in a prompt for payer 1 to enter username, followed by a prompt for player 2 to enter username once player 1 has completed input |2 is entered and prompt 1 appears, followed by prompt 2 upon completing prompt 1 input |Pass|
|1.15   |Input Validation| If usernames are the same, a message stating usernames must be different appears, and both users are asked to reselect usernames  |Username is entered for both players and feedback appears as expected|Pass|
|1.16   |Loading Information| Once both usernames are selected, player 1 is prompted to select their color |Both usernames are entered, and player 1 username appears asking them to select a color|Pass|
|1.17   |Logic| Player 2's color is automatically assigned to the color that player 1 didn't select |Player 1 selects red and player 2 is assigned yellow |Pass|

### Screenshots where applicable for Game Setup

  1.1                        | 1.2
:-------------------------:|:-------------------------:
![](documentation/images/1.1.png) | ![](documentation/images/1.2.png)
 
 1.3                     | 1.4
:-------------------------:|:-------------------------:
![](documentation/images/1.3.png) | ![](documentation/images/1.4.png)

1.5                     | 1.6
:-------------------------:|:-------------------------:
![](documentation/images/1.5.png) | ![](documentation/images/1.6.png)

1.7, 1.8                     | 1.9
:-------------------------:|:-------------------------:
![](documentation/images/1.7_1.8.png) | ![](documentation/images/1.9.png)

1.12                       | 1.13
:-------------------------:|:-------------------------:
![](documentation/images/1.12.png) | ![](documentation/images/1.13.png)

1.14                       | 1.15
:-------------------------:|:-------------------------:
![](documentation/images/1.14.png) | ![](documentation/images/1.15.png)

1.16                       |1.17
:-------------------------:|:-------------------------:
![](documentation/images/1.16.png)|![](documentation/images/1.17.png)

### Game Play - Single Player Mode

| Test | Category         | Expected Result                     | Actual Result                                              | Pass/Fail |
|------|------------------|-------------------------------------|------------------------------------------------------------|-----------|
|2.1   |Input Validation  | When column selection prompt appears, letters cannot be inputted | 'd' is entered and feedback is given to user to choose a whole number between 0 and 6 |Pass|
|2.2   |Input Validation  | Numbers outwith 0 - 6 cannot be entered to column selection| '7' is entered and feedback is given to user to choose a whole number between 0 and 6 |Pass|
|2.3   |Input Validation  | Non integers cannot be entered to column selection| '1.5' is entered and feedback is given to user to choose a whole number between 0 and 6 |Pass|
|2.4   |Loading Information  | When a whole number between 0 and 6 is entered, the current users counter is added to the corresponding column | '6' is entered and a counter appears in column 6 |Pass|
|2.5   |Logic | When user selects a column with counter already on it, the counter is added to the next row up | User selects column and counter appears above highest counter in column as expcted |Pass|
|2.6   |Logic | Computer is thinking message appears once user enters column selection | Users counter is added and message appears as expected |Pass|
|2.7   |Logic | Once computer is thinking message dissapears, computers counter appears in a random column (computer column choice is non random in certain cases - see [Win Detection](#win-detection)) | Computer message dissapears and the correspoinding counter color is added to the game area |Pass|
|2.8   |Logic | If computer chooses a column that already has a counter in it, the computers counter is added to the next row up | Computer chooses a column with counter on bottom row and counter is added to row directly above as expected |Pass|
|2.9   |Logic | If user chooses a column that is full, a message stating column is full appears and user is prompted to reselect a column| Full column is chosen and feedback is given to user as expected |Pass|
|2.10   |Logic | Computer never chooses full column| Computer's choice is always a column with an available space as expected |Pass|

### Screenshots where applicable for Game Play - Single Player Mode

2.1                        | 2.2                      |2.3
:-------------------------:|:-------------------------:|:-------------------------:
![](documentation/images/2.1.png) | ![](documentation/images/2.2.png)|![](documentation/images/2.3.png)

2.4                        | 2.5         
:-------------------------:|:-------------------------: 
![](documentation/images/2.4a.png) ![](documentation/images/2.4b.png) |![](documentation/images/2.6a.png)![](documentation/images/2.6b.png) 

2.6                        | 2.7
:-------------------------:|:-------------------------:
![](documentation/images/2.6_final.png) | ![](documentation/images/2.7_final.png)

 2.8                        | 2.9         
:-------------------------:|:-------------------------: 
![](documentation/images/2.8a.png) ![](documentation/images/2.8b.png) |![](documentation/images/2.9.png) 

### Game Play - Two Player Mode

| Test | Category         | Expected Result                     | Actual Result                                              | Pass/Fail |
|------|------------------|-------------------------------------|------------------------------------------------------------|-----------|
|3.1   |Logic | Once one player has selected a column, the other player is prompted with username appearing before message| Prompt message alternates between usernames and counter colors as expected|Pass|
|3.2   |Logic | When either player selects a column with a counter already on it, the counter is added to the next row up| Counter is added 1 row above for either player as expected|Pass|
|3.3   |Logic | When either player selects a column that is full, a message stating column is full appears and user is prompted to reselect a column| Feedback appears as expected when either player selects a full column|Pass|

### Screenshots where applicable for Game Play - Two Player Mode

 3.1                        | 3.2    
:-------------------------:|:-------------------------: 
![](documentation/images/3.1.png) |![](documentation/images/3.2a.png) ![](documentation/images/3.2b.png) ![](documentation/images/3.2c.png) 

 3.3                        |
:-------------------------:|
![](documentation/images/3.3a.png)![](documentation/images/3.3b.png)  |



### Win Detection

| Test | Category         | Expected Result                     | Actual Result                                              | Pass/Fail |
|------|------------------|-------------------------------------|------------------------------------------------------------|-----------|
|4.1   |Logic | When a player or computer has a vertical streak of 4 of their counters in any column, the game is ended| Vertical streak is reached in any column and game ends. A sample of columns are given as screenshots |Pass|
|4.2  |Logic | When a player or computer has a horizontal streak of 4 of their counters in any row, the game is ended| Horizontal streak is reached in any row and game ends. A sample of rows are given as screenshots |Pass|
|4.3  |Logic | When a player or computer has a diagonal streak of 4 of their counters the game is ended| Diagonal streak is reached  and game ends. A sample of scenarios are given as screenshots |Pass|
|4.4   |Logic | When a player wins the game, a well done message appears containing their username | User wins and message appears as expected (See 4.1 - 4.3 screenshots) |Pass|
|4.5  |Logic | When the computer wins, a message containing the players username appears stating computer has won| Computer wins and message appears as expected|Pass|
|4.6  |Logic | In single player mode, computer detects when player is about to win and if possible, blocks their streak with a counter| Player has a streak of 3 and computer blocks as expected|Pass|
|4.7  |Logic | In single player mode, computer detects when itself is about to win and if possible, adds a counter to its own streak| Computer has a streak of 3 and next move from computer is winning move as expected|Pass|

### Screenshots where applicable for Win Detection

- For tests 4.1, 4.2 and 4.3, a sample of scenarios have been given as screenshots. Examining the logic in board.check_winner function, shows that the below screenshots can be extrapolated as evidence of all scenarios passing the test. The Function is also independent of wether computer or human played the streak, therefore the given screenshots also apply to single player mode.

- 4.1 : Below is a sample of scenarios where a vertical win has been detected. 

6th column red win                      | 3rd column yellow win | 
:-------------------------:|:-------------------------: 
![](documentation/images/4.1a.png)| ![](documentation/images/4.1b.png)  



- 4.2 : Below is a sample of scenarios where a horizontal win has been detected. Above each image, the column range over which the streak is achieved is given.

0 - 3 yellow win    | 1 - 4 yellow win        | 2 - 5 red win | 3 - 6 red win
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------: 
![](documentation/images/4.2a.png)| ![](documentation/images/4.2b.png)| ![](documentation/images/4.2c.png) |![](documentation/images/4.2d.png) 


- 4.3 Below is a sample of scenarios where a diagonal win has been detected. Above each image, the column range over which the streak is achieved is given, along with the slope direction.

0 - 3 upwards red win  | 1 - 4 upwards red win      |  2 - 5 upwards red win |  3 - 6 upwards red win
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------: 
![](documentation/images/4.3a.png)| ![](documentation/images/4.3b.png)| ![](documentation/images/4.3c.png) |![](documentation/images/4.3d.png) 

0 - 3 downwards yellow win  | 1 - 4 downwards yellow win      |  2 - 5 downwards yellow win |  3 - 6 downwards yellow win
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------: 
![](documentation/images/4.3e.png)| ![](documentation/images/4.3f.png)| ![](documentation/images/4.3g.png) |![](documentation/images/4.3h.png) 

4.5, 4.6, 4.7 | 
:-------------------------:|
![](documentation/images/4.5.png)|  


### Replay and Exiting Game

| Test | Category         | Expected Result                     | Actual Result                                              | Pass/Fail |
|------|------------------|-------------------------------------|------------------------------------------------------------|-----------|
|5.1   |Loading Information | When a game is ended, entering 'y' takes the user back to the instructions | 'y' is entered and instructions screen appears as expected|Pass|
|5.2   |Loading Information | Usernames and colours are reselected when game is replayed| Pressing enter on second instructions screen loading prompts username and color selection as expected|Pass|
|5.3   |Loading Information | Game screen loads as normal when game is replayed| Game screen loads as expected|Pass|
|5.4   |Loading Information | Pressing enter without inputting 'y' at end of game exits game and goodbye message appears| Enter is pressed at end of game and message appears as expected|Pass|


### Screenshots where applicable for Replay and Exiting Game
5.1                     | 5.4                         | 
:-------------------------:|:-------------------------: 
![](documentation/images/5.1.png)| ![](documentation/images/5.3.png)  

 
## User Stories Testing

 
## Validation Testing
 
 All three .py files have been validated through the [Code Institute Python Validator](https://pep8ci.herokuapp.com/). run.py and setup.py passed with no errors or warnings. board.py had two warnings regarding lines with whitespace, however these keep reappearing on deletion. As they don't affect any running of the code I chose to ignore these warnings. Screenshots of the results of the validator for each file are given below.

 - run.py
 
  ![](documentation/images/run.png)

  - setup.py

 ![](documentation/images/setup.png)

- board.py

 ![](documentation/images/board.png)

