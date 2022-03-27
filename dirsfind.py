#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Name__ = "dirsFind"
__Description__ = "Find hidden directories."
__Author__ = "Md. Nur Habib"


# Import Modules
from os import system
import sys
try:
    from urllib import response
except ModuleNotFoundError:
    system("pip install urllib3")
try:
    import requests
except ModuleNotFoundError:
    system("pip install requests")
try:
    import argparse
except ModuleNotFoundError:
    system("pip install argparse")
try:
    import re
except ModuleNotFoundError:
    system("pip install re")
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    system("pip install bs4")

from core.banner import BannerFunction
from core.colors import *


def regex(content):
    pattern = "(\"|')(\/[\w\d?\/&=#.!:_-]{1,})(\"|')"
    matches = re.findall(pattern, content)
    response = ""
    i = 0
    for match in matches:
        i = i + 1
        if i == len(matches):
            response = response + match[1]
        else:
            response = response + f"{match[1]}\n"
    return(response)


# Print Banner Here
BannerFunction()


parser = argparse.ArgumentParser(
    description=f'{bold}{blue}Extract hidden GET Parameters From Website.')
parser.add_argument('-u', help='Website uniformResourceLocator.')
parser.add_argument('-o', help='Save output', nargs="?")
parser.add_argument('-s', help='Do not print result.', action="store_true")
parser.add_argument(
    '-d', help=f'Includes domain name in output.{reset}', action="store_true")


argumentsVariable = parser.parse_args()

uniformResourceLocator = f"{argumentsVariable.u}/"
try:
    requestVariable = requests.get(uniformResourceLocator, verify=False)
except requests.exceptions.MissingSchema:
    argumentsVariable.u = f"http://{argumentsVariable.u}"
    uniformResourceLocator = f"{argumentsVariable.u}/"
    requestVariable = requests.get(uniformResourceLocator, verify=False)
soup = BeautifulSoup(requestVariable.text, 'html5lib')
scriptsVariable = soup.find_all('script')

linkofList = [argumentsVariable.u]
directoryArryVariable = []

for script in scriptsVariable:
    try:
        if script['src'][0] == "/" and script['src'][1] != "/":
            script = uniformResourceLocator.split("/")[0:2] + script['src']
            linkofList.append(script)
        else:
            pass
    except:
        pass
for linkFromLinkList in linkofList:
    responseVar = requests.get(linkFromLinkList, verify=False)
    outputVariable = regex(responseVar.text).split("\n")
    for line in outputVariable:
        pathArray = line.strip().split("/")
        path = ""
        for i in range(len(pathArray)):
            if i == len(pathArray) - 1:
                if "." in pathArray[i]:
                    pass
                else:
                    path = f"{path} {pathArray[i]} /"
            else:
                path += f"{pathArray[i]} /"
        if path != "/" and path != "//":
            directoryArryVariable.append(path.replace("//", "/").split("#")[0])
        else:
            pass

for directory in list(set(directoryArryVariable)):
    if argumentsVariable.o:
        output = open(argumentsVariable.o, "a")
        if argumentsVariable.d:
            output.write(argumentsVariable.u.split(
                "/")[0] + "//" + argumentsVariable.u.split("/")[2] + directory + "\n")
        else:
            output.write(f"{directory}\n")
    if argumentsVariable.s:
        pass
    else:
        if argumentsVariable.d:
            print(argumentsVariable.u.split("/")
                  [0] + "//" + argumentsVariable.u.split("/")[2] + directory + reset)
        else:
            print(f"{bold} {blue} {directory} {reset}")