#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def main():
    """Main Function"""
    line = "I think I understand regular expressions"

    matchResult = re.match('think', line, re.M|re.I)
    if matchResult:
        print("Match Found: "+matchResult.group())
    else:
        print("No Match was Found")

    searchResult = re.search('think', line, re.M|re.I)
    if searchResult:
        print("Search Found: "+searchResult.group())
    else:
        print("Nothing Found in Search")

if __name__ == '__main__':
    main()
