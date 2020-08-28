# Crowdmarker
Crowdmarker is a Python script to assist TAs in grading work on the  [Crowdmark](https://crowdmark.com/) platform.
Crowdmarker allows you to quickly insert comments by moving the cursor to where you would like to insert a comment
and hit a key to insert and save a comment with its associated points. 

Crowdkmarker also has mapped the F key to save a booklets score and move to the next unmarked booklet, and the G
key to enter a perfect score and move to the next unmarked booklet.

## Getting Started
### Prerequisites
- [Python 3](https://www.python.org/downloads/)
- A TA or Professor level account on [Crowdmark](https://crowdmark.com/)
- A Linux distro with root privileges. These instructions will use Debian compatibles OSs but can be changed for any distro.
- (Optional) [Python venv](https://docs.python.org/3/library/venv.html) is shipped with Python 3 but for some reason some distros separate it out into a separate package, such as python3-venv on Ubuntu/Debian.
Sorry Linux users, but you will have to install this if you haven't already.

### Installation
- Install or upgrade to [Python 3](https://www.python.org/downloads/).
Clone this repository, and move into it
- `git clone https://github.com/marcoscz1995/Crowdmarker.git`
- `cd Crowdmarker`

Configure your OS for Evdev (see [here](https://python-evdev.readthedocs.io/en/latest/install.html) for more info)
- `sudo apt-get install python3-dev python3-pip gcc`
- `sudo apt-get install linux-headers-$(uname -r)`

Configure your OS for PyAutoGui (see [here](https://stackoverflow.com/questions/34939986/how-to-install-pyautogui) for more info)
- `sudo pip3 install python3-xlib`
- `sudo apt-get install scrot python3-tk python3-dev`

(Optional, but recommended) Create and activate a virtual environment.
- `python3 -m venv crowdmarker-env`
- `source crowdmarker-env/bin/activate` 

Install the required packages
- `pip3 install -r requirements.txt`
If you get errors like `Failed building wheel for XXXX` you might need to install wheel
- `pip3 install wheel`

### Determine keyboard event number
Run keyboard_event_determiner.py (This script will run for three seconds, so be quick!)
- `sudo python3 keyboard_event_determiner.py`
- Click any key on the keyboard you wish to assign keys to.

You should see output like this in your terminal: `/dev/input/event7`. Record the number you see at the end of the output. In this case I would record 7 as my keyboard event number.


### Determine keyboard key codes
Run keycode_determiner.py
- `python3 keycode_determiner.py`

Click on the keys you would like to assign comments to. For example if you would like to assign the letter A to a comment, click on A and you should see in you terminal something like `KEY_A`. Record this.

Note: you should avoid the already assigned shortcut keys in Crowdmark (L, H, J, K, E, N, P, T, Z, C, X, Q, S, D), as well as 
the letters F and G as those are already mapped as described earlier (these can however be changed/removed in lines 85-88 in crowdmarker.py).

Tip: when selecting keys I suggest choosing those on the left hand side of the keyboard. This way you can select
comments with your left hand and choose where to insert them using your mouse with your right hand. I find this
the most efficient use of this script.

### Insert user inputs into Crowdmarker
Insert your comments, points, and associated keyboard keys and event to `crowdmarker.py`
- open `crowdmarker.py` in your favourite text editor
- in line 132 change `INSERT_EVENT_NUMBER_HERE` to the number you got from running `keyboard_event_determiner.py`
- in line 133 change `INSERT_QUESTIONS_MAX_SCORE_HERE` to the questions max score that you will be marking
- in lines 134 insert your comment, points and key code you want to assign to it that you get from running `keycode_determiner.py`. Add as many comments as you have keycodes. Just follow the format of `["comment", point, "key code"]`.

Note: if you want to put latex code that starts with reserved python string formating such as '\f' or '\n', just 
add 'r' before the start of the comment. For example: 
- `r"the correct answer is $$\frac{1}{2}$$"`

### Start marking
Once you are satisfied with your comments sign into Crowdmark, go to the question you want to mark and run the `crowdmarker.py` file.
- `python3 crowdmarker.py`
- go to your desired Crowdmark question
- move the cursor to where you would like to insert a comment
- click the associated key for that comment

The comment will then be inserted.

Happy Crowdmarking!

Note: due to how the script works, you should **not** move the cursor while the comment is being inserted as the comment will not be saved or the points will not be added. Also the comment cannot be posted too close to the margins of the questions as the points can be recorded wrong.

### Turn off the script
When you are done marking or want to turn off the script
- go to the terminal and press `Contrl+C` or hit the `Escape` key from anywhere to end the script. 

To deactivate the virtual environment just type in your terminal
- deactivate
 
### Contributing
If you would like to improve this script or have an idea to make it better, please post it to the github issues page. If you would like to develop it I will gladly accept pull requests.

Note: if you plan on using [Selenium](https://www.selenium.dev/) to improve the script consider that because [Crowdmark](https://crowdmark.com/) is written with [Ember.js](https://emberjs.com/) which uses dynamically generated attributes, there are many issues that make inserting comments difficult. In particular, when a long comment is inserted the page will jump to the next question. 
