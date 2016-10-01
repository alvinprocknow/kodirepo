# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Metal Videos Addon by Alvin Procknow
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

addonID = 'plugin.video.metalvideos'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ACDC = "acdcVEVO"
YOUTUBE_CHANNEL_ANTHRAX = "AnthraxNFYT"
YOUTUBE_CHANNEL_BLACKSABBATH = "OfficialSabbath"
YOUTUBE_CHANNEL_METALLICA = "MetallicaTV"

# Entry point
def run():
    plugintools.log("metalvideos.run")
    
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
    plugintools.log("metalvideos.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="AC/DC",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ACDC+"/",
        thumbnail='https://yt3.ggpht.com/-eEW7OmuC_B4/AAAAAAAAAAI/AAAAAAAAAAA/4Y6xL6tKlcM/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Anthrax",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ANTHRAX+"/",
        thumbnail='https://yt3.ggpht.com/-rAIP0G9Erfs/AAAAAAAAAAI/AAAAAAAAAAA/wusBCHa9ACM/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Black Sabbath",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_BLACKSABBATH+"/",
        thumbnail='https://yt3.ggpht.com/-l0v4nW0hN04/AAAAAAAAAAI/AAAAAAAAAAA/0sB1Ct7YwVU/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Metallica",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_METALLICA+"/",
        thumbnail='https://yt3.ggpht.com/-KfpwETSc-OE/AAAAAAAAAAI/AAAAAAAAAAA/d9daqOEKOrk/s255-c-k-no-rj-c0xffffff/photo.jpg',
        folder=True )

run()
