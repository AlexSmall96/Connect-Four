# Connect Four
This python terminal application is an arcade-style version of the classic game Connect Four.

The game has a classic arcade feel to it, which fits well within the limits of a python terminal application. The application prints a board and counters to the terminal to illustrate the game and is updated through user input. The game can be played as a two-player game, with both players operating the same device, or as a one-player game, with the user playing against the computer. The computer choice is mostly random, but the computer has some intelligence programmed in as it blocks streaks of 4 being played by the user and can detect when it is about to win. The user(s) can select their usernames, and the game is replayable, giving the user a customized, complete experience. 

## Live Site 
[https://connect-four-kxsw.onrender.com/](https://connect-four-kxsw.onrender.com/)
![](documentation/images/live_site_1.png) | ![](documentation/images/live_site_2.png)

The deployed project is currently on Render's free tier. Projects on this tier spin down during periods of inactivity, therefore, there may be a delay when loading the above URL.

## Repository 
[https://github.com/AlexSmall96/Connect-Four](https://github.com/AlexSmall96/Connect-Four)

## Author 
Alex Small
## Table of Contents
- [Connect Four](#connect-four)
  * [Live Site](#live-site)
  * [Repository](#repository)
  * [Author](#author)
  * [Table of Contents](#table-of-contents)
- [UX](#ux)
  * [Target Audience](#target-audience)
  * [Project Goals and Planning](#project-goals-and-planning)
    + [Game Logic Flowchart](#game-logic-flowchart)
  * [User Stories](#user-stories)
    + [Site User](#site-user)
    + [Website Owner](#website-owner)
  * [Features](#features)
  * [Future Features](#future-features)
  * [Testing](#testing)
  * [Frameworks & Programs Used](#frameworks---programs-used)
  * [Python Libraries Used](#python-libraries-used)
- [Deployment](#deployment)
    + [Deploying the Site to Heroku](#deploying-the-site-to-heroku)
    + [Forking the Repository on GitHub](#forking-the-repository-on-github)
    + [Cloning the Repository on GitHub](#cloning-the-repository-on-github)
- [Credits](#credits)
  * [Content](#content)
  * [Code](#code)
  * [Acknowledgements](#acknowledgements)
# UX
## Target Audience
The application is targeted towards anyone, with adults appreciating the retro arcade style, playful computer messages, and the basic artificial intelligence involved.  Children can enjoy the ability to play a fully functioning game in a simple terminal environment.
 
## Project Goals and Planning
The goal of this project was to create a game that displayed enough complexity in the python code, that could also be visualized creatively and engagingly in the python terminal. Due to the rules of the game, the logic required to create a fully functioning connect four application is quite complex at times, particularly with win detection. The project also aims to provide a user-friendly experience, with easy-to-follow instructions, simple input methods, and a customizable and replayable experience.

### Game Logic Flowchart
The below flowchart was used to plan and illustrate the logic of the game. Green arrows signify correct input or proceeding to the next step, while red arrows signify incorrect input.

![](documentation/images/flowchart.png)

## User Stories
### Site User

As a site user, I want to:

- See a visually appealing title that fits the theme of the game
- Receive clear instructions on how to set up and play the game
- Customise elements of the game such as username
- Receive clear feedback on the outcome of the game
- Have the ability to replay the game

### Website Owner

As a site owner, I want to:

- Express my design ideas freely and creatively
- Add my unique ideas to a game such as customizable usernames
- Write complex logic to ensure the game is fully functional in all play modes
- Showcase my skills and advertise my portfolio

## Features

The features of the site are given below, along with an image and its value to the user.

Feature                    |    Image                   |         Value to User
:-------------------------:|:-------------------------: | :-------------------------: 
Title                      | ![](documentation/images/Title.png)| An eye-catching title to draw the user's attention, stating clearly what game it is and giving the user an idea of the arcade style of the game  
Welcome Message             | ![](documentation/images/welcome.png)| A welcoming message, setting up the playful theme of the game. Gives the user the ability to choose when the instructions are loaded by pressing enter.      
Instructions            | ![](documentation/images/instructions.png)| Details the instructions clearly, both the rules of the game and how to input information. Gives the user the ability to choose when to load the next screen by pressing enter.
No. of players selection          | ![](documentation/images/no_players.png)| Allows the user to choose whether to play against the computer or another player using the same device. This allows the user to always be able to play even if they are alone.
Username selection         | ![](documentation/images/usernames.png)| Allows the user(s) to choose their username(s), which personalizes the game and makes the feedback messages more engaging.
Game area         | ![](documentation/images/game_area.png)| Bright colors allow the user to see their counters on the board, the board itself is well structured making the game feel more realistic and giving the players clear feedback on their progress.
Column input        | ![](documentation/images/input.png)| Provides the user with a simple and intuitive way of inputting their column choice to add a counter to the game board
Win detection       | ![](documentation/images/win_detection.png)| Gives the user the complete experience of playing a fully functioning connect four game, with vertical, horizontal, and diagonal wins being detected.
Win feedback message | ![](documentation/images/win_feedback.png)| Provides the user with a personalized well done message when they win the game, containing their username.
Replay option | ![](documentation/images/win_feedback.png)| Allows the user to smoothly and efficiently replay the game, reselecting the game mode, usernames, and colors. This creates a complete and enjoyable experience for the user.
Computer is thinking message | ![](documentation/images/computer_thinkin.png)| Makes the game more engaging and fun, and gives the user the feeling of playing against an intelligent computer.
Computer win detection and prevention | ![](documentation/images/4.5.png)| Allows the user to experience a fully functioning game even in single-player mode, with the computer making intelligent decisions.
Commiserations message | ![](documentation/images/computer_won.png)| Further personalizes the game, completing the experience with a message containing their username
Goodbye message | ![](documentation/images/goodbye.png)| Completes the experience with a simple goodbye message, thanking the user for playing and allowing them to visit the developer's GitHub profile to explore more projects.

## Future Features

- More complex Artificial Intelligence algorithms could be implemented to make the computer perform better and therefore make single-player mode more challenging. A common algorithm that is used in game theory is known as a [Minimax](https://en.wikipedia.org/wiki/Minimax) algorithm, which could be implemented in this case.

- Another feature that could be developed is the ability to play two-player mode online with another player. 

- Further developments of this project may involve fixing the bug detailed in the Issues Found Section of [TESTING.MD](https://github.com/AlexSmall96/Connect-Four/blob/main/TESTING.md). When the 'Computer is thinking message...' is displayed, the user is still able to input a column choice, which affects their future inputs and results in multiple counters appearing on the board at once.

## Testing
Testing is detailed fully in [TESTING.MD](https://github.com/AlexSmall96/Connect-Four/blob/main/TESTING.md).

## Frameworks & Programs Used

- [Github](https://github.com/) 
- Gitpod
- [Heroku](https://id.heroku.com/login)
- [Figma](https://www.figma.com/)
- [Markdown Table of Contents Generator](https://ecotrust-canada.github.io/markdown-toc/).
- Python

## Python Libraries Used

- [os](https://docs.python.org/3/library/os.html): This module provides a portable way of using operating system-dependent functionality. It was used in this project to provide a simple way of clearing the terminal after each turn, so the game board can be reprinted. 

- [time](https://docs.python.org/3/library/time.html) : This module provides various time-related functions. The function time.sleep() was used in this project to allow the 'Computer is thinking...' to be displayed for 1.5 seconds, giving the impression of a computer deciding which column to select.

- [random](https://docs.python.org/3/library/random.html): This module implements pseudo-random number generators for various distributions. It was used in this project in single-player mode, when the computer hasn't detected any potential wins the column choice is random.


# Deployment
### Deploying the Site to Heroku

1. Create an account on [Heroku](https://id.heroku.com/login) and log in.
2. Navigate to the Dashboard.
3. Click 'New', and 'Create new app'.
4. Select the appropriate name, app names must be unique so 'python-connect-four' will be unavailable.
5. Select Location.
6. Click 'Create app'.
7. Navigate to the 'Settings' tab, and click "Reveal Config Vars".
8. Add a Config Var with KEY: 'PORT' and value: '8000', and select 'Add'.
9. Navigate to the 'Buildpacks' section and click 'Add buildpack'. 
10. Add in order'python' then 'nodejs' to the buildpacks section. Order can be changed by clicking and dragging.
11. Navigate to the 'Deployment' tab. For 'Deployment method', select Github.
12. Under 'Search for a repository to connect to', enter the appropriate GitHub username and repository name
13. To deploy the repository, either select 'Enable Automatic Deploys', which deploys the site after each push to GitHub or Manually click 'Deploy Branch'
14. In both deployment methods, the main branch or any forked branches may be chosen, see [Forking the Repository on Github](#Forking-the-Repository-on-GitHub)

### Forking the Repository on GitHub
1. On GitHub.com, navigate to the main page of the [Connect Four](https://github.com/AlexSmall96/Connect-Four) repository.
2. In the top-right corner of the page, click Fork.
3. Select an owner for the forked repository.
4. By default, forks are named the same as their upstream repositories. You can change the name of the fork to distinguish it further.
5. Optionally, add a description of your fork.
6. Choose whether to copy only the default branch or all branches to the new fork. For many forking scenarios, such as contributing to open-source projects, you only need to copy the default branch. By default, only the default branch is copied.
7. Click Create fork.
### Cloning the Repository on GitHub
1. On GitHub.com, navigate to the main page of the [Connect Four](https://github.com/AlexSmall96/Connect-Four) repository.
2. Above the list of files, click Code.
3. Copy the URL for the repository.
4. Open Terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier.
7. Press Enter to create your local clone.

# Credits
## Content
The content of the site is all original thought, however, the game itself is based on the classic game [Connect Four](https://en.wikipedia.org/wiki/Connect_Four)

## Code
The resources used for this project were the [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+UK+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=1578649861&hsa_grp=62188641240&hsa_ad=635720257674&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAiA5Y6eBhAbEiwA_2ZWIUE0LRewvfAYnQS69Lujb5s2FrQjmX0Idzqj-Olbamn1DbS2D-R7gBoC-1AQAvD_BwE
)  Python Essentials Module, along with some external resources:

- The code used to color the o's in the title was taken from the following article on [stackabuse](https://stackabuse.com/how-to-print-colored-text-in-python/).

- The symbols used to create the title, board and counters were inspired by [alt-codes.net](https://www.alt-codes.net).

- The code used to clear the last line of the terminal when 'Computer is thinking message ...' displays was taken from the following forum [stackoverflow](https://stackoverflow.com/questions/44565704/how-to-clear-only-last-one-line-in-python-output-console).

All external resources are commented on in the code at the relevant places.

## Acknowledgements 
This application was created as a portfolio 3 project for the Diploma in Full Stack Software Development from [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+UK+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=1578649861&hsa_grp=62188641240&hsa_ad=635720257674&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAiA5Y6eBhAbEiwA_2ZWIUE0LRewvfAYnQS69Lujb5s2FrQjmX0Idzqj-Olbamn1DbS2D-R7gBoC-1AQAvD_BwE
)
I would like to thank my mentor Harry Dhillon for his encouraging support and detailed feedback throughout this project.
