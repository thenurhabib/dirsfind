#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__Name__ = "dirsFind"
__Description__ = "Find hidden directories."
__Author__ = "Md. Nur Habib"

try :
    from core.colors import *
except ModuleNotFoundError :
    from colors import *

def BannerFunction():
    print(f"""{bold}{yellow}
     _____  _          ______ _           _ 
    |  __ \(_)        |  ____(_)         | |
    | |  | |_ _ __ ___| |__   _ _ __   __| |
    | |  | | | '__/ __|  __| | | '_ \ / _` |
    | |__| | | |  \__ \ |    | | | | | (_| |
    |_____/|_|_|  |___/_|    |_|_| |_|\__,_|
    {red}
                                @thenurhabib {reset}
""")