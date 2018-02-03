#-*-coding: utf-8 -*-
import random
red = '\033[31m' # Red
white = '\033[1;37m' # White
green = '\033[32m' # Green
orange = '\033[0;33m' # Orange
header1 = """
\033[1;37m

      ..      .        _            .          .. 
   x88f` `..x88. .>   u            @88>  x .d88"  
 :8888   xf`*8888%   88Nu.   u.    %8P    5888R   
:8888f .888  `"`    '88888.o888c    .     '888R   
88888' X8888. >"8x   ^8888  8888  .@88u    888R   
88888  ?88888< 888>   8888  8888 ''888E`   888R   
88888   "88888 "8%    8888  8888   888E    888R   
88888 '  `8888>       8888  8888   888E    888R   
`8888> %  X88!       .8888b.888P   888E    888R   
 `888X  `~""`   :     ^Y8888*""    888&   .888B . 
   "88k.      .~        `Y"        R888"  ^*888%  
     `""*==~~`                      ""      "%    
                  CREATE FRAMEWORK
 """
                  
header2 = """ 
\033[1;37m                 
 _______________________
< Evil Create Framework >
 -----------------------
       \   ,__,
        \  (oo)____
           (__)    )\ 
              ||--|| *
 """
header3 = """
\033[1;37m
oooooooooooo              o8o  oooo  
`888'     `8              `""  `888  
 888         oooo    ooo oooo   888  
 888oooo8     `88.  .8'  `888   888  
 888    "      `88..8'    888   888  
 888       o    `888'     888   888  
o888ooooood8     `8'     o888o o888o  Creators.
"""

header4 = """
\033[1;36m

__________      ___________
___  ____/__   ____(_)__  /
__  __/  __ | / /_  /__  / 
_  /___  __ |/ /_  / _  /  -Creators
/_____/  _____/ /_/  /_/
"""   
header5 = """
\033[31m

██╗   ██╗ ██████╗██████╗ ████████╗
██║   ██║██╔════╝██╔══██╗╚══██╔══╝
██║   ██║██║     ██████╔╝   ██║   
╚██╗ ██╔╝██║     ██╔══██╗   ██║   
 ╚████╔╝ ╚██████╗██║  ██║   ██║   
  ╚═══╝   ╚═════╝╚═╝  ╚═╝   ╚═╝   
"""
header6 = """
\033[31m

 .S    S.    .S   .S_sSSs     .S       S.     sSSs  
.SS    SS.  .SS  .SS~YS%%b   .SS       SS.   d%%SP  
S%S    S%S  S%S  S%S   `S%b  S%S       S%S  d%S'    
S%S    S%S  S%S  S%S    S%S  S%S       S%S  S%|     
S&S    S%S  S&S  S%S    d*S  S&S       S&S  S&S     
S&S    S&S  S&S  S&S   .S*S  S&S       S&S  Y&Ss    
S&S    S&S  S&S  S&S_sdSSS   S&S       S&S  `S&&S   
S&S    S&S  S&S  S&S~YSY%b   S&S       S&S    `S*S  
S*b    S*S  S*S  S*S   `S%b  S*b       d*S     l*S  
S*S.   S*S  S*S  S*S    S%S  S*S.     .S*S    .S*P  
 SSSbs_S*S  S*S  S*S    S&S   SSSbs_sdSSS   sSS*S   
  YSSP~SSS  S*S  S*S    SSS    YSSP~YSSY    YSS'    
            SP   SP      \033[1;37m           Creators\033[31m
            Y    Y  
\033[1;37m
"""
def xe_header():
    headers = [header1, header2, header3, header4, header5, header6]
    return random.choice(headers)