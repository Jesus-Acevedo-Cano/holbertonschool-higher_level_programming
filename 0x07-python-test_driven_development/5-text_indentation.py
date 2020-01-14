#!/usr/bin/python3
""" identate text module """


def text_indentation(text):
    """  
       identate text  lines after each character . ? :
       text: input text to identate
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    cnt = 0

    for ind, var in list(enumerate(text)):
        if var in ".?:":
            txtind = text[cnt: ind + 1].strip()
            print("{}". format(txtind), end="\n\n")
            cnt = ind + 1

    if cnt < len(text):
        txtc = text[cnt:].strip()
        print("{}". format(txtc), end="")
