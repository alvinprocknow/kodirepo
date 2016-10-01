# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Guitar Videos Addon by Alvin Procknow
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: Alvin Procknow
# Twitter:  @alvinprocknow
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.guitarvideos'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ANDERTONSMUSIC = "AndertonsMusic"
YOUTUBE_CHANNEL_CHICAGOMUSICEXCHANGE = "chicagomusicexchange"
YOUTUBE_CHANNEL_EYTSCHPI42 = "EytschPi42"
YOUTUBE_CHANNEL_GEMINIGUITAR = "gsogoz"
YOUTUBE_CHANNEL_GUITARWORLD = "guitarworld"
YOUTUBE_CHANNEL_GUITARISTMAGAZINE = "GuitaristMag"
YOUTUBE_CHANNEL_INTHEBLUES = "intheblues"
YOUTUBE_CHANNEL_JOEBONAMASSATV = "JoeBonamassaTV"
YOUTUBE_CHANNEL_JUSTINSANDERCOE = "JustinSandercoe"
YOUTUBE_CHANNEL_PREMIERGUITAR = "premierguitar"
YOUTUBE_CHANNEL_QUISTTV = "QuistTV"
YOUTUBE_CHANNEL_ROBCHAPPERS = "RobChappers"
YOUTUBE_CHANNEL_STEVESTINE = "stinemusiclessons"
YOUTUBE_CHANNEL_THATPEDALSHOW = "UCnUXq8mGmoHt0e6ItuTs10w"

# Entry point
def run():
    plugintools.log("guitarvideos.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("guitarvideos.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Andertons Music Co",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ANDERTONSMUSIC+"/",
        thumbnail='https://yt3.ggpht.com/-TNpuBm24H7A/AAAAAAAAAAI/AAAAAAAAAAA/aMNpnykWdc0/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chicago Music Exchange",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_CHICAGOMUSICEXCHANGE+"/",
        thumbnail='https://yt3.ggpht.com/-SH0cBwtgM5E/AAAAAAAAAAI/AAAAAAAAAAA/XphWDVvqYjI/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="EytschPi42",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_EYTSCHPI42+"/",
        thumbnail='https://yt3.ggpht.com/-uq1efmj7fXY/AAAAAAAAAAI/AAAAAAAAAAA/729g71_Vrbc/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gemini Guitar",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_GEMINIGUITAR+"/",
        thumbnail='https://yt3.ggpht.com/-FiaylSBKS7w/AAAAAAAAAAI/AAAAAAAAAAA/YLWDX0byiMY/s255-c-k-no-mo-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Guitar World",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_GUITARWORLD+"/",
        thumbnail='https://yt3.ggpht.com/-Bh5mMRuom_E/AAAAAAAAAAI/AAAAAAAAAAA/gubKXsmcNcU/s255-c-k-no-mo-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Guitarist Magazine",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_GUITARISTMAGAZINE+"/",
        thumbnail='https://yt3.ggpht.com/-l5s40Km6I-c/AAAAAAAAAAI/AAAAAAAAAAA/dPSL06KDq3Y/s255-c-k-no-mo-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="intheblues",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_INTHEBLUES+"/",
        thumbnail='https://yt3.ggpht.com/-cEOlaZCUnmQ/AAAAAAAAAAI/AAAAAAAAAAA/CC2WyfcF59M/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JoeBonamassaTV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_JOEBONAMASSATV+"/",
        thumbnail='https://yt3.ggpht.com/-NYE-vGs_3yI/AAAAAAAAAAI/AAAAAAAAAAA/fLOoehGAjxA/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JustinGuitar",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_JUSTINSANDERCOE+"/",
        thumbnail='https://yt3.ggpht.com/-5lZN4lWqIJ4/AAAAAAAAAAI/AAAAAAAAAAA/OTjz43hchDk/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Premier Guitar",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_PREMIERGUITAR+"/",
        thumbnail='https://yt3.ggpht.com/-X7u9tGcg3HI/AAAAAAAAAAI/AAAAAAAAAAA/Bao6TQ8ED_k/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="QuistJam",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_QUISTTV+"/",
        thumbnail='https://yt3.ggpht.com/-hp5OjYfzUDI/AAAAAAAAAAI/AAAAAAAAAAA/u5l6ivAO-mI/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rob Chapman",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ROBCHAPPERS+"/",
        thumbnail='https://yt3.ggpht.com/-v_yLFUU8jH8/AAAAAAAAAAI/AAAAAAAAAAA/EjHnr2dkAoo/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Steve Stine",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_STEVESTINE+"/",
        thumbnail='https://yt3.ggpht.com/-mxJ5ghmBNXU/AAAAAAAAAAI/AAAAAAAAAAA/tWwg7QRVtIE/s255-c-k-no-mo-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="That Pedal Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_THATPEDALSHOW+"/",
        thumbnail='https://yt3.ggpht.com/-lPBvYNlm6Xc/AAAAAAAAAAI/AAAAAAAAAAA/5lM37ZYdfp8/s255-c-k-no-mo-rj-c0xffffff/photo.jpg',
        folder=True )

run()
