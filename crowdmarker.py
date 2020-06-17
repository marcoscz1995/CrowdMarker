from math import floor
import threading

from pynput import keyboard
from pynput.keyboard import Key, KeyCode
import pyautogui as pyg
from PIL import ImageFont

font = ImageFont.truetype('arial.ttf', 14)


class CrowdMarker(threading.Thread):
    def __init__(self, comments, max_score, next_booklet_key, perfect_score_key):
        super(CrowdMarker, self).__init__()
        self.comments = comments
        self.max_score = max_score
        self.next_booklet_key = next_booklet_key
        self.perfect_score_key = perfect_score_key

    def enter_comment_mode_get_click_position(self):
        # enter comment mode, left click to add comment, get click position
        pyg.press('V')
        pyg.click()
        (current_x, current_y) = pyg.position()
        return (current_x, current_y)

    def add_comment(self, comment, current_x, current_y):
        # note:long comments will change the verticle position of btns below it
        # comments is a list of size 4
        # we get only comment_content. index on a list is O(1).
        # time complx of  this function: O(1)
        comment_content = comment[0]
        x_move_comment = 12
        y_move_comment = 15
        (updated_x, update_y) = (current_x +
                                 x_move_comment, current_y +
                                 y_move_comment)
        pyg.click(updated_x, update_y)
        pyg.write(comment_content)

    def add_points(self, comment, current_x, current_y):
        # note:long comments will change the verticle position of btns below it
        # comments is a list of size 4
        # we get only comment_content. index on a list is O(1).
        # time complx of  this function: O(2*1) = O(1)
        points = comment[1]
        x_move_points = comment[2]
        y_move_points = comment[4]
        (updated_x, update_y) = (current_x +
                                 x_move_points, current_y +
                                 y_move_points)
        pyg.click(updated_x, update_y)
        pyg.write(str(points))

    def save_comment(self, comment, current_x, current_y):
        x_move_save = comment[3]
        y_move_save = comment[4]
        (updated_x, update_y) = (current_x +
                                 x_move_save, current_y +
                                 y_move_save)
        pyg.click(updated_x, update_y)

    def enter_score(self):
        pyg.press('enter')

    def enter_score_move_to_next_booklet(self):
        pyg.press('enter', presses=2)

    def enter_perfect_score(self):
        max_score = str(self.max_score)
        pyg.press(max_score)
        self.enter_score_move_to_next_booklet()

    def add_comment_points(self, comment):
        (current_x, current_y) = self.enter_comment_mode_get_click_position()
        self.add_comment(comment, current_x, current_y)
        self.add_points(comment, current_x, current_y)
        self.save_comment(comment, current_x, current_y)

    def on_release(self, key):
        if key == KeyCode.from_char(self.next_booklet_key):
            self.enter_score_move_to_next_booklet()
        elif key == KeyCode.from_char(self.perfect_score_key):
            self.enter_perfect_score()
        elif key == Key.esc:
            return False
        else:
            if key in self.comments:
                comment_pnts = self.comments.get(key)
                self.add_comment_points(comment_pnts)
            else:
                pass

    def run(self):
        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.join()


class Comment:
    y_txt_area_pxls = 252
    pxls_b4_frst_ovrflow = 803
    y_default_change = 108
    x_move_point = 255
    x_move_save = 26
    y_move_overflow = 20

    def __init__(self, comments):
        self.comments = {
            KeyCode.from_char(comment[2]):
            [comment[0], comment[1],
             self.x_move_point, self.x_move_save,
             self.set_y_move(comment[0])]
            for comment in comments}

    def set_y_move(self, comment):
        cmnt_pxl_y = font.getsize(comment)[0]
        if cmnt_pxl_y > self.pxls_b4_frst_ovrflow:
            pxls_aftr_frst_ovrflw = cmnt_pxl_y - self.pxls_b4_frst_ovrflow
            y_ovrflw_cnt = floor(pxls_aftr_frst_ovrflw / self.y_txt_area_pxls)
            y_pxls_to_add = y_ovrflw_cnt * self.y_move_overflow
            y_ovrflow_change = self.y_default_change + y_pxls_to_add
            return y_ovrflow_change
        return self.y_default_change


if __name__ == "__main__":
    '''
    Replace the info in user_input for the comment and points you want,
    and whichever keyboard key you want to associate it with.

    Change MAX_SCORE to the max score of the question you are marking.

    Change NEXT_BOOKLET to whichever key you want to move to next umarked,
    booklet, or leave as 'f' the default.

    Change PERFECT_SCORE to whichever key you want to insert a perfect score,
    or leave as 'g' the default.

    Happy Crowdmarking!
    '''
    MAX_SCORE = INSERT_QUESTIONS_MAX_SCORE_HERE
    NEXT_BOOKLET = 'f'
    PERFECT_SCORE = 'g'
    user_input = [["comment1", 3, 'a'],
                  ["comment2", -1, 'r'],
                  ["comment3", 2, 'y']]

    comments = Comment(user_input)
    ta = CrowdMarker(comments.comments, MAX_SCORE, NEXT_BOOKLET, PERFECT_SCORE)
    ta.start()
