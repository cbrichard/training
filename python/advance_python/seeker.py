#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import argparse

def main():
    """Main Func"""
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help='specify word to search for')
    parser.add_argument('filename', help='specify file to search')
    args = parser.parse_args()

    searchFile = open(args.filename)
    lineNum = 0

    for line in searchFile.readlines():
        line = line.strip('\n\r')
        lineNum += 1
        searchResult = re.search(args.word, line, re.M|re.I)
        if searchResult:
            print(str(lineNum)+': '+line)

if __name__ == '__main__':
    main()
