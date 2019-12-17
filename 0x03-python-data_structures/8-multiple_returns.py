#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(0, len(sentence) + 1):
        if i == len(sentence):
            break
    return (i, sentence[0])
