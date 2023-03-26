# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Ina", color="#CCFFCC", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define m = Character("Mei", color="#FFCCE5", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define r = Character("Rika", color="#CCE5FF", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define a = Character("Abe", color="#FFFFCC", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define k = Character("Karin", color="#FFCCFF", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ]) #098fc1 (previous shadow color)#086f95
define l = Character("Leopold", color="#CCFFE5", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define u = Character("Naomi", color="#CCCCFF", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define s = Character("Marisa", color="#E5CCFF", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define b = Character("Bernard", color="#CCFFFF", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define p = Character("Peter", color="#FFCCCC", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
define g = Character("Hannah", color="#FFCCFF", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])
#define a = Character("Alice", color="#ffc0cb", who_outlines=[ (0, "#075c7c", 2, 2) ], what_outlines=[ (0, "#075c7c", 2, 2) ])

define narrator = Character(None, what_outlines=[ (0, "#075c7c", 2, 2) ])  #098fc1

#old #FAE282 yellow c0ffd5 blue ffc0cb pink ffd5c0 ffff00 green 99DDCF FAD1FF FAD1FF FFE5CC C7CEFF FFC785

#new #FFCCCC red! #FFFFCC yellow! #CCFFCC green! #CCCCFF purple #E5CCFF violet! #FFCCFF pink #FFCCE5 oldpink! #CCE5FF blue! FFE5CC orange

# The game starts here.

label start:

    $ rika_mei_score = 0
    $ marisa_ina_score = 0
    
    $ ina_score = 0
    $ mei_score = 0
    
    $ rika_score = 0
    $ marisa_score = 0
    
    $ ina_status = 'none'
    $ mei_status = 'none'
    $ rika_status = 'none'
    $ marisa_status = 'none'
    
    stop music fadeout 2.0

#### DEBUG MENU #######################################################

    #jump debugmenu      

#######################################################################
#### PART 1 ###########################################################
#######################################################################

label prologue:

    window hide
    scene black 
    with fade
    #pause(0.5)
    #play sound "audio/light3.ogg" fadein 1.0
    #scene leaves_logo with Dissolve(1.0)
    #pause(1)
    #stop sound fadeout 2.0
    scene instructions1 with pixellate
    pause
    scene instructions2 with pixellate
    pause
    play sound "audio/edgemeadow.ogg" loop fadein 5.0
    scene black with pixellate
    stop music fadeout 10.0
    window hide
    pause(1)

label p1c1:

    #play sound "audio/edgemeadow.ogg" loop fadein 2.0
    
    scene abbotsford16 with Dissolve(5.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 25.0 xalign 1.0 yalign 0.0
    
    #pause(1)
    window show    
    pause(1)

    "The nights had been growing steadily warmer."
    "A sickening fragrance of decomposing leaves lingered in the air as I made my way towards school."
    "And though I was desperately trying to recall a dream of crown roast, that I had been torn from violently no more than twenty minutes ago, I still felt grateful—"
    pause(0.5)
    "—grateful that the mornings were growing lighter again, no longer forcing me to make this miserable journey through pitch darkness."
    play music "audio/mus_vnmysticgate.ogg" loop fadein 20.0 
    pause(0.5)
    "And it was with these thoughts in mind that I became aware of a drifting presence."
    "Circling around me — scanning its environment with the trepidation of a child."
    "I turned around."
    pause(0.5)
    scene street with Dissolve(1)
    pause(0.5)
    show mari skirt normal day open at center with Dissolve(0.5)
    "Before me stood a young woman, no older than twenty-five."
    "From her sophisticated style and demeanor, I could immediately make out that she wasn't from around here."
    
    show mari skirt normal day closed at center with Dissolve(0.2)
    show mari skirt normal day open at center with Dissolve(0.2)
        
    "And the moment she noticed me, she approached — slowly at first, but more confidently once she picked up on my friendly nature."

    show mari skirt normal day closed at center with Dissolve(0.2)
    show mari skirt normal day open at center with Dissolve(0.2)
    
    s "Um, excuse me—"
    s "Could you help me? "
    s "I'm looking for a place called {i}Fairview apartments.{/i}"
    
    show mari skirt normal day closed at center with Dissolve(0.2)
    show mari skirt normal day open at center with Dissolve(0.2)   
        
    #### MARISA/INA 1 ####
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        s "Could you tell me where that is?"
        
        "Of course I can.": #Mei? You saw us on Saturday? But 
            $ marisa_ina_score += 1
            show mari skirt normal day closed at center with Dissolve(0.2)
            show mari skirt normal day open at center with Dissolve(0.2) 
            "I could discern a panic in her eyes — and I empathized with her, as it wasn't long since I had been a newcomer in this town myself, just as lost as she was."
            "Soon, however, I'd landed a job in the newspaper delivery business — the first job I'd ever held — and it wasn't long before I'd grown familiar with every street and borough of this deceptively outstretched town." #place?
            "I flashed her a reassuring smile."
            pause(0.5)
            a "Fairview? That's not far from here." 
            a "Just head back up the road and turn left at central square. You can't miss it."
            show mari skirt smile day open at center with Dissolve(0.5)

            "She let out a sigh of relief."
            pause(0.5)            
            a "Are you visiting someone who lives here?"
            show mari skirt smile day closed at center with Dissolve(0.2)
            show mari skirt smile day open at center with Dissolve(0.2)
            s "Visiting—? Um, yes. "
            s "I'm visiting—"
            s "—myself."
            "I stared at her in confusion."
            show mari skirt smile day closed at center with Dissolve(0.2)
            show mari skirt smile day open at center with Dissolve(0.2)
            s "It's {i}me{/i}, that lives at Fairview apartments. But I just moved in yesterday afternoon, so I forgot um— the fastest way home." 
            "She flashed me a silver house key."
            show mari skirt normal day open at center with Dissolve(0.5)
            s "I really thought I wouldn't get lost this time."
            "Her voice turned melancholic."
            show mari skirt normal day closed at center with Dissolve(0.2)
            show mari skirt normal day open at center with Dissolve(0.2)
            s "It's not like I'm unfamiliar with these surroundings, you know?"
            s "I used to live here as a child, until I was about six years old. I've even visited a few times since then."
            s "But things have changed. The town has expanded—"
            "She stood there for a second reminiscing, her fluttering blonde hair shining in the early morning sun."
            stop music fadeout 3.0
            show mari skirt glad day closed at center with Dissolve(0.5)
            s "Anyway, I need to go home now."
            s "To do, um— "
            s "I'm not really sure."
            show mari skirt smile day open at center with Dissolve(0.5)
            "She smiled."
            pause(1)
            s "I'll see you around."
            pause(0.5)
            a "See you—"
            
        "I'm afraid I'm running late already — please ask someone else.": 
            show mari skirt serious day open at center with Dissolve(0.5)
            s "Heavens. That was uncalled for."
            s "This is my first time experiencing the brutal countryside honesty that they warned me about."
            show mari skirt serious day closed at center with Dissolve(0.2)
            show mari skirt serious day open at center with Dissolve(0.2)
            s "I'm not even a true outsider, you know? I was born here, although we moved away when I was still a child."
            s "But I apologize, I'm holding you up."
            s "Please be on your way."      
                        
    
    #### MARISA/INA 1 ####
    

    stop music fadeout 2.0
    hide mari with Dissolve(1)
    
    "And then she disappeared, just as cautiously as she had arrived."
    pause(1)

    "With increased speed, I continued on towards school — fearing that this short delay would once more reinforce my persistent reputation of tardiness." #auto forward to opening???
    play music "<from 11.7>audio/mus_songrainyday.ogg" noloop fadein 4.0
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene white with Dissolve(1.0)
    pause(1)

#### OPENING VIDEO

label opening:

    scene white 

    #TODO
    # Show logo sooner on in the video (Leaves presents -mari- prd by S.O.C.A.H. -Rika- Deluge -etc-)
    # Add a piece of text at ending
    # End with some scrolling clouds?
    # resize imgs where necessary. probably all (even cave can be resized) 
        
    #scene opening_park with Dissolve(2.0):
    #    subpixel True
    #    xalign 0.0 yalign 1.0
    #    linear 8.0 xalign 1.0 yalign 0.0 #ease, linear, easin, easeout   
    scene schoolroad27: #playground16:
        subpixel True
        xalign 1.0 yalign 1.0
        linear 9.0 xalign 0.0 yalign 0.0 #ease, linear, easin, easeout
    with Dissolve(1.5)
    show opening_leaves with Dissolve(1.5)
    pause(2.0) 
    hide opening_leaves with Dissolve(0.5)

    # MARISA
    #hide rika
    #hide pattern_purple
    show pattern_blue:
        subpixel True
        xalign -1.0 yalign 0.0
        linear 7.5 xalign 2.0 yalign 0.0 #ease, linear, easein, easeout
    pause(1)
    show mari corset smile day closed:
        subpixel True
        xalign -1.0 yalign 0.0
        easein 2.0 xalign 0.5 yalign 0.0 #ease, linear, easein, easeout
    pause(2.0)
    show mari corset smile day open with Dissolve(0.3)
    show tulips16 behind pattern_blue:
        subpixel True
        xalign 0.0 yalign 1.0
        linear 8.0 xalign 1.0 yalign 0.0 #ease, linear, easin, easeout
    #hide pathtrees16
    pause(0.5)
    show mari corset smile day open:
        subpixel True
        xalign 0.5 yalign 0.0
        easeout 1.5 xalign 2.0 yalign 0.0 #ease, linear, easein, easeout    
    
    #pause(2)
    pause(1)
    show opening_socah with Dissolve(1.5)
    pause(2.0) 

    #pause(1)

    # RIKA
    hide mari
    show pattern_purple:
        subpixel True
        xalign -1.0 yalign 0.0
        linear 7.5 xalign 2.0 yalign 0.0 #ease, linear, easein, easeout
    hide opening_socah with Dissolve(0.5)
    pause(0.5)
    show rika uni happy day closed:
        subpixel True
        xalign -1.0 yalign 0.0
        easein 2.0 xalign 0.5 yalign 0.0 #ease, linear, easein, easeout
    pause(2.0)
    show rika uni happy day open with Dissolve(0.3)
    show cave16 behind pattern_purple:
        subpixel True
        xalign 0.0 yalign 1.0
        linear 11.0 xalign 0.0 yalign 0.0 #ease, linear, easin, easeout
    
    
    hide tulips16
    pause(0.5)
    show rika uni happy day open:
        subpixel True
        xalign 0.5 yalign 0.0
        easeout 1.5 xalign 2.0 yalign 0.0 #ease, linear, easein, easeout    
    
    pause(3)        
    show logo with Dissolve(2.0)
    pause(2)  
        

    
    # INA
    hide rika
    #hide pattern_blue
    show pattern_pink:
        subpixel True
        xalign -1.0 yalign 0.0
        linear 7.5 xalign 2.0 yalign 0.0 #ease, linear, easein, easeout
    hide logo with Dissolve(1.0)
    #pause(1)
    show ina shirt serious day closed:
        subpixel True
        xalign -1.0 yalign 0.0
        easein 2.0 xalign 0.5 yalign 0.0 #ease, linear, easein, easeout
    pause(2.0)
    show ina shirt serious day open with Dissolve(0.3)
    show marisaroom16 behind pattern_pink:
        subpixel True
        xalign 0.1 yalign 1.0
        linear 8.0 xalign 0.0 yalign 0.0 #ease, linear, easin, easeout
    hide cave16 #pathtrees16
    pause(0.5)
    show ina shirt serious day open:
        subpixel True
        xalign 0.5 yalign 0.0
        easeout 1.5 xalign 2.0 yalign 0.0 #ease, linear, easein, easeout    
    
    pause(3)
    
    # MEI 
    hide ina
    #hide pattern_pink
    show pattern_yellow:
        subpixel True
        xalign -1.0 yalign 0.0
        linear 7.5 xalign 2.0 yalign 0.0 #ease, linear, easein, easeout
    pause(1)
    show mei tshirt happy day closed:
        subpixel True
        xalign -1.0 yalign 0.0
        easein 2.0 xalign 0.5 yalign 0.0 #ease, linear, easein, easeout
    pause(2.0)
    show mei tshirt happy day open with Dissolve(0.3)

    show pathtrees16_twi behind pattern_yellow:
        subpixel True
        xalign 0.0 yalign 0.0
        linear 10.0 xalign 0.0 yalign 1.0 #ease, linear, easin, easeout

    hide marisaroom16
    pause(0.5)
    show mei tshirt happy day open:
        subpixel True
        xalign 0.5 yalign 0.0
        easeout 1.5 xalign 2.0 yalign 0.0 #ease, linear, easein, easeout    
    
    pause(5)
    #scene white with Dissolve(2.0)
    #pause(1)
    #scene logo_text with Dissolve(2.0)
    #pause(3)
    
    scene opening_sky2 with Dissolve(2.0):
        subpixel True
        xalign 1.0 yalign 1.0
        linear 15.0 xalign 0.0 yalign 0.0
    
    pause(4)
    stop music fadeout 25.0
    scene white with Dissolve(5.0)    
    pause(3)
    #show pattern_purple:
    #    subpixel True
    #    xalign 0.5 yalign 0.0
    #    easein 5.0 xalign 5.0 yalign 0.0 #ease, linear, easein, easeout    
    #show rika uni sad day open with easeinleft
    #pause(5)
    #scene black with Dissolve(1.0)   



label p1c2:

    play sound "audio/officesound.ogg" loop fadein 3.0 

    scene office with Dissolve(3.0)
    #show ina shirt angry book open at left with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)
    
    
    "By the time I reached the ever cramped office of the {i}Sunday Abbot{/i}, I was fully out of breath."
    #the little student newspaper with big aspirations, that I worked for. 
    "Ina — our ever punctual editor-in-chief — sat waiting on me."
    
    play music "audio/mus_vnaquamarine.ogg" loop fadein 10.0
    show ina shirt serious day open at center with Dissolve(1)
    pause(0.5)
    n "There you are, Abe. Your irresponsibility never ceases to amaze me." #risen to new hights
    show ina shirt serious day closed at center with Dissolve(0.2)
    show ina shirt serious day open at center with Dissolve(0.2)
    n "Even after pushing back your starting time to 9 A.M, you still manage to be late — every. single. week. "
    n "Sometimes I wonder if there's even a point—"
    "I interrupted her."
    show ina shirt hopeless day open at center with Dissolve(0.2)

    a "What about Mei? She isn't here yet—"
    "But Ina had already began opening the countless boxes, that had been dumped haphazardly across the room." #maybe change a little
    #She sighed.
    show ina shirt worried day closed at center with Dissolve(0.2)
    show ina shirt hopeless day open at center with Dissolve(0.2)

    n "Well, at least you're not delaying the dispersal of important headlines—" #big news, big headlines
    n "—we've appeared to hit a dull news-season."
    n "With the municipal election campaigns waiting to start, it seems that there really isn't much to report on." #not started yet
    show ina shirt serious day open at center with Dissolve(0.5)
    "She pouted."
    pause(0.5)
    a "Isn't there any political gossip to write about?"
    show ina shirt worried day closed at center with Dissolve(0.2)
    show ina shirt scared day open at center with Dissolve(0.2)
    n "Nothing. They're keeping their lips sealed."
    show ina shirt happy day open at center with Dissolve(0.5)
    n "But you just wait until the elections begin. The mud flinging will be out in full force."
    n "I'm sure what we're witnessing now is the silence before the storm. There'll be plenty of headlines before long. "
    pause(0.5)
    window hide
    pause(0.5)
    scene white with Dissolve(2.0)
    pause(1)
    scene title1 with Dissolve(2.0)
    pause(2)
    play audio "audio/knock.ogg"
    scene white with Dissolve(2.0)
    scene office 
    show ina shirt happy day open at center
    with Dissolve(2.0)
    window show
    pause(0.5)    
    play audio "audio/window.ogg"
    "The door swung open—"
    show ina shirt happy day open at left  #make her slide
    show mei tshirt happy day open at right 
    with easeinright
    "—and a blonde girl made a hurried entrance." #door swung open
    m "Time for work! Let's do our best today!"
    
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt happy day open with Dissolve(0.2)
    
    n "There, that's an attitude you could learn from — Abe."
    pause(0.5)
    a "But she was {i}twenty minutes{/i} late—"
    "Mei — ignoring my comment — had begun leafing through this week's edition of the Sunday Abbot." #make this less awkward 'latest edition'???
    
    
    
    m "Cool Ina! Your piece on the {i}arched marble moth{/i} made it to the front page!"
    pause(0.5)
    a "Who would have thought—"
    #Mei had crouched down and was inspecting the latest edition of our weekly paper, while Ina had begun loading our messenger cart.
    #Mei had already begun fussing over the boxes, loading our heavy-duty messenger bags to their breaking point.
    #Mei 
    #TODO
    #Due to the lay-out of the town 
    
    #pay extra attention to the order of following segments
    
    pause(0.5)
    
    "Ever since Mei's addition to the delivery team, we had worked out ways to distribute the paper as efficiently as possible — more than halving my regular working hours in the process."
    "And although it was pleasant to free up some time on the weekends, the change had instantly presented Ina the opportunity to slash my already meager wages."
    #"Though the amenities in Abbotsford didn't allow for much luxury spending — as my previous life in the capital had — 
    "I couldn't deny the reality that I was undergoing a personal financial crisis." #not again?
    
    show mei tshirt happy day closed at right with Dissolve(0.2)
    show mei tshirt happy day open at right with Dissolve(0.2)
    stop music fadeout 3.0
    
    
    
    
    
    
    m "Come on, Abe! We'll do the tenement buildings together. Then after that we can split up and do the rest of town."

    pause(0.5)
    hide mei with Dissolve(0.5)
    hide ina with Dissolve(0.5)
    pause(0.5)
    window hide
    play music "audio/mus_vninn.ogg" loop fadein 4.0 #too catchy? more thematic music?
    play sound "audio/edgemeadow.ogg" loop fadein 2.0 
    scene schoolroad16 with fade:
        subpixel True
        xalign 1.0 yalign 1.0
        easein 15.0 xalign 0.0 yalign 0.0

    pause(1)
    window show
    pause(1)
    "After loading our delivery cart with three boxes of papers, we made our way in the direction of town."

label p1c3:

    #scene schoolroad with Dissolve(1.0)
    

    
    #pause(1)
    
    "The area beyond the school was sparsely developed, with only a few mansions rising up infrequently from behind spiked gates, each surrounded by acres of woodland."
    
    "While I pulled the cart, Mei looked over the subscription directory, stopping me at irregular intervals to deliver a paper or two at a house we passed by."
    
    show mei tshirt happy day open at center with Dissolve(0.5)
    
    m "Can you smell it, Abe? Nature is blossoming."
    
    show mei tshirt happy day closed at center with Dissolve(0.2)
    show mei tshirt happy day open at center with Dissolve(0.2)
    m "This hardly feels like work, now that Spring is in the air. "
    pause(0.5)
    a "Work smells like work — no way to hide it. " #no other way to put it
    a "The scent of fresh printing-ink may seem nice at first, but at the end of the day I always have difficulty washing it from my hands."
    a "And I end up smelling like I'm hot-off-the-press, far into Sunday afternoon."
    show mei tshirt interested day open at center with Dissolve(0.5)
    "Mei smirked."
    show mei tshirt happy day closed at center with Dissolve(0.2)
    show mei tshirt interested day open at center with Dissolve(0.2)
    m "That's how it is — isn't it?"
    m "But to be honest, I really don't mind the smell." 
    show mei tshirt happy day closed at center with Dissolve(0.2)
    show mei tshirt interested day open at center with Dissolve(0.2)
    m "The ink we use has an earthy scent, that pairs well with a floral perfume—"
    pause(0.5)
    a "Mei — when did you become so {i}metropolitan.{/i}"
    show mei tshirt blush day open at center with Dissolve(0.5)
    "She blushed."
    pause(0.5)
    m "S-shut up!"
    stop music fadeout 4.0
    pause(1)
    scene leopoldhouse with Dissolve(1.0)
    pause(1)
    
    "Not much later, we arrived at a large residence."
    "Out in the yard I detected an eager face, clearly awaiting our arrival."
    
    play music "audio/mus_grieg1.ogg" loop fadein 6.0 #right music? keep happy music?
    show leo smile open at left with Dissolve(0.5)
    #TODO better positioning
    
    l "There you are, kids. Fashionably late, as always."
    l "Let me read the garbage you're disseminating today." #can't wait/ let me see what
    
    show mei tshirt nice day open at right with Dissolve(0.5)    
    
    "Though not unfriendly, councilman Leopold — the town's disgraced marquis — always held a close eye on our attempts at journalism."
    "It wasn't long since he himself had been the subject of countless headlines, publicizing his dealings with the seedy underworld."
    "But recently Leopold appeared to have cleaned up his act."
    show mei tshirt nice day open with Dissolve(0.5) 
    m "Here you go."
    show document at Position(xpos=0.25, xanchor=0.5) with Dissolve(0.5)
    "Grumbling appreciatively, he browsed through the newspaper."
    
    show mei tshirt happy day closed with Dissolve(0.2)
    show mei tshirt nice day open with Dissolve(0.2)    
    
    m "Nothing written about you today?"
    show leo laughing open with Dissolve(0.5)
    "Leopold smiled."
    show leo laughing closed with Dissolve(0.2)
    show leo laughing open with Dissolve(0.2)
    l "No, it seems like Ina has retained her decorum." #maintained
    l "I don't mind your paper reporting the {i}news{/i}, you see—"
    show leo serious open with Dissolve(0.5)
    l "—but it's when the line between the public and private sphere blurs, that I have my reservations about her journalism."
    show leo serious closed with Dissolve(0.2)
    show leo serious open with Dissolve(0.2)
    l "It isn't easy. Being a public figure." #you see, you know...
    l "It becomes so much harder to {i}indulge{/i} when everyone's watching you."
    
    l "You slip up once — make one tiny mistake — and it's magnified a thousandfold."
    show mei tshirt sad day open with Dissolve(0.2)
    "I nodded compassionately."
    show leo serious closed with Dissolve(0.2)
    show leo serious open with Dissolve(0.2)    
    l "It's a lonesome endeavor." #"And you don't have any friends. "
    l "Do you know what my party has done to me, for the upcoming elections?"
    pause(0.5)
    a "No—"
    l "They lowered me to eleventh place on the list. "
    l "Just out of spite, over things that happened in the past—"
    pause(0.5)
    a "Eleventh place? What does that mean?"
    show leo serious closed with Dissolve(0.2)
    show leo serious open with Dissolve(0.2)      
    l "It means the end—"
    l "—of my political career, that is. "
    l "My party, A.I.R, only holds eight seats in the town council. So I have zero chance of returning to my position next year."
    show mei tshirt serious day closed with Dissolve(0.2)
    show mei tshirt sad day open with Dissolve(0.2)

    m "Maybe if you campaign {i}really{/i} hard—" #mei says this
    l "Forget about it. It's political homicide." #this is, hit job
    "He scowled."
    pause(0.5)
    a "Just think of all the free time you'll have." #abe says this"
    show leo serious closed with Dissolve(0.2)
    show leo serious open with Dissolve(0.2)    

    l "Hm. I'll need it—"
    
    l "To make matters worse, my deadbeat son is returning home this year after dropping out of university."
    l "He was majoring in {i}German romantic theater{/i} — or something equally useless — but even that turned out too demanding for him. " #simlarly useless
    l "And now he can't find a job for the life of him—"
    show leo serious closed with Dissolve(0.2)
    show leo serious open with Dissolve(0.2)   
    l "Can't you kids put him to work delivering papers—?"
    show mei tshirt happy day open with Dissolve(0.2)
    a "I think our team is pretty much complete."
    show leo smile open with Dissolve(0.5)    
    "He chuckled."
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)
    l "Well I can't blame you for keeping your distance. He's a real slacker, hasn't worked a day in his life—"
    l "—and still, he'd be the type to consider himself too good for this kind of work."
    show mei tshirt angry day open with vpunch
    "Mei jumped up."
    m "No one is too good to deliver the Sunday Abbot!"
    
    show mei tshirt angry day closed with Dissolve(0.2)
    show mei tshirt angry day open with Dissolve(0.2)
    l "Never mind."
    l "Bernard is his name. You might catch him loitering around town."
    l "I hope to have him off my hands soon."
    
    stop music fadeout 3.0
    pause(0.5)
    hide mei with Dissolve(0.5)
    hide leo 
    hide document
    with Dissolve(0.5)
    pause(0.5)
    window hide
    pause(0.5)
    stop sound fadeout 1.0
    scene canal with fade
    play sound "audio/cricketsafternoon.ogg" loop fadein 1.0
    pause(1)
    window show
    pause(0.5)
    
    #TODO happy music returns? maybe no music
    
    "We said goodbye to the grumbling marquis and made our way to the edge of town, where a working-class district lay that was irregularly littered with council houses."
    play audio "audio/bark2.ogg"
    play music "audio/mus_vn1234piano.ogg" fadein 10.0
    show phyrrus_small at left with easeinleft
    "We were welcomed by a loud bark."
    
    #TODO phyrrus appears
    
    show mei tshirt happy day open at right behind phyrrus_small with Dissolve(0.5)
    
    m "Good morning Phyrrus! You're up early."
    show mei tshirt happy day closed with Dissolve(0.2)
    show mei tshirt happy day open with Dissolve(0.2)
    m "Phyrrus here has been helping me on Saturdays, by pulling the cart and protecting me against danger. "
    "She reached out to give the dog a pat on the head—"
    play effects "<from 1.0>audio/angrydog.ogg" noloop
    #play audio "audio/bark1.ogg"
    show phyrrus_small at Position(xpos=0.53, xanchor=0.5) #with ease   
    show mei tshirt blush day open at Position(xpos=0.85, xanchor=0.5)
    with easeinleft    
        #with Dissolve(0.2)

    "—but in an instant, the dog lunged at her and sank its teeth deep into her her arm."
    stop effects fadeout 4.0
    m "Phyrrus! That hurt!"
    show phyrrus_small at Position(xpos=0.43, xanchor=0.5) with ease
    "Reluctantly, the dog retreated."
    
    m "Please be more careful, Phyrrus — we don't have time to play."
    
    #a "I'm uncertain of that dog had been protection you, or that you need protection against it."
    
    pause(0.5)
    hide mei with easeoutright
    hide phyrrus_small with easeoutright


    pause(0.5)
    #TODO change scenery
    scene playground with Dissolve(0.5)
    pause(1)
    

    "Our work proceeded quickly, and it wasn't even lunchtime by the time we rounded the last tenement block."   
    "Phyrrus followed us at a safe distance."    
    
    show mei tshirt happy day open at right with Dissolve(0.5)
    
    m "We're doing great, Abe! Phyrrus and I'll take the cart and finish off the remaining suburbs."
    show mei tshirt happy day closed with Dissolve(0.2)
    show mei tshirt happy day open with Dissolve(0.2)
    m "You should have enough papers left to cover the city center."
    
    a "Are you sure you'll be safe?"
    show phyrrus_small at left with easeinleft    
    m "Don't worry Abe, I have Phyrrus by my side."
    pause(0.5)
    a "{i}That's what I was worried about—{/i}"
    
    #have phyrrus show up here?
    pause(0.5)
    
    "I thanked Mei and we each went our way."

    pause(0.5)
    hide mei with easeoutright
    hide phyrrus_small with easeoutright
    pause(0.5)
    stop music fadeout 2.0
    #hide ina with Dissolve(0.5)
    #hide rika with Dissolve(0.5)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)

label p1c4:

    play sound "audio/citysounds.ogg" loop fadein 5.0 #webeside clock

    scene ichthys with Dissolve(1.0)
    #show ina shirt angry book open at left with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)
    
    
    "Abbotsford's town center isn't large — and as I made my way from letterbox to letterbox, I thought to myself that Mei had truly drawn the shortest straw by agreeing to cover the suburbs."
    pause(0.5)
    "Mei, however, appeared to derive a lot more satisfaction from the work than I did — so it seemed fair that she would take on the lion's share of the workload." # and as I made myself across central square, where the large Ichthys Church stood, my mind was filled with scornful thoughts. "
    pause(0.5)
    "Suddenly, I picked up a distinct laughter." #familliar face/voice
    play music "audio/mus_bachwtk3.ogg" loop fadein 6.0    
    show rika uni happy day open at Position(xpos=0.70, xanchor=0.5) with Dissolve(1)    
    r "Look, it's Abe — always the bearer of glad tidings." #good tidings?
    
    "I glanced in the direction of the sound and made out two girls, both of whom attended my high school."
    #"She had been speaking to the girl next to her, who I recognized from school." #improve !!!!!!! TODO TODO
    show naomi uni serious day glas at left with Dissolve(1)    
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "This is Naomi, you may know her. She's on the swim team."
    show naomi uni intent day glas with Dissolve(0.5)
    "Naomi acknowledged me with a curt nod of her head."
    show naomi uni serious day glas with Dissolve(0.5)    
    
    a "So what are you girls doing here? Church isn't until tomorrow, right?"
    
    #We need to get the church ready in time for the sermon tomorrow.
    
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    
    r "Of course it isn't, but we're helping with the preparation for the Sunday service."
    r "We're here to do some routine maintenance on the church properties."
    pause(0.5)
    a "Can't the church afford to hire {i}specialists{/i} for that kind of work?"
    show rika uni mischievous day open with Dissolve(0.5)
    r "It's just recurring tasks. Old buildings require a lot of upkeep—"
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)    
    r "But please follow me. I want you to look at something."
    stop music fadeout 3.0
    pause(0.5)
    hide rika with Dissolve(0.5)
    hide naomi with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    scene church with Dissolve(1.0)
    play music "<from 118.0>audio/mus_voctiefe2.ogg" loop fadein 12.0 
    pause(1)
    
    "As I followed the girls through the main entrance, into the nave of the church, I could hear soothing tones seeping in through the walls." #choir was practicing in auditorium (let rika explain this?)
    pause(0.5)    
    show rika uni mischievous day open with Dissolve(0.5)     
    r "That's the boys choir, they're practicing in the auditorium."
    r "I hope you don't mind the sound." #conservatory
    
    # "Though most parts of the Ichthys complex had been erected during recent times, it encompassed the seventeenth century structure of the original church of Abbot."
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)       
    "She beckoned me onward."
    pause(0.5)
    hide rika with Dissolve(0.5)
    
    stop music fadeout 3.0
    pause(1)
    scene catacombs with Dissolve(1.0)
    play effects "<from 75.0>audio/mus_voctiefe1_damp.ogg" loop fadein 10.0 
    pause(1)    
    
    "We headed down a short staircase and through a narrow corridor, that led into a crypt that was situated directly underneath the church."
    
    pause(1)
    scene crypt_dark with Dissolve(1.0)
    pause(1)   
    
    "In the faint light I could make out the walls. They were covered with engravings that appeared worn and faded, as though they had once been exposed to the elements."
    pause(0.5)
    show rika uni mischievous nig open at Position(xpos=0.7, xanchor=0.5) with Dissolve(1)
    show naomi uni intent nig glas at left with Dissolve(1)
    pause(0.5)
    "Rika pointed upward."
    
    show rika uni mischievous nig closed with Dissolve(0.2)
    show rika uni mischievous nig open with Dissolve(0.2)
    
    r "There. There should be a light bulb above that door, but it isn't working anymore."
    r "Are you tall enough to look behind there?"
    show naomi uni suprised nig glas with Dissolve(0.2)
    "I stretched myself to see over the casing of the door, where I could barely discern a small light socket."
    pause(0.5)
    a "I can probably reach it, but it's pretty high up."
    a "Can't you just use a step-ladder." #and do it yourselves?
    show naomi uni smile nig glas with Dissolve(0.2)
    "Naomi giggled."
    
    u "I mean, we {i}could.{/i} But just think of all the spiders that live up there—"
    u "Please help us Abe — now that you're here anyway."
    show naomi uni serious nig glas with Dissolve(0.2)    
    "I reached over the door with my hand until I felt the smooth surface of an incandescent bulb."
    r "Carefully I unscrewed it, setting a fine stream of age old dust pouring downward over my clothes."
    pause(0.5)
    "The bulb came loose."
    pause(0.5)
    "I stepped down and held it to Rika's ear —{nw}"
    play audio "audio/brokenbulb.ogg"
    extend " shaking it, so that a rattling sound became clearly audible." #TODO SFX
    show rika uni sad nig open with Dissolve(0.5)
    r "A burnt out bulb, just as I thought."
    r "But don't worry—"
    "She dug around in her uniform pocket."
    show rika uni happy nig open with Dissolve(0.5)
    r "—we bought a new one. This one uses advanced {i}Light Emitting Diode{/i} technology."
    r "It should last much longer and save the church on electricity."
    #Light emitting diode"
    "Smirking, I took the bulb from her and carefully screwed it into its socket. "
    scene crypt 
    show rika uni happy day open at Position(xpos=0.7, xanchor=0.5)
    show naomi uni serious day glas at left 
    with Dissolve(0.1)
    scene crypt_dark
    show rika uni happy nig open at Position(xpos=0.7, xanchor=0.5)
    show naomi uni serious nig glas at left 
    with Dissolve(0.1)
    scene crypt 
    show rika uni happy day open at Position(xpos=0.7, xanchor=0.5)
    show naomi uni serious day glas at left 
    with Dissolve(0.1)
    scene crypt_dark
    show rika uni happy nig open at Position(xpos=0.7, xanchor=0.5)
    show naomi uni serious nig glas at left 
    with Dissolve(0.1)

    
    
    
    scene crypt 
    show rika uni happy day open at Position(xpos=0.7, xanchor=0.5)
    show naomi uni serious day glas at left 
    with Dissolve(0.1)
    
    "When I was nearly done it began to emit a blinding light."
    "I had to catch myself to retain my balance, as the entire crypt — that had been steeped in darkness just a moment ago — was suddenly illuminated." #TODO effect
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "There, that wasn't too much trouble. Was it?"
    pause(1)
    "As my eyes grew accustomed to the light, I became aware of my surroundings."
    "We were standing inside a windowless catacomb. Large stone slabs covered the walls around us, every one of them inscribed with time-worn glyphs."
    pause(1)
    a "Some places are better kept in darkness—"
    show rika uni sad day open with Dissolve(0.2)
    r "Oh not at all — do you see these stones?"
    r "Do you know where they come from?"
    pause(0.5)
    a "They look like gravestones to me—"
    show rika uni happy day open with Dissolve(0.5)
    "Rika smiled."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "That would be correct."
    
    r "You should take a look at the dates on these stones."
    r "Some date back to the early fourteen-hundreds."
    show naomi uni intent day glas with Dissolve(0.2)
    r "When this town was still situated on an island—"
    show rika uni happy day open  with Dissolve(0.5)
    r "Did you know there used to be a different church on Abbot?"
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "It served the congregation up until 1653."
    r "Its ruins can still be visited, close to the southern point."
    r "The old church even had an adjacent graveyard — but I'm afraid the encroaching sea made for watery graves."
    r "And the salt water ate at the foundations of the church, rotting away the wood and making the stone walls tilt over threateningly."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "When a large winter storm swept away the cemetery gates — one dark December night — the community decided it was time to build a new and more splendid church, on higher laying land. "
    r "That's the building we're now standing in."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "Construction began immediately, although work was halted many times in pursuit of new funding."
    r "All building supplies had to be transported from the mainland. And when funds ran out, many stones were taken from the old church to continue the project."
    
    r "After forty years of construction, the new church was completed — and our place of worship was moved to this new location."
    show rika uni sad day open with Dissolve(0.2)
    r "The dead, however, stayed behind in their old cemetery."
    r "There the remains of our forefathers languished beneath the skeleton of a decrepit chapel, constantly threatened by the washing sea."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "And the reverend Kuyper, my great forefather, decided that something was to be done—"
    #But we couldn't leave these graves behind.
    
    r "Now that work on the new church was finished, the villagers commenced with the process of moving the dead to the new location."
    r "They began with the graves that were in immediate danger of being swallowed by the sea." #before they began moving inland."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "But, as you can imagine, it was unpleasant work. No one found joy in digging up old bones—"
    
    r "—and the graveyard relocation project grew into an effort that spanned multiple centuries, often lying still for decades. "
    r "It wasn't until the beginning of the twentieth century, that the last of the graves was moved to dry land."
    show rika uni mischievous day open with Dissolve(0.5)
    "Rika glared at us ominously, while a silver sheen glistened through her ink-black hair."
    #"The choir had stopped singing. The church was filled with deathlike silence." #change choir #is this needed? depends on sfx
    #"Naomi sat looking at Rika, an expression of discomfort filling her eyes."

    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)
    r "But even then, they say at least a few graves must have been overlooked — their contents swept into the endless depths of the ocean." #SFX
    
    show rika uni sad day open with Dissolve(0.5)           
    #"Suddenly."
    #a "Anyway, if that's all you needed me for, I'd better be on my way—"

    r "Oh Abe, I apologize, we've been keeping you from your work. And to think that it's almost lunch time."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "Won't you have lunch with us? Naomi has packed sandwiches." #what kind of lunch
    r "Come on Naomi, after our hard work, I say we've deserved a break. We'll finish decorating in the afternoon."
    stop effects fadeout 3.0
    pause(0.5)
    hide rika with Dissolve(0.5)
    hide naomi with Dissolve(0.5)
    pause(0.5)
    pause(1)
    scene church with Dissolve(1.0)
    play music "<from 18.0>audio/mus_voctiefe2.ogg" loop fadein 12.0 
    pause(1)   
    
    "We climbed back up the stairs and settled among the pews." 
    
    show naomi uni smile day glas at left with Dissolve(0.5)
    show rika uni happy day open at Position(xpos=0.7, xanchor=0.5) with Dissolve(0.5)
    
    u "I made these at home, please let us share them together."
    u "I hope you didn't have other plans for lunch."
    "I shook my head."
    show rika uni happy day closed with Dissolve(0.2)
    pause(0.5)
    a "Usually I don't even get around to eating on days like these—"
    "Naomi handed me a sandwich."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)    
    r "So how have you been doing, Abe? Are you fully prepared for finals?"
    "I grumbled a reply."
    show rika uni mischievous day open with Dissolve(0.5)
    r "Oh and—"
    r "—I haven't received your submission form for {i}easter break{/i} yet." 
    r "Could you hurry up and fill one out? We're running short on applicants."
    "I looked up from my sandwich."
    pause(0.5)
    a "{i}Easter break—?{/i}"
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)
    r "Haven't you seen the notices at school?"
    r "It's our yearly outing — where we stay at the beach for a few days, as a last escapade before finals start." #let Naomi say this
    
    #It's open to anyone, though it's usually usually as a last escapade before finals start.
    r "We'll hold nightly study sessions, but mainly it will be a care-free vacation."
    r "Naomi and I are on the organizing committee together—"
    "Rika took out a small form from her purse."
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)    
    r "Please fill this out as soon as possible. You wouldn't want to miss easter break."
    r "And let me know if you think of anyone else who would be interested in attending—"
    r "As registration is low this year, anyone is welcome. Not just graduate students."
    pause(0.5)
    
    #### RIKA 1 ####
    
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        r "Will you join us on easter break?"
        
        "I'd love to!": #Mei? You saw us on Saturday? But 
            $ rika_mei_score += 1
            show rika uni mischievous day closed with Dissolve(0.5)
            r "I knew you would."
            r "Please fill this out and hand it to me at the earliest possible occasion."
            pause(0.5)
            "I accepted the form, slipping it into my pocket thoughtlessly."
            show rika uni mischievous day open with Dissolve(0.5)     
            r "I hope you own a pair of swimming trunks."

        "This doesn't sound like my cup of tea.": #Mei? You saw us on Saturday? But 
            show rika uni sad day open 
            show naomi uni serious day glas
            with Dissolve(0.5)       
            r "Hmm. How disappointing."
            r "Please give it some consideration."
            show rika uni mischievous day open with Dissolve(0.5) 
            "She held out the form, and begrudgingly I accepted it."
            
    #### RIKA 1 ####
    
    
    
    
    
    #show rika uni mischievous day closed with Dissolve(0.2)
    #show rika uni mischievous day open with Dissolve(0.2) 
    #"Rika winked."
    # 
    #
    #pause(0.5)
    #"Thoughtlessly I slipped the piece of paper into my pocket."
    
    stop music fadeout 7.0
    pause(0.5)
    hide naomi with Dissolve(0.5)
    hide rika with Dissolve(0.5)
    pause(0.5)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)

label p1c5:

    play sound "audio/citysounds.ogg" loop fadein 5.0 

    scene ichthys with Dissolve(1.0)
    #show ina shirt angry book open at left with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)
    
    "Emphasizing that I really needed to return to work, I thanked the girls and said goodbye."

    pause(0.5)

    "And with a well-filled stomach I moved onward through the Saturday streets, which had come alive with the bustle of pedestrians enjoying their weekend."
    
    pause(0.5)
    
    "But I couldn't deny that my conversation with Rika and Naomi had stirred a certain anxiety in me."
    pause(0.5)
    "The truth was that finals were rapidly approaching."
    "And my ever increasing obligations towards the school paper, as well as my leisurely approach to life, had not left much time for study." #lot going on at the same time
    pause(0.5)   
    "I resolved halfheartedly to start studying that very evening."
    pause(0.5)
    
    scene abbotsford16 with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 15.0 xalign 1.0 yalign 0.0
    pause(0.5)    
    
    "In the meantime, my work was coming along nicely."
    pause(0.5)
    "In less than an hour I'd managed to complete the houses around central square and the shopping district, where very few subscribers lived."
    
    pause(0.5)
    
    play music "audio/mus_vnlove1.ogg" loop fadein 20.0 #right tune?
    "When suddenly—"
    "—I was struck by a strong sensation of {i}déjà-vu.{/i}"
    
    pause(0.5)
    scene street with Dissolve(0.5)
    pause(0.5)
    
    show mari skirt normal day open at center with Dissolve(0.5)
    pause(0.5)
    
    a "Good afternoon, out and about again?"
    
    show mari skirt normal day closed at center with Dissolve(0.2)
    show mari skirt normal day open at center with Dissolve(0.2)
    
    s "I—I am!"
    
    if marisa_ina_score == 0:
        s "Just so you know. I found my way home this morning, even without your help."
        pause(0.5)
        a "I apologize for my rudeness, but you need to realize that time is money."
    else:
        show mari skirt smile day open at center with Dissolve(0.5)
        s "Thank you for your clear directions this morning. I found my way home in a heartbeat."
        s "You're so knowledgeable about the lay-out of this town—"

        show mari skirt smile day closed at center with Dissolve(0.2)
        show mari skirt smile day open at center with Dissolve(0.2)
    
        a "It comes with the job description."
    
    "I presented her with an issue of the Sunday Abbot."

    a "Here, take one — we always have plenty left at the end of the day." #sudden?


    show mari skirt smile day closed at center with Dissolve(0.2)
    show mari skirt smile day open at center with Dissolve(0.2)    
    s "A newspaper—?"
    show mari skirt normal day open at center
    #show document at Position(xpos=0.44, xanchor=0.5) 
    with Dissolve(0.5)
    "Curiously, she looked it over."
    show mari skirt normal day closed at center with Dissolve(0.2)
    show mari skirt normal day open at center with Dissolve(0.2)
    
    s "That's wonderful — for a town like this."
    s "Are you on the board of editors?"
    pause(0.5)
    a "Not officially, although I stand in at times—" #jump in?

    show mari skirt smile day open at center with Dissolve(0.5)   
    "She smiled."
    show mari skirt smile day closed at center with Dissolve(0.2)
    show mari skirt smile day open at center with Dissolve(0.2)   
    s "Well, it must be exciting, with the elections coming up."
    s "Thank you so much for this. I'll make sure to get a subscription."
    pause(0.5)
    a "Please don't feel obliged to—"
    show mari skirt smile day closed at center with Dissolve(0.2)
    show mari skirt smile day open at center with Dissolve(0.2)    
    s "No. I definitely will. As soon as I get home—"

    show mari skirt serious day open at center with Dissolve(0.5)  
    s "—which is in that general direction, isn't it?"
    "She gestured northward, towards the edge of town."
    "I sighed."
    
    a "Follow me — I'll pass by your place in a little bit."
    a "Just a few more stops along the way."
    show mari skirt serious day closed at center with Dissolve(0.2)
    show mari skirt serious day open at center with Dissolve(0.2)
    s "Oh thank you, Abe. I got lost again. "
    s "I shouldn't have taken that right turn at the mini mart—"
    pause(1)
    hide mari with Dissolve(0.5)
    pause(1)
    scene villageroad with Dissolve(0.5)
    pause(1)
    "I followed my course, with Marisa trailing behind me, until we approached Fairview apartments." 
    
    pause(1)
    scene mainstreet with Dissolve(1.0) #TODO in hallway? Facade is nor right angle for dialogue
    pause(1)
    show mari skirt normal day open at center with Dissolve(0.5)
    pause(1)
    
    "Outside of the main entrance, she turned to me, standing so close that I could feel her breath." #smile as bright as etc.
    show mari skirt normal day closed with Dissolve(0.2)
    show mari skirt normal day open with Dissolve(0.2)
    s "You saved me again, I would be lost without you."
    s "Please come upstairs. I'll make you some tea—"
    show mari skirt normal day closed with Dissolve(0.2)
    show mari skirt normal day open with Dissolve(0.2)
    s "—as I have no other way to thank you."
    pause(0.5)
    hide mari with Dissolve(0.5)
    pause(0.5)
    scene corridor with Dissolve(0.5)
    pause(1)
    "We made our way up the spartan staircase and through a narrow corridor, before entering her flat." #accurate description
    stop music fadeout 2.0
    pause(1)
    stop sound fadeout 1.0
    #scene marisaroom with Dissolve(1.0)
    scene studio with Dissolve(1.0)
    play sound "audio/officesound.ogg" loop fadein 1.0
    pause(1)
    
    #"She disappeared into the kitchen to put on water, before returning with a self-conscious expres." #meh
    play music "audio/mus_vnperidot.ogg" loop fadein 18.0 #maybe continue previous track?
    show mari skirt normal day open at center with Dissolve(0.5)
    
    s "I apologize again for causing you so much trouble."
    
    show mari skirt normal day closed at center with Dissolve(0.2)
    show mari skirt normal day open at center with Dissolve(0.2)
    
    s "Normally I'm very independent — you should realize that. "
    
    s "It's just that this is my first time truly living on my own."
    
    "She wrung her hands nervously."
    show mari skirt normal day closed at center with Dissolve(0.2)
    show mari skirt normal day open at center with Dissolve(0.2)
        
    
    s "I mean — when I was in college, I lived with roommates in a shared apartment. "

    show mari skirt smile day open at center with Dissolve(0.5)
    s "We were independent, but we divided the chores. I mainly did the laundry."
    s "And the other girls would cook and clean."
    s "And now that I'm living by myself, it feels like I have to do everything alone."
    show mari skirt smile day closed at center with Dissolve(0.2)
    show mari skirt smile day open at center with Dissolve(0.2)
    
    s "I've been getting lost — around town, even though this place is far smaller than the city — but also in my head."
    s "I think it's just that I've had so much on my mind—"
    
    #She laughed self-consciously.
    show mari skirt serious day open at center with Dissolve(0.5)
    
    s "Just a minute — the tea should be ready."
    pause(0.5)
    hide mari with Dissolve(0.5)
    
    "She bounded into the kitchen, where I could hear her rattling with teacups." #sfx 
    "And I waited in the empty studio apartment — which, although neatly furnished, still had a certain impersonal feel to it. As though it hadn't been fully made into a home."
    
    # description of room
    pause(0.5)
    show mari skirt normal day open at center with Dissolve(0.5)
    
    s "I made Earl Grey. I hope you like it, as it's all I've got."
    
    "She let out a melancholy sigh."
    
    show mari skirt normal day closed at center with Dissolve(0.2)
    show mari skirt normal day open at center with Dissolve(0.2)
    
    s "Student life is nothing like the real world, you know? "
    s "At college you're sheltered, cared for — you have your path set out for you. "
    s "But now that's all over — a grand, open future beckons me."#invitingly."
    
    #
    pause(0.5)
    
    a "So why did you come to Abbotsford?"
    #She giggled embarrassedly.
    show mari skirt smile day open at center with Dissolve(0.5)
    s "Oh I like this town. I used to live here, back when I was very small."
    s "Didn't I tell you?"
    show mari skirt smile day closed at center with Dissolve(0.2)
    show mari skirt smile day open at center with Dissolve(0.2)
    s "And I'm not just freeloading. I have a job. A real job! "
    s "Although I won't be starting it just yet—"
    show mari skirt serious day open at center with Dissolve(0.5)
    "She grew silent."
    pause(0.5)
    a "What kind of job—?"
    show mari skirt serious day closed at center with Dissolve(0.2)
    show mari skirt serious day open at center with Dissolve(0.2)
    s "Oh I cant tell you — not until next week."
    s "Because it's a secret—"
    show mari skirt smile day open at center with Dissolve(0.5)    
    s "And I know what you journalists are like." #press?
    
    "She shivered, giddily."
    show mari skirt smile day closed at center with Dissolve(0.2)
    show mari skirt smile day open at center with Dissolve(0.2)
    s "But I have a job! I can't even fathom it—"
    s "I'm on the fast lane to success." #highway, speedway
    s "Soon it won't be lukewarm tea — but champagne filling these cups."
    
    show mari skirt glad day closed at center with Dissolve(0.5)
    
    "She broke out in animated laughter, as I felt a strange tingle make its way down the back of my neck."
    pause(0.5)
    hide mari with Dissolve(0.5)
    pause(0.5)
    "Marisa got up. She walked over to the corner of the room to pick up her shopping bag — which she had discarded thoughtlessly upon entry — and brought out a packet of cinnamon buns."
    
    show mari skirt glad day closed at center with Dissolve(0.5)
    
    #She passed me a bowl of rolls. #have her take something from shopping bag
    s "Here, have something to eat. It's passed lunch time."
    "I was about to decline, but she had already handed me a roll, and I saw no polite way to refuse it."
    s "I realize you must be on your way, but you won't be able to deliver papers on an empty stomach." #rika said this too
    
    #
    
    # A map, yes, that would be a good idea. Wouldn't it?
    # I'll make my way to the tourist information later this afternoon.
    # She spoke the words unenthousiastically.
    # It's great to have everything on walking distance.
    
    #
    stop music fadeout 4.0
    pause(1)
    hide mari with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    scene mainstreet with Dissolve(1.0)
    play sound "audio/citysounds.ogg" loop fadein 1.0
    
    "After no less than three cinnamon buns, I exited Fairview apartments. "
    "The day had progressed, and I was borne down, physically as well as mentally, by the weight of the newspapers that remained in my bag."
    "And though I encountered people sitting in their gardens, basking temptingly in the early spring sun, I vowed solemnly not to be held up until I had delivered the remainder of my route."
    #"I must persevere. The people depend on me." #used once before in prev game "as ina would say:"
    
    pause(1)
    scene house with Dissolve(1.0)
    pause(1)
    
    "It wasn't much later that I came across a slouched over figure, slowly making its way in my direction." #
    pause(0.5)
    play music "audio/mus_grieg16.ogg" loop fadein 12.0
    show mei tshirt sad day open at center with Dissolve(1)
    pause(0.5)
    

    a "Hi Mei. How are you getting along?"
    show mei tshirt nice day open at center with Dissolve(0.5)
    "From under her worn appearance, she flashed me a vulnerable smile."
    show mei tshirt happy day closed at center with Dissolve(0.2)
    show mei tshirt nice day open at center with Dissolve(0.2)
    
    m "I'm okay, Abe. I worked really hard, I only have the West End left."
    m "Phyrrus left more than an hour ago. I think he decided he'd rather spend the afternoon lying in the sun."
    "She cast a glance at my messenger bag."
    show mei tshirt happy day closed at center with Dissolve(0.2)
    show mei tshirt nice day open at center with Dissolve(0.2)    
    m "But wow. You look like you're almost done—"
    m "You must have had a tough afternoon."
    
    "I chuckled awkwardly."
    show mei tshirt sad day open at center with Dissolve(0.5)    
    m "I'm really tired. And to be honest, I'm starved."
    m "How about we stop for a late lunch together—"
    show mei tshirt nice day open at center with Dissolve(0.5)    
    #"She smiled apologetically."
    
    "My belly protested in all its overindulgence."
    "While I had been spending the afternoon eating and socializing, Mei must have been working uninterruptedly."
    "I could hardly reject her offer on the account that I'd already eaten two full lunches—"
    pause(0.5)
    a "You know what?"
    a "I'd love to, it's just—"
    "She stared at me hopefully."
    show mei tshirt happy day closed at center with Dissolve(0.2)
    show mei tshirt nice day open at center with Dissolve(0.2)    
    a "—I've been feeling a little nauseous lately."
    
    a "I'm going to finish my work quickly, before going to bed—"
    a "But please eat something for {i}my{/i} sake."
    show mei tshirt serious day open at center with Dissolve(0.5)
    m "You're ill—? "
    "A worried expression had come over her."
    show mei tshirt serious day closed at center with Dissolve(0.2)
    show mei tshirt serious day open at center with Dissolve(0.2)
    m "Nauseous—? It could be a fever—"
    m "You better hurry home quickly. Let me deliver the rest of your papers."
    pause(0.5)
    "I could feel the blood rushing to my head."
    pause(0.5)
    a "No, no—"
    a "I'm fine. Hard work will set me free."
    
    pause(0.5)
    "Bent over in shame, I hurried towards the last mailboxes of the day. "
    stop music fadeout 5.0
    pause(0.5)
    hide mei with Dissolve(0.5)
    pause(1.0)

    #hide rika with Dissolve(0.5)
    pause(1.0)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)

label p1c6:

    play sound "audio/crowfield.ogg" loop fadein 2.0 

    scene school_side with Dissolve(1.0)
    #show ina shirt angry book open at left with Dissolve(1.0)
    pause(1)
    play audio "audio/schoolbell.ogg"
    window show    
    pause(1)
    #play music "audio/mus_lotusland.ogg" loop fadein 8.0 #was poucet    
    
    "In the months leading up to finals, the school days were short and filled with repetition."

    scene office with Dissolve(1.0)
    pause(1)
    
    play music "audio/mus_lotusland.ogg" loop fadein 6.0 #intentional
    show ina shirt serious day open at center with Dissolve(1)
    pause(0.5)
    
    n "Spring has come early this year."
    n "Look outside, the Tilia are budding — but it won't last long, you know?"
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt serious day open with Dissolve(0.2)
    n "If we have a cold spell in April, the new foliage will freeze to death."
    n "Nature punishes presumptuousness harshly—"
    
    show ina shirt serious day open at left with easeinright #TODO move her, could also be a zoom out
    
    "She turned away from the window."
    
    n "But anyway—"
    show ina shirt happy day open with Dissolve(0.5)
    n "The two of you did a great job, last Saturday." #mei isn't there
    n "I'll need you to keep up that attitude over the coming weeks, as the electoral campaigns will be starting next Wednesday."
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt happy day open with Dissolve(0.2)
    n "Although we're just a weekly paper, we're the only dedicated news source this town has."
    n "That means whenever something big happens down here, our reporting will be the focus point of all national media."
    pause(0.5)
    a "{i}If{/i} something big happens—"
    
    show ina shirt worried day open with Dissolve(0.5)
    n "These elections are a chance for the Sunday Abbot to break into the national headlights—"
    "So I'll need you at your sharpest." #whole section is a little cheesy
    
    show ina shirt happy day open with Dissolve(0.5)
    "She let out a giggle."
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt happy day open with Dissolve(0.2)
    n "And you should hear this—"
    
    n "Currently, the parties are in the process of announcing their leading candidates."
    n "Flock 05 — the town's second party — just published a press release this morning."
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt happy day open with Dissolve(0.2)    
    n "Their party has been in trouble lately, as their previous frontrunner was arrested on domestic abuse charges." #meh
    n "He hasn't been convicted yet, but it's a bad look for them."
    
    n "Ahead of the coming elections, Flock has been searching frantically for a new leader."
    n "Just take a look at who they've chosen."
    window hide
    pause(0.5)
    show press release with easeinbottom
    pause(0.5)
    window show
    "She presented me with a press release on her phone. I immediately recognized the accompanying photograph." #phone? Or printed on paper? Include img.
    pause(0.5)
    "I coughed."
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt happy day open with Dissolve(0.2) 
    n "A person with no experience at all."
    n "Apparently she just graduated from law school. Dabbled a little in student politics."
    n "And she did some — modeling work?" #(law major?) 
    hide press release with easeoutbottom
    "Ina snickered."
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt happy day open with Dissolve(0.2) 
    n "I couldn't think of a more incompetent candidate—"
    n "—but let's not be too quick to write her off."
    pause(0.5)
    a "Are you sure that's her? She looks an awful lot like someone I crossed paths with last Saturday."
    show ina shirt angry day open with Dissolve(0.5)
    n "Crossed paths with—?"
    pause(0.5)
    a "I think so. But she didn't strike me as the type to lead a political movement — if you know what I mean."
    a "What was her name again? Marisa—"
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)

    n "{i}Marisa Roosevelt.{/i}"
    n "Her name is in the press release."
    n "And you're saying you ran in to her?"
    n "Maybe she was in town for deliberations."
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)    
    n "She'll probably move here sometime soon. You need to be a legal resident of Abbotsford to run for office."
    
    "I smiled."
    pause(0.5)
    a "She has an apartment already — though I'm not sure if she's fully aware of it herself."
    
    "Ina ignored my remark. From the sound of her right index finger rapidly tapping against her skirt, I could tell that she was coming up with a scheme." #meh #SFX
    show ina shirt serious day open with Dissolve(0.5)    
    "She turned to me with a serious expression in her eyes."
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt serious day open with Dissolve(0.2)   

    n "I think this could be a good thing, Abe."

    n "This year, I want to take a deep dive into the individual campaigns." #As journalists, we need to be unbiased — however, t
    n "Flock 05, as a movement, has been on the rise for a good number of years. Their politics are popular under a large section of disenfranchised voters."
    n "Some voices speculate that they could even form a sincere challenge to the political establishment of our town."
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt serious day open with Dissolve(0.2)
    n "I want to kick off the campaign season with an extra thick edition of the Sunday Abbot, providing an overview of all contesting parties."
    a "Ex—extra thick?"
    "My shoulder still felt cramped from last Saturday."
    show ina shirt obsessed day open with Dissolve(0.5)
    n "I want in-depth interviews with the leading candidates of every party."
    n "I can interview the town mayor, and the smaller opposition leaders."
    n "But I'd like {i}you{/i} to interview Marisa."
    "I swallowed."
    pause(0.5)
    a "An interview? Me—?"
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt obsessed day open with Dissolve(0.2)
    n "Yeah, you. It sounds like you have one foot in the door with her already. We can't let an opportunity like this go to waste. "
    pause(0.5)
    #### MARISA/INA 2 ####
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        n "So, will you conduct this interview for me?"
        
        "Most definitely not!": #Mei? You saw us on Saturday? But 
            $ marisa_ina_score += 1
            show ina shirt happy day closed with Dissolve(0.2)
            show ina shirt happy day open with Dissolve(0.2)
            n "Oh, Abe — I love it when you defy me." 
            n "Please have the interview with Marisa on my desk by Friday." 
            show ina shirt happy day closed with Dissolve(0.2)
            show ina shirt happy day open with Dissolve(0.2)
            n "Otherwise you can say goodbye to your Saturday job."

            "Although I was tempted to call her bluff — I realized I was functionally redundant, now that Mei had joined the delivery team."
            "Meekly I acquiesced."
            show ina shirt happy day closed with Dissolve(0.2)
            show ina shirt happy day open with Dissolve(0.2)
            
        "Do I even have a choice?": 
            show ina shirt angry day open with Dissolve(0.5)
            n "You don't."
            n "But I find it important to grant you the illusion of control."
            n "Please have that interview on my desk by Friday." 
            show ina shirt serious day closed with Dissolve(0.2)
            show ina shirt angry day open with Dissolve(0.2)
    
    #### MARISA/INA 2 ####
        
    n "This is a large responsibility. Please don't disappoint me."
    
    show ina shirt serious day at center with easeinleft
    
    "Ina took place at her desk, ordering papers and humming to herself in a contented manner."
    "It appeared that my presence was no longer needed."
    
    "And I was already on my way to the door — my mind set on returning home before Ina could lay anymore unsolicited work on my shoulders — when a question sprang to mind."
    "I turned around."
    
    pause(0.5)
    
    #Hurriedly I left the office of the Sunday Abbot, 
    
    a "Hey Ina — I was wondering."
    a "Have you ever been on easter break?"
    show ina shirt worried day open with Dissolve(0.5)
    "Ina looked up from her paperwork. A gloomy expression forming in her eyes." #you may have used this a lot this chapter
    show ina shirt worried day closed with Dissolve(0.2)
    show ina shirt worried day open with Dissolve(0.2)
    n "Easter break—? "
    n "Why — are you {i}going{/i}?"
    pause(0.5)
    a "I—I'm not sure. Are you—?" #I was just wondering"
    show ina shirt angry day open with Dissolve(0.5)
    n "Easter break—? Me—?"
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)
    n "That's where the stuck-up types loaf around on the beach under the pretense of study—"
    n "I have absolutely — {i}definitely{/i} — no interest in being a part of that."

    pause(0.5)
    stop music fadeout 2.0
    hide ina with Dissolve(0.5)
    pause(0.5)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)

label p1c7:

    play sound "audio/officesound.ogg" loop fadein 5.0 

    scene bluehall with Dissolve(1.0)
    #show ina shirt angry book open at left with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)    
    play music "audio/mus_bachwtk20.ogg" loop fadein 5.0
    show rika uni mischievous day open at center with Dissolve(1)   
    pause(0.5)
    "Before I could even make it to the end of the corridor, I was cornered by Rika Kuyper." #rewrite
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)
    
    r "Abe, I'm so glad to run in to you. You're just the person I was looking for."
    pause(0.5)
    a "That {i}can't{/i} be true—"
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)
    r "Oh but it is. For I have something newsworthy to report."
    r "And for that reason I need — {i}a journalist.{/i}"
    
    "She stared up at me with pleading eyes — though I could detect a certain playfulness in her voice." #light playfullness
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)    
    r "Sometimes, involving the press is the only way to achieve true righteousness in this world."
    r "They don't call you guys the {i}fourth estate{/i} for nothing, do they?"
    
    pause(0.5)
    a "I really don't think I'm the right person for this—"
    a "—Ina's in her office, all leads can be submitted to her."
    show rika uni sad day open at center with Dissolve(0.5)
    "Her face fell."
    show rika uni sad day closed at center with Dissolve(0.2)
    show rika uni sad day open at center with Dissolve(0.2)
    r "Come on Abe, you know how Ina feels about me—"
    r "Please come with me for a bit, I want to show you something."
    pause(0.5)
    
    
    #### RIKA/MEI 2 ####
    
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        r "Will you spare me your time?"
        
        "Sure. Just for once.": #Mei? You saw us on Saturday? But 
            $ rika_mei_score += 1
            show rika uni mischievous day closed with Dissolve(0.5)
            r "Oh you have no idea how thankful I am."
            r "For this truly is a matter of the greatest importance."
            #r "And it will only cost you a minute What I want to show you is on the way home for you.""

        "I'm sorry, I have far too much homework to do.":
            show rika uni sad day closed with Dissolve(0.2)  
            show rika uni sad day open with Dissolve(0.2)       
            r "Oh but Abe. What I want to show you is on the way home for you."
            r "It won't even cost you a minute."
            show rika uni mischievous day closed with Dissolve(0.5)           
            r "Please follow me."
            
    #### RIKA/MEI 2 ####
    
    #a "I really—"
    #show rika uni happy day open at center with Dissolve(0.5)
    #r "Don't worry, it's on the way home for you. It'll only take a minute."
    pause(0.5)
    stop music fadeout 2.0
    hide rika with Dissolve(0.5)
    pause(0.5)
    "Begrudgingly I followed her. "
    
    pause(1)
    
    stop sound fadeout 1.0
    scene pathtrees with Dissolve(1.0)
    play sound "audio/cricketsafternoon.ogg" loop fadein 1.0
    pause(1)
    play music "audio/mus_bachwtk5.ogg" loop fadein 4.0 #keep other track?
    
    "Rika walked next to me in a confident pace, forcing me to increase my tempo to keep up with her."
    "And as we walked, she seemed thrilled with herself, grinning with a mysterious sense of anticipation."
    pause(0.5)
    "Though I'm not easily thrown off my game, her lingering silence made me the slightest bit uncomfortable." #to the point where I felt an urge to break the tension."
    
    #pause(0.5)
    show rika uni mischievous day open at center with Dissolve(1)
    pause(0.5)    
    a "So how did your service go, yesterday?"
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2) 
    "She moaned favorably."
    pause(0.5)
    a "No more lights that burnt out—?" #burning out?
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)    
    r "Preparation is key."
    r "No ritual can go without rehearsal."
    r "Ritual {i}is{/i} rehearsal, or so they say."
    "She shot me an inquisitive glance."
    pause(1)
    "We were walking down lightkeepers lane — a picturesque trail that led to the woodlands in the southeast."
    "Great plum trees rose up on both sides of the path, arching together into a canopy of green."
    pause(0.5)
    a "Rika—?"
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)      
    r "Yes—?"
    a "That thing you want to show me—"
    "I paused for a second, to catch my breath."
    pause(0.5)
    a "It isn't {i}really{/i} on the way home — is it?"
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)     
    r "She put a finger to her mouth."
    r "Oh quiet now — this is a shortcut."
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2) 
    r "Anyway, we're almost there."
    pause(0.5)
    hide rika with Dissolve(0.5)
    stop music fadeout 3.0
    "The lines of trees grew thicker, turning into a forest." #leading into
    
    pause(1)
    scene churchruins with Dissolve(1.0)
    pause(1)
    
    "And after a while the path gave way to a clearance, in the midst of which there lay a ruin."
    pause(0.5)
    play music "audio/mus_bachwtk12.ogg" loop fadein 4.0
    show rika uni sad day open at Position(xpos=0.7, xanchor=0.5) with Dissolve(1.0)
    pause(0.5)
    r "{i}Vanity of vanity — all is vanity.{/i}"
    r "There it lies, what remains of our old church. "
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "As you can see, many stones have been taken away and repurposed."
    r "And these ruins wither under the force of the elements, stones crumbling—"
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)    
    r "Currently we're standing at the place where the graveyard used to be, before the graveyard relocation project took place."
    
    r "In the past, the sea came up just a few yards from where we're standing. But after the reclamation of the surrounding land, the water slowly disappeared."
    
    #r "Some of the headstones that had been swept up by the ocean could even be retrieved, after the sea fell dry. " #improve
    #r "They had been buried under fathoms of mud."
    
    #
    #And then of course, there were the skeletons."
    #Her lips curled into an impish smile.
    
    #"By that time, the graveyard relocation project had already come to an end."
    
    #One by one the graves that once stood here had been exhumed and the remains of the dead were carefully placed inside a casket, to be transported together with its gravestone.
    
    "In the fickle daylight I gazed upon the desolated church, as it cast its lengthening shadows over the mossy forest floor."
    
    show rika uni happy day open with Dissolve(0.2)
    
    r "Proper burial is of such pivotal importance to our faith."
    r "For those who sleep in the dust of the earth will awake one day — some to everlasting life."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "We believe, upon the second coming of our lord and savior, that burial forms a prerequisite for entrance into the kingdom of heaven."
    
    #"I felt a shiver down my spine."
    
    #When the bones were reburied beneath the new church, a short funeral service was held.
    
    #
    #ause(0.5)
    
    #a "Say, Rika, I find this all very interesting—"
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "But let me get to the point."
    
    #One by one the graves that once stood here had been exhumed and the remains of the dead were carefully placed inside a casket, to be transported together with it's gravestone.
    
    r "Over the course of the centuries, three-hundred-twenty-six headstones were transported to the new church's crypt."
    r "And three-hundred-twenty-six caskets were buried underneath."
    
    show rika uni sad day open at Position(xpos=0.25, xanchor=0.5) with easeinright
    
    r "The thing is, not all of these caskets held our dead." #effect?
    
    #SFX
    #a "I jumped." #stirred, twitched
    pause(0.5)
    a "Are you saying some of the graves were empty?"
    
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "Empty, yes, or even worse — they held the remains of those unhallowed." #meh
    
    r "It happened at the beginning of the previous century." #at the begin
    
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    
    r "In 1934 the islanders were close to exhuming the last of the old graves. "
    r "Only forty headstones remained, and a large concerted effort was undertaken to complete the remaining work and close the old graveyard for good." #before the sea consumed the remaining land
    
    
    stop sound fadeout 2.0
    scene beach_bw 
    show rika uni sad day open at Position(xpos=0.25, xanchor=0.5)
    with Dissolve(2.0)
    play sound "audio/sealapping.ogg" loop fadein 2.0
    
    r "It was during these days that an esteemed scientist visited our island."
    show bulwer at Position(xpos=0.86, xanchor=0.5) behind rika with Dissolve(1)
    r "Doctor Bram Bulwer, chairholder at the department of Forensic Anthropology at Leiden University. "
    
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    
    r "Bram's intentions were rather sinister. He seemed interested in creating an anatomical archetype of the inhabitants of the isle of Abbot. "
    r "Among the nations elites, many prejudices existed against our people."    
    
    r "Considering how isolated our community was, we were an interesting case study — genetically speaking."
   
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    
    r "But back then, the islanders were clueless of the doctor's true intentions, and like we've always done with guests, we welcomed him in our midst and provided him with hospitality."

    show rika uni happy day open with Dissolve(0.5)
    
    r "Bulwer did a lot of important work in our community — providing medical checkups to the elderly, and administering polio shots to schoolchildren."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "My grandmother still remembers how he came to their school, lining up the children by length and taking all their measurements. Their arms, their legs—"
    r "—their skulls."
    
    r "Bulwer wasn't questioned at the time, as people still held medical experts in high regard—"
    
    show rika uni sad day open with Dissolve(0.5)
    
    r "Until he began involving himself with the graveyard relocation project. "
    
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "Immediately upon his arrival, he offered to help with the exhumation of the graves. And during the first few days he spent his every spare hour helping the digging crew."
    
    r "But after some time this lead to uneasiness."
    
    r "On multiple occasions, the doctor was accused of treating the exhumed remains without proper regard."
    
    r "Taking skulls out of the graves, inspecting them, measuring them — treating them without the due reverence that should be observed during the handling of a deceased person."
    
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    
    r "It led to arguments, and the doctor agreed to cease his participation in the relocation project.  "
    
    r "But even after this incident, Bulwer was spotted near the old graveyard a few times, observing the workers and the empty graves. "
    
    #
    
    r "After four weeks, Bulwer departed for the mainland, never to return. And the islanders all but forgot about his mystifying presence."
    
    scene churchruins_twi
    show rika uni sad twi open at Position(xpos=0.25, xanchor=0.5)
    with Dissolve(2)
    
    "Rika's face grew dark."
    
    show rika uni sad twi closed with Dissolve(0.2)
    show rika uni sad twi open with Dissolve(0.2)
    
    r "Until—"
    pause(0.5)
    a "Until?"
    
    r "Until doctor Bulwer died, twenty years ago."
    r "After his death, his personal archive was made public. A routine move by the university."
    r "His writings shone a new light into his stay on the island."
    show rika uni sad twi closed with Dissolve(0.2)
    show rika uni sad twi open with Dissolve(0.2)    
    r "A notebook from 1937 makes mention of 'three Abbot skulls' that are in possession of the doctor. "
    r "That's the only time he mentions that term — 'three Abbot skulls'. Just as an aside. "
    show rika uni sad twi closed with Dissolve(0.2)
    show rika uni sad twi open with Dissolve(0.2)
    r "And it can only be speculated what exactly took place."
    r "But I — and many on the island with me — suspect that Bulwer must have snuck out one dark night, exhumed three graves, and replaced three of our skulls with other specimen from his undoubtedly vast collection."
    r "Before carefully resealing the graves."
    
    r "Thus leaving him in possession of three exceedingly rare skulls from the eccentric population of Abbot."
    pause(0.5)
    a "Are you saying the doctor went through all that trouble to steal some old bones? "
    
    show rika uni sad twi closed with Dissolve(0.2)
    show rika uni sad twi open with Dissolve(0.2)
    r "He did — he stole the remains of our ancestors. To display them in a cabinet, as some kind of exotic curio."
    
    r "We must return these remains, the Abbot skulls, so that we can bury them in our native soil. "
    r "These people, these poor souls, they have the right to a Christian burial. This is of fundamental religious importance to us."
    
    #reason he kept them secret was because they were so deformed
    
    "I looked at her uncomprehendingly."
    
    show rika uni mischievous twi open with Dissolve(0.5)
    
    r "Oh you may find my obsession morbid, but these bones tell the story of our people."
    r "Each of my ancestors has been buried on this island — far back into the dark ages."
    show rika uni mischievous twi closed with Dissolve(0.2)
    show rika uni mischievous twi open with Dissolve(0.2)
    r "It's a humbling thought, to have them all in one place."
    r "To know that I will, one day, lie among them — in the depths of the earth, protected by a sheltering church and a mighty God that rules from above."
    
    "Rika's eyes shone in an exalted glare — and I realized she could continue preaching like this for hours."
    show rika uni mischievous twi closed with Dissolve(0.2)
    show rika uni mischievous twi open with Dissolve(0.2)
    a "Listen Rika, I'm running late."
    a "Maybe we could continue this conversation at a later—"
    
    show rika uni mischievous twi closed with Dissolve(0.2)
    show rika uni mischievous twi open with Dissolve(0.2)
    
    r "It's okay. I'm done."
    r "All I want to ask you—"
    
    r "You see."
    show rika uni sad twi open with Dissolve(0.5)
    r "After Bulwer's archives were published, we petitioned the university to return the skulls."
    r "But they only sent us a short reply — explaining that no record existed of skulls from Abbot, and that their mention in the notebook was likely an error."
    r "After that, all our further pleas went unanswered."

    show rika uni happy twi open with Dissolve(0.5)
    r "We need someone — someone with journalistic inlets — to look further into this case."
    r "To do due research. To find out everything there is to know about these relics, and to publicize the whole dark matter — so that the university will be forced to reveal the {i}skeletons in its closet.{/i}"
    
    # TODO: add passage where they walk home through the tulip fields (this is a shortcut, according to Rika) 
    #rika can explain a little more, maybe cite: From the depths we call to you, o lord.
    
    "She looked up, at the setting sun."
    show rika uni happy twi closed with Dissolve(0.2)
    show rika uni happy twi open with Dissolve(0.2)
    r "I apologize, Abe. It's growing late and I've led you astray."
    a "I'm beginning to realize this really wasn't much of a shortcut." #too much
    show rika uni happy twi closed with Dissolve(0.2)
    show rika uni happy twi open with Dissolve(0.2)
    r "It wasn't — was it?"
    r "But I know a quicker way back to town, that leads through the fields."
    r "I promise we'll have you home before sundown."
    stop music fadeout 3.0

    pause(0.5)
    
    hide rika with Dissolve(0.5)
    pause(0.5)

    scene woodpath_twi with Dissolve(1) #better img
    pause(0.5)
    "She took me down a bicycle path that led out of the woods."
    pause(1)
    "Within a few minutes, we came upon a little used trail that ran through the tulip fields."
    
    pause(0.5)
    window hide
    stop sound fadeout 1.0
    pause(1)
    #scene tulips with fade
    
    scene tulips16 with Dissolve(1.0):
        subpixel True
        xalign 1.0 yalign 1.0
        easein 10.0 xalign 0.0 yalign 0.0
    #pause(1)
    
    play sound "audio/summernight.ogg" loop fadein 1.0
    pause(1)
    window show
    pause(0.5)
    
    a "We {i}have{/i} picked the season—"
    
    pause(1)
    play music "audio/mus_bachwtk18.ogg" loop fadein 5.0
    show rika uni happy twi open at Position(xpos=0.45, xanchor=0.5) with Dissolve(1)
    pause(1)
    
    r "Pretty, aren't they—?"
    r "In a few days, these flowers will be harvested and flown in cooled crates to places all across the globe."
    pause(0.5)
    "She pointed towards a purple spotted flower."
    show rika uni happy twi closed with Dissolve(0.2)
    show rika uni happy twi open with Dissolve(0.2)    
    r "Just imagine — this poor thing could be wilting in a vase in Beijing by the end of the week."
    show rika uni sad twi open with Dissolve(0.5)

    r "To think that something of such beauty would await such a cruel fate."
    show rika uni sad twi closed with Dissolve(0.2)
    show rika uni sad twi open with Dissolve(0.2)
    r "But eventually that is the path of all things radiant."

    r "It just shows that we truly live in a fallen creation — that groans under the consequences of our sin."
    r "{i}Vanity of vanity — all is vanity.{/i}"
    #show rika uni sad day closed at center with Dissolve(0.2)
    #show rika uni sad day open at center with Dissolve(0.2)
    pause(0.5)
    "She sighed."
    show rika uni sad twi closed with Dissolve(0.2)
    show rika uni sad twi open with Dissolve(0.2)
    r "At least the farmers can harvest gold."
    r "A batch of these tulips will fetch a small fortune at auction. "
    r "And come May, the land is plowed and wheat is sown, and the cycle goes on as usual." #later Ina can refer to the tulip harvest."
    #bring up easter break. 
    #bring up interview? Mention father's name.
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    stop music fadeout 2.0
    #hide ina with Dissolve(0.5)
    #hide rika with Dissolve(0.5)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(2)

label p1c8:

    play sound "audio/extractor.ogg" loop fadein 5.0 #we need more indoor sounds beside clock
    #play music "audio/mus_lotusland.ogg" loop fadein 2.0 #was poucet
    scene blueroom with Dissolve(3.0)
    #show ina shirt angry book open at left with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)
    
    "Wednesday morning."
    pause(0.5)
    "I just remembered the interview I'd been asked to conduct with Marisa — the scatterbrained girl that I'd met last Saturday. "
    "With our deadline approaching rapidly, I pondered what my next move should be."
    "Ina couldn't expect me — realistically — to produce a quality interview on such a short notice. "
    "And where to start? I didn't even have her phone number."
    "I was certain that if I'd just show up at her door, out of the blue, she'd be sure to reject me—"
    pause(1)
    "I pondered the thought for a second."
    pause(1)
    "{i}A rejection—!{/i}"
    "That was what I needed!"
    pause(0.5)
    "If could simply tell Ina that Marisa had refused to grant me an interview, I'd be free from my obligations."
    "After all — {i}no means no{/i}."
    "And then Ina would be able to interrogate her herself on a later date."
    
    pause(0.5)
    stop sound fadeout 1.0
    scene corridor with Dissolve(1.0) #hallway?
    pause(0.5)
    
    "Driven by these motivations — and without any prior preparation — I found myself knocking on the door of Marisa's apartment."
    
    #scene marisaroom with Dissolve(1.)
    #TODO maybe he's using the intercom, or she's out in the hallway
    pause(0.5)
    play music "audio/mus_vnconfession.ogg" loop fadein 8.0
    show mari skirt normal day open at center with Dissolve(1)    
    pause(0.5)
    s "An interview—?"
    a "Yes, for our paper. It shouldn't take more than a few hours of your time — but I understand if you're busy."
    show mari skirt smile day open at center with Dissolve(0.5)    
    s "Busy—? Not at all!"
    show mari skirt smile day closed at center with Dissolve(0.2) 
    show mari skirt smile day open at center with Dissolve(0.2)     
    s "You've caught me a little off guard, but I'd love to give an interview."
    show mari skirt smile day closed at center with Dissolve(0.2) 
    show mari skirt smile day open at center with Dissolve(0.2)      
    "A sinking feeling took hold of me."
    
    s "You must have heard about my appointment as the new leading candidate for Flock 05."
    s "I'm so sorry I couldn't tell you last time we met. I was under strict orders to keep it a secret until our press release went out on Sunday night."
    s "And now you want to conduct an interview? A real interview?! With me?!"
    "She was beaming. "
    show mari skirt smile day closed at center with Dissolve(0.2) 
    show mari skirt smile day open at center with Dissolve(0.2)  
    s "Oh this is all so exciting. "
    s "I was becoming a little disappointed, you know?"
    s "You're the first local press outlet to show interest in my new position."
    pause(0.5)
    a "We're the {i}only{/i} local press outlet—"
    show mari skirt smile day closed at center with Dissolve(0.2) 
    show mari skirt smile day open at center with Dissolve(0.2)  
    s "I want to tell you everything about our movement."
    show mari skirt normal day open at center with Dissolve(0.5)       
    s "But — um. I was actually in the middle of something. My apartment is a mess."
    s "Please meet me in the café across the street in fifteen minutes. We'll conduct the interview there."
    pause(0.5)
    hide mari with Dissolve(0.5)
    stop music fadeout 3.0
    
    pause(0.5)
    window hide
    pause(0.5)
    stop sound fadeout 1.0
    scene black with Dissolve(1.0)
    scene ristorante with Dissolve(1.0)
    play sound "audio/officesound.ogg" fadein 1.0 loop
    play music "audio/mus_terraemotus.ogg" loop fadein 5.0
    pause(1)
    window show
    pause(0.5)
    "As I sat in the empty cafe, tenderly sipping a triple ristretto, a thousand thoughts passed through my mind." #ristretto may be too hip for abbotsford"
    "Part of me was ready to escape while it was still possible — hastily scribbling an excuse note on a piece of paper before winging it out the door."
    "But simultaneously I found myself making up potential interview questions, as a fickle attempt to alleviate the very worst outcome."
    "Because I realized I probably wouldn't have the nerve to escape — that I would remain sitting here, caught like a deer in headlights, counting down the seconds until my inescapable demise."
    
    pause(1)
    #
    
    "{i}And there she was.{/i}"
    "As I watched her approaching, through the window, I noticed something luminous in her appearance, that I hadn't detected back when I saw her in the hallway." #did he see her?
    #"It wasn't until she sat down before me that I realized she'd put on make-up."
    
    pause(1)
    show mari corset smile day open at center with Dissolve(0.5)    
    pause(1)
    s "This is a great place, isn't it?"
    show mari corset smile day closed at center with Dissolve(0.2)
    show mari corset smile day open at center with Dissolve(0.2)
    s "So close by."
    pause(0.5)
    a "Easy to find your way home from—"
    
    #a "So, how have you been doing? Have you been able to find your way home?" #meh
    show mari corset smile day closed at center with Dissolve(0.2)
    show mari corset smile day open at center with Dissolve(0.2)
    s "Don't tease me, I've been doing a lot better."
    s "I bought a map, you know—"
    
    show mari corset normal day open at center with Dissolve(0.5)
    
    s "Anyway, I'm very glad you're willing to talk to me."
    s "Though some national papers ran our press release, you're the first journalist to show interest in our actual story."
    show mari corset normal day closed at center with Dissolve(0.2)
    show mari corset normal day open at center with Dissolve(0.2)
    s "But please go easy on me today, you should know I've only been instated recently. "
    pause(0.5)
    a "That's right. I heard there was an issue with your predecessor—"
    show mari corset normal day closed at center with Dissolve(0.2)
    show mari corset normal day open at center with Dissolve(0.2)
    s "My predecessor, Jurgen— "

    show mari corset blush day open at center with Dissolve(0.5)
    "She blushed." #TODO blush
    show mari corset blush day closed at center with Dissolve(0.2)
    show mari corset blush day open at center with Dissolve(0.2)
    s "Let's not talk about him at all. I believe the gutter press have uncovered all of his shady dealings."
    show mari corset serious day open at center with Dissolve(0.5)
    "She lowered her voice."
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)
    s "New political parties attract all kinds of, um— types, you know?"
    s "When you're building up a movement, it isn't always possible to separate the wheat from the chaff."
    s "But I think we've left these days behind. I want us to look towards the future, not the past. "
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)
    s "We've dealt with Jurgen in a responsible manner — and now we're ready to turn the page. "
    s "You can quote me on that, verbatim. Are you taking notes?"
    pause(0.5)
    a "Um, yeah—"
    "Hastily I produced a notebook from my bag."
    #pause(0.5)
    
    "I was trying to recall some of the questions that I had prepared before Marisa's entry — none of which I'd thought to write down."
    pause(0.5)
    a "So, em— Could you tell me something about your goals as a leader?"
    "I mean— What would you do if you were elected? "
    show mari corset normal day open at center with Dissolve(0.5)    
    "She shuffled anxiously."
    show mari corset normal day closed at center with Dissolve(0.2)
    show mari corset normal day open at center with Dissolve(0.2)
    s "Well, that's the real question, isn't it—"
    "She thought long and hard."
    pause(1)
    show mari corset normal day closed at center with Dissolve(0.2)
    show mari corset normal day open at center with Dissolve(0.2)    
    s "Flock 05 wants to bring balance and safety."
    s "Many things have become unbalanced in our town. "
    s "A.I.R. — Abbotsford's largest political party — has ruled continuously for the past sixty years."
    s "And though they seem like an obvious choice for those seeking stability, we believe their sole rulership has caused a steady decline."

    show mari corset serious day open at center with Dissolve(0.5)   
    s "Nothing immediate or life threatening — but small things."
    s "Like the social cohesion in our town, the sense of safety on the streets, rising corruption."
    s "Many values that were once commonplace, have all but disappeared. "
    
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)       
    
    s "And because this disappearance was a gradual process, spanning many decades — it has passed many by."
    s "Until 2005, when a small group of concerned citizens joined forces against the rising tide. Working hard to provide a political alternative to the time-worn status quo."
    s "Even as an opposition party, Flock has been able to achieve so much for our community—"
    "She clasped her hands together forcefully."
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)        
    s "And now, we believe we're ready to take the lead."
    pause(0.5)
    a "These are fighting words for a new frontrunner—"

    show mari corset blush day open at center with Dissolve(0.5)
    s "D—does it really sound that way?"
    "She shuffled around nervously in her seat."
    show mari corset blush day closed at center with Dissolve(0.2)
    show mari corset blush day open at center with Dissolve(0.2)
    s "You can tone it down a little in the article—"
    show mari corset blush day closed at center with Dissolve(0.2)
    show mari corset blush day open at center with Dissolve(0.2)
    s "Please don't paint me in too bad a light."
    s "You may have heard people speak negatively about our movement. Stating that we are extremists of some kind. "
    s "But you must understand that there is nothing extreme about our goals."
    s "All we want is to live in a fair and safe society. Isn't that the most {i}moderate{/i} stance of all?"

    show mari corset smile day open at center with Dissolve(0.5)
    "She smiled a tender smile."
    show mari corset smile day closed at center with Dissolve(0.2)
    show mari corset smile day open at center with Dissolve(0.2)
    s "You know how it goes. Whenever you challenge the powers that be, they'll do anything to paint you in a bad light. "
    s "We've been called vandals, authoritarians, bullies. "
    
    s "But please realize, we're nothing like that."
    s "They call us names in order to cast doubt upon our intentions."
    pause(0.5)
    a "Politics can be horrible at times." #Abe says this"
    show mari corset smile day closed at center with Dissolve(0.2)
    show mari corset smile day open at center with Dissolve(0.2)
    s "Exactly! But it's a game — you see?"
    s "I need to be resilient."
    # TODO: is this the place for Hobbesian theorization?
    
    #
    #TODO scene toilets 
    stop music fadeout 4.0
    #
    
    #TODO meeting takes place in the toilets, change scene fittingly
    "A waitress came by to take Marisa's order. I got up to visit the restroom. "

    stop sound fadeout 3.0
    #hide mari with Dissolve(0.5)
    #pause(1)
    #"While we had been speaking, the café had slowly filled up. "
    #stop sound fadeout 1.0
    pause(1)
    
    scene toilets with Dissolve(0.5)
    play sound "audio/fridge.ogg" loop fadein 1.0
    pause(1)
    "And as I approached the washbasin to wash my hands, a young man brushed by me." 
    pause(0.5)
    "He turned around."
    pause(1)
    show bern coat serious day open at center with Dissolve(1)
    pause(0.5)
    b "How are the {i}madeleines{/i} here?"
    pause(0.5)
    a "The madeleines—?"
    a "I have no idea—"

    show bern coat smile day open at center with Dissolve(0.5)
    "He grinned playfully."
    show bern coat smile day closed at center with Dissolve(0.2)
    show bern coat smile day open at center with Dissolve(0.2)
    b "You {i}don't—?{/i}"
    pause(0.5)
    b "Having your doubts already?"
    
    pause(1)
    hide bern with Dissolve(0.5)
    pause(1)
    
    "And with these words he slipped through the door." #, sitting down at a table which was covered in newspapers." #improve
    pause(1)
    stop sound fadeout 1.0
    scene ristorante with Dissolve(1.0)
    play music "<from 60.0>audio/mus_terraemotus.ogg" loop fadein 6.0
    pause(1)
    show mari corset serious day open at center with Dissolve(0.5)
    pause(1)
    "When I returned to the common area, Marisa sat behind a steaming cup of latte."
    
    
    "She gestured towards the young man — who had seated himself at a nearby table, where he read his paper auspiciously."
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)
    s "Did that guy say anything to you?" #He left for the toilets just after you got up.
    
    "There was a hint of acrimony in her voice."
    pause(0.5)
    a "That guy? He asked me about the confectionery." #right term?
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)    
    s "The {i}confectionery?{/i}"
    s "That's strange, isn't it?"
    pause(0.5)    
    a "I don't know — it was just a question."
    "She pouted."
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)      
    s "He shouldn't be asking questions like that."
    

    show mari corset normal day open at center with Dissolve(0.5)
    s "Anyway, let us return to the interview."
    s "I was telling you about the core principals of our party."
    
    show mari corset normal day closed at center with Dissolve(0.2)
    show mari corset normal day open at center with Dissolve(0.2)
    s "At Flock we are realists. We do not delude ourselves with soothing fairy tales about human benevolence."
    
    "She had become serious, uttering her words clearly and without hesitation."
    "There was little that reminded me of the timid, forlorn girl that I'd led home last Saturday."
    

    show mari corset serious day open at center with Dissolve(0.5)
    
    s "We believe society constitutes no more than a thin veneer of civility, that hides away the true horrors of human nature."
    
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)
    s "This is a subject I've explored extensively during my studies."
    s "In the natural state — without rules and institutions to enforce peace — humans are in a constant condition of struggle. "
    s "We'd live in continual fear of violent death, our lives {i}solitary, poor, nasty, brutish, short—{/i}"
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)
    s "A good government needs to be fair and strong, to withhold man from its natural inclinations towards violence."
    s "And we, as Flock, are ready to take that position away from the current political elite — that has become the very embodiment of that which it vowed to protect us from."

    show mari corset normal day open at center with Dissolve(0.5)
    a "How many votes would you need to have a shot at winning the mayoral office?"
    "She pondered."
    show mari corset normal day closed at center with Dissolve(0.2)
    show mari corset normal day open at center with Dissolve(0.2)
    s "Hm— Quite a bit more than we currently have."
    s "And A.I.R. would have to lose some."

    show mari corset smile day open at center with Dissolve(0.5)
    "She smiled and spoke to me in a hushed voice."
    show mari corset smile day closed at center with Dissolve(0.2)
    show mari corset smile day open at center with Dissolve(0.2)
    s "But we have a {i}secret weapon.{/i}"
    s "An influential politician will be joining our party soon."
    s "To back me up, as my right hand man."
    
    show mari corset smile day closed at center with Dissolve(0.2)
    show mari corset smile day open at center with Dissolve(0.2)
    
    s "We should be able to release his name somewhere next week."
    s "But please hint at this news in your article. To create some suspense."
    s "I promise you, he's an established political figure."
    s "I believe his backing will truly push our movement into the lead—"
    play audio "audio/swipe.ogg"
    stop music fadeout 2.0
    show mari corset normal day open at center with Dissolve(0.2)
    "A stir beside us."
    pause(0.5)
    b "Sounds like you've been getting mixed up in sleazy circles again, {i}Madeleine—{/i}"
    "It was the young man, who had switched over to a table closer to ours."
    "Marisa's entire demeanor changed in an instant."

    show mari corset angry day open at center with Dissolve(0.2)
    s "You stay out of this!" #Who're you talking to?!"
    pause(0.5)
    play music "audio/mus_grieg14.ogg" loop fadein 3.0
    show bern coat smile day open at left 
    show mari corset angry day open at right 
    with easeinleft
    
    b "You haven't changed a bit, Madeleine. And it appears that you've found a new victim."
    show mari corset normal day open with Dissolve(0.2)
    "He leaned over to me."
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)
    b "Don't be fooled by her charm."
    b "You wouldn't be the first young man to succumb to her wiles."
    show mari corset normal day closed with Dissolve(0.2)
    show mari corset normal day open with Dissolve(0.2)
    s "Ignore him, Abe. Let's continue the interview."
    s "Bernard here is a terrible person. A bully."
    s "At university, he hung around with a band of low-lives."
    s "Wreaking havoc, causing trouble for students that actually tried to accomplish something in their lives."
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)    
    b "Accomplish something—? Like taking charge of an authoritarian movement—?" #like leading a
    show mari corset serious day open with Dissolve(0.5)
    s "Nonsense. Come on, he's ruining the interview."
    s "Let's go up to my apartment."
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)    
    b "Up to her apartment already?"
    b "You're a lost cause, young man."
    b "{i}Sic transient gloria mundi.{/i}"
    
    hide mari with Dissolve(0.5)

    "Fuming, Marisa pulled me out of the establishment"
    stop music fadeout 5.0
    pause(1)
    hide bern with Dissolve(0.5)
    pause(1)

    #hide ina with Dissolve(0.5)
    #hide rika with Dissolve(0.5)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)

label p1c9:

    play sound "audio/officesound.ogg" loop fadein 2.0 

    scene studio with Dissolve(1.0)
    #show ina shirt angry book open at left with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)
    play music "audio/mus_vnirretrievably.ogg" loop fadein 5.0  #maybe vnconfession
    show mari corset serious day open at center with Dissolve(0.2)
    
    
    "Marisa sighed."
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)
    s "Do you see what's happening? You can't even go for a quiet conversation without being harassed in this town."
    s "What a nuisance that Bernard is. I hope he goes away soon."
    s "He's probably visiting his dad, who lives down here. Poor man."
  
    "She clasped her hands together tenderly."
    pause(0.5)
    a "Anyway, I think I have enough material for a decent article. The piece should be out next Sunday, together with interviews with the other party leaders."
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)    
    s "Thank you for the interview."
    
    "She hesitated—"

    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)  
    s "Please don't paint me in too negative a light. As I said, our movement hasn't always been treated fairly by the press. "
    s "And it causes prejudices. Like these things Bernard said to me—"
    show mari corset smile day open at center with Dissolve(0.5)
    s "But I feel that you're a sincere reporter. Who would be willing to give us a chance."
    show mari corset smile day closed at center with Dissolve(0.2)
    show mari corset smile day open at center with Dissolve(0.2)
    s "If you treat us fairly, I may be able to help you—"
    show mari corset serious day open at center with Dissolve(0.5)    
    "She grew serious."
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)

    s "To help you — with a revelation."
    s "I know things, about the political elite in this town."
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)
    s "About the mayor."
    pause(0.5)
    a "Mayor {i}Van Linden?{/i} What do you know about him?"
    show mari corset serious day closed at center with Dissolve(0.2)
    show mari corset serious day open at center with Dissolve(0.2)
    s "It's too soon, I can't tell. But lets talk again."
    "She scribbled something down on a piece of paper."
    show mari corset smile day open at center with Dissolve(0.5)
    s "Here's my number, I'm sure we'll be in contact a lot during the campaign season."
    
    pause(1)
    hide mari with Dissolve(0.5)
    
    "We headed to the door."
    
    stop sound fadeout 1.0
    scene corridor with Dissolve(1.0) #TODO: make this straight?
    pause(0.5)

    show mari corset smile day open at center with Dissolve(0.5)
    pause(0.5)
    
    s "Oh yeah, I was wondering—"
    s "—are you going on the easter break outing?"
    pause(0.5)
    a "Easter break? How do you know about that—?"
    show mari corset smile day closed at center with Dissolve(0.2)
    show mari corset smile day open at center with Dissolve(0.2)
    s "Rika invited me, I thought it might be fun."
    a "Rika— You met Rika—? "
    show mari corset smile day closed at center with Dissolve(0.2)
    show mari corset smile day open at center with Dissolve(0.2)
    s "Yes, her father is in the town council, you know?"
    s "He's a politician for A.I.R. — but a respectable one."
    pause(0.5)
    a "Well that sounds like her — I think she's been inviting everyone."
    a "You should know easter break is mostly aimed at high-school students."
    show mari corset normal day open at center with Dissolve(0.2)
    "Her lip sank down sullenly."
    show mari corset normal day closed at center with Dissolve(0.2)
    show mari corset normal day open at center with Dissolve(0.2)
    s "You think so? I though it would be fun, as a relief from politics."
    
    s "How about you let me know if you decide to go. Then at least I'll have someone to talk to."
    s "You have my number."

    stop music fadeout 2.0
    hide mari with Dissolve(0.5)
    #hide rika with Dissolve(0.5)


    pause(0.5)
    window hide
    pause(1)
    stop sound fadeout 3.0
    scene black with Dissolve(3.0)
    pause(1)
    #####################################################################################################
    if rika_mei_score > 1:
        show prog_mika p at Position(xpos = 0.5, xanchor=0.5, ypos=0.3, yanchor=0.5) with easeinright
    elif rika_mei_score == 1:
        show prog_mika n at Position(xpos = 0.5, xanchor=0.5, ypos=0.3, yanchor=0.5) with easeinright
    else:
        show prog_mika d at Position(xpos = 0.5, xanchor=0.5, ypos=0.3, yanchor=0.5) with easeinright
        
    pause(0.25)
    
    if marisa_ina_score > 1:
        show prog_marina p at Position(xpos = 0.5, xanchor=0.5, ypos=0.7, yanchor=0.5) with easeinright
    elif marisa_ina_score == 1:
        show prog_marina n at Position(xpos = 0.5, xanchor=0.5, ypos=0.7, yanchor=0.5) with easeinright  
    else:
        show prog_marina d at Position(xpos = 0.5, xanchor=0.5, ypos=0.7, yanchor=0.5) with easeinright
        
    
    #####################################################################################################
    pause(2)
    hide prog_mika with easeoutleft
    pause(0.25)
    hide prog_marina with easeoutleft
    
    
    pause(1)
    ##PART 2 - title
    play sound "audio/edgemeadow.ogg" loop fadein 5.0
    scene white with Dissolve(1.0)
    pause(1)
    scene title2 with Dissolve(1.0)
    pause(2)
    scene white with Dissolve(1.0)





    #######################################################################
    #### PART 2 ###########################################################
    #######################################################################



label p2c1:


    #scene schoolroad with Dissolve(3.0)

    scene schoolroad16 with Dissolve(3.0):
        subpixel True
        xalign 1.0 yalign 1.0
        easein 15.0 xalign 0.0 yalign 0.0
    
    pause(1)
    window show    
    pause(1)
    
    "On Saturday, Mei and I took to our paper route the way we'd grown accustomed to."
    "Unlike last week, work proceeded with few distractions — and it was just after noon that I found myself heading back to school to drop off my leftover newspapers."
    
    #Suddenly I was approached by marquis Leopold."
    pause(0.5)
    scene leopoldhouse with Dissolve(1.0)
    play music "audio/mus_grieg25.ogg" loop fadein 6.0
    pause(0.5)
    l "Good afternoon, Abe. Any news for me today?"
    
    show leo smile open at left with Dissolve(0.5)
    
    "I looked around to see marquis Leopold, coming down the street behind me."
    pause(0.5)
    a "Sure, we dropped it in your mailbox this morning. Haven't you found it yet?"
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)
    
    l "You have—? My mistake."
    l "I haven't been home all day, you see?"
    pause(0.5)
    a "Well, it should be in there. "
    a "I'd go read it if I were you. It's a special edition to mark the start of the campaign season."
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)    
    l "Ah, that's exactly the kind of news I subscribed for—"
    l "—not that nonsense about dying insects."
    pause(0.5)
    hide leo with Dissolve(0.5)
    pause(0.5)
    "Leopold headed over to his mailbox."
    #show leo smile closed with Dissolve(0.2)
    pause(0.5)
    show leo smile open at left  
    show document at Position(xpos=0.26, xanchor=0.5)
    with Dissolve(0.5)
    pause(0.5)
    l "That's a nice picture of Marisa you have on the front page."
    pause(0.5)
    a "You like her? She's the main rival to your party this year."
    show leo laughing open with Dissolve(0.5)
    "Leopold grinned."
    show leo laughing closed with Dissolve(0.2)
    show leo laughing open with Dissolve(0.2)
    l "My party."
    l "I agree that A.I.R. was once my party."
    pause(0.5)
    a "Are you still torn up about your low placement on the electoral list?"
    show leo laughing closed with Dissolve(0.2)
    show leo laughing open with Dissolve(0.2)    
    l "{i}Et tu, Brute?{/i}"
    show leo serious open with Dissolve(0.5)
    "He sighed."
    show leo serious closed with Dissolve(0.2)
    show leo serious open with Dissolve(0.2)
    #My term in A.I.R. has been a heavy one. I had one lousy little scandal, when that journalist photographed me in a nightclub.
    #I though it were two scandals.
    #Whatever — the thing is, you know these puritans in there will never let me live it down.
    #They published their electoral list last thursday, you know on what position they placed me?
    #I shook my head.
    #Fifteenth.
    #He paused for a second, to let the words sink in.
    #Fifteenth place. It's a direct insult, you see? As the Abbotsford city council only has fourteen seats in total. "
    #And to 
    
    l "They have betrayed me — ended my political career. "
    l "You get in one little scandal, and this is what they do to you. "
    pause(0.5)
    a "A.I.R. does claim to be a Christian party, you know—" #I guess
    show leo serious closed with Dissolve(0.2)
    show leo serious open with Dissolve(0.2)    
    l "To hell they are — these damn puritans will never let me live it down."
    
    #l "It's such an insult."
    l "They should have taken the honorable path and just thrown me out—"
    l "—but to avoid commotion and to humiliate me even further, they placed me on a unelectable position."
        
    "He glanced over Marisa's image again."
    show leo smile open with Dissolve(0.5)
    l "But I feel that I may still have a part to play." #part hasn't been played
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)
    
    l "I've been in talks with the leadership of Flock 05 over the past few weeks."
    l "And this morning, they've agreed to let me grace the second place on the ballot for their party these upcoming elections." #in onderhandeling
    a "You—? Second place for Flock? That's quite a switch—"
    show leo smile closed with Dissolve(0.2)
    show leo smile open with Dissolve(0.2)    
    
    l "An official press release will go out tomorrow evening, so please keep this between the two of us for now."
    l "But I reckon — with my experience and Marisa's charisma — we'll be able to elevate this shady club into a true political juggernaut." #club? confederacy?
    l "A.I.R. will regret double crossing me. Just mark my words."
    
    #
    pause(0.5)
    "Suddenly Bernard appeared in the doorway of Leopold's house."
    #"And when it emerged into the afternoon sun, I realized that it was Bernard." #meh
    #sound to my right, and to my surprise I turned round to see Bernard in the doorway."
    #pause(0.5)
    "Initially he made a disgruntled impression — but the second he recognized me, his spirits appeared to lift."
    pause(0.5)
    show bern coat embarassed day closed at Position(xpos=0.75,xanchor=0.5, ypos=0.52, yanchor=0.5) with Dissolve(0.5)
    pause(0.5)
    b "Hi Abe! Is that bed-wetting old grandpa bothering you?"
    "Leopold chuckled."
    show leo smile closed with Dissolve(0.5)
    l "I see you've met my deadbeat son?"
    l "He receives free food and board — and this is how he thanks me." #speaks of me
    show bern coat embarassed day closed with Dissolve(0.2)
    show bern coat embarassed day open with Dissolve(0.2)
    #"Bernard joined us." #already joined us
    
    show bern coat smile day open with Dissolve(0.2)
    b "You need to support your poor son a little, now that he's standing on his own two feet."
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)
    b "Or am I interfering with your illicit dealings."
    show leo laughing open with Dissolve(0.5)    
    l "Nothing here is illicit—"
    show leo laughing wink with Dissolve(0.2)
    show leo laughing open with Dissolve(0.2)
    "With a wink, Leopold excused himself — although I could tell he was irked by Bernard's banter."
    pause(0.5)   
    hide leo 
    hide document
    with Dissolve(0.5)
    
    pause(1)
    "I turned to Bernard."
    show bern coat smile day open at Position(xpos=0.5,xanchor=0.5, ypos=0.52, yanchor=0.5) with easeinright    

    
    a "Congratulations on finishing university—"
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)
    b "I haven't exactly finished university—"
    show bern coat think day open with Dissolve(0.5)
    b "—although you could say I'm {i}finished{/i} with university."
    pause(0.5)
    "He was staring after his father — who carefully moved his way up the stairs to the house, the Sunday Abbot clasped flimsily under his arm."
    show bern coat think day closed with Dissolve(0.2)
    show bern coat think day open with Dissolve(0.2)
    b "Pathetic—"
    b "He's got a penchant for trouble, that man."
    pause(0.5)
    "Bernard sighed."
    show bern coat think day closed with Dissolve(0.2)
    show bern coat think day open with Dissolve(0.2)
    b "I always thought local politics would be an outlet for him — a harmless way to keep him occupied."
    b "But it appears he can't stop embarrassing himself."
    show bern coat smile day open with vpunch
    "Suddenly Bernard grabbed me by the arm, jovially."
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)
    b "I apologize, young man. I didn't really have the chance to introduce myself to you when we met last Thursday—"
    b "—although I'm sure {i}Madeleine{/i} has filled you in."
    pause(0.5)
    a "You studied with her in Bremersberg?"
    show bern coat serious day open with Dissolve(0.5)
    b "Sure. In different faculties though — I mostly dabbled in German Literature, some Theater—"
    show bern coat serious day closed with Dissolve(0.2)
    show bern coat serious day open with Dissolve(0.2)
    b "I wrote my last essay on {i}Almansor.{/i}"
    b "You wouldn't be partial to the works of Heinrich Heine, would you?" #refer to lorelei and almansor"
    
    #, some forays into Sociology and Anthropology— #getting annoying?"
    #better segue?"
    
    "I shook my head."
    pause(0.5)
    "I was reminded of something that Rika had asked me."
    pause(0.5)
    a "Hey Bernard, while you were studying, did you ever come across the department of Forensic Anthropology?"
    show bern coat serious day closed with Dissolve(0.2)
    show bern coat serious day open with Dissolve(0.2)    
    b "Anthropology? I hope you don't want to measure my \njaw-alignment—"
    pause(0.5)
    a "No, it's nothing like that."
    a "A friend of me is very interested in skulls — for some reason. "
    a "She will graduate high school this year, and wants to study Anthropology. Preferably at Leiden University, if I'm not mistaken."
    show bern coat serious day closed with Dissolve(0.2)
    show bern coat serious day open with Dissolve(0.2)      
    b "Leiden. That's prestigious—"
    b "They have a good Anthropology department there."
    show bern coat smile day open with Dissolve(0.5)
    b "Pretty girls, also—" #the girls here are weird"
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)
    b "One of their professors is actually teaching a guest course at Bremersberg University at the moment. Peter Helsing, I believe his name is. "
    b "He drives down there once a week. You should ask to speak to him. "
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)
    b "I hear it's a very popular course, although I was never that interested."
    pause(0.5)
    b "I rather concern myself with the living." #matters of the living
    pause(0.5)
        
    stop music fadeout 2.0
    hide bern with Dissolve(0.5)
    pause(0.5)
    #hide rika with Dissolve(0.5)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)

label p2c2:

    play sound "audio/officesound.ogg" loop fadein 5.0 
    scene office with Dissolve(1.0)
    #show ina shirt angry book open at left with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)
    
    
    "Monday. Ina's office."
    pause(1)
    play music "audio/mus_ravelmenuet.ogg" loop fadein 6.0
    show ina shirt worried day open at Position(xpos=0.4,xanchor=0.5) with Dissolve(1)
    pause(1)
    n "I was impressed with your interview."
    #"She appeared reluctant to admit it."


    show ina shirt worried day shut with Dissolve(0.2)
    show ina shirt worried day open with Dissolve(0.2)
    n "We got a call from a the {i}Evening Mirror{/i}, a national newspaper, to co-opt the article in their Wednesday issue."
    n "Marisa's presence appears to have stirred a broader interest in the town council elections."
    pause(0.5)
    a "Are you saying my interview will be distributed nationwide? "
    show ina shirt angry day open with Dissolve(0.5)
    "She scowled."
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)
    n "It's not just {i}your{/i} interview, they'll be publishing excerpts from mine as well—"
    
    show ina shirt happy day open with Dissolve(0.5)
    
    
    n "And hey—"
    n "Considering how you seem to have a great entry with Flock 05—"
    "Her tone had become friendlier."
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt happy day open with Dissolve(0.2)    
    n "—I was wondering if you'd consider covering their entire campaign." #wondering wondering
    pause(0.5)
    a "Huh—? What do you mean?"
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt happy day open with Dissolve(0.2)
    n "That you'd serve as a dedicated reporter."
    n "If you do Flock, I'll do the other parties." #That way the load will be distributed evenly."
    n "I mean — your chemistry with Marisa, we can't let that go to waste."
    pause(0.5)
    #a "I'm not sure if you could call it {i}chemistry—{/i}" #should?
    
    #### MARISA/INA 3 ####
    
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        n "Can I count on you for this?"
        
        "Cover their entire campaign? But we have finals coming up—":
            show ina shirt angry day open with Dissolve(0.5)
            n "Hmpf."
            pause(0.5)
            "I was taken aback. Though Ina had asked me to fill in on previous occasions — whenever she was in a pinch — I'd never been this involved in the editorial proceedings of the paper."
            show ina shirt serious day closed with Dissolve(0.2)
            show ina shirt angry day open with Dissolve(0.2)
            n "I'm sure you'll manage."
            n "I think this will be a great way to take your mind of studying now and again."
            pause(0.5)
            a "Taking my mind {i}off{/i} studying isn't exactly the problem—"
            show ina shirt serious day closed with Dissolve(0.2)
            show ina shirt angry day open with Dissolve(0.2)            
            "She shrugged."
        
        "You can count on me.": #Mei? You saw us on Saturday? But 
            $ marisa_ina_score += 1
            show ina shirt happy day closed with Dissolve(0.2)
            show ina shirt happy day open with Dissolve(0.2)
            "Ina smiled."
            n "After summer, we will both be star reporters."
            
    #### MARISA/INA 3 ####

    
    pause(0.5)
    a "But I wonder if there will even be anything worth writing about."
    a "Do you think Marisa's party could truly gain a foothold in our town?"

    show ina shirt serious day open with Dissolve(0.5)
    #"She became serious."
    n "I'm not sure."
    n "A.I.R. has always held an absolute majority in the town council, and the people here are generally steadfast."
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt serious day open with Dissolve(0.2)
    n "But times are changing. A party like Flock can build up support by challenging the status quo." #more
    #some history of Flock"
    
    n "And to a certain extent, we can't blame the voters. When there's nothing to choose, a political elite will become arrogant, lazy, corrupt."
    n "Then, as soon as an alternative raises its head, people welcome it, under the assumption that any change is good change."
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt serious day open with Dissolve(0.2)
    n "But will the rise of Flock 05 truly bring about {i}good{/i} change—?"
    n "Only time can tell."
    n "Especially now that they're under new leadership—"
    n "If only we could get to know Marisa — from really up close."#foreshadow decision to go on trip."
    
    
    #Ina delves into authoritarianism" TODO: could me more, more authpers.
    
    #
    #pause(0.5)
    show ina shirt happy day open with Dissolve(0.5)
    "Then she grinned, as though she'd just remembered something."
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt happy day open with Dissolve(0.2)
    n "Moreover, something interesting has happened. It appears Flock has attracted a new candidate."
    pause(0.5)
    a "Oh yeah, Leopold—"
    show ina shirt scared day open with Dissolve(0.5)
    "Her eyes widened in amazement."
    
    show ina shirt worried day closed with Dissolve(0.2)
    show ina shirt scared day open with Dissolve(0.2)
    n "You read the press release?! That's unlike you—"
    n "But you're right — it's Leopold."
    show ina shirt worried day closed with Dissolve(0.2)
    show ina shirt scared day open with Dissolve(0.2)  
    n "I guess it figures. The marquis was a bad fit for A.I.R."
    n "He's an unpredictable man — joining an unpredictable party."
    #stop music fadeout 3.0
 
    pause(1)
    stop sound fadeout 1.0
    hide ina with Dissolve(0.5)
    pause(0.5)
    scene school_front with Dissolve(1.0)
    play sound "audio/crowfield.ogg" loop fadein 1.0
    pause(1)
    
    "We went outside, and while I accompanied Ina to the bike shed, I recalled something that I wanted to tell her."
    
    show ina shirt serious day open at left with Dissolve(0.5)
    
    a "Ina. Before you go—"
    a "During the interview, Marisa hinted at something."
    a "She says she knows of some kind of scandal that involves the political elite of Abbotsford."
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt serious day open with Dissolve(0.2)
    n "Please tell me more."
    "It was clear I'd caught Ina's attention."
    pause(0.5)
    a "There isn't much more. Just that it's a well hidden secret, leading up all the way to the mayor."
    a "Marisa promised to elaborate further, if we were fair in our coverage of her party."
    
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt serious day open with Dissolve(0.2)
    n "Hmpf."
    n "You will need to get to the bottom of this."
    n "But please be cautious."
    n "This could be a political game Marisa is playing, in an attempt to damage her political opponents."
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt serious day open with Dissolve(0.2)
    n "We can't go around publishing unsubstantiated rumors. Make sure you get hard facts—"
    stop music fadeout 2.0
    
    #pause(0.5)
    
    "At that moment, a cloud of ebony hair descended upon us — Ina stopped speaking immediately." 
    pause(0.5)
    show rika uni mischievous day open at Position(xpos=0.7, xanchor=0.5) with Dissolve(1) 
    play music "audio/mus_bachwtk21.ogg" loop fadein 15.0
    pause(0.5)
    r "Abe, Ina— "
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)
    r "I apologize for disturbing what must have been a very important editorial meeting."
    
    "Ina eyed her up suspiciously."
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)
    r "But I have great news! We're very — {i}very!{/i} — close to reaching the participation threshold for easter break. " #participant threshold
    r "If the two of you could sign up now, the trip will be guaranteed to continue!"
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt serious day open with Dissolve(0.2)
    a "You're so close already—? I though you were struggling to find people to attend."
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)
    
    r "We were, but we've made great progress — two people signed up just yesterday."
    r "A rather strange looking young man—"
    show rika uni happy day open with Dissolve(0.5)    
    r "—and Marisa Roosevelt, the new girl in town."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2) 
    r "Have you met her?"
    show ina shirt curious day open with Dissolve(0.5)
    "I could see Ina tense up." #meh
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "Such a nice girl — she's really trying to fit in. "
    r "She even attended our church service yesterday, and now she's coming on easter break—"

    "Ina interrupted her."
    show ina shirt obsessed day open with Dissolve(0.5)

    n "Abe would like to buy a ticket!"
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt obsessed day open with Dissolve(0.2)    
    "I turned towards Ina, muttering at her under my breath — but she shot me a deathly glare."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)    
    r "Oh that's great Abe, thank you!"
    r "Let me hand you a ticket. Please be sure to pay me before coming Sunday."
    show rika uni mischievous day open with Dissolve(0.2)    
    r "This means I only have one more ticket left to sell. Hmm—"
    "Rika eyed Ina pressingly." #stared at
    #Ina shuffled uncomfortably—"

    show ina shirt worried day open with Dissolve(0.5)
    n "What—"
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)   
    r "Come on, Ina. You'll have a great time."
    r "You could write a report for the school paper."
    show ina shirt angry day open with Dissolve(0.5)
    "Ina begun shuffling uncomfortably." #nauseous. #begun?

    a "I think she'll take it—"
    #She was speaking with a feeble voice."
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)   
    r "Really—? Wonderful!"
    pause(0.5)
    "Meekly, Ina accepted the last ticket from an overjoyed Rika — before wandering off in silence." #disappearing
    
    #
    pause(0.5)
    hide ina with Dissolve(1)
    pause(0.5)
    
    show rika uni happy day closed at center with easeinright 
    pause(0.5)
    
    r "It's a big step for her. Ina hates joining in with social events."
    
    "I nodded."
    show rika uni happy day closed at center with Dissolve(0.2)
    show rika uni happy day open at center with Dissolve(0.2)
    r "But I'm sure she'll have a great time."
    r "Once she feels the warm sand against her skin, all reservations will melt off her like ice."
    show rika uni happy day closed at center with Dissolve(0.2)
    show rika uni happy day open at center with Dissolve(0.2)    
    r "{i}Do not cast away your confidence, which has great reward—{/i}"
    pause(0.5)
    "A silence fell."
    show rika uni sad day open at center with Dissolve(0.5)
    r "So Abe, have you been able to look into the issue of the skulls?"
    show rika uni sad day closed at center with Dissolve(0.2)
    show rika uni sad day open at center with Dissolve(0.2)
    "I was caught completely off guard."
    pause(0.5)
    a "The skulls? I—"
    a "I have, I {i}have{/i} actually—"
    pause(0.5)
    a "At Bremersberg there is a lecturer who is connected to the department of Forensic Anthropology at Leiden University."
    pause(0.5)
    show rika uni sad day closed at center with Dissolve(0.2)
    show rika uni sad day open at center with Dissolve(0.2)    
    r "There is—?"
    pause(0.5)
    a "I think if we'd just talk to him, ask him politely, he may tell us more about the skulls."
    show rika uni mischievous day open at center with Dissolve(0.5)
    "Rika chuckled."
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)
    r "Ask him politely—? "
    r "Oh Abe, sometimes I feel as though you receive the world like a little child."
    r "But I'm glad you've put in the work. I'm truly grateful for that."
    r "It's worth a try."
    pause(0.5)
    "She began browsing through her calendar." #meh
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)
    r "Let's attempt to get in contact with this lecturer of yours, and make the trip to Bremersberg."
    r "I will call you to make further arrangements."
    stop music fadeout 2.0
    pause(0.5)
    hide rika with Dissolve(0.5)
    pause(0.5)
        
    stop music fadeout 2.0
    #hide ina with Dissolve(0.5)
    #hide rika with Dissolve(0.5)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)

label p2c3:

    play sound "audio/extractor.ogg" loop fadein 2.0 
    play music "audio/mus_bachrecorder.ogg" loop fadein 15.0 #was poucet
    scene blueroom_twi with Dissolve(1.0)
    #show ina shirt angry book open at left with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)
       
    
    #I figured I should finally start preparing for my exams. 
    "That evening, I sat in my room, staring at the stacks of unopened textbooks."
    "With all the extra work Ina had piled upon me, I reckoned there would be little time to get around to any real studying. "
    "Especially now that she'd signed me up for a four day trip I hadn't planned for."
    "Yeah — why {i}had{/i} she signed me up for that trip?"
    play audio "audio/dialing.ogg" fadein 1.0
    show ina_call with easeinbottom
    "I took out my phone."
    
    pause(1)
    
    n "Abe—? What's the matter?"
    pause(0.5)
    a "Why did you sign me up for easter break? I thought you hated these kinds of outings."
    pause(0.5)
    "An awkward guffaw resounded through the telephone."
    pause(0.5)
    n "I did, sure. But I changed my mind."
    n "Do you know what I was thinking?"
    n "I was thinking — a trip like this is a {i}godsend.{/i}"
    n "You'll be able to observe Marisa, day and night, for four days straight."
    n "You'll be able to get close and intimate—"
    n "—truly get inside her mind."
    pause(0.5)
    "I sighed."
    pause(0.5)
    a "At least we're in this together—"
    pause(0.5)
    n "Yeah, thanks for that—"
    pause(0.5)
    n "Anyway — if that's all, I have to go. I have editing to do."
    pause(0.5)

    "Ina hung up the phone."
    hide ina_call with easeoutbottom    
    "As always, ulterior motives were at play."
    "Ina expected me to mobilize my budding friendship with Marisa as a means to generate more headlines for her ailing newspaper."
    pause(0.5)    
    "And though I resigned myself to the prospect of going on the easter trip, I resolved not to let things get out of hand." #— considering I couldn't afford to lose my delivery job —
    
    pause(0.5)
    
    "Determined to spend the rest of the evening in a productive manner, I was in the process of opening my trigonometry textbook{nw}"
    play audio "audio/phonecall.ogg"
    extend " when my phone began to hum."
    
    show rika_call with easeinbottom
    
    #maybe move this conversation to before Ina call?"
    "When I picked up the call, Rika's voice rang out, tinnily."
    pause(0.5)
    r "Abe — there have been developments."
    r "I looked up that guy, Peter van Helsing. He teaches a lecture on Thursday afternoons."
    r "So I called the university explaining that we're high school students, interested in pursuing Cultural Anthropology next year."
    r "They told me to come to his lecture next Thursday, and that he'd talk to us afterwards."
    pause(0.5)
    
    #### RIKA/MEI 3 ####
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        r "A meeting with a real professor. Isn't that great?"
        
        "So are you going?": #Mei? You saw us on Saturday? But 
            #show rika uni sad day closed at left with Dissolve(0.5)
            "She laughed disdainfully."          
            r "We're {i}both{/i} going. We can walk to the station from school."
            
        "What time do we leave?": 
            $ rika_mei_score += 1
            "Rika let out an appreciative moan."
            pause(0.5)
            r "At three, after our last class has ended."
    
    #### RIKA/MEI 3 ####
    
    
    #a "So you're going?"

    
    pause(1)
    r "Also, I'm very excited that you'll be joining us on easter break." #coming on
    r "We were in a bit of pinch, as most senior students have come to regard the easter break outing as a waste of time." #overuse of pinch?
    r "But in reality, the trip is a great way to relax before finals, whilst also providing a chance to reiterate over the important parts of the curriculum."
    r "We will be staying at the rustic village of Ryebury, which lies on the lakeside."
    pause(0.5)
    "I detected an uncharacteristic excitement in her voice."
    r "My family owns an inn over there, which we're able to charter at a very good rate."
    # But we needed enough participants, to make it all worthwile—"
    
    r "Anyway, we're leaving Monday afternoon. Please don't be late—"
    stop music fadeout 6.0
    pause(0.5)
    "She terminated the call—"
    hide rika_call with easeoutbottom
    "And the room was filled with nothing else than the drone of our neighbors' extractor fan."
    pause(0.5)
    "Unopened textbooks stared at me."
    "Defeated, I crawled into bed."
    stop music fadeout 6.0 
    pause(1)
    window hide
    
    scene blueroom_nig with Dissolve(2.0)

    #hide ina with Dissolve(0.5)
    #hide rika with Dissolve(0.5)

    stop sound fadeout 1.0
    scene black with Dissolve(2.0)
    pause(1)

label p2c4:

    play sound "audio/officesound.ogg" loop fadein 5.0 

    scene bluehall with Dissolve(2.0)
    window show    
    pause(1)
    play music "audio/mus_bachwtk23.ogg" loop fadein 6.0
    show rika uni mischievous day closed at center with Dissolve(0.5)

    "On Thursday afternoon, I encountered Rika sitting outside my last class — blocking off all possible escape routes."

    #TODO let's head to the station platitudes
    
    #pause(0.5)
    #hide rika with Dissolve(0.5)
    pause(0.5)
    stop sound fadeout 1.0

    scene schoolroad16 with Dissolve(1.0):
        subpixel True
        xalign 1.0 yalign 1.0
        easein 15.0 xalign 0.0 yalign 0.0

    play sound "audio/edgemeadow.ogg" loop fadein 1.0
    pause(0.5)
    
    "We made our way towards the station."
    
    "And though I had been anticipating the trip to Bremersberg with mild reluctance, I had to admit the gentle spring breeze and the omnipresent signals of nature awaking stirred a certain fancy in me."
        
    #pause(1)
    #stop sound fadeout 1.0
    #scene train with Dissolve(1.0) #other train image? in city? #TODO station sounds
    #play sound "audio/station.ogg" loop fadein 2.0
    #pause(1)
    
    pause(1)
    "We arrived at the station just in time for the three o'clock train."
    
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene trainin3 with fade
    play sound "audio/train.ogg" loop fadein 1.0
    pause(1) 
    window show
    scene trainin3 with vpunch
    pause(0.5)
    show rika uni sad day open at center with Dissolve(1.0)
    pause(0.5)
    show rika uni sad day open at center with vpunch
    #"Rika made a worn-out impression."
    #show rika uni sad day open with vpunch
            
    r "Thank you for coming on this trip with me."
    show rika uni sad day open with vpunch
    r "I would have gone alone — it's just that I've been so busy lately."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)    
    r "With finals, and swimming practice—"
    show rika uni sad day open with vpunch    
    r "—and to make things worse, my father has asked me to help him canvas for his re-election campaign."
    show rika uni sad day open with vpunch
    r "I detest the work — but I can't refuse him."
    
    pause(1)
    "Abbotsford is only a short trainride away from the city, and it was within fifteen minutes that we approached the first suburbs."
    stop sound fadeout 5.0   
    "Gradually the train slowed down, before coming to a cautious stop."
    
    pause(0.5)
    hide rika with Dissolve(0.5)
    pause(0.5)
    window hide
    #pause(0.5)

    #scene stationhall with Dissolve(1.0)
    play sound "audio/citysounds.ogg" loop fadein 1.0
        
    #pause(1)    
    scene shoppingstreet with fade
    pause(1)
    window show
    pause(1)
    show rika uni sad day open at Position(xpos=0.35, xanchor=0.5) with Dissolve(0.5)
    pause(1)
    
    r "Bremersberg."
    r "What a god-forsaken place."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)      
    r "Built after the reclamation of the Marshpolder — it aspires to be a hallmark of post-war architecture."   
    r "But in all its craftsmanship, it lacks culture—"
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)  
    r "—it lacks character."    
    r "The citizens here are strangers to one another — unlike in our little town."
    pause(0.5)
    "I smiled."
    pause(0.5)
    a "Maybe that's not so bad—?"
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)     

    r "It is."

    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)      
    r "If everyone is anonymous, there is no accountability."
    r "Places like these breed evil."
   
    stop music fadeout 3.0
    pause(1)
    hide rika with Dissolve(0.5)
    pause(1)
    stop sound fadeout 1.0
    scene anthropology with Dissolve(1.0) #img of the building surrounded by bushes
    play sound "audio/clock.ogg" loop fadein 1.0
    pause(1)
    
    "When we arrived at the faculty of social sciences, professor Helsing's lecture was still in progress."
    "We waited outside of the auditorium until he was finished and all the students had filed out."
    
    pause(1)
    scene computerroom with Dissolve(1.0) # computer room
    pause(1)

    play music "audio/mus_satie.ogg" loop fadein 6.0 #cliche but may be fitting
    show pete neutral day open at Position(xpos=0.70, xancho=0.5) with Dissolve(0.5)
    pause(1)
    "A short, dark haired man welcomed us."
    show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.2)    
    p "You must be the students that contacted me."
    show rika uni happy day open at Position(xpos=0.25, xanchor=0.5, ypos=0.53 ,yanchor=0.5) with Dissolve(0.5) 
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    p "Rika—?"
    pause(0.5)

    "The professor extended his hand, which she accepted gracefully."
    show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.2)
    p "Peter Helsing — pleased to meet you."
    p "I'm delighted to see young people take an interest in the science of anthropology."
    p "And so proactive too, to reach out to me like this."
    p "You don't see that very often these days—"
    show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.2)
    p "—but it's the way to go. In the social sciences, I mean."
    p "You need to get ahead, know the right people."
    "He let out a dry cough."
    show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.2)    
    p "Please tell me about yourselves."
    
    #TODO: maybe move to a study? or the museum?
    
    
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "My name — as you know — is Rika Kuyper. And this is Abe."
    r "We're in our last year of high school—"
    r "—and although it's still a month until finals, I'm sure they will prove to be no more than a formality."
    
    "She shot me a cunning grin."
    show rika uni mischievous day open with Dissolve(0.5)    
    r "Personally, the reason I contacted you, is that I'm seeking direction."
    r "I'm quite sure I want to major in anthropology — but what type? Cultural? Linguistic? Forensic?"
    
    "In a thinly veiled attempt at feigning youthful enthusiasm, her voice was rising steadily."
    show rika uni mischievous day closed with Dissolve(0.2)
    show rika uni mischievous day open with Dissolve(0.2)   
    r "—and then, the next question arises: where do I go? I mean Bremersberg is nearby, but there are much better universities. Leiden? Maybe even Oxbridge?"
    show pete smiling day closed with Dissolve(0.5)
    "Peter placed a reassuring hand on her shoulder."

    p "Don't worry, you're doing great."
    p "You can only make one decision at a time."
    show pete neutral day open with Dissolve(0.5)
    p "Personally I would advise against Bremersberg, as they don't even have a dedicated Anthropology department down here."
    p "That's why they've asked me to make the commute from Leiden once a week."
    show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.2)
    p "But there's no need to come to a hasty decision."

    show rika uni happy day open with Dissolve(0.2)
    "Rika let out a sigh of relief."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)
    r "I'm sorry."
    r "It's such an ambivalent time for me. I feel like all my steps are magnified."
    r "As though they could set loose an unstoppable chain-reaction."
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)    
    r "But I apologize for wasting your precious time."
    r "Please tell us about your renowned anthropology department."
       
    
    #"He coughed." #kind of an awkward dialogue"
    show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.2)
    
    p "I will."
    p "But the next class should be starting here in a short while. Let's continue our conversation in the exposition area."
    pause(0.5)
    hide pete with Dissolve(0.5)
    hide rika with Dissolve(0.5)    
    pause(1)
    scene university with Dissolve(1.0)
    pause(1)
    "We followed Peter into an adjacent building, where glass cabinets displayed a multitude of zoological exhibits."
    
    show pete neutral day open at Position(xpos=0.70, xanchor=0.5) with Dissolve(0.5)
    pause(0.5)
    show rika uni happy day open at Position(xpos=0.25, xanchor=0.5, ypos=0.53, yanchor=0.5) with Dissolve(0.5) #TODO: better positioning
    
    show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.2)
    p "Let me tell you a little about my field."
    
    p "Anthropology is the study of humans—"
    p "—but what you encounter, at times, has few traces of {i}humanity{/i} left inside." 
    show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.2)
    p "Anthropologists delve into the dark depths of our past."
    p "The violent, trauma-ridden, tearing away from our previous existence as animals—"
    p "—and the turbulent process of becoming human."
    
    show pete ominous day open with Dissolve(0.2)
    p "When I visited the rain forests of West-Papua a year ago, I was away from civilization for months."
    p "I watched as a man skin a boar with his bare hands—"
    p "—and then I helped him remove its entrails, and clean the blood and feces from it's flesh."
    show pete smiling day closed with Dissolve(0.5)    
    "The professor reveled at the sight of my disgusted face — as though he were enjoying the lurid details he threw our way. "
    #show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.5)
    p "Anthropology is great, but it isn't for the faint of heart. Especially when you take it {i}seriously.{/i}"
    p "At our department, we do science the old-fashioned way." 
    p "We try to disengage from the petty trends that have come to dominate our field over the past decades—"
    p "—the wholesome fairy tales of universal brotherhood and noble savages, that naive students are attracted to like flies."
    "He leered at Rika, who shrugged coolly. "
    
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)  
    r "How about {i}Bram Bulwer{/i}? Was {i}he{/i} old-fahsioned?"
    show pete sad day open with Dissolve(0.5)    
    "The professor stirred at the sound of this name."
    show pete sad day closed with Dissolve(0.2)
    show pete sad day open with Dissolve(0.2)

    p "Bram Bulwer—?"

    p "You appear to have read up on the history of our department." 
    p "Bram should be regarded as a pioneer in our field. He didn't shy away from anything—"
    show pete sad day closed with Dissolve(0.2)
    show pete sad day open with Dissolve(0.2)
    p "—even when he probably should have."
    show rika uni sad day open with Dissolve(0.5) 
    p "But why do you bring up his name?"
    pause(0.5)
    "Rika took a deep breath."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)  
    r "I found something in a book of his — and I was wondering if you could clarify."
    #show document at Position(xpos=0.25, xanchor=0.5) with Dissolve(0.5)
    "She took out a stack of paperwork from her bag, some of which she had marked with page markers."
    show rika uni sad day closed with Dissolve(0.2) #TODO have rika show papers?
    show rika uni sad day open with Dissolve(0.2)    
    r "Please look at these."
    r "On this page of his notebook, he writes something about {i}three Abbot skulls{/i} — and I'm curious what he was referring to. " #i was, i was
    r "But I can't find anything more about them."
    
    "Peter looked at her — appearing genuinely confused."
    show pete sad day closed with Dissolve(0.2)
    show pete sad day open with Dissolve(0.2)    
    p "I have no idea what that could be."
    show pete ominous day open with Dissolve(0.5)
    "But then his eyes narrowed."
    show pete ominous day closed with Dissolve(0.2)
    show pete ominous day open with Dissolve(0.2)
    p "This is such a particular inquiry, it makes me wonder why you'd ask—" #said before #curious
    p "Are you, by any chance, from Abbotsford—?"
    pause(0.5)
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)      
    "Rika remained silent for a moment — then she nodded."
    pause(0.5)
    
    p "I thought so."
    p "We've received inquiries about these skulls before — from a church."
    p "Did {i}they{/i} put you up to this?"
    
    "Rika shook her head violently."
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)        
    r "No— not at all. We're truly curious."
    
    "The professor sighed."
    show pete ominous day closed with Dissolve(0.2)
    show pete ominous day open with Dissolve(0.2)    
    p "Look, I'm telling the truth when I say that I have no idea what Bram was referring to in these notebooks."
    p "But considering the sustained interest from your community—"
    show rika uni happy day open with Dissolve(0.5)       
    "Rika's lips curled into a precocious smile."
    pause(0.5)
    p "—I'm willing to do a quick search in the archives."
    p "Next week — or whenever I find a PhD student who I can delegate this task to."
    
    "He sighed."
    show pete ominous day closed with Dissolve(0.2)
    show pete ominous day open with Dissolve(0.2)  
    p "But after this, you will really need to let the issue rest."
    p "I understand how an aside like this can spark interest in an affected community. But most likely it's nothing."
    p "A typographical error, or a wild idea—"
    show rika uni happy day closed with Dissolve(0.2)
    show rika uni happy day open with Dissolve(0.2)    
    "Rika nodded understandingly, although I saw a glimmer of hope shining in her eyes."
    show pete neutral day open with Dissolve(0.2)
    p "I hope you kids do decide to study at my department — especially after all the trouble you've put me through."
    show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.2)
    p "It'll be a huge change of environment for you. After growing up in such a {i}rural{/i} community."
    a "I never grew up in—"
    
    "He cut me off."
    show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.2)
    p "College is a time to expand your mind, to question the assumptions instilled in you during your upbringing."
    p "I'll contact you as soon as I receive more information."
    stop music fadeout 3.0
    
    pause(0.5)
    
    hide pete with Dissolve(0.5)
    hide rika with Dissolve(0.5)
    pause(0.5)
    window hide
    pause(1)
    play sound "audio/citysounds.ogg" loop fadein 1.0
    scene anthropology with fade #TODO what is this? outside?
    pause(1)
    window show
    pause(0.5)
    show rika uni mischievous day open at center with Dissolve(0.5)
    pause(0.5)
    
    
    r "Well — that went well."
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)    
    "Rika was beaming." #She was beaming.
    pause(0.5)
    a "You think so? He didn't seem too happy with the ruse we came up with."
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)
    r "Oh sure he didn't, but that was just a way to get a foot in the door."
    
    r "Matters like these require a personal touch. A dull letter from an orthodox congregation is easily cast aside."
    r "But as soon as give your inquiry a youthful, pretty face — it becomes a lot harder for a man like Peter to say no."
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)
    "She flashed me a meaningful grin."
    pause(0.5)
    a "I didn't really notice him looking at you in that way."
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)    
    r "Oh but he {i}was{/i} looking—"
    show rika uni mischievous day closed at center with Dissolve(0.2)
    show rika uni mischievous day open at center with Dissolve(0.2)      
    r "—at {i}you{/i}."
    pause(0.5)
    hide rika with Dissolve(0.5)
    pause(0.5)
    "Rika burst out in a contagious laughter that persisted all the way to the station." #sustained, lingered
    pause(0.5)

    scene bremersberg with Dissolve(1.0)
    pause(0.5)
    
    #"I led her back to the station — while she continued giggling at her sophomoric allusion to something that was likely a capital sin in her world view."
    
    "Afternoon rush hour had commenced, and the city was tense with the bustle of cars."
    pause(0.5)
        
    stop music fadeout 2.0
    #hide ina with Dissolve(0.5)
    #hide rika with Dissolve(0.5)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with Dissolve(2.0)
    pause(2)

label p2c5:

    play sound "audio/cricketsafternoon.ogg" loop fadein 5.0 
    scene blueroom_twi with Dissolve(3.0)
    pause(1)
    window show    
    pause(1)
        
    #"On Monday morning I made my way towards the station. " #TODO this needs better introduction
    #"Though I had been anticipating Easter break with mild reluctance, I had to admit the gentle Spring breeze and the omnipresent signals of nature awakening were stirring a certain fancy in me."
    
    "Monday morning."
    pause(0.5)    
    "I lay for a second in blissful ignorance—"
    pause(0.5)
    play audio "audio/doorbell.ogg"
    pause(0.5)
    "—until the reality of my situation intruded on me."
    


    
    pause(1)
    scene black with Dissolve(1.0)

    play audio "audio/doorbell.ogg"
    pause(1)
    "After forcing myself out of bed, I climbed down the stairs to open the door."
    stop sound fadeout 1.0
    pause(1)
    play sound "audio/crowfield.ogg" loop fadein 1.0
    play music "audio/mus_vnlove1.ogg" loop fadein 10.0
    scene residential #with Dissolve(1.0)
    show naomi uni serious day glas at center 
    with Dissolve(0.5)
    pause(0.5)
    
    #"—only to be met by Naomi's cold stare."
    #pause(0.5)
    u "Good morning Abe."
    a "Naomi—? To what do I owe the honor?"
    show naomi uni intent day glas at center with Dissolve(0.5)
    u "Rika and I are both out and about — gathering the late sleepers."
    u "She's picking up Mei at this very moment."
    u "You wouldn't want to miss the train, would you?"
    pause(0.5)
    "Although I'd been aware that easter break was rapidly approaching — early morning amnesia seemed to have erased it entirely from my mind."
    
    show naomi uni smile day glas at center with Dissolve(0.5)
    u "I hope you're packed and ready. Come on, let's head for the station."
    pause(0.5)
    scene villageroad with Dissolve(1.0) 
    pause(0.5)    
    "I retrieved my bag and followed her through the empty streets."
    "While we walked, I could feel an undeniable tension in the air."
    pause(0.5)
    "After a while, Naomi broke the silence."
    pause(0.5)
    #scene street 
    show naomi uni smile day glas at center with Dissolve(1.0)  
    pause(0.5)    
    #TODO
    
    u "The weather-forecast for the coming days has been good."
    u "Even though the water may be cold, we can expect all-round pleasant temperatures."
    
    "Her vague attempts at small-talk felt unsettling to me."
    pause(0.5) 
    #a "Oh, I'll enjoy myself — rain or shine."
    "I muttered a wry response."
    show naomi uni intent day glas at center with Dissolve(1.0)
    #"She sulked."
    u "A—Abe. I've been meaning to ask you something."
    "Her voice sounded brittle, as though she were mustering up great courage just to talk to me."
    pause(0.5)    # "I looked up."
    u "It's about a fr—"
    stop music fadeout 1.0
    

    
    #"It wasn't long before I detected Bernard, traveling in the same direction as I. As soon as he took notice of me, he came my way."

    play audio "audio/swipe.ogg"
    play music "audio/mus_grieg10.ogg" loop fadein 6.0
    show bern coat smile day open at right #with Dissolve(0.5)
    show naomi uni serious day glas at left 
    with easeinright
    "Out of nowhere, a looming figure pushed itself into my field of sight."    

    "Startled by the sudden interruption, Naomi swallowed her words."
    pause(0.5)
    b "Abe — old boy! Great to see you're tagging along."

    
    a "Bernard—? Are {i}you{/i} coming on easter break?"
    show naomi uni smile day glas with Dissolve(0.5)
    u "Um, he is — he was one of the last people to sign up."
    a "Hm. I guess Rika managed to coerce you—"
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)
    b "There was no coercion required—"
    b "—I'm due for an outing, you see?" #meh
    b "It's important to distract your mind every once in a while."
    b "Water, sky, female companionship — isn't that what life is all about?"
    show naomi uni serious day glas at left with Dissolve(0.5)    
    "Naomi leered at him."
    pause(0.5)
    hide bern with Dissolve(0.5)
    hide naomi with Dissolve(0.5)

    pause(0.5)
    scene abbotsfordstation with Dissolve(1.0)   #TODO add station img
    pause(0.5)
    "When we arrived at station square, a small committee stood waiting on us."
    
    show mari skirt serious day open at left  with Dissolve(1) #Make sure characters are well spaced
    
    s "W—What is {i}he{/i} doing here?!"

    show rika dress happy day open at Position(xpos = 0.72, xanchor=0.5) with Dissolve(1)
    r "Him—? Oh, he seemed interested in joining us. And we were still short of participants—"
    
    show bern coat smile day open at center behind mari with Dissolve(0.5)
    show mari at Position(xpos = 0.15, xanchor=0.5) with easeinleft #Make sure     
    #show rika at Position(xpos = 0.8, xanchor=0.5) with easeinright
    
    b "Madeleine — as soon as I heard you were coming, I knew I couldn't be left out."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    "I looked at Marisa without saying anything."
    show mari skirt serious day closed with Dissolve(0.2)
    show mari skirt serious day open with Dissolve(0.2)
    s "Rika — you {i}really{/i} shouldn't have done that. Bernard is trouble."
    s "You're so annoying, Bernard. "
    s "And it looks like you've been harassing poor Abe again." #too
    show mari skirt serious day closed with Dissolve(0.2)
    show mari skirt serious day open with Dissolve(0.2)    
    s "Well, I'm not associating with you during {i}any{/i} part of this trip—"
    show mari skirt serious day closed with Dissolve(0.2)
    show mari skirt serious day open with Dissolve(0.2)     
    "She shrugged haughtily."
    s "—please keep your distance from me."
    
    hide mari with easeoutleft #slideout better?
    pause(1)

    hide bern with easeoutright
    pause(1)
    
    "Mei showed up — and after fifteen minutes even Ina appeared, carrying two suitcases."
    show ina shirt serious day open at left with Dissolve(0.5)    
    "She looked as sullen as ever."
    
    show ina shirt serious day closed at left with Dissolve(0.2)
    show ina shirt serious day open at left with Dissolve(0.2)    
    n "I've brought my laptop — and books."

    n "That inn better have good security."
    pause(0.5)
    "Rika stifled a laugh."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    r "Oh Ina, I {i}am{/i} glad you agreed to come."
    r "We need someone to make sure we get around to studying." #meh
    stop music fadeout 4.0
    pause(0.5)
    hide rika with Dissolve(0.5)
    hide ina with Dissolve(0.5)
    
    pause(1)
    stop sound fadeout 1.0
    show train with Dissolve(1.0)
    play sound "audio/station.ogg" loop fadein 1.0
    pause(1)
    "Collectively, we made our way to the platform."    
    pause(1)
    stop sound fadeout 1.0
    scene trainin with Dissolve(1.0) #TODO
    play sound "audio/train.ogg" fadein 1.0 loop
    pause(1)
    "The train shot past miles and miles of farmland."
    show trainin with vpunch
    "Here and there, acres of green were interspersed with brightly colored tulip fields — imparting seasonal variety upon the otherwise monotonous train ride."
    pause(1)
    show mei tshirt happy day open at center with Dissolve(0.5)
    pause(1)
    
    m "The flowers are pretty, aren't they?"
    show mei with vpunch
    m "They always cheer me up, when spring comes around."
    show mei with vpunch
    a "Are you looking forward to the trip?"
    show mei tshirt happy day closed at center with Dissolve(0.2)
    show mei tshirt happy day open at center with Dissolve(0.2)
    m "I love visiting new places."
    show mei with vpunch
    m "The people, the culture—"
    show mei with vpunch
    a "Ryebury is only a thirty minute trainride away, you know—"
    show mei tshirt happy day closed at center with Dissolve(0.2)
    show mei tshirt happy day open at center with Dissolve(0.2)
    m "Incredible, isn't it?"
    show mei with vpunch
    stop sound fadeout 1.0
    pause(1)
    
    play sound "audio/summermeadow.ogg" loop fadein 1.0
    scene ryebury with fade
    pause(1)
    play music "audio/mus_vnhappy.ogg" loop fadein 3.0
    
    "After exiting the train at Ryebury station, we made our way through the narrow streets that led to the inn — a townhouse style building that counted three floors."
    pause(1)
    "A soothing breeze — originating from the giant lake — could be felt throughout town."
    pause(1)
    "When we arrived at the inn, Rika let us in swiftly."
    pause(1)
    stop sound fadeout 1.0
    scene innreception with Dissolve(1.0)
    play sound "audio/officesound.ogg" loop fadein 1.0
    pause(1)
    show rika dress happy day open at center with Dissolve(1)
    pause(1)
    
    #"After entering, Rika addressed us in a sheperdly fashion."


    
    r "Dear travel companions."
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)
    r "My family has been gracious enough to make this property available to us students, year after year."
    r "Let us ensure that they continue this tradition — by acting as responsible stewards and leaving this place even cleaner than we encountered it."
    
    show rika dress happy day closed at center with Dissolve(0.2)
    show rika dress happy day open at center with Dissolve(0.2)
    
    r "But most importantly — please make yourselves at home and enjoy the fellowship together."
    r "You're free to share in all of the amenities this inn has to offer, even though they may be sparse."
    r "Thank you for attending Abbotsford High's seventh annual easter break. Let's study hard and be joyful!"
    
    pause(0.5)
    hide rika with Dissolve(0.5)
    pause(0.5)
    scene innstairs with Dissolve(1.0)
    pause(0.5)
    
    
    "I carried my luggage up the stairs before helping Ina, who was clearly struggling."
    #pause(0.5)
    "And then I swung open the door to the master bedroom—"
    "—just in time to witness a spectacle unfold."
    
    pause(0.5)
    scene innbedroom with Dissolve(1.0)
    pause(0.5)
    show mari skirt angry day open at left  with Dissolve(0.5)
    pause(0.5)
    
    

    
    s "Get out, Bernard! I'm not sharing my room with you — let alone a double bed!"
    pause(0.5)
    show bern coat embarassed day open at right with Dissolve(0.5)
    pause(0.5)    
    b "Madeleine— You're so cold."
    b "I may as well just sleep with the cellar rats—"
    pause(0.5)
    
    #### MARISA/INA 4 ####
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        s "Oh Abe, it's good that you came — what do you have to say about all of this?!"
        
        "Bernard, don't be a nuisance. Let her have the room.": #Mei? You saw us on Saturday? But 
            $ marisa_ina_score += 1
            show mari skirt smile day closed with Dissolve(0.5)
            s "There, Bernard. Now it's two against one."
            show mari skirt serious day open with Dissolve(0.5)
            s "You should be ashamed — to intrude upon a lady's private chambers."
            
        "I feel like the two of you are destined to be together.": 
            show bern coat smile day open at center with Dissolve(0.5)
            s "Abe, how dare you say such a thing?!"
            show mari skirt serious day open with Dissolve(0.5)
            s "Oh, all you boys are the same—"
    
    #### MARISA/INA 4 ####   
    
    pause(0.5)
    "Attracted by the noise, Rika stuck her head around the corner."
    
    show rika uni sad day open at center behind mari with Dissolve(0.5)
    show bern at Position(xpos = 0.8, xanchor=0.5) with easeinright
    r "Oh you two— "
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "Marisa, come with me. We can share the penthouse suite."
    pause(0.5)
    r "Abe, maybe you should room here with Bernard."
    hide mari with easeoutleft
    r "Then Ina can take the family room, together with—"
    
    show ina shirt worried day open at left with easeinleft
    
    n "I—"
    
    show rika uni sad day closed with Dissolve(0.2)
    show rika uni sad day open with Dissolve(0.2)
    r "What?"
    n "I was thinking Abe and I could share a room, in case we'd need to work on newspaper business."
    show rika uni happy day open at center with Dissolve(0.5)
    "Ina was blushing visibly, and I noticed Rika's lips arch into a mischievous smile."
    #"She blushed." #blush?
    show rika uni happy day closed at center with Dissolve(0.2)
    show rika uni happy day open at center with Dissolve(0.2)
    r "Oh Ina — there will be more than enough opportunity for that."

    r "It's just that we can't allow mixed dormitories—"
    show rika uni happy day closed at center with Dissolve(0.2)
    show rika uni happy day open at center with Dissolve(0.2)    
    r "—my family wouldn't approve of that {i}at all{/i}."
    
    show ina shirt worried day closed with Dissolve(0.2)
    show ina shirt worried day open with Dissolve(0.2)
    n "Hmpf. It's not even like—"
    "Her voice trailed off."
    
    #n "I understand—"
    #pause(1)
    
    scene innfamilyroom with Dissolve(1.0) #familyroom
    pause(1)
    
    "We carried Ina's luggage up to the family room, where she immediately began to unpack."
    
    show ina shirt serious day open at center with Dissolve(0.5)
    pause(0.5)
    n "Now Abe, you may think we're here on some kind of vacation, but I don't want to let this trip go to waste."
    show ina shirt serious day closed at center with Dissolve(0.2)
    show ina shirt serious day open at center with Dissolve(0.2)
    n "We kicked off the campaign season with some light interviews, to bring out the human factor behind each party."
    n "Now, however, is the time to start digging deeper."
    n "If you get the chance, please ask Marisa about her political strategy."
    n "I will do the same for Rika, to find out what she knows about her father's campaign."
 
    #n "Politics are like a game of chess, each player has a battle plan—"
    "She paused."
    pause(0.5)
    show ina shirt serious day closed at center with Dissolve(0.2)
    show ina shirt serious day open at center with Dissolve(0.2)  
    n "But there's more I want you to look into."
    n "Remember what Marisa said, about the scandal she claimed to have uncovered?"
    n "I want you to hear her out about this."
    n "There should be an—"
    
    stop music fadeout 1.0
    play audio "audio/knock.ogg"
    "Just then Naomi knocked on the door — Ina became deathly silent."
    
    pause(0.5)
    hide ina with Dissolve(0.5)
    pause(0.5)
    "I excused myself."
    pause(0.5)
    window hide
    pause(0.5)
    
    scene innbedroom with Dissolve(1.0) 
    
    pause(0.5)
    window show
    pause(0.5)
    "When I returned to the master bedroom, I found Bernard combing his hair in the mirror."
    pause(1.0)
    
    play music "audio/mus_grieg2.ogg" loop fadein 6.0
    show bern coat think day open at center with Dissolve(0.5)
    
    #pause(0.5)
    b "Well Abe — it seems like the morality police has condemned us to one another."
    show bern coat think day closed at center with Dissolve(0.2)
    show bern coat think day open at center with Dissolve(0.2)
    b "And personally — I don't mind. This may even provide an opportunity for us to grow closer."

    b "I reckon this is your first time— "

    show bern coat smile day open at center with Dissolve(0.2)
    "He grinned."
    #show bern coat smile day closed at center with Dissolve(0.2)
    #show bern coat smile day open at center with Dissolve(0.2)
    b "—sharing the bed with another man?" #too many homosex jokes?"
    show bern coat smile day open at center with vpunch    
    "I shot backward."
    show bern coat smile day closed at center with Dissolve(0.2)
    show bern coat smile day open at center with Dissolve(0.2)
    b "Ho—ho. I see a parochial fear growing in your eyes, but I can assure you there's nothing to be shy about."
    b "Once you go to college, you'll realize how much joy there is in fraternizing with your fellow brethren." #peers
    b "Life is a symposium, my friend. Love is all around."#All is full of love. "
    show bern coat smile day closed at center with Dissolve(0.2)
    show bern coat smile day open at center with Dissolve(0.2)
    b "Let's go out and be bohemian!"

    pause(0.5)   
    stop music fadeout 2.0
    hide bern with Dissolve(0.5)
    pause(0.5)
    window hide
    stop sound fadeout 1.0
    scene black with Dissolve(1.0)
    pause(0.5)
    scene beach with Dissolve(1.0) 
    play sound "audio/sealapping.ogg" loop fadein 1.0
    pause(0.5)
    window show
    pause(0.5)
    "After lunch we headed up to the beach. " #explanation?
    "Rybury lies on a tideless lake, large enough to hide the opposite banks from view."
    pause(0.5)   
    play music "audio/mus_vnnostalgic.ogg" loop fadein 6.0
    show ina swim serious day open at left with Dissolve(0.5)

    pause(0.5)
    n "I figure this is what it all comes down to."    
    show ina swim serious day closed with Dissolve(0.2)
    show ina swim serious day open with Dissolve(0.2)    
    n "The beach—"
    n "—if that is what you can call it. "#Ina & Bernard
    show ina swim worried day open with Dissolve(0.5)
    n "Anyway, I brought my books."
    show ina swim worried day closed with Dissolve(0.2)
    show ina swim worried day open with Dissolve(0.2)    
    n "You can go ahead and splash around in the water—"
    n "—I'm getting cold just looking at it."
    pause(0.5)
    hide ina with Dissolve(0.5)
    pause(0.5)
    "Ina rolled out her bath towel."
    pause(0.5)   
    "Naomi, who had been observing the scene, approached us."
    show naomi bikini smile day glas at Position(xpos = 0.4, xanchor=0.5) with Dissolve(0.5) #swith leo-naomi orientation?   
    #a "I think I'm going to join Ina — take it easy and enjoy the view."
    pause(0.5)    
    u "Um. I think I'm going in for a swim."
    u "I need to stay in shape, for the championships this summer. "
    #"Naomi pulled off her school uniform, which she hardly went without." #took off glasses?? #can she take off uniform?
    show naomi bikini smile day open with Dissolve(0.5)
    "Carefully she removed her glasses, passing them to Ina for safekeeping."
    "Not wearing her school uniform, Naomi appeared unnaturally pale under the clouded afternoon sky."
    show naomi bikini serious day open with Dissolve(0.5)
    u "P-Please don't stare at me—"
    u "I should have brought my sports swimsuit — this is very uncomfortable."
    pause(0.5)
    hide naomi with Dissolve(0.5)
    pause(0.5) 
    scene lake with Dissolve(0.5)
    pause(0.5)    
    "I continued down the waterline to where Rika stood, looking out into the distance."
    pause(0.5)

    show rika dress sad day open at Position(xpos = 0.25, xanchor=0.5) with Dissolve(0.5)
    pause(0.5)    
    #r "Oh beautiful sea, what they've done to you." #this is a bit boring, think of new dialgues
    #show rika dress sad day closed at left with Dissolve(0.2)
    #show rika dress sad day open at left with Dissolve(0.2)
    #r "Tamed by the interfering hand of humanity—"
    
    r "Can you see how dark the waters are?"
    r "At some points, the lake gets very deep."
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)
    r "When this used to be a sea, tidal currents would tear long rifts along the former shoreline."
    pause(0.5)
    show mei bikini happy day open at right with Dissolve(0.5)
    pause(0.5)
    m "Rika really loves the sea. Maybe a little {i}too{/i} much, at times."
    show mei bikini happy day closed at right with Dissolve(0.2)
    show mei bikini happy day open at right with Dissolve(0.2)
    m "But I don't mind them turning it into a lake."
    m "The water is much calmer that way."
    m "Rika, are you going to try to swim up to the {i}humming stone?{/i}"
    
    show rika dress happy day open with Dissolve(0.5)
    "I looked into the distance, where small black spot shimmered at the horizon."
    
    #TODO: can mei tell this piece:

    
    "The humming stone was an underwater rock feature, that reached up right to the water level, so that it was visible whenever a wave opened up the water's surface."
    show rika dress happy day closed with Dissolve(0.5)
    show rika dress happy day open with Dissolve(0.5)
    "The rock had always been a hazard for passing ships, as they could easily rupture their hull on its unseen edges."
    stop music fadeout 6.0
    "And Rika had told me that many tales existed about the humming stone — featuring all kinds of hideously deformed creatures that lived there and feasted upon the flesh of drowned sailors."
    
    pause(0.5)
    hide rika with Dissolve(0.5)
    hide mei with Dissolve(0.5)
    pause(0.5)
    scene beach with Dissolve(1.0) 
    pause(0.5)
    "Not much later, Marisa approached me."
    pause(0.5)
    play music "audio/mus_vnlove3.ogg" loop fadein 10.0
    show mari bikini smile day open at center with Dissolve(0.5)
    pause(0.5)
    s "Hey Abe, I hadn't found a chance to thank you yet."
    pause(0.5)
    a "Thank me—? For what?"
    show mari bikini smile day closed at center with Dissolve(0.2)
    show mari bikini smile day open at center with Dissolve(0.2)
    s "For your feature piece on Flock, last week. The interview came out beautifully." #our party?
    pause(0.5)
    a "Oh it's nothing, thank you for your cooperation."
    show mari bikini smile day closed at center with Dissolve(0.2)
    show mari bikini smile day open at center with Dissolve(0.2)
    s "I'm serious, it was such a beautiful article. And so honest."
    s "I must admit, I was having second thoughts before it came out."

    show mari bikini serious day open at center with Dissolve(0.5)
    s "Our movement is used to being treated unfairly by the media, due to prejudices that people have—"
    show mari bikini serious day closed at center with Dissolve(0.2)
    show mari bikini serious day open at center with Dissolve(0.2)
    s "—but I wanted to trust you, Abe, because you were so kind to me."
    s "You kept your promise, and treated us fairly."
    "A fierce determinism had formed in her eyes."
    s "That's all we ask for, to be treated fairly."
    s "If only the press would report the facts—"
    
    pause(0.5)
    a "Did you hear our piece was picked up by the {i}Evening Mirror?{/i}"

    show mari bikini smile day open at center with Dissolve(0.5)    
    s "Yes! It's fabulous!"
    show mari bikini smile day closed at center with Dissolve(0.2)
    show mari bikini smile day open at center with Dissolve(0.2)
    s "I've been receiving phonecalls from across the low countries."
    s "Who would ever think the concerns of our little town would gain national interest?"
    
    show mari bikini normal day closed at center with Dissolve(0.5)
    
    "Then she sighed."
    show mari bikini normal day closed at center with Dissolve(0.2)
    show mari bikini normal day open at center with Dissolve(0.2)
    s "I have to be careful though."
    s "Lecherous journalists have been making comments on my appearance. "
    #s "They've been digging and found out that I did modeling work while I was in university."
    s "The fact is, I did some modeling work while I was in university."
    show mari bikini normal day closed at center with Dissolve(0.2)
    show mari bikini normal day open at center with Dissolve(0.2)
    s "And now the press has dug up photographs." #Bernhard can comment, later, that he saw her pictures."
    s "I need to tread carefully."
    s "Although this kind of coverage can spark interest in our movement — it distracts from our core message."
    show mari bikini normal day closed at center with Dissolve(0.2)
    show mari bikini normal day open at center with Dissolve(0.2)
    s "As I said, we are seldom treated fairly."
    s "I want to be a serious politician."


    "Rika, who was standing nearby, turned her head."
    pause(0.5)
    show rika dress happy day open at Position(xpos = 0.7, xanchor=0.5)
    show mari bikini normal day open at left 
    with easeinright
    r "Oh but you {i}are{/i} a serious politician, Marisa. I read your interview, it was great."
    r "My father is very excited about you — he's looking forward to working as your colleague."
    #show mari bikini normal day closed at left with Dissolve(0.2)
    show mari bikini smile day open at left with Dissolve(0.5)
    s "Your father — councilman Kuyper — said that?!"
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    r "He did. He thinks you'll be a serious competitor in the race. That A.I.R. will have a heavy task maintaining its majority position."
    r "But he agrees with many of the ideas you expressed in your interview. About creeping corruption and the gradual erosion of moral values in our town."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    r "Maybe this year, we'll see a transformation — in which things change for the better."
    
    r "Where {i}our community{/i} wins, in the long run. And not just one political party."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    r "{i}As overseers of His creation we must be above reproach.{/i}"
    r "That's right, isn't it?"
    show mari bikini smile day open with Dissolve(0.5)    
    s "Oh Rika, you put things to words so nicely."
    show mari bikini smile day closed with Dissolve(0.2)
    show mari bikini smile day open with Dissolve(0.2)
    s "Have you ever considered a career in {i}politics{/i}—?"
    stop music fadeout 3.0
    pause(1)
    hide mari with Dissolve(0.5)
    hide rika with Dissolve(0.5)
    pause(1)
    
    stop sound fadeout 1.0
    scene ryebury_twi with Dissolve(1.0)
    pause(1)
    "When evening fell, we gorged ourselves on seafood from the local cafeteria, before heading back to the inn."
    pause(1)
    
    scene innreception_nig with Dissolve(1.0)
    play sound "audio/night_interior.ogg"  loop fadein 1.0
    pause(0.5)
    show rika dress happy day open at center with Dissolve(0.5)
    pause(0.5)
    r "We will have our first study session at eight."
    r "Feel free to retreat to your rooms until then."
    
    #TODO more lines
    pause(0.5)
    hide rika with Dissolve(0.5)
    pause(0.5)
    scene innbedroom_nig with Dissolve(1.0)
    pause(1)
    play music "audio/mus_grieg10.ogg" loop fadein 6.0
    show bern coat smile day open at center with Dissolve(1)
    pause(1)
    b "There we are, Abe."
    show bern coat smile day closed at center with Dissolve(0.2)
    show bern coat smile day open at center with Dissolve(0.2)
    
    b "This must be the life the gods had envisioned for us."
    b "Lounging in the sun during the day — contemplating the classics at night."
    
    pause(0.5)
    a "Does that mean you'll be joining our study session?"

    show bern coat serious day open at center with Dissolve(0.5)
    b "Oh not at all, that's for you highschoolers. Personally, I've done enough studying for a lifetime."
    
    "He was staggering, like a weary soldier." #was staggering #meh
    pause(0.5)
    a "So Bernard, what are you going to do now that you're out of university?"
    b "Are you going to look for a job?"
    show bern coat serious day closed at center with Dissolve(0.2)
    show bern coat serious day open at center with Dissolve(0.2)
    b "Hm. I'm not sure—"
    b "I want to live an easy life — filled with art and beauty."
    b "I've always aspired to be a playwright, you see?"
    b "Although I'm afraid there aren't many openings in that field."
    show bern coat serious day closed at center with Dissolve(0.2)
    show bern coat serious day open at center with Dissolve(0.2)
    b "I've done some amateur productions in college. I loved that."
    show bern coat smile day open at center with Dissolve(0.5)    
    b "Especially the auditions for the female parts—"
    
    
    #"He was drifting away." #meh
    pause(0.5)
    a "You have some of your father in you—"

    show bern coat angry day open at center with Dissolve(0.5)
    "He snapped back fiercely."
    show bern coat angry day closed at center with Dissolve(0.2)
    show bern coat angry day open at center with Dissolve(0.2)
    b "Shut your mouth! Don't say these things!"
    
    b "That man wouldn't recognize beauty if it spat him in the face. He corrupts all that he touches."
    b "Poor Madeleine—"
    pause(0.5)
    a "I heard she used to be a model—"
    show bern coat smile day open at center with Dissolve(0.5)    
    "His eyes lit up."
    show bern coat smile day closed at center with Dissolve(0.2)
    show bern coat smile day open at center with Dissolve(0.2)

    b "She was—!"
    b "I tried to get her to play the lead part in a production of {i}Salome{/i} one time, but naturally she turned up her nose."

    b "But I've collected her entire catalog. I even went out to buy an issue of {i}Lighthouse{/i} when she was featured in there— "
    show bern coat smile day closed at center with Dissolve(0.2)
    show bern coat smile day open at center with Dissolve(0.2)
    b "I'll show you when we get home."
    pause(0.5)
    "I nodded affirmatively."
    #But of course she'd never thank me."
    #The mystery of love is greater than the mystery of death."
        
    pause(1)
    
    "Rika called for us to gather in the common room downstairs."
    pause(0.5)
    hide bern with Dissolve(0.5)
    stop music fadeout 2.0
    pause(0.5)
    window hide
    pause(1)
    scene innbar with fade
    
    
    pause(1)
    #show bern coat think day open at left with Dissolve(0.2)
    window show
    pause(1)
    play music "audio/mus_bachwtk3.ogg" loop fadein 5.0
    show rika dress happy day open at Position(xpos = 0.25, xanchor=0.5) with Dissolve(1) #TODO positioning
    #show mei tshirt interested day open at center with Dissolve(0.2)
    #show mari skirt normal day open at right with Dissolve(0.2)
    pause(0.5)
    r "This evening will be dedicated to study."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    r "Senior students, let's look over the examination syllabus \ntogether—"
    #show mei tshirt happy day closed with Dissolve(0.2)
    show mei tshirt interested day open at right with Dissolve(0.5)
    m "If we're not in our finals year, can we go out to the beach to explore?"
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)
    r "Of course not! That would defy the spirit of the trip."
    r "Mei — you can go over your regular homework for now. I can't imagine you aren't behind {i}somewhere{/i}."
    show mei tshirt sad day open with Dissolve(0.5)
    "Mei pouted self-consciously." #TODO actually have her pout
    hide mei with Dissolve(0.5)
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)
    r "And Marisa, Bernard. Please think of something to do."
    r "Marisa, you probably have some council matters to attend to." # delve into."
    show mari skirt smile day open at right with Dissolve(0.5)    
    "Marisa held up her laptop."
    show mari skirt smile day closed at right with Dissolve(0.2)    
    show mari skirt smile day open at right with Dissolve(0.2)    
    s "I'm at it already!" #behind already
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)
    r "And Bernard— You do whatever it is you do—"
    #show bern coat think day closed at center with Dissolve(0.2)
    #show bern coat think day open at center behind rika with Dissolve(0.5)
    b "I'll just shut up and read Nabokov." #shut up and read
    "Grumbling, he sat himself down in a corner."
    
    #hide bernard with Dissolv
    pause(0.5)
    hide mari with Dissolve(0.5)
    hide rika with Dissolve(0.5)
    pause(0.5)
    #picture them seating?
    #show ina shirt serious day closed at center with Dissolve(0.2)

    #show rika dress happy day open with Dissolve(0.5)
    #show naomi uni serious day open at right with Dissolve(0.5)

    
    #
    
    "Rika, Naomi, Ina and I began working through our biology-reader."
    "It wasn't long before I realized that I was so dramatically behind that there was little point in asking questions."
    pause(0.5)
    show ina shirt serious day open at Position(xpos = 0.25, xanchor=0.5, ypos = 0.60, yanchor=0.5) with Dissolve(0.5)
    pause(0.5)
    "Ina sat staring into empty space, similarly lost, even though I'd always pictured her to be decent student."
    stop music fadeout 10.0
    "Soon, Mei came over to our table." #It wasn't long before
    pause(0.5)
    show mei tshirt interested day open at Position(xpos = 0.75, xanchor=0.5, ypos = 0.60, yanchor=0.5) with Dissolve(0.5)
    pause(0.5)
    m "Ina, please help me with this. I cannot find the hypotenuse—"
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt serious day open with Dissolve(0.2)
    n "Mei, I've explained this to you before—"
    pause(0.5)
    "Everyone appeared to welcome the distraction."
    hide mei with Dissolve(0.5)
    hide ina with Dissolve(0.5)
    pause(0.5)
    

    show mari skirt smile day open at Position(xpos = 0.75, xanchor=0.5, ypos = 0.60, yanchor=0.5) with Dissolve(0.5)
        
    s "Rika, I was wondering."
    s "If the land around Abbotsford forms an artificial island — then how come some of the houses in Ryebury look so {i}old{/i}?" #marisa asks this
    #pause(0.5)
    play music "audio/mus_bachwtk8.ogg" loop fadein 6.0
    show rika dress happy day open at Position(xpos = 0.25, xanchor=0.5, ypos = 0.60, yanchor=0.5) with Dissolve(0.5)
    pause(0.5)
    "Rika glanced up from her syllabus."

    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)

    r "The Marshpolder was reclaimed in 1942."
    r "Back then, a large stretch of sea around the isle of Abbot was dammed off — before being pumped dry and connected to the mainland."#, and the area around the former isle of Abbot was pumped dry and connected to the mainland."
    r "Ryebury is one of the oldest communities on the new-formed land — the houses here were built in the forties, thus containing salient traits of prewar architecture."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    r "Soon after its founding, some of the fishing families from Abbot settled here, in an attempt to revive their old trade."
    r "While the lake was filled with brackish water, they were still able to fish for herring and haddock—"
    r "—but once the water grew sweet, they had to venture out through the giant floodgates up north to fish on the northern sea."
    #r "They still make excellent fish-balls though." #we can try them soon
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    
    r "You should understand that the reclamation of the Marshpolder left a huge impression on the inhabitants of the isle of Abbot."
    r "Gradually, they witnessed the surrounding waters sink down, until only a vast wasteland of mud remained."
    r "Their idyllic island life was brutally torn away from them—"
    r "—and these scars run deep in our community." #meh
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    r "But besides all the sorrow, the reclamation had some interesting side effects."
    r "Although the newly drained seabed was untraversable at first, soon archaeologists descended upon Abbotsford to see what they could dig up from the mud."
    r "And though the island community — still traumatized from their dramatic change in lifestyle — was uncharacteristically unwelcoming of their sudden arrival, the archaeologists proceeded to erect barracks and set to work."
    show mari skirt smile day closed with Dissolve(0.2)
    show mari skirt smile day open with Dissolve(0.2)    
    "By now, all present had put down their books and sat listening intently to Rika's story."
    
    show mari skirt smile day closed with Dissolve(0.2)
    show mari skirt smile day open with Dissolve(0.2)
    
    s "So— What did the archaeologists find?"
    show rika dress happy day open at Position(xpos = 0.25, xanchor=0.5, ypos=0.5, yanchor=0.5) with ease    
    "Rika got up from the table." #have her stand up?
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    r "All this talking has made me thirsty. Let's see if they've left us anything to drink—"
    
    hide rika with easeoutleft
    "She walked behind the bar, where a small refrigerator stood."
    
    r "We have tonic, ginger ale—"
    m "Ch-chocolate milk!"
    
    "After Rika had returned with refreshments, she resumed talking."
    pause(0.5)
    show rika dress happy day open at Position(xpos = 0.28, xanchor=0.5, ypos=0.6, yanchor=0.5) with easeinleft
    pause(0.5)
    r "Anyway, Marisa, to answer your question."
    show rika dress sad day open with Dissolve(0.2)
    r "The archaeologists mainly found bones."
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)
    r "The first place where they started digging, was around the old graveyard."
    show rika dress happy day open with Dissolve(0.5)    
    r "And as I told you, Abe—"
    #show rika dress happy day closed with Dissolve(0.2)
    #show rika dress happy day open with Dissolve(0.2)
    "She nodded at me."
    r "—they unearthed a number of old gravestones that had eroded off from the island and lodged themselves in the former seabed."
    r "And along with their gravestones, naturally, they found the remains of the deceased."
    r "Which they immediately returned to the community, to be buried underneath the new church."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    r "Then, after the graveyard was done, they expanded their search."
    #The Isle of Abbot was an interesting place."
    r "On the exposed seabed, the archaeologists found remains of concentric embankments running around the island, that had been swept away in the past by rising waters."
    r "Abbot used to be quite large. But ever since the late middle ages, the island slowly lost land to the encroaching sea."
    r "The archaeologists even found the foundations of stone huts, that had once been submerged completely."
    hide mari with Dissolve(0.5)
    "Rika took a sip from her glass, which contained a clear liquid." #change
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)    
    r "But for the most part, they found bones."
    r "Boring old bones."
    r "What a terrible time these archaeologists must have had, digging fruitlessly in the mud."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)     
    
    r "But you must all be getting very tired. I suggest we beak up this meeting, in order for us to get some well-deserved sleep."
    
    "I could hear Bernard stir in his chair."
    pause(1)
    show bern coat smile day open at Position(xpos= 0.75, xanchor=0.5, ypos=0.6, yanchor=0.5) with Dissolve(0.5)
    pause(0.5)
    stop music fadeout 6.0
    b "Excuse me. I couldn't help but overhear your conversation."
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)
    
    
    b "Just {i}bones{/i} you say?"
    b "Aren't you leaving out an interesting detail?"

    show rika dress sad day open with Dissolve(0.5)   
    r "What are you referring to?"
    
    "Rika's tone had become dismissive."
    play music "audio/mus_vntension.ogg" loop fadein 16.0
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)
    b "If I'm not mistaken, I recall there was a certain — {i}implement{/i}."
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)
    r "I'm too tired to play guessing games. Let's all go up to our rooms."
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)
    b "Let me refresh your memory."
    

    b "There was a curious artifact that archaeologists found near the island. They keep it in at display case a the university."
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)    
    r "What—?"    
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2) 
    b "I believe they call it the {i}Aelian implement{/i}."    
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)       
    r "Oh that— That's a well known hoax."
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)    
    b "It was a hammer of sorts—"
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2) 
    r "And it wasn't real. The Aelian implement has been conclusively proven to be planted by one of the researchers as a prank."
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)     
    b "Well, if it really was a hoax—"
    b "—then what a hoax it was."
    show bern coat smile day closed with Dissolve(0.2)
    show bern coat smile day open with Dissolve(0.2)      
    b "One downcast afternoon, an archaeologist dug up a tool—"
    b "—no more than twelve inches long, shaped like an asymmetrical double faced hammer."
    b "It was completely unique to the area, and forged from a heavy, dark steel."
    show bern coat serious day open with Dissolve(0.5)      
    b "One of its faces was blunt, like an ordinary hammer — but the other narrowed into a sharp reinforced point."
    b "As though it were used to kill animals, with one single blow to the head."
    show bern coat serious day closed with Dissolve(0.2)
    show bern coat serious day open with Dissolve(0.2)   
    b "And the implement was crafted in a way, that was wholly unknown to these regions." 
    b "At first glance, its surface displayed a scaling of miniature steel shields, overlapping each other to form a thin steel plating."
    b "But upon further inspection, this plating appeared to continue beyond the surface, in layers that descended all the way to its core."
    b "And the scales interlocked in such a precise way, that they contracted upon touch — forming an almost fleshlike grip, without sacrificing any of the tensile strength of the tool."#crafted in such a meticulous way, that "
    show bern coat serious day closed with Dissolve(0.2)
    show bern coat serious day open with Dissolve(0.2) 
    b "And the most curious thing about this item—"
    b "—was that it seemed impervious to oxidation."
    show bern coat serious day closed with Dissolve(0.2)
    show bern coat serious day open with Dissolve(0.2) 
    b "After all those centuries that is must have spent lying on the ocean floor, it was without even a speck of rust."
    
    stop music fadeout 12.0
    "Rika coughed."
    show rika dress happy day open with Dissolve(0.5) 
    r "How scary, Bernard."
    r "Isn't it great to share lurid horror tales among friends?"
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2) 
    r "But please don't overdo it. We wouldn't want to give Mei nightmares."
    show bern coat smile day open with Dissolve(0.5)     
    "I heard Marisa clear her throat."
    s "Bernard enjoys telling tall tales."
    s "The thing is, he never knows when to stop—"
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2) 
    r "Come everyone, let's go to bed. We still have three more days before us."
    pause(0.5)
    hide rika with Dissolve(0.5)
    hide bern with Dissolve(0.5)        
    #r "Too charred for that—"
    #r "As though cattle, sheep had been ignited in whole—"
    
    #r "And then, one downcast afternoon—"
    
    #r "They discovered hammer of sorts, with a pointed spike. "
    
    #r "Completely unique to the region, and made out of a heavy, dark, steel that appeared unscathed under its rust coat."
    
    #TODO
    
    #maybe move the drinking to later, so that Marisa can get drunk. Rika decides they'll drink juice for now."
    #Rika discribes a mysterious artifact. Ina takes unnatural amount of interest. "
        
    #b "That sounds like it could be an implement of sacrifice."
    #"Suddenly, Rika's demeanor changed."
    #r "Oh well, I guess they're just rumors made up by senile old men."
    
    #bit of a climax, implement of sacrifice - refer to human sacrifice? Sea got things? More mysterious. adorned with nautical themes
       
    
    
    #summarize rest of the evening. Studying."
    
    #"At around twelve, Rika decided that it was time to go to bed." #improve
    #r "Anyway, you must all be tired from your journey—"
    #m "It was only thirty minutes—" #bad
    
    #mention medieval expansion of the island
    #then get more mysterious. Charred remains.
    #strange artifacts. (imply that Rika is getting a little drunk) Describe a meat cleaving tool or something/sacrificial knife/hammer.
    #maybe something horrible, archaeologist mutilated horribly.
    #about going to bed
   
    
    pause(1)
    stop music fadeout 2.0
    #hide ina with Dissolve(0.5)
    #hide rika with Dissolve(0.5)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)

label p2c6:

    play sound "audio/officesound.ogg" loop fadein 5.0 
    scene innbedroom_mor with Dissolve(1.0)
    play music "audio/mus_vnwayhome.ogg" loop fadein 6.0
    pause(1)
    scene black with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)
    
    "The next morning, I was woken up by an oppressive sensation—" #pressing
    "Bernard — who had initially agreed to observe a broad patch of no-mans-land between both our sides — had somehow managed to shift so far diagonally that he was now taking up a full three quarters of the bed."
    pause(1)
    "A stale odor hung throughout the room. Without a second thought I shot into my clothes and made my way out onto the landing—"
    
    pause(1)
    scene innstairs with Dissolve(1.0)
    pause(1)
    "—only to catch a shadow disappearing down the stairway." #stairs
    pause(1)
    stop sound fadeout 1.0
    scene black with Dissolve(1.0)
    scene ryebury_shadow with Dissolve(1.0) #TODO
    pause(1)
    "I followed it—"
    pause(1)
    "—through the streets of Ryebury—"
    pause(1)
    scene lake_twi with Dissolve(1.0) #TODO (or night version)
    play sound "audio/seawaves.ogg" loop fadein 3.0
    pause(1)
    "—out onto the shore, where I observed it for a while as it stared into the distance of the lake." #towards rising sun?
    
    "And it wasn't long before the shadow disrobed and slid into the lake."
    #"—because the shadow belonged to Rika." #was rika
    pause(1)
    "Rika was a practiced swimmer, and I watched as she performed her workout routine."
    scene lake with Dissolve(2.0)
    "And while I rested in the chalky sand, the sun rose behind me, casting long shadows into the lake." #up over the horizon
    
    pause(1)
    
    "After a forty minute workout, she swam up to me."
    
    #scene rikashore with Dissolve(1.0)
    
    scene rikashore with Dissolve(1.0):
        subpixel True
        xalign 0.0 yalign 1.0
        easein 20.0 xalign 1.0 yalign 0.0  
    
    "With her hair tied up in a single ponytail, she made and almost child-like impression."
    pause(0.5)
    r "Good morning Abe. Have you been spying on me all this time—?"
    

    pause(0.5)
    
    a "I—I just went for a morning walk."
    
    r "That's funny, I never pictured you as an early riser—"
    r "But it's okay, I'm not the type to tense up before an audience."
    
    "She smiled teasingly."
    pause(0.5)
    #potentially change scene to sea 
    


        
    stop music fadeout 2.0
    #hide ina with Dissolve(0.5)
    #hide rika with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)

label p2c7:

    play sound "audio/sealapping.ogg" loop fadein 5.0 
    #play music "audio/mus_lotusland.ogg" loop fadein 2.0 #was poucet
    scene beach with Dissolve(1.0)
    #show ina shirt angry book open at left with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)
    
    "After taking a shower at the facility building, Rika changed out of her swimming clothes."
    pause(0.5)
    
    show rika dress happy day open at Position(xpos=0.25, xanchor=0.5) with Dissolve(0.5)    
    pause(0.5)
    
    r "I received an email from Peter Helsing this morning."
    r "Apparently he has urgent news he wants to discuss with us."
    show rika dress sad day open with Dissolve(0.2)    
    "She let out an inconvenienced moan."
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)
    r "He'll be in town tomorrow, but I really don't want to go to the city. Not while we're on spring break."
    r "I'll try to get him to meet us here at the shore. It would only be a fifteen minute drive for him—"
    "I nodded."
    
    show rika dress happy day open with Dissolve(0.5)
    
    
    r "Ah, I can see the usual crowd is beginning to rear its head."

    #maybe have her banter with Marisa for a bit."
    
    pause(0.5)
    show bern shirtl think day open at Position(xpos=0.73, xanchor=0.5) with Dissolve(1.0)
    pause(0.5)
    r "Good morning Bernard, I'm glad to see you're awake. Did you find our amenities up to standards?"
    show bern shirtl think day closed with Dissolve(0.2)
    show bern shirtl think day open with Dissolve(0.2)
    b "Sure did. I was out cold tonight, that sea air really helps a man wind down."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    a "I noticed—" #good, used before?
    pause(1)
    #
    
    #TODO
    #bernard appears –> marisa appears, chases away bernard –> rika appears, hits it off with marisa
    
    #hide bern with Dissolve(0.5)
    #hide rika with Dissolve(0.5)
    
    # change scene
    #pause(1)
    scene lake with Dissolve(0.5)
    play music "audio/mus_vnaquamarine.ogg" loop fadein 6.0
    pause(1)
    show ina swim serious day open at center with Dissolve(0.5)
    
    n "Hey Abe — there you are."
    show ina swim serious day closed with Dissolve(0.2)
    show ina swim serious day open with Dissolve(0.2)
    n "I've been looking for you all morning."
    n "Have you even eaten breakfast—?"
    #pause(0.5)
    a "How kind of you to worry about me."
    show ina swim serious day closed with Dissolve(0.2)
    show ina swim serious day open with Dissolve(0.2)
    n "Come on, let's look for a quiet place."
    n "Even though we're on easter break — the Sunday Abbot never skips an issue."
    n "Let's hold an editorial meeting, before the beach becomes too crowded."
    pause(0.5)
    a "A meeting—?"
    a "But Ina, I thought we could take it easy for a few days—"
    
    "She grabbed me by the arm."
    pause(1)
    hide ina with Dissolve(0.5)
    pause(1)
    scene beach with Dissolve(0.5)
    pause(1)
    show ina swim happy day open at left with Dissolve(1.0)
    pause(1)
    
    #TODO: new location
    
    n "So, have you noticed anything?"
    show ina swim happy day closed  with Dissolve(0.2)
    show ina swim happy day open with Dissolve(0.2)
    n "That Marisa girl, I don't know what to think of her."
    n "She appears so immature at times, the way she bickers with Bernard."
    n "I wonder if Flock will be able to retain its current position, with her in the lead."
    pause(0.5)
    a "She's getting on with Rika alright—"
    show ina swim serious day open with Dissolve(0.5)    
    n "Hm—"
    "Ina pondered for a second."
    show ina swim serious day closed  with Dissolve(0.2)
    show ina swim serious day open with Dissolve(0.2)
    n "She is, isn't she—?"
    n "I wonder what will come of that."
    n "As you know, Rika's father is a member of A.I.R."
    
    n "He leads the Kuyper faction — an autonomous wing within the party."
    n "If Marisa manages to sway John Kuyper, it could lead to division within A.I.R."
    n "Although I'm not sure if she would be capable of that—"
    #explained already?"
    #explain the Kuyper faction."
    pause(0.5)
    a "You know what, maybe they're just becoming friends."
    a "Although she is dependable, Rika can come off as lonely at times. And Marisa hardly knows anyone in town."
    a "Not everything is a political game, you know—?"
    "Ina grumbled."
    show ina swim serious day closed with Dissolve(0.2)
    show ina swim serious day open with Dissolve(0.2)
    n "That's where you're wrong, Abe." 
    #stop music fadeout 2.0
    n "Very wrong—"
    
    play music "audio/mus_vnhappy.ogg" loop fadein 1.0
    show mei bikini interested day open at right with Dissolve(0.5)    
    "Suddenly, Mei appeared—" 
    show mei bikini happy day closed with Dissolve(0.2)
    show mei bikini interested day open with Dissolve(0.2) 
    m "Abe, Ina — what are you discussing?"
    "I welcomed the break from Ina's paranoid ramblings like a breath of fresh air."
    pause(0.5)
    a "Hi Mei, you're late for the editorial meeting. Please tell us what you will be contributing to the next issue—"
    show mei bikini sad day open with Dissolve(0.5)
    
    
    m "You're holding an editorial meeting?! On the {i}beach{/i}?!"
    show mei bikini serious day closed with Dissolve(0.2)
    show mei bikini sad day open with Dissolve(0.2)
    m "Why didn't you tell me—?!"
    show mei bikini happy day open with Dissolve(0.5)

    m "But never mind! You need to listen to what I've discovered!"
    show mei bikini happy day closed with Dissolve(0.2)
    show mei bikini happy day open with Dissolve(0.2)
    m "While the two of you have been vacationing — I have been running a covert investigation!"
    show ina swim happy day open with Dissolve(0.5)
    "Ina stifled a laugh."

    show mei bikini serious day open with Dissolve(0.5)
    m "And you must hear — I have discovered a mystery!"
    a "Wow Mei, please tell us!"
    show mei bikini serious day closed with Dissolve(0.2)
    show mei bikini serious day open with Dissolve(0.2)
    m "Those basalt blocks there—"
    "She pointed towards the breakwater that stretched out behind us."
    #"I have found something about about them"
    m "—that stone isn't from around here!"
    m "I can tell by the quartz layers and some of the markings."
    "She lowered her voice, to the point where is was no more than a whisper."
    m "Illegal smuggling of rare stone is an international crime. I believe we may be on to— "
    pause(0.5)
    
    #### RIKA/MEI 4 ####
    play audio "audio/decision.ogg"
    menu:
        with Dissolve(1.0)
        m "—a conspiracy!"
        
        "Ina, stop the presses!": #Mei? You saw us on Saturday? But 
            $ rika_mei_score += 1
            show mei bikini happy day shut with Dissolve(0.5)
            a "We may have to put out an extra edition to cover this breaking story."
            show ina swim serious day open with Dissolve(0.5)
            "Ina reprimanded me from under her breath."
            n "{i}Don't encourage her—{/i}"
            
        "Oh Mei, you always crack me up—": 
            show mei bikini angry day open with Dissolve(0.5)
            "Mei glared at me."
            a "Shut up, Abe. You're being a bully."
    
    #### RIKA/MEI 4 ####    
        
    
    pause(0.5)


    pause(0.5)
    hide ina
    hide mei
    with Dissolve(0.5)
    pause(0.5)
    window hide
    pause(0.5)
    scene lake with Dissolve(1)
    pause(0.5)
    # Ina: theory of corrupted enlightenment leading to authoritarianism.
    # Marisa delves into her world view.
    # Talk about property ownership. (Leopold pays for Marisa's apartment.)
    # Naomi acts strangely. Very pale, skeletal.
    window show
    pause(0.5)
    
    "As the afternoon progressed, the beach became increasingly crowded with beach-goers, who were drawn like flies to the exceptionally favorable weather conditions."
    
    "As forecasted, the temperatures had been gradually rising over the past week — and underneath the unbroken rays of the midday sun, it felt as though summer had come early."

    pause(0.5)
    show bern shirtl angry day open at Position(xpos=0.70, xanchor=0.5) with Dissolve(0.5)

    "And as I made my way through the multitude of people, I encountered Bernard."
    "He stood staring into the distance, an overwhelmed look in his eyes."
    
    show bern shirtl angry day closed with Dissolve(0.2)
    show bern shirtl angry day open with Dissolve(0.2)    
    
    a "Hi Bernard, it's getting pretty busy. Have you seen the others?"
    
    "My words appeared to pass right through him."
    show bern shirtl angry day closed with Dissolve(0.2)
    show bern shirtl angry day open with Dissolve(0.2) 

    b "Can you feel it, Abe? Nature has fully awoken from its state of hibernation."

    b "All is teeming with life."
    
    show bern shirtl angry day closed with Dissolve(0.2)
    show bern shirtl angry day open with Dissolve(0.2) 
    
    b "The sheer amount of precocious female beauty — swimwear bursting at the seams."
    
    b "It's all too much, too sudden—"
    
    show bern shirtl angry day closed with Dissolve(0.2)
    show bern shirtl angry day open with Dissolve(0.2) 
    
    b "I think I'm suffering from sensory overload."
    
    pause(0.5)
    show beachgirl at left with Dissolve(0.5)
    show bern shirtl serious day open with Dissolve(0.2)     
    pause(0.5)
    
    "Just then a young woman, who had been hovering nearby, approached us."
    pause(0.5)
    g "I'm sorry to interrupt your conversation. But could you tell me if there is a post office nearby?"
    
    "There was a timid quality to her soft-spoken voice."
    
    g "I want to send a postcard to my grandma, but I haven't even found as much as a letter box—"
    
    pause(0.5)
    
    a "I'm not sure, did you see a post office, Bernard."
    
    "Bernard just stood staring at her — wholly paralyzed."
    pause(0.5)
    a "I'm sorry, my friend has been feeling a little {i}indisposed{/i} lately."
    a "But I'm sure there'll be a post office in the village."
    pause(0.5)
    g "Thank you! I'll be off then—"
    g "Who knows, I might just see you guys around."
    
    pause(0.5)
    hide beachgirl with Dissolve(0.5)
    pause(1)
    
    "I turned to Bernard."
    a "Come on, what's the matter with you?"
    a "Wasn't this the whole reason you came here? To mingle with attractive girls?"
    show bern shirtl serious day closed with Dissolve(0.2)
    show bern shirtl serious day open with Dissolve(0.2)
    b "Oh Abe, you don't understand—"
    b "I couldn't. It would break the enchantment.."
    "He sighed."
    show bern shirtl serious day closed with Dissolve(0.2)
    show bern shirtl serious day open with Dissolve(0.2)    
    b "{i}Man is born free — yet everywhere he is in chains.{/i}"
    pause(0.5)
    
    b "Come on, it's probably time to head back to the inn."
    
    pause(0.5)
    hide bern with Dissolve(0.5)
    pause(0.5)
    scene ryebury with Dissolve(1.0)
    pause(0.5)
    
    "As we left the overcrowded beach, Bernard slowly returned to his senses."
    
    show bern shirtl angry day open at center with Dissolve(1)
    b "Oh Abe, you know, if I were ever to give something to the world—"
    b "—it would be a grand beauty contest."
    show bern shirtl angry day closed at center with Dissolve(0.2)
    show bern shirtl angry day open at center with Dissolve(0.2)
    b "A biannual event, where the greatest embodiment of female aesthetics is chosen from a pool of thousands — to be crowned princess over this blessed earth."
    
    "I chuckled."
    pause(0.5)
    a "A beauty contest? You mean like a {i}miss-election{/i}?"
    a "Would {i}that{/i} be your gift to humanity?"

    show bern shirtl smile day open at center with Dissolve(0.2)
    b "Oh it's not like that at all—"
    b "—for in a miss-election both the interior and the exterior of women are judged."
    show bern shirtl smile day closed at center with Dissolve(0.2)
    show bern shirtl smile day open at center with Dissolve(0.2)
    b "But in my contest — it's {i}only{/i} about the exterior!"
    b "Because that's what it's all about! The origin of man!"
    show bern shirtl smile day closed at center with Dissolve(0.2)
    show bern shirtl smile day open at center with Dissolve(0.2)
    b "Do you remember the {i}Judgment of Paris{/i}, from Greek mythology?"
    b "When the young prince Paris gifted his golden apple to Aphrodite — crowning her the most beautiful goddess of all?"
    b "Eventually, that single event led to the destruction of Troy and the birth of the modern world."
    show bern shirtl angry day open at center with Dissolve(0.5)
    b "It was all because of a beauty pageant."
    show bern shirtl angry day closed at center with Dissolve(0.2)    
    show bern shirtl angry day open at center with Dissolve(0.2)
    b "If not for beauty, what else do we have—"
    
    stop music fadeout 3.0
    "He had become overly sentimental, reveling in his idiotic words—"
    
    ####################
    
        
    stop music fadeout 2.0
    #hide ina with Dissolve(0.5)
    #hide rika with Dissolve(0.5)
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0
    scene black with fade
    pause(1)

label p2c8:

    play sound "audio/night_interior.ogg" loop fadein 5.0 
    scene innbar with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)
    
    play music "audio/mus_vnretrospective.ogg" loop fadein 3.0 #play music "audio/mus_vnhappy.ogg" loop fadein 3.0
    # they do some studying, Marisa is tired and keeps moaning for alcohol.

    "That evening, we returned to the common room."
    pause(0.5)
    #show mari corset smile day closed with Dissolve(0.2)
    show mari corset smile day open at left with Dissolve(0.5)
    pause(0.5)
    s "Come on, Rika. Open up the liquor cabinet. It's time to mix some cocktails!"
    pause(0.5)
    #show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open at Position(xpos=0.70, xanchor=0.5) with Dissolve(0.5)
    pause(0.5)
    "Rika pouted doubtfully—"
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)
    r "I'm not sure, Marisa. The school has entrusted us to act responsibly at all times."
    show mari corset smile day closed with Dissolve(0.2)
    show mari corset smile day open with Dissolve(0.2)
    s "Oh come on—"
    s "A {i}little{/i} alcohol won't hurt, will it? You must have started taking holy communion by now—"
    s "We've all worked so hard — you can't hold an excursion without some leisure." #indulgence
    
    a "Marisa, we've spent the entire day at the beach—"
    show rika dress happy day open with Dissolve(0.2)    
    "But Rika had already yielded."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)    
    r "Well okay, since we're all of drinking age I see no issue in indulging a little."
    r "But all those that are still enrolled in Abbotsford High will be limited to {i}one{/i} glass."
    r "Please don't make me regret this."
    pause(0.5)
    play audio "audio/swipe.ogg"
    hide mari with easeoutleft
    pause(0.5)
    "With a squeal of delight, Marisa bounded towards the bar, where she began stirring up a batch of {i}Tom Collinses{/i}. "
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)       
    b "I'll have a glass of the {i}Glenfarclas 15 year old{/i}—"
    "Bernard's words were lost in the ambient murmur."
    hide rika with Dissolve(0.5)    
    
    
    pause(0.5)
    #show mari corset smile day closed with Dissolve(0.2)
    show mari corset smile day open at left with Dissolve(0.5)
    pause(0.5)
    "When Marisa returned, she handed each of us a glass of clear liquid."
    pause(0.5)
    
    show mei tshirt happy day open at right with Dissolve(0.5)

    m "Wow, this is good."
    show mei tshirt happy day closed with Dissolve(0.2)
    show mei tshirt happy day open with Dissolve(0.2)
    m "Better than wine."
    show mei tshirt happy day closed with Dissolve(0.2)
    show mei tshirt happy day open with Dissolve(0.2)    
    m "It makes you sleepy, though."
    #show mei tshirt happy day closed with Dissolve(0.2)
    #show mei tshirt happy day open with Dissolve(0.2)
    pause(0.5)
    show mei tshirt happy day closed with Dissolve(0.4)  
    pause(0.5)
    "Carefully we carried Mei up to her bed."
    pause(0.5)
    scene black with Dissolve(1.0)
    pause(1)
    scene innbar with Dissolve(1.0)
    
    pause(0.5)
    "As the night progressed, the common room grew quieter."
    pause(0.5)    
    show ina shirt serious day open at Position(xpos = 0.25, xanchor=0.5, ypos = 0.60, yanchor=0.5) with Dissolve(0.5)
    show mari corset smile day open at Position(xpos = 0.70, xanchor=0.5, ypos = 0.60, yanchor=0.5) with Dissolve(0.5)
    pause(0.5)
    "Marisa, Ina and I sat studying at one of the round oak tables. While Bernard sat in a corner, working on one of his plays."
    "At times we could hear him break out, reciting one of his lines with pathos. But for the most part he was quiet."
    
    pause(1)
    
    show mari corset smile day closed with Dissolve(0.2)
    show mari corset smile day open with Dissolve(0.2)
    s "Hey Ina—"
    "Marisa put down her glass — which was her third of the night."
    show mari corset smile day closed with Dissolve(0.2)
    show mari corset smile day open with Dissolve(0.2)    
    s "I love what you are doing with the Sunday Abbot."
    s "It has such a broad appeal, I'd never expected that from a school paper."
    show ina shirt angry day open with Dissolve(0.5) 
    "Ina's eyes narrowed."
    show ina shirt serious day closed with Dissolve(0.2) 
    show ina shirt angry day open with Dissolve(0.2) 
    n "I would like to draw your attention to the fact that we are {i}not{/i} a school paper—"
    "Marisa ignored her remark."
    show mari corset smile day closed with Dissolve(0.2)
    show mari corset smile day open with Dissolve(0.2)       
    s "Oh Ina. I'm sure you have a brilliant future ahead of you."
    show mari corset serious day open with Dissolve(0.5)    
    s "I know people who could—"

    "She let out a hiccup."
    show mari corset serious day closed with Dissolve(0.2)
    show mari corset serious day open with Dissolve(0.2) 
    s "—I know people, I mean, who could really open doors for you."
    show ina shirt serious day closed with Dissolve(0.2) 
    show ina shirt angry day open with Dissolve(0.2) 
    n "That's kind, Marisa, but I ask you to maintain the integrity of our relationship."
    n "Our only current concern is to cover the town council elections in a fair and objective manner—"
    "Ina's words trailed off — and I could tell that she was thinking rapidly."
    show mari corset normal day open with Dissolve(0.5)
    s "Oh Ina, you're so {i}good{/i}. It's no fun—"
    show mari corset smile day open with Dissolve(0.5)
    s "—and that's so much {i}fun{/i}."
    #Then she drew overly serious."
    s "But to be a good journalist, you should be able to spin your web a little."
    #s "To network— "
    s "—like the incy wincy spider."
    #"Marisa broke out giggling, before suddenly becoming overly serious." #better segue
    
    
    ######################################
    show ina shirt kind day open with Dissolve(0.5)
    "Ina smiled."
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt kind day open with Dissolve(0.2)
    n "Maybe you're right, Marisa."
    show mari corset blush day open with Dissolve(0.5)
    n "Maybe I {i}should{/i} spin my web."
    n "Couldn't you help us out a little?"
    n "As a politician, you must be privy to all kinds of information."
    show ina shirt happy day closed with Dissolve(0.2)
    show ina shirt kind day open with Dissolve(0.2)    
    n "Can I refill your glass for you?"
    stop music fadeout 4.0
    show mari corset blush day closed with Dissolve(0.5)
    
    s "Oh Ina. There's no need to get me drunk."
    s "I'll tell you anything you want."
    show mari corset blush day open with Dissolve(0.5)
    "She stared into Ina's eyes intensely."
    
    play music "audio/mus_vntension.ogg" loop fadein 30.0
    #s "I want to tell you something, for your paper—"
    s "Have you ever heard the story of {i}Anna Sanders{/i}?" #improve
    pause(0.5)
    "Ina shook her head."
    show mari corset blush day closed with Dissolve(0.2)
    show mari corset blush day open with Dissolve(0.2)     
    s "On 56 Oystercatcher Lane, there is an apartment on the second floor — so small and unassuming that you'd hardly notice it. " #improve
    s "There is something off about this apartment, something I've been wanting to share—"
    show ina shirt serious day open with Dissolve(0.2)   
    "Even though Marisa was slurring her words, Ina had become all ears."
    show mari corset blush day closed with Dissolve(0.2)
    show mari corset blush day open with Dissolve(0.2) 
    s "There are things happening in Abbotsford — Ina — that cannot bear the light of day."
    s "Things that are impossible to uncover without the right {i}entrances{/i}." #sfx?
    
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt serious day open with Dissolve(0.2)
    n "So what's the deal with 56 Oystercatcher Lane?"
    "I saw Ina make a quick note of the address in her notebook. "
    
    s "Things have happened in Oystercatcher Lane — dark, disgusting things."
    s "If I told you, you wouldn't believe me."
    s "But please—"
    "Marisa moved to take another sip of her glass, but Ina stopped her."
    show mari corset blush day closed with Dissolve(0.2)
    show mari corset blush day open with Dissolve(0.2) 
    s "In the registry there are ways to look up the, um— {i}provenance{/i} of all of Abbotsford's real estate—"
    s "—and the, tax status. The tax exempt status, I mean."
    show mari corset blush day closed with Dissolve(0.2)
    show mari corset blush day open with Dissolve(0.2)     
    s "Please look into that. I'm sure you'll figure out for yourself, eh— what's going on."
    s "That this leads up all the way to the mayor."
    show ina shirt angry day open with Dissolve(0.5)  
    "Ina frowned."
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)  
    n "Mayor Van Linden—?"
    n "Your main political rival, you mean?"
    "Marisa brushed aside Ina's remark."
    show mari corset blush day closed with Dissolve(0.2)
    show mari corset blush day open with Dissolve(0.2) 
    s "Don't believe me. Look it up for yourselves, do your duty—"
    "Before Ina could stop her, she took a large sip from her glass." #maybe Ina is encouraging her to drink instead of preventing her?"
    pause(0.5)
    a "Marisa — who was Anna Sanders?"
    show mari corset blush day closed with Dissolve(0.2)
    show mari corset blush day open with Dissolve(0.2)     
    s "Anna—?"
    
    "A look of utter sadness appeared in her eyes."
    show mari corset blush day closed with Dissolve(0.2)
    show mari corset blush day open with Dissolve(0.2)     
    s "Oh proud saint Margaret—"
    "For a second, she hid her face in her hands—"
    "—before she broke out singing:" #wailing
    show mari corset angry day open with Dissolve(0.5)
    s "{i}Oh I forbid you maidens, all{/i}"
    s "{i}that wear gold in you hair,{/i}"
    s "{i}to come or go by Carterhaugh,{/i}"
    s "{i}for young Tam Lin is there!{/i}"
    show mari corset serious day open with Dissolve(0.5)    
    #stop music fadeout 6.0
    "From the corner of the room, I could hear Bernard humming along with the tune."
    pause(0.5)    
    "Ina sighed—"
    show ina shirt serious day closed with Dissolve(0.2)
    show ina shirt angry day open with Dissolve(0.2)    
    n "She's had too much."
    n "A little wine can loosen tongues, but too much and it {i}detaches{/i} them."
    n "It won't be long before she passes out. Come on, Abe — let's go to bed."

    
    ################################
    # Finds naomi eavesdropping on their conversation.
    pause(0.5)
        
    hide ina with Dissolve(0.5)
    hide mari with Dissolve(0.5)
    pause(0.5)
    "While Ina, Marisa and Bernard tidied up the common room, I made my way towards the stairs, in order to assure myself an uncontested sleeping spot for the night."
    
    pause (0.5)
    stop music fadeout 30.0
    scene black with Dissolve(1)
    pause(0.5)
    "But the second I stepped out into the dark hallway, I bumped into an unseen figure."
    
    play audio "audio/clothesdrop.ogg"
    show naomi uni suprised nig glas at left with vpunch
    
    a "Naomi—?"
    a "I thought you went to bed an hour ago—"
    
    u "Um— I eh—"
    u "I just came down for a glass of water—"
    u "P—Please excuse me."

    "I stepped aside, giving her free access to the common room."
    pause(0.5)
    a "Well go ahead—"
    

    show naomi uni intent nig glas with Dissolve(0.5)
    u "No— I've changed my mind."
    play audio "audio/swipe.ogg"
    hide naomi with Dissolve(0.5)
    "And without any further explanation, she disappeared up the stairs."
    
    #pause(0.5)

    
    #stop music fadeout 6.0
    pause(1)
    window hide
    pause(1)
    stop sound fadeout 1.0

    pause(1)
    


label p2c9:

    play sound "audio/officesound.ogg" loop fadein 5.0 
    scene reception with Dissolve(1.0)
    pause(1)
    window show    
    pause(1)
    
    
    "The next day we hung around at the inn until noon, when Rika and I distanced ourselves from the rest of the crowd."
    
    pause(1)
    stop sound fadeout 1.0
    scene beachpoint with Dissolve(1.0)
    play sound "audio/seawaves.ogg" loop fadein 2.0
    pause(1)
    "She'd arranged to meet up with Peter near the north point, where a natural sandbar ran far out into the lake."
    
    pause(0.5)
    
    "Frequented only by incidental birdwatchers, this secluded place would offer enough privacy to discuss our affairs."
        
    play music "audio/mus_chopincello.ogg" loop fadein 6.0
    show rika dress happy day open at Position(xpos=0.25, xanchor=0.5, ypos=0.53, yanchor=0.5) with Dissolve(1)
    show pete neutral day open at Position(xpos=0.70, xanchor=0.5) with Dissolve(1)
    
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)
    r "Thank you for taking the time to talk to us."
    show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.2)    
    p "It's nothing — I wish my own students would take this much interest in my work."    
    p "But students can be so calculating these days."
    p "'Will this be on the exam?' is what they ask me, whenever I delve too deep into a subject."
    p "As if grades are all that matters."
    p "You can't become an anthropologist just by taking tests."
    show rika dress happy day closed with Dissolve(0.2)
    show rika dress happy day open with Dissolve(0.2)    
    r "So how {i}does{/i} one become an anthropologist?"
    show pete neutral day closed with Dissolve(0.2)
    show pete neutral day open with Dissolve(0.2)   
    p "Hm—"
    p "You need to be willing to take a long look into the eyes of humanity."
    p "Even if you are chilled to the bone by what stares back at you."
    #p "You need to do what it takes—"
    show rika dress mischievous day open with Dissolve(0.5)
    "Rika smirked."
    show rika dress mischievous day closed with Dissolve(0.2)
    show rika dress mischievous day open with Dissolve(0.2)
    r "Let me guess—"
    r "Sometimes you may even need to {i}get on your knees and dig up graves.{/i}"
    show pete sad day open with Dissolve(0.5)
    "Peter swallowed."
    show pete sad day closed with Dissolve(0.2)
    show pete sad day open with Dissolve(0.2)
    p "I—It's not like that."
    
    #########
    
    #p "Look—"
    p "The thing you must understand—"
    show pete sad day closed with Dissolve(0.2)
    show pete sad day open with Dissolve(0.2)
    p "In the days of Bram Bulwer, there were many academic misconceptions about isolated communities like yours."
    p "Scholars speculated that the inhabitants of Abbot suffered from physical and mental degeneration, due to inbreeding that would occur on the island."

    show pete sad day closed with Dissolve(0.2)
    show pete sad day open with Dissolve(0.2)    
    p "There were many stereotypes about the Abbotian islanders — with their short arms and pasty white skin that almost appeared translucent on bright days."
    show rika dress sad day open with Dissolve(0.5)    
    "Rika's eyes shot fire."
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)
    r "How about that—"
    
    show pete sad day closed with Dissolve(0.2)
    show pete sad day open with Dissolve(0.2)       
    p "These were just century-old misconceptions."
    p "I think even Bulwer had to reconsider his hypothesis — in the end."
    p "Because in his notes, he states that the genetic makeup of the Abbot skulls appeared far more genetically diverse than expected."
    "Rika murmured approvingly."
    show pete sad day closed with Dissolve(0.2)
    show pete sad day open with Dissolve(0.2)       
    p "{i}Far{/i} more diverse—"
    p "—leading to speculation that Abbot may have operated as a trading port at some time during the late middle ages."
    
    #TODO: some gruesome stories?
    
    #Maybe delve into cult anthro theories here?
    show pete sad day closed with Dissolve(0.2)
    show pete sad day open with Dissolve(0.2)   
    p "For Bram, it must have been a disappointment."
    p "Anthropologists are always looking for isolated pockets of human settlement, where development has stood still."
    
    stop music fadeout 4.0
    show pete smiling day closed with Dissolve(0.2)
    "His lips curled into an ominous grin."
    
    p "In West-Papua there are still some tribes that live entirely without outside contact."
    
    #p "From a distance, of course."
    
    p "Life there is tough but simple — for the most part, people get by with basic farm work."
    
    play effects "audio/haunting.ogg" loop fadein 25.0
    show pete ominous day open with Dissolve(0.5) 
    
    p "But a mysterious, ritualized violence permeates all aspects of daily life."

    show pete ominous day closed with Dissolve(0.2)
    show pete ominous day open with Dissolve(0.2) 
    
    #TODO
    p "Religious torture, skin incisions — it's enough to make you question their sanity."
    
    #p "Abuse, mutilation, "
    
    p "But although it may appear cruel to an outsider, to them it's a deliberate way to come to terms with the wanton terror — the disease, famine, death — that nature inflicts upon them every day."
    
    #p "Their animistic beliefs dictate that every force of nature is embedded by some kind of spirit."
    
    p "Mirroring nature's violence within their communities, is a way to assert control over the animistic spirits that embody the destructive forces of nature."
    
    #p "Disease, famine, death — without any institutions to guard themeselves from nature — they have internalized the constant state of danger."
    
    #animism, nature is being
    pause(0.5)
    "Even though the beach was wholly empty, Peter had lowered his voice to a whisper."
    show pete ominous day closed with Dissolve(0.2)
    show pete ominous day open with Dissolve(0.2) 
    p "In some parts of the rain forest, systemic infanticide is still commonplace."
    
    p "I have seen mothers abuse their children — not even sadistically, but matter-of-factly, as though it were the most natural thing in the world."
    
    p "Up to 50 percent of children in these communities are killed before their second birthday—"
    show pete ominous day closed with Dissolve(0.2)
    show pete ominous day open with Dissolve(0.2)    
    
    p "—by their own parents."
    
    show rika dress mischievous day open with Dissolve(0.5)
    "Rika smiled at Peter coolly."
    stop effects fadeout 6.0
    show rika dress mischievous day closed with Dissolve(0.2)
    show rika dress mischievous day open with Dissolve(0.2)
    r "Well, it appears that your exotic vacation has left quite an impression on you."
    
    show pete sad day open with Dissolve(0.5) 
    "Peter's face turned sour."
    show pete sad day closed with Dissolve(0.2)
    show pete sad day open with Dissolve(0.2) 
    #p "It did—"
    

    ###############################
    p "But look at the time — I have a class to teach at two. I really {i}should{/i} get going." #sudden
    play music "audio/mus_bachwtk10.ogg" loop fadein 10.0    
    show rika dress sad day open with Dissolve(0.5)
    r "Wait a minute, Peter — aren't you forgetting something?"
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)
    r "Did you manage to find the skulls I asked you about?"
    r "And would there be any way to return them to our community? To their rightful resting place—"
    show pete sad day closed with Dissolve(0.2)
    show pete sad day open with Dissolve(0.2)     
    p "Yes, um— No. I mean, I'm doing my best."
    p "The department is looking into it — but I still have to clear some matters."
    p "Even if we do find them, I will need explicit permission to release them to you."
    p "You have no idea how many old bones the anthropology department owns."
    p "Because that's all they are, in the end."
    p "Maybe we shouldn't even go through the hassle—"
    show rika dress sad day closed with Dissolve(0.2)
    show rika dress sad day open with Dissolve(0.2)
    r "We should, Peter."
    r "Please contact me as soon as you hear more about the skulls."
    r "Theft of human remains isn't a trivial matter — maybe informing the press about this whole history would help you expedite the process within your department."
    "She nodded at me, meaningfully — as I felt a shudder of realization pass through me." #meaningfully?
    show pete shocked day open with Dissolve(0.5)    
    p "Oh please don't, I assure you they are working as hard as they can."
    show pete sad day closed with Dissolve(0.2)
    show pete shocked day open with Dissolve(0.2)      
    p "I mean — maybe now isn't the right moment to inform the press."
    p "We could invite them once we hand over the skulls to you, though."
    p "Then we'll both be featured in a positive light."
    show pete smiling day closed with Dissolve(0.5)      
    "He smirked."

    pause(0.5)
    p "As you seem to realize all too well, academia is all about public relations."
    
    pause(1)
    
    
        
    stop music fadeout 2.0
    hide pete with Dissolve(0.5)
    hide rika with Dissolve(0.5)

    pause(0.5)
    window hide
    pause(1)
    stop sound fadeout 3.0
    scene black with Dissolve(3.0)
    pause(1)
    #####################################################################################################
    if rika_mei_score > 3:
        show prog_mika p at Position(xpos = 0.5, xanchor=0.5, ypos=0.3, yanchor=0.5) with easeinright
    elif rika_mei_score > 1:
        show prog_mika n at Position(xpos = 0.5, xanchor=0.5, ypos=0.3, yanchor=0.5) with easeinright
    else:
        show prog_mika d at Position(xpos = 0.5, xanchor=0.5, ypos=0.3, yanchor=0.5) with easeinright
        
    pause(0.25)
    
    if marisa_ina_score > 3:
        show prog_marina p at Position(xpos = 0.5, xanchor=0.5, ypos=0.7, yanchor=0.5) with easeinright
    elif marisa_ina_score > 1:
        show prog_marina n at Position(xpos = 0.5, xanchor=0.5, ypos=0.7, yanchor=0.5) with easeinright  
    else:
        show prog_marina d at Position(xpos = 0.5, xanchor=0.5, ypos=0.7, yanchor=0.5) with easeinright
        
    
    #####################################################################################################
    pause(2)
    hide prog_mika with easeoutleft
    pause(0.25)
    hide prog_marina with easeoutleft
    
    
    pause(1)
    ##PART 3 - title
    #play sound "audio/ventilator.ogg" loop fadein 1.0
    #scene white with Dissolve(1.0)
    #pause(1)
    #scene title3 with Dissolve(1.0)
    #pause(2)
    #scene white with Dissolve(1.0)
    
    
    
    
    #######################################################################
    #### PART 3 ###########################################################
    #######################################################################
    
    #######################################################################
    #### PART 4 ###########################################################
    #######################################################################
    
    #######################################################################
    #### PART 5 ###########################################################
    #######################################################################

    #################################################################################################################################
    ########################################### ENDING ###############################################################################
    #################################################################################################################################


    # This ends the game.
    "\[Thank you for playing the early access version of Deluge: Sermon for the Dead.\]"
    "\[We would love to hear your thoughts on the game. Please consider sending us your feedback through the Steam community hub, or in a game review.\]"
    return



    #################################################################################################################################
    ########################################### DEBUG ###############################################################################
    #################################################################################################################################
    
    label debugmenu:
    
    menu:
        "{i}enter debug menu?{/i}"
       
        "{i}no (start game){/i}":            
            jump prologue
            
        "{i}yes{/i}":            
            ". . ."     
    
    menu:
        "{i}where to?{/i}"
        ####################
        "Part 1_1":            
            jump p1c1            
        "1_2":            
            jump p1c2
        "1_3":            
            jump p1c3
        "1_4":            
            jump p1c4
        ####################    
        "1_5":            
            jump p1c5
        "1_6":            
            jump p1c6
        "1_7":            
            jump p1c7
        "1_8":            
            jump p1c8
        "more":
            ". . ."
            
    menu:
        "{i}where to?{/i}"
        ####################
        "Part 2_1":            
            jump p2c1
        "2_2":            
            jump p2c2
        "2_3":            
            jump p2c3
        "2_4":            
            jump p2c4
        "2_5":            
            jump p2c5
        "2_6":            
            jump p2c6
        "2_7":            
            jump p2c7
        "2_8":            
            jump p2c8
        "more":
            ". . ."    


