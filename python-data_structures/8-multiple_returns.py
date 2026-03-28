#!/usr/bin/python3
def multiple_returns(sentence):
    first_chrc = sentence[0] if len(sentence) != 0 else None
    return len(sentence), first_chrc
