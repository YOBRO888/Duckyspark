# !/usr/bin/python3
# -*- coding: utf-8 -*-

# version 0.33
# Authors:
# Alexander Yakovlev <a.yakovlev911@gmail.com> https://github.com/toxydose
# https://awake.pro/
# Vlad Khomenko https://github.com/eclipse7

from __future__ import print_function
import sys


# help
HELP = '''
========== Duckyspark {v.0.33} ==============================
https://github.com/toxydose/Duckyspark/
Translator from USB-Rubber-Ducky payloads (Ducky script) to a Digispark code.
=============================================================
Authors:
Alex Bridges <a.yakovlev911@gmail.com> https://github.com/toxydose
Vlad Khomenko https://github.com/eclipse7
https://awake.pro/ community

Options:
  -h, --help            Show basic help message and exit

Usage:

    python3 Duckyspark_translator.py [payload.txt] [output_file] - 
     specify payload file and output file

    python Duckyspark_translator.py [payload.txt]  - 
     translated payload will be saved in "digipayload.ino"

---------------------------------------------------------------
Ducky payloads you can find here:
https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Payloads

Or, you can simply write your own payloads using Ducky script:
https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript
----------------------------------------------------------------
'''


# order is important
SPECIAL_BUTTONS = {'CONTROL_RIGHT': 'MOD_CONTROL_RIGHT',
                   'CONTROL_LEFT':  'MOD_CONTROL_LEFT',
                   'CONTROL':       'MOD_CONTROL_LEFT',

                   'CTRL_RIGHT':    'MOD_CONTROL_RIGHT',
                   'CTRL_LEFT':     'MOD_CONTROL_LEFT',
                   'CTRL':          'MOD_CONTROL_LEFT',

                   'SHIFT_RIGHT':   'MOD_SHIFT_RIGHT',
                   'SHIFT_LEFT':    'MOD_SHIFT_LEFT',
                   'SHIFT':         'MOD_SHIFT_LEFT',

                   'ALT_RIGHT':     'MOD_ALT_RIGHT',
                   'ALT_LEFT':      'MOD_ALT_LEFT',
                   'ALT':           'MOD_ALT_LEFT',

                   'GUI_RIGHT':     'MOD_GUI_RIGHT',
                   'GUI_LEFT':      'MOD_GUI_LEFT',
                   'GUI':           'MOD_GUI_LEFT',
                   'WINDOWS':       'MOD_GUI_LEFT'}

# menu = Shift + F10
BUTTONS = {'a': 'KEY_A',
           'b': 'KEY_B',
           'c': 'KEY_С',
           'd': 'KEY_D',
           'e': 'KEY_E',
           'f': 'KEY_F',
           'g': 'KEY_G',
           'h': 'KEY_H',
           'i': 'KEY_I',
           'j': 'KEY_J',
           'k': 'KEY_K',
           'l': 'KEY_L',
           'm': 'KEY_M',
           'n': 'KEY_N',
           'o': 'KEY_O',
           'p': 'KEY_P',
           'q': 'KEY_Q',
           'r': 'KEY_R',
           's': 'KEY_S',
           't': 'KEY_T',
           'u': 'KEY_U',
           'v': 'KEY_V',
           'w': 'KEY_W',
           'x': 'KEY_X',
           'y': 'KEY_Y',
           'z': 'KEY_Z',

           'F1': 'KEY_F1',
           'F2': 'KEY_F2',
           'F3': 'KEY_F3',
           'F4': 'KEY_F4',
           'F5': 'KEY_F5',
           'F6': 'KEY_F6',
           'F7': 'KEY_F7',
           'F8': 'KEY_F8',
           'F9': 'KEY_F9',
           'F10': 'KEY_F10',
           'F11': 'KEY_F11',
           'F12': 'KEY_F12',

           'LEFTARROW':     'KEY_ARROW_LEFT',
           'RIGHTARROW':    'KEY_ARROW_RIGHT',
           'UPARROW':       'KEY_ARROW_UP',
           'DOWNARROW':     'KEY_ARROW_DOWN',
           'LEFT':          'KEY_ARROW_LEFT',
           'RIGH':          'KEY_ARROW_RIGHT',
           'UP':            'KEY_ARROW_UP',
           'DOWN':          'KEY_ARROW_DOWN',

           'DELETE':        'KEY_DELETE',
           'DEL':           'KEY_DELETE',
           'PRINTSCREEN':   'KEY_PRT_SCR',
           'TAB':           'KEY_TAB',
           'ESCAPE':        'KEY_ESC',
           'SPACE':         'KEY_SPACE',
           'ENTER':         'KEY_ENTER'}

# arguments
payload_input = ''
payload_len = 0

if len(sys.argv) == 2:
    try:
        payload_input = open(sys.argv[1], "r")
        sys.stdout = open("digipayload.ino", "w")
        payload_len = len(open(sys.argv[1], "r").readlines())
    except IOError:
        print('\nError! File "' + sys.argv[1] + '" does not exist!\n')
        exit()
elif len(sys.argv) == 3:
    try:
        payload_input = open(sys.argv[1], "r")
        sys.stdout = open(sys.argv[2] + '.ino', 'w')
        payload_len = len(open(sys.argv[1], "r").readlines())
    except IOError:
        print('\nError!, File "' + sys.argv[1] + '" does not exist!\n')
        exit()
elif len(sys.argv) > 3:
    print('Too much Arguments')
    exit()
else:
    try:
        payload_input = open('payload.txt', "r")
        sys.stdout = open("digipayload.ino", "w")
        payload_len = len(open('payload.txt', "r").readlines())
    except FileNotFoundError:
        print (HELP)
        exit()

# Digispark program fragment
print('//generated by Duckyspark https://github.com/toxydose/Duckyspark\n')
print('#include "DigiKeyboard.h"')
print('#define KEY_ESC     41')
print('#define KEY_BACKSPACE 42')
print('#define KEY_TAB     43')
print('#define KEY_PRT_SCR 70')
print('#define KEY_DELETE  76')
print('#define KEY_ARROW_RIGHT 0x4F')
print('#define KEY_ARROW_DOWN  0x51')
print('#define KEY_ARROW_UP    0x52\n')

print('void setup() {\n')
print('DigiKeyboard.delay(5000);')  # this delay was implemented caused by windows delay before Digispark starts to work
print('DigiKeyboard.sendKeyStroke(0);')
# ---------------------------------------

for i in range(payload_len):
    line = payload_input.readline().replace('\n', '')

    if len(line) < 1:
        print('', end='')

    else:

        if 'REM' in line:
            print('//', line.replace('REM ', ''))

        else:
            if 'DELAY' in line:
                print('DigiKeyboard.', end='')
                print(line.replace('DELAY', 'delay(').replace(' ', ''), end='')
                print(');')

            elif 'STRING' in line:
                print('DigiKeyboard.', end='')
                print(line.replace('"', '")); DigiKeyboard.print(char(34)); DigiKeyboard.print(F("')
                      .replace('\\', '")); DigiKeyboard.print(char(92)); DigiKeyboard.print(F("')
                      .replace('STRING ', 'print(F("'), end='')
                print('")', end='')
                print(');')

            elif 'MENU' in line:
                line = 'KEY_F10'
                mod = 'MOD_SHIFT_LEFT'
                print('DigiKeyboard.', end='')
                print('sendKeyStroke(', end='')
                print(str(line), end='')
                print(',' + mod, end='')
                print(');')

            else:
                mod = ''
                for key in SPECIAL_BUTTONS.keys():
                    if key in line:  # order in keys is important
                        line = line.replace(key, '')
                        mod += SPECIAL_BUTTONS.get(key) + ' | '
                mod += '0'

                line = line.replace(' ', '')
                if line in BUTTONS.keys():
                    line = BUTTONS.get(line)
                else:
                    line = '0'

                print('DigiKeyboard.', end='')
                print('sendKeyStroke(', end='')
                print(str(line), end='')
                print(',' + mod, end='')
                print(');')

        if len(line) < 1:
            print('', end='')

# Digispark program fragment
print('\n}')
print('\n')
print('void loop() {\n')
print('}\n')
# -----------------------------------

payload_input.close()
