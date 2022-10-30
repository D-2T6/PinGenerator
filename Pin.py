#!/usr/bin/evn python
import os, string, secrets
os.system('clear')
numbers = string.digits

pin = ''.join(secrets.choice(numbers) for i in range(6))

#ASCII
import sys, time

def ascii(txt) :
        for i in txt :
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.003)
ascii('''\r\x1b[0;31m
                       .:::!~!!!!!:.
                    .xUHWH!! !!?M88WHX:.
                  .X*#M@&!!  !X!M&&&&&&WWx:.
                 :!!!!!!?H! :!&!&&&&&&&&&&8X:
                !!~  ~:~!! :~!&!#&&&&&&&&&&8X:
               :!~::!H!<   ~.U&X!?R&&&&&&&&MM!
               ~!~!!!!~~ .:XW&&&U!!?&&&&&&RMM!
                 !:~~~ .:!MST#&&&&WX??#MRRMMM!
                 ~?WuxiW*‛   ‛√#&&&&8!!!!??!!!
               :X- M&&&&       ‛rT#&T~!8&WUXU~
              :%‛  ~#&&&m:    \x1b[1;35m✪\x1b[0;31m   ~!~ ?&&&&&&
            :!‛.-   ~T&&&&8xx.  .xWW- ~x&&&&&
 .......   -~~:<‛ !    ~?T#&&@@W@*?&&   \x1b[1;35m✪\x1b[0;31m  /‛
\x1b[1;30m𝐆\x1b[0;31m |W&@@M!!! .!~~ !!     .:XUW&W!~ ‛&-:    :
\x1b[1;30m𝐇\x1b[0;31m |#&~~‛.:x%‛!!  !H:   !WM&&&&Ti.: .!WUn+!‛
\x1b[1;30m𝐎\x1b[0;31m |:::~:!!‛:X~ .: ?H.!u °&&&B&&&!W:U!T&&M~
\x1b[1;30m𝐒\x1b[0;31m |.~~   :X@!.-~   ?@WTWo(‛*&&&W&TH&! ‛
\x1b[1;30m𝐓\x1b[0;31m |Wi.-!X\$?!-~    / ?&&&B&Wu(‛**&RM!
 .......         /   ~&&&&&B&&en:‛‛
            \x1b[0;31m         ~‛##*&&&&M~\x1b[0;37m
         =[    \x1b[0;31m ━━──────\x1b[0;31m𝙲 𝚈 𝙱 𝙴 𝚁\x1b[0;31m──────━━\x1b[0;37m
+  --  --=[\x1b[0;37m━━──────\x1b[0;31m𝐈 𝐍 𝐃 𝐎 𝐍 \x1b[0;37m𝐄 𝐒 𝐈 𝐀 𝐍\x1b[0;31m──────━━\x1b[0m
''')

#\x1b[1;37m[\x1b[1;32m•\x1b[1;37m] \x1b[1;31mR \x1b[1;37mI
running_text = "\x1b[0;37mPress Enter to Continue\r\x1b[0;31mPress Enter to Continue\r                       \r"
for i in running_text :
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.050)

def text(e) :
        for i in e :
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.1)
text("\x1b[0;37myour pin generated is:\x1b[0;31m "), pin
for i in pin + ' ' :
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
input()
