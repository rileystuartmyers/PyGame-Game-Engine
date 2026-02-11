from entityClass import *
from gameClass import *
from mapClass import *
from dialogueClass import *
from mainMenuClass import *

gameContents = game(name = "gameContents", 
            caption = "Frogburg", 
            size = WINDOWSIZE, 
            FPS = 60, 
            background = r"icons/tempBack.png",
            iconPath = r"icons/frog_art/icon.png")

gameContents.createMap(name = "2fort", 
               size = WINDOWSIZE, 
               musicPath = r"sound/mainmenu_sound/wav.wav",
               block_size = (10, 10), 
               background = r"icons/sball.png",
               portals = [portal("port",
                                 "default_map", 
                                 "icons/default_map.png", 
                                 (WINDOWx * 2/3, WINDOWy * 8/9)), 
                          portal("port", 
                                 "beach", 
                                 DEFAULT_PORTAL_IMG, 
                                 (WINDOWx * 1/3, WINDOWy * 8/9))])
                                 
gameContents.maps["2fort"].setBackground(r"icons/2fort.png")

gameContents.createPortal("2fort_portal", 
                  "2fort", 
                  "icons/2fort.png", 
                  (WINDOWx * 2/3, WINDOWy / 3/5))



p0 = entity("Frog", 
            r"icons/frog_art",
            (WINDOWx / 4, WINDOWy / 4), 
            False, 
            "player", 
            (110, 110))

p1 = entity("Frog2", 
            r"icons/frog_art",
            (WINDOWx / 2, WINDOWy / 2), 
            False, 
            "player", 
            (110, 110))

p2 = entity("Frog2", 
            r"icons/frog_art",
            (WINDOWx / 2, WINDOWy / 2), 
            False, 
            "player", 
            (110, 110))


gameContents.addPlayer(p0)
gameContents.addEntity(p1)
gameContents.addEntityWithMap(entity = p2, 
                      map = "2fort")
                      
gameContents.addEntity(entity("Frog2", 
                      r"icons/frog_art",
                      (WINDOWx * 1/3, WINDOWy * 1/2), 
                      False, 
                      "player", 
                      (110, 110)))

gameContents.createProjectile(spawnCoords = (100, 100))

p1.addDialogue(
    
    dialogueBox(
    iconPath = r"icons/frog_art/icon.png",
    header = "Frog", 
    body = ["Hello, I'm Frog.",
            "Blah",
            "Blahb",
            "Ribidi Toilet..."])

)

p1.addDialogue(

    dialogueBox(
        iconPath = r"icons/frog_art/icon.png", 
        header = "Frog", 
        body = ["BLAH BLAH BLAH",
                "Bye now!"])

)

p1.addDialogue(

    dialogueBox(
        iconPath = r"icons/frog_art/icon.png", 
        header = "Frog", 
        body = ["BLAH BLAH BLAH",
                "Bye now!"])


)

gameContents.currentMusic.play(loops = -1)