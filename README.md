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

### Installation
- Install or upgrade to [Python 3](https://www.python.org/downloads/).

 Clone this repository, and move into it
- `git clone https://github.com/marcoscz1995/Crowdmarker.git`
- `cd Crowdmarker`

(Optional, but recomended) Create a virtual environment and activate it.
- `python3 -m venv crowdmarker-env`
- source crowdmarker-en/bin/activate 

Install the required packages
- `pip install -r requirements.txt`

### Determine keyboard event number
Run keyboard_event_determiner.py
- `python keyboard_event_determiner.py`
- Click any key on the keyboard you wish to assign keys to.

You should see output like this in your terminal: `/dev/input/event7`. Record the number you see at the end of the output. In this case I would record 7 as my keyboard event number.

### Determine keyboard key codes
Run keycode_determiner.py
- `python keycode_determiner.py`

Click on the keys you would like to assign comments to. For example if you would like to assign the letter A to a comment, click on A and you should see in you terminal something like `KEY_A`. Record this.

Note: you should avoid the already assigned shortcut keys in Crowdmark (l,h,j,k,e,n,p,t,z,c,x,q,s,d), as well as 
the letters F and G as those are already mapped as described earlier (these can however be changed/removed in lines 85-88).

Tip: when selecting keys I suggest choosing those on the left hand side of the keyboard. This way you can select
comments with your left hand and choose where to insert them using your mouse with your right hand. I find this
the most efficient use of this script.  

### Insert user inputs into Crowdmarker
Insert your comments, points, and associated keyboard keys and event to `crowdmarker.py`
- open `crowdmarker.py` in your favourite text editor
- in line 132 change `INSERT_EVENT_NUMBER_HERE` to the number you got from running `keyboard_event_determiner.py`
- in line 133 change `INSERT_QUESTIONS_MAX_SCOREE_HERE` to the questions max score that you will be marking
- in lines 134 insert your comment, points and key code you want to assign to it that you get from running `keycode_determiner.py`. Add as many comments as you have keycodes. Just follow the format of `["comment", point, "key code"]`.

Note: Due to Pythons string formatting this script does not support the use of Latex commands that start with '\f' such as '\frac{}{}'. 

### Start marking
Once you are satisfied with your comments sign into Crowdmark, go to the question you want to mark and run the `crowdmarker.py` file.
- `python crowdmarker.py`
- go to your desired Crowdmark question
- move the cursor to where you would like to insert a comment
- click the associated key for that comment

The comment will then be inserted.

Happy Crowdmarking!

Note: due to how the script works, you should not move the cursor while the comment is being inserted as the comment will not be saved or the points will not be added. Also the comment cannot be posted to close to the margins of the questions as the points can be recorded wrong.

### Turn off the script
When you are done marking or want to turn off the script
- go to the terminal and press `Contrl+C` to end the script

To deactivate the virtual environment just type in your terminal
- deactivate
 
### Contributing
If you would like to improve this script or have an idea to make it better, please post it to the github issues page. If you would like to develop it I will gladly accept pull requests.

Note: if you plan on using [Selenium](https://www.selenium.dev/) to improve the script consider that because [Crowdmark](https://crowdmark.com/) is written with [Ember.js](https://emberjs.com/) which uses dynamically generated attributes, there are many issues that make inserting comments difficult. In particular, when a long comment is inserted the page will jump to the next question. 
