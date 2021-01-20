#!/usr/bin/env python3
import sys
import os
from pathlib import Path
import PySimpleGUI as sg
import emoji
import io

#hashtags
academics = ['#NMSA', '#NMSchoolfortheArts', '#Academics', '#publicschool', '#Dance', '#Music', '#Theatre', '#VisualArts', '#CreativeWriting']
general = ['#NMSA', '#NMSchoolfortheArts', '#publicschool', '#statewide', '#artist', '#youngartist', '#creative', '#youngcreative', '#highschool', '#artschool', '#Dance', '#Music', '#Theatre', '#VisualArts', '#CreativeWriting']
admissions = ['#NMSA', '#NMSchoolfortheArts', '#applynow', '#publicschool', '#statewide', '#outreach', '#residential', '#tuitionfree', '#artist', '#youngartist', '#creative', '#youngcreative', '#highschool', '#artschool']
music = ['#NMSA', '#NMSchoolfortheArts', '#Music', '#publicschool', '#statewide', '#artist', '#youngartist', '#creative', '#youngcreative', '#highschool', '#artschool']
theatre = ['#NMSA', '#NMSchoolfortheArts', '#Theatre','#publicschool', '#statewide', '#artist', '#youngartist', '#creative', '#acting', '#youngcreative', '#highschool', '#artschool']
va = ['#NMSA', '#NMSchoolfortheArts', '#VisualArts','#publicschool', '#statewide', '#artist', '#youngartist', '#creative', '#youngcreative', '#highschool', '#artschool']
cw = ['#NMSA', '#NMSchoolfortheArts', '#CreativeWriting','#publicschool', '#statewide', '#artist', '#youngartist', '#creative', '#youngcreative', '#highschool', '#artschool']
dance = ['#NMSA', '#NMSchoolfortheArts', '#Dance','#publicschool', '#statewide', '#artist', '#youngartist', '#creative', '#youngcreative', '#highschool', '#artschool']

converter ={
'general': general,
'': general,
' ': general,
'admissions': admissions,
'academics': academics,
'music': music,
'theatre': theatre,
'visual arts': va,
'va': va,
'creative writing': cw,
'cw': cw,
'dance': dance,
'g': general,
'a': admissions,
'ad': admissions,
'ac': academics,
'm': music,
't': theatre,
'v': va,
'c': cw,
'd': dance
}


# Emojis
emoji_chain_link = emoji.emojize(':link:')
emoji_finger_down = emoji.emojize(':point_down:', use_aliases=True)
emoji_tickets = emoji.emojize(':ticket:')


#spits out tags from list by name
def tagerator(category = general, numtags = 100):
    x = 0
    # if type(category) == None:
    #     category = general
    tags = []
    for tag in category:
        tags.append(category[x])
        x += 1
        if x >= numtags:
            break
    print(' '.join(tags), file=open(file, "a", encoding="utf-8"))


# Very basic window.  Return values as a dictionary

layout = [
            [sg.Text('Please enter the following information.')],
            [sg.Text('What is the category of the post?' , size=(40, 1)), sg.InputText(default_text='cw, dance, music, theatre, va academics, or admissions - Or leave blank for a general post', key='_CAT_')],
            [sg.Text("Is it ticketed?", size=(40, 1)), sg.InputText(key='_TICKET_')],
            [sg.Text('Link? Y/N If just the standard events link, type "Y".', size=(40, 1)), sg.InputText(key='_LINK_')],
            [sg.Multiline(size = (90, 5), key='_POST_')],
            [sg.Submit(), sg.Cancel()]
        ]

window = sg.Window('Simple data entry GUI', layout)

event, values = window.Read()

window.Close()

category, tickets, link, post = [values['_CAT_'], values['_TICKET_'], values['_LINK_'], values['_POST_']]

#Get post content
#category?

# print('''What the category of the post?

# cw, dance, music, theatre, va academics, or admissions

# - Or leave blank for a general post -

# Use the name or the first letter.
# ''')

#get category
category = str(category)
category = category.lower() if category != 'cw, dance, music, theatre, va academics, or admissions - Or leave blank for a general post' else 'general'
tags = converter.get(category)

#ticketed?
tickets = str(tickets)
tickets = tickets.lower()
ticketed = True if tickets == 'y' else False

# #link?
# if tickets == 'y' and link == None or 'y':
#     if category[0] == 't':
#         link = f'nmschoolforthearts.org/theatre-tickets/'
#     elif category[0] == 'm':
#         link = f'nmschoolforthearts.org/music-tickets/'
#     elif category[0] == 'd':
#         link = f'nmschoolforthearts.org/dance-tickets/'
#     elif category[0] == 'c':
#         link = f'nmschoolforthearts.org/cw-tickets/'
#     else:
#         link = f'nmschoolforthearts.org/tickets/'
# else:
#     # link = input('\nAny link? If just the standard events link, type "Y", else type the link. (If No "N" or Leave Blank) \n> ')
#     link = link.lower()
#post text
# post = input('\nPlease enter the text for your post:\n\n')




#make file?
# makefile = input('\nWould you like to save a file as well? y/N \n> ')
# makefile = makefile.lower()
# Always make file
createfile = True #if makefile == 'y' else False
path = Path(os.getcwd())

#Output File
try:
    if createfile == True:
        if not os.path.isdir(Path('./Social Media Posts')):
            os.mkdir(Path('./Social Media Posts'))
    #save output to file
    # with open(f'.\\Social Media Posts\\{filename}.txt', 'w') as f:
    #     file = f
except OSError:
    print('File could not be saved. Directory does not exist and could not be created')


print('\nEnter the file name:')
filename = input(' > ')
file = Path(f'./Social Media Posts/{filename}.txt')

#Print Posts
#Facebook
print('\n\nFACEBOOK', file=open(file, "a", encoding="utf-8"))
print(f'\n{post}', file=open(file, "a", encoding="utf-8"))
tagerator(tags,3)
if ticketed:
    print(f'{link}\n{emoji_finger_down}Click Here to buy {emoji_tickets}tickets{emoji_tickets}!{emoji_finger_down}', file=open(file, "a", encoding="utf-8"))
elif link == 'y':
    print(f'\nhttps://www.facebook.com/pg/nmschoolforthearts/events\n{emoji_finger_down}Click Here for more info!{emoji_finger_down}', file=open(file, "a", encoding="utf-8"))
elif link != 'y' and category == admissions:
    print(f'{link}\n{emoji_finger_down}Click the link to apply now!{emoji_finger_down}', file=open(file, "a", encoding="utf-8"))
elif link == 'n':
    None
else:
    print(f'{link}\n{emoji_finger_down}Click Here for more info!{emoji_finger_down}', file=open(file, "a", encoding="utf-8"))

#Instagram
print('\n\nINSTAGRAM', file=open(file, "a", encoding="utf-8"))
if ticketed:
    print(f'\n{post}.\n.\nClick the {emoji_chain_link}link{emoji_chain_link} in the bio to buy {emoji_tickets}tickets{emoji_tickets}!\n.\n.\n.', file=open(file, "a", encoding="utf-8"))
elif link == 'n':
    print(f'\n{post}.\n.\n.', file=open(file, "a", encoding="utf-8"))
elif link != 'y' and category == admissions:
    print(f'\n{post}.\n.\nClick the {emoji_chain_link}link{emoji_chain_link} in the bio to apply now!\n.\n.\n.', file=open(file, "a", encoding="utf-8"))
else:
    print(f'\n{post}.\n.\nClick the {emoji_chain_link}link{emoji_chain_link} in the bio for more info!\n.\n.\n.', file=open(file, "a", encoding="utf-8"))
tagerator(tags)

#Twitter
print('\n\nTWITTER', file=open(file, "a", encoding="utf-8"))
print(f'\n{post}', file=open(file, "a", encoding="utf-8"))
tagerator(tags,3)
if ticketed:
    print(f'\n{emoji_finger_down}Click Here to buy {emoji_tickets}tickets{emoji_tickets}!{emoji_finger_down}\n{link}\n', file=open(file, "a", encoding="utf-8"))
elif link == 'y':
    print(f'\n{emoji_finger_down}Click Here!{emoji_finger_down}\nhttps://www.facebook.com/pg/nmschoolforthearts/events\n', file=open(file, "a", encoding="utf-8"))
elif link != 'y' and category == admissions:
    print(f'{emoji_finger_down}Click the link to apply now!{emoji_finger_down}\n{link}', file=open(file, "a", encoding="utf-8"))
elif link == 'n':
    None
else:
    print(f'\n{emoji_finger_down}Click Here!{emoji_finger_down}\n{link}\n', file=open(file, "a", encoding="utf-8"))

input(f'\n\n{filename} was saved to {path}\\Social Media Posts\\{filename}.txt.\n\nPress any key to exit.')
