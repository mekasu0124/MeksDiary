# MeksDiary
 A simple diary application usable by anyone.

 Table Of Contents

- [Installation and Running The Application](#installation-and-running-the-application)
- [Issues](#issues)

# Installation and Running The Application

To be able to run this application, you will need the following items installed on your computer:

1) Python & Git
    - Windows: [How To Install Python On Windows](https://learn.microsoft.com/en-us/windows/python/beginners)
    - Mac: [How To Install and Update Python On Mac](https://www.dataquest.io/blog/installing-python-on-mac/#installing-python-mac:~:text=script%20on%20Mac-,Installing%20and%20Updating%20Python%20on%20Mac,-I%20have%20two)
    - Linux: Python should come with your os by default. If you open your terminal and type `python --version` and you get no results, then you will need to run `sudo apt-get install python pip` or if you're on arch linux `sudo pacman -S python pip`.

    - To install Git on your system, [click here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

2) After you've installed python, you will need to clone this repository.
    - Open your command prompt and cd to the desired install location.
    - Once inside the desired install location, type `git clone https://github.com/mekasu0124/MeksBattleShip.git`
    - After the clone has finished you will need to create a virtual environment. cd into the cloned repo using `cd MeksBattleShip` and run the following:
        - Windows: `python.exe -m venv env`
        - Mac & Linux: `python -m venv env`
    - Once the venv has finished, you'll then type either command below (os dependent) to activate the venv:
        - Windows: `env\Scripts\activate`
        - Mac & Linux: `source env/bin/activate`
    - After activation, your terminal should look something like this `(env) C:\Users\Usr\<path_to_cloned_repo>`. Now you need to install the requirements for the program.
        - Windows: `python.exe -m pip install -r requirements.txt`
        - Mac & Linux: `pip install -r requirements.txt`

3) From here, you *should* be all finished. You'll simply stay in the same terminal with the activated virtual environment and just run `python main.py` to launch the game. 

# Issues

For anyone that may have issues with the application itself, please head over to the issues tab of this repository and [post a good issue](https://github.com/codeforamerica/howto/blob/master/Good-GitHub-Issues.md). From there, the issue will be reviwed and a change *may* be put into place. Not all changes may take effect/affect as I am more focused on the application working correctly as opposed to suggestions. If you are posting a suggestion, please put "Suggestion" in the title of your issue. Do keep in mind that I do not work for Python and if you're having issues getting python to work, please join their [discord server](https://www.pythondiscord.com/) and request assistance from there. Otherwise, any issues with PySide6 or the application itself, I'll be happy to help in any way that I can.