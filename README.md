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
- (Optional) [Python venv](https://docs.python.org/3/library/venv.html) is shipped with Python 3 but for some reason some distros separate it out into a separate distro package, such as python3-venv on Ubuntu/Debian.
Sorry Linux users, but you will have to install this if you haven't already.
### Installation
- Install or upgrade to [Python 3](https://www.python.org/downloads/).

 Clone this repository, and move into it
- `git clone https://github.com/marcoscz1995/Crowdmarker.git`
- `cd Crowdmarker`

(Optional, but recomended) Create a virtual environment and activate it.
- `python3 -m venv crowdmarker-env`
- `source crowdmarker-env/bin/activate` 

Install the required packages
- `pip install -r requirements.txt`


### Insert user inputs into Crowdmarker
Insert your comments, points, and associated keyboard keys and event to `crowdmarker.py`
- open `crowdmarker.py` in your favourite text editor
- in line 141 change `INSERT_QUESTIONS_MAX_SCORE_HERE` to the questions max score that you will be marking
- in lines 142 and 143 change the letters 'f' and 'g' to whatever keys you want to map to move to the next unmarked booklet and enter a perfect score, respectively. Or do not change them if you want to keep those default values.
- in lines 144 insert your comment, points and key code you want to assign to it. Add as many comments as you have keycodes. Just follow the format of `["comment", point, 'key code']`. Example: `["show what lemma used here", -1, 'r']`

Note: you should avoid the already assigned shortcut keys in Crowdmark (l,h,j,k,e,n,p,t,z,c,x,q,s,d).

Note: if you want to put latex code that starts with reserved python string formating such as '\f' or '\n', just 
add 'r' before the start of the comment. For example: [r"the correct answer is $$\frac{1}{2}$$", -2, 'a']

Tip: when selecting keys I suggest choosing those on the left hand side of the keyboard. This way you can select
comments with your left hand and choose where to insert them using your mouse with your right hand. I find this
the most efficient use of this script.  

### Start marking
Once you are satisfied with your comments sign into Crowdmark, go to the question you want to mark and run the `crowdmarker.py` file.
- `python crowdmarker.py`
- go to your desired Crowdmark question
- move the cursor to where you would like to insert a comment
- click the associated key for that comment

The comment will then be inserted.

Happy Crowdmarking!

Note: due to how the script works, you should not move the cursor while the comment is being inserted as the comment will not be saved or the points will not be added. Also the comment cannot be posted too close to the margins of the questions as the points can be recorded wrong.

### Turn off the script
When you are done marking or want to turn off the script
- Press the `Esc` key to end the scrip key to end the scriptt

To deactivate the virtual environment just type in your terminal
- deactivate
 
### Contributing
If you would like to improve this script or have an idea to make it better, please post it to the github issues page. If you would like to develop it I will gladly accept pull requests.

Note: if you plan on using [Selenium](https://www.selenium.dev/) to improve the script consider that because [Crowdmark](https://crowdmark.com/) is written with [Ember.js](https://emberjs.com/) which uses dynamically generated attributes, there are many issues that make inserting comments difficult. In particular, when a long comment is inserted the page will jump to the next question. 
