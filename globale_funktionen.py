#
# 
#
#   Globale Variabeln
#
#
#
##########################################################################
#Bottoken
def get_token():
    token = "MTA1MDcyMTgzMzkyNzgzOTc4MA.GCYry1.xbJE-TFzHVj1ziHlGWq1VwGNjBYHzvSAmuLekc"
    return token

#Timeoutchannel-ID
def timeoutchannel():
    timoutchannel_ID = 1050097182969176274
    return timoutchannel_ID


##########################################################################
#Api-Key for requests
def get_api():
    api = "a46716a76c270dcc6f0ad9968d7c2eb9"
    return api

#Website für Titel (Wetterquelle)
def getweathersource(ort):
    source = "https://openweathermap.org/city/" + ort
    return source

#Website google maps
def getgoogleplace(ort):
    source = "https://google.ch/maps/place/" + ort
    return source

#Link für google maps icon
def mapsicon():
    source = "https://cdn-icons-png.flaticon.com/512/2991/2991231.png"
    return source
##########################################################################
#Start-String for weatherbot, pushbot and help
def weatherbotstarter():
    weatherbotstartcommand = "/weather"
    return weatherbotstartcommand

#Start-String or stop-String for Pushnotification
def pushbotstarter():
    pushbotstartercommand = "/setpush"
    return pushbotstartercommand

def help1():
    help = "/help"
    return help

def help2():
    help = "/?"
    return help

##########################################################################
#errormeldung text
def errortext():
    meldung = "Bitte Ort eingeben. Mit \"/help\" oder \"/?\" bekommst du Hilfe."
    return meldung

##########################################################################
#benutzte api
def apisource():
    source = "openweathermap.org api"
    return source