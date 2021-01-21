# This is simple code snippet to get the data out of the dirivng license as show in use case

import pytesseract
from pytesseract import Output
import cv2
import pandas as pd

poppler_path = '' # path to poppler
pytesseract.pytesseract.tesseract_cmd = '' # path to pytesseract.exe

if __name__ == '__main__':

    image = cv2.imread('Uk_licence.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    rows = []
    custom_config = r'-c preserve_interword_spaces=1 --oem 3 --psm 3 -l eng'
    d = pytesseract.image_to_data(image, config=custom_config, output_type=Output.DICT)
    df = pd.DataFrame(data=d)
    # clean up blanks
    df1 = df[(df.conf != '-1') & (df.text != ' ') & (df.text != '')]
    # sort blocks vertically
    sorted_blocks = df1.groupby('block_num').first(
    ).sort_values('top').index.tolist()
    for block in sorted_blocks:
        curr = df1[df1['block_num'] == block]
        sel = curr[curr.text.str.len() > 3]
        char_w = (sel.width/sel.text.str.len()).mean()
        prev_par, prev_line, prev_left = 0, 0, 0
        text = ''
        for ix, ln in curr.iterrows():
            # add new line when necessary
            if prev_par != ln['par_num']:
                text += '\n'
                prev_par = ln['par_num']
                prev_line = ln['line_num']
                prev_left = 0
            elif prev_line != ln['line_num']:
                text += '\n'
                prev_line = ln['line_num']
                prev_left = 0

            added = 0  # num of spaces that should be added
            if ln['left']/char_w > prev_left + 1:
                added = int((ln['left'])/char_w) - prev_left
                text += ' ' * added
            text += ln['text'] + ' '
            prev_left += len(ln['text']) + added + 1
        text += '\n'
        for row in text.split("\n"):
            rows.append(row)

    # Print the data that we have extracted
    for i in rows:
        print(i)
