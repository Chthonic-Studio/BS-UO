# Definitions of characters

define q = Character(_("Quinn"), color="#c4e143")
define a = Character(_("???"), color="#8d1704")
define l = Character(_("Logan"), color="#ab7e24")
define ladeeva = Character(_("Miss Ladeeva"), color="#90dfae")
define alan = Character(_("Alan"), color="#a0a0a0")
define han = Character(_("Mr. Han"), color="#37377b")
define yselle = Character(_("Yselle"), color="#074325")

# Definitions of objects

define dramatic = Dissolve(4.0)
image alieneye = "alieneye.png"
image eye = "the_eye.png"
image gazer = "gazer.png"
define flash = Fade(.25, 0.0, .75, color="#fff")

# The game starts here.

label fork:

    $ renpy.save('The Docks')

    scene bloody_corridor_2 with dramatic

    play music "horror.ogg"

    "He had managed to get here, only a few more steps to get to the docks."

    if sanity < 3:

        "His mind was starting to fill with the images of the horrors he had seen, and he could not help but feel like he was going to lose his mind at any moment now."
    
    else:

        "He could not help to feel a slight ray of hope shine upon him. But the crushing sensation of having to still crawl through the bloody and darkened shafts of the ship was still there."
    
    "This one was a particularly hard one to navigate through, as he had to squeeze through spaces where the gore on the floor was so thick that it felt like glue."

    "He even got some on his mouth, and had to repress the feeling of vomiting out just to avoid having to vomit all over himself."

    "At some points, he could feel his own breath rebounding to his face, which came back with the mixed smell of blood and vomit."

    show quinn worried at right

    q "I can't believe I'm doing this..."

    q "Not far now, not far now..."

    if health < 4:
        
        "The pain he felt was also contributing to slowing him down. But he managed to get through it, and finally reached the entrance to the docks."

    else:
        
        "But his efforts paid off, as he finally reached the entrance to the docks."
    
    jump dockentrance

label dockentrance:

    scene bloody_corridor_7 with dramatic

    "He had finally reached the entrance to the docks."

    "The ground in front of the door was a total carnage, with body parts laying around, and there was a severed head of someone who Quinn didn't want to look at, just from the fear of it being someone he knew."

    "The door was locked, but there should be survivors behind it, so he only had to announce himself, and he'd be safe, finally, without having to crawl those shafts again."

    show quinn at right

    q "Finally..."

    q "I made it..."

    "The celebration was cut short, however, as he heard a loud noise coming from behind him."

    show alan crazy at left 
    with flash

    alan "..."

    "He was holding a piece of broken glass in his hand, which was already bloodied from not holding it properly, but it didn't seem like Alan was in the mindset to care about that."

    #Alan is completely insane, driven crazy by the visions. He is not going to listen to reason, and will attack Quinn on sight.
    #The player has to fight him, and if they lose, they will die.
    #If they win, they will be able to proceed to the docks.
    #The descriptions are going to be creepy, unnerving, and will make the player feel chills.
    #The style of writing is going to be similar to that of Stephen King and H.P. Lovecraft.
    #Descriptions are going to be lenghty and detailed, and the player will be able to feel the fear and the horror that Quinn is feeling.

    #The fight is going to be a turn-based fight, where the player has to choose between attacking or defending

    show quinn worried at right
    
    q "Alan, please... just stop..."

    "Alan was not listening to him, and he was slowly approaching him with the broken glass in his hand, looking straight at Alan without even blinking."

    if health < 4:

        "Quinn was not in the best of conditions to fight, but he knew that he had to do something. He raised his hands, preparing himself"

    else:

        "Quinn raised his hands in preparation to defend himself, but he was not sure if he would be able to defend himself against Alan."

    $ renpy.force_autosave('checkpoint')

    "Alan suddenly lunged at him, and Quinn was forced to defend himself."

    jump fight

label fight:

    menu:

        "Try to disarm him":

            jump disarm

        "Hit him":

            jump defend

        "Hit his damaged leg" if tip == True:

            jump tipattack

label tipattack:

    "Quinn aimed a kick at the leg that was damaged, and hit it with tremendous force."

    "Alan lost his balance and fell to the ground, and the glass shard fell to his side."

    menu:

        "Use the glass shard to stab him":

            jump stabdisarm

        "Hit him while he's down":

            jump hitdisarm 

        "Try to subdue him":

            jump subdue

label defend:

    "Quinn tried to defend himself by hitting Alan, and he managed to connect a hit to his face, but Alan was too fast, and he managed to cut Quinn's arm with the glass shard."

    $ health -= 1

    with redflash

    play sound "slash.ogg"

    q "AAAAAAHHH!!!"

    "Blood started to pour out of the wound, and Alan, acting like nothing had just happened."

    if health < 1:

        "The accumulated wounds of Quinn were too much, the ground beneath him had gathered a pool of blood, and he was starting to feel dizzy."

        with redflash

        "That was the only thing Alan needed to use the shard to slash his neck."

        with hpunch

        play sound "slash.ogg"

        "He grabs his neck, trying to stop the bleeding, but Alan leaps at him and starts stabbing him repeatedly in the chest, with so much force that Quinn's body is lifted off the ground with each stab."

        play sound "slash.ogg"
   
        "In the end, Quinn's chest is caved in, with a gaping hole in the middle of it."

        "As he dies, he can see Alan's face, which is now covered in his blood, and he can see that Alan is smiling, as if he had found peace."

        "{i}Some say the best defense is a good attack{/i}"

        $ renpy.full_restart()

        return

    else: 

        jump fight


label subdue:

    "Quinn tried to subdue Alan by grabbing him by the neck in a lock, but, without any hesitation, Alan grabbed Quinn's arm and bit it, hard."

    with vpunch

    "He bit with so much force that he managed to bite through Quinn's arm, and he started to chew on it, tearing the flesh apart with his teeth."

    with redflash
    
    q "AAAAAAHHH!!!"

    "Quinn screamed in pain, and he tried to pull his arm away, but Alan's grip was too strong."

    "As Alan broke out of the lock, he grabbed Quinn's head with both hands, and he started to pull it apart, tearing the flesh and skin apart."

    with redflash

    "Quinn tried to fight back, but he was in too much pain, and he was not able to do anything."

    "At one point, before Quinn could pass out from the pain, Alan started to squeeze his head, and Quinn could feel his skull cracking under the pressure, the sound of his own bones being crushed was the last thing he heard."

    "{i}That might not have been the best idea, let's go at it again, shall we?{/i}"

    $ renpy.full_restart()

    return


label disarm:

    "Quinn aimed at the hand that was holding the glass, and tried to disarm him."

    "Alan's movements were fast but held no malice, and Quinn was able to dodge his attack and grab his arm."

    "The thing was, Alan's grip was so strong that Quinn was not able to get him to let go of the glass, even as the glass was cutting through the tendons of his hand."

    "Alan was not even flinching, and he was still looking at Quinn with the same expression of pure rage."

    "As they struggled with the glass shard, Alan suddenly lunged his head forwards to bite Quinn's face."

    menu:

        "What will you do?"

        "Try to dodge":

            jump dodgedisarm

        "Headbutt him":

            jump hitdisarm

        "Use the glass to stab him":

            jump stabdisarm
        
        "Hit his damaged leg" if tip == True:

            jump tipattack

label dodgedisarm:
    
    "Quinn tries to dodge the bite, but in the process, Alan's grip on the glass shard tightens, and it slips of Quinn's hand."

    with hpunch

    "With a swift motion, Alan stabs Quinn in the neck."

    with redflash

    play sound "slash.ogg"

    "He grabs his neck, trying to stop the bleeding, but Alan leaps at him and starts stabbing him repeatedly in the chest, with so much force that Quinn's body is lifted off the ground with each stab."

    play sound "slash.ogg"
    
    "In the end, Quinn's chest is caved in, with a gaping hole in the middle of it."

    "As he dies, he can see Alan's face, which is now covered in his blood, and he can see that Alan is smiling, as if he had found peace."

    "{i}Let's try again, shall we?{/i}"

    $ renpy.full_restart()

    return

label hitdisarm:

    "Quinn managed to headbutt Alan, stopping him from biting him, but his grip on the shard slipped, letting Alan push through, stabbing Quinn in the stomach."

    $ health -= 3
    
    with redflash

    play sound "slash.ogg"

    if health < 1:

        "The accumulated wounds were too much for Quinn, and he fell to the ground, bleeding profusely."
        
        "Alan leaps at him and starts stabbing him repeatedly in the chest, with so much force that Quinn's body is lifted off the ground with each stab."

        "In the end, Quinn's chest is caved in, with a gaping hole in the middle of it."

        "As he dies, he can see Alan's face, which is now covered in his blood, and he can see that Alan is smiling, as if he had found peace."

        "{i}Let's try again, shall we?{/i}"

        $ renpy.full_restart()

        return

    else:

        "Quinn pulls the shard out of his stomach, as it had luckly not pierced too deep, and grabs it in his hand."

        menu:

            "Stab him":

                jump stabdisarm

            "Try to subdue him":

                jump subdue

label stabdisarm:

    "Quinn stabs Alan in the chest with the glass shard, and Alan doesn't stop moving, so Quinn stabs him again."

    with redflash
    play sound "slash.ogg"

    "And again."

    with redflash
    play sound "slash.ogg"

    "And again."

    if sanity < 3:

        "And again."

        with redflash
        play sound "slash.ogg"

        "Then Quinn gets down on his knees and starts stabbing Alan in the face, over and over again, until Alan's face is nothing but a bloody mess."

        "Quinn tightens his grip on Alan's neck, and Alan's eyes bulge out of their sockets, and he starts to convulse."

        show eye at truecenter
        with flash
        hide eye

        "Quinn keeps tightening his grip, and Alan's eyes start to bleed, and his tongue starts to come out of his mouth."

        show eye at truecenter
        with flash
        hide eye

        "Quinn keeps tightening his grip, and Alan's eyes pop out of their sockets, and his tongue falls out of his mouth."

        show eye at truecenter
        with flash
        hide eye

        "Quinn keeps tightening his grip, and Alan's head explodes, covering Quinn in blood and brain matter."

        play sound "crush.gg"
        show gazer at truecenter
        with flash
        hide eye

        "He starts to laugh, and he can't stop. Why? Why is this so freaking funny?"      

        "It's a weird feeling, weird, but strangely... good."      

        $ sanity -= 1

    else:

        "Alan finally stops moving, and Quinn lets go of the shard, letting it fall to the ground."

        show quinn scared at right

        "I...I killed him..."

        "Quinn looks at his hands, which are covered in blood, and he starts to feel sick."

        "He starts to feel dizzy, and he falls to the ground, and he starts to vomit."

        "He wants to lay down, just stop for a moment, but he knows that he can't."

        "He has to keep going."

    "After a moment he needed to collect himself, he gets up and starts walking towards the door to the docks."

    jump dock

label dock:

    "Finally, he could reach the door."

    show quinn worried at right

    q "Hey! I'm Quinn, let me in!"

    "There was silence."

    "He tried again."

    q "I'm Quinn, from the technical staff, please let me in!"

    "Nothing."

    "He feared the worst, but almost when his knees were about to fail him, the door creaked open."

    if sanity < 2:

        jump aliendock

    else:

        "He saw a familiar face, and he felt like he was going to cry."

        if s_logan == True:

            jump logan_ending

        elif s_yselle == True:

            jump yselle_ending

        else: 

            jump dock

label logan_ending:

    scene normal_docks with dramatic

    "Logan was standing in front of him, and he was alive."

    show logan scared at left

    l "Quinn! Yes! I knew you'd make it you cockroach!"

    q "God it's so good to see your face for once..."

    "For the first time in a while, Quinn felt hope."

    "He went past the door, which was immediately shut behind him, and he was greeted by the sight of the rest of the surviving crew."

    "It was a small group, probably around 20 people, less than 10% of the total crewmembers."

    "A small escape pod was in the middle of the room, and it was clear that they were preparing to abandon the ship."

    "There was one person missing though..."

    q "Where's Yselle?"

    "Logan's face visibly darkened, and he looked pained."

    l "She's... she's dead. She was killed by that thing."

    if saw_gazer == True:

        q "That creature with fangs?"

        l "Fangs? I don't... oh god, you saw it? Did you look at it?"

        q "Yes, on one of the cameras... why?"

        l "Shit... that thing has somehow killed just the ones that have seen it..."

        "Immediately after Logan said that, a loud thud was heard from the gate, and a dent the size of a fist was in the middle of it."

        with hpunch

        l "What?!"

        "Crewmember" "It's that beast! It decided to attack!"

        "Crewmember" "Why now?!"

        l "Shit, looks like it knows we're escaping..."

        q "What should I do?"

        l "Run to the ship! Everyone, run to the ship, we have to go now!"

        "Crewmate" "But what of the others?!"

        l "Feel free to stay if you want! Everyone else, with me!"

        "Logan confidently started running towards the ship they were preparing just a few seconds ago."

        l "Looks like you are still a lucky guy, managed to get here last."

        q "I really don't feel lucky at all..."

        "Just before they started boarding the ship, another loud thud could be heard, along with the sound of metal creaking."

        with hpunch

        "The creature had punched a hole right through the door."

        l "Start the engine! Let's go!"

        "Through that hole, a glowing red eye could be seen."

        l "Do not look at it! Remember what happened to everyone else!"

        "The ship's engine finally started, and all the people in the docks had boarded."

        "Except for one person, a kid that foolishly stared at the door."

        "He was frozen in place, staring at the eye."

        "Crewmember" "Hey, kid! Snap out of it!"

        "Crewmember" "Someone, grab him!"

        l "No! Leave him! We have to go now! He is already gone"

        q "Logan! He's just a kid!"

        l "I know! But there's nothing we can do for him now!"

        "The ship started to move, floating in the air, and the hole in the door had gotten bigger by the creature that was using its massive strength to break through."

        jump sacrifice1

    else:

        q "What thing?"

        l "It's a good thing you haven't seen it, there's a beast roaming the ship, but it just kills the one that see it."   

        "Immediately after Logan said that, a loud thud was heard from the gate, and a dent the size of a fist was in the middle of it."

        with hpunch

        l "What?!"

        "Crewmember" "It's that beast! It decided to attack!"

        "Crewmember" "Why now?!"

        l "Shit, looks like it knows we're escaping..."

        q "What should I do?"

        l "Run to the ship! Everyone, run to the ship, we have to go now!"

        "Crewmate" "But what of the others?!"

        l "Feel free to stay if you want! Everyone else, with me!"

        "Logan confidently started running towards the ship they were preparing just a few seconds ago."

        l "Looks like you are still a lucky guy, managed to get here last."

        q "I really don't feel lucky at all..."

        "Just before they started boarding the ship, another loud thud could be heard, along with the sound of metal creaking."

        with hpunch

        "The creature had punched a hole right through the door."

        l "Start the engine! Let's go!"

        "Through that hole, a glowing red eye could be seen."

        l "Do not look at it! Remember what happened to everyone else!"

        "The ship's engine finally started, and all the people in the docks had boarded."

        "Except for one person, a kid that foolishly stared at the door."

        "He was frozen in place, staring at the eye."

        "Crewmember" "Hey, kid! Snap out of it!"

        "Crewmember" "Someone, grab him!"

        l "No! Leave him! We have to go now! He is already gone"

        q "Logan! He's just a kid!"

        l "I know! But there's nothing we can do for him now!"

        "The ship started to move, floating in the air, and the hole in the door had gotten bigger by the creature that was using its massive strength to break through."

    menu: 

        "Leave with the rest":

            "Quinn would have leaped towards that kid to help him in a heartbeat, had not the recent events left a scar in his mind."

            "He knew in the back of his mind that he would not be able to help him, and that he would only be able to die with him."

            show gazer angry at truecenter
            with dissolve

            a "WRAAAAAAAAAAAAAAA!!!"

            "They could hear the beast enraged scream, perhaps at the fact that it had lost its prey."

            "Quinn was tempted to look at it, but he knew better than that by now."

            "The ship finally left the docks, and seconds later, had already escaped the ship."

            "He was finally safe, but he could not help but feel like this was not a win."

            "All those deaths...Yselle..."

            l "We made it...Shit, we made it"

            "But at least, he was not alone."

            q "Why cuss at that?"

            l "I...I don't know, I just want to rest..."

            q "I'm never going back to space..."

            "After going through hell, they were finally safe."

            "..."

            "{i}Or were they{/i}"


        "Save the kid":

            jump sacrifice

 
label yselle_ending:

    scene normal_docks with dramatic

    "Yselle was standing in front of him, and she was alive."

    show yselle scared at left

    y "Quinn! Oh god thank you, you're alive"

    q "Yselle!"

    "He ran to her and embraced her. They usually would have refrained from such demonstrations of affection but they couldn't care about that right now."

    "For the first time in a while, Quinn felt hope."

    "He went past the door, which was immediately shut behind him, and he was greeted by the sight of the rest of the surviving crew."

    "It was a small group, probably around 20 people, less than 10% of the total crewmembers."

    "A small escape pod was in the middle of the room, and it was clear that they were preparing to abandon the ship."

    "There was one person missing though..."

    q "Where's Logan?"

    "Yselle's face visibly darkened, and she looked pained."

    y "He's... he died. He was killed by that thing."

    if saw_gazer == True:

        q "That creature with fangs?"

        y "What do you mean by fangs...oh, no, you saw it? Did you look at it?"

        q "Yes, on one of the cameras... why?"

        y "No no no! That thing has somehow killed just the ones that have seen it..."

        "Immediately after Logan said that, a loud thud was heard from the gate, and a dent the size of a fist was in the middle of it."

        with hpunch

        y "What is that?!"

        "Crewmember" "It's that beast! It decided to attack!"

        "Crewmember" "Why now?!"

        y "It somehow knows we're about to leave... we have to go now!"

        q "What should I do?"

        y "Run, get to the ship! Everyone, run to the ship, we have to leave now!"

        "Crewmate" "But what of the others?!"

        y "I'm sorry but we can't risk everyone here...I'm sorry"

        "Yselle started running towards while wearing a heavy expression to the ship they were preparing just a few seconds ago."

        y "I thank whatever deity guided you here Quinn, a few more seconds and you had been left behind."

        q "I don't know about deities, but I'm really thankful about that."

        "Just before they started boarding the ship, another loud thud could be heard, along with the sound of metal creaking."

        with hpunch

        "The creature had punched a hole right through the door."

        y "It is breaking through, we have to go now! Hurry!" 

        "Through that hole, a glowing red eye could be seen."

        y "Do not look at that! Remember what happened to everyone else!"

        "The ship's engine finally started, and all the people in the docks had boarded."

        "Except for one person, a kid that foolishly stared at the door."

        "He was frozen in place, staring at the eye."

        "Crewmember" "Hey, kid! Snap out of it!"

        "Crewmember" "Someone, grab him!"

        y "Oh no... I...I don't..."

        q "Let's save him!"

        y "We... can't, we will all die if we stop now."

        "The ship started to move, floating in the air, and the hole in the door had gotten bigger by the creature that was using its massive strength to break through."

        jump sacrifice1

    else:

        y "What thing?"

        y "There's a beast roaming the ship, killing just the ones that see it. Thankfully you haven't seen it."   

        "Immediately after Yselle said that, a loud thud was heard from the gate, and a dent the size of a fist was in the middle of it."

        with hpunch

        y "What is that?!"

        "Crewmember" "It's that beast! It decided to attack!"

        "Crewmember" "Why now?!"

        y "It somehow knows we're about to leave... we have to go now!"

        q "What should I do?"

        y "Run, get to the ship! Everyone, run to the ship, we have to leave now!"

        "Crewmate" "But what of the others?!"

        y "I'm sorry but we can't risk everyone here...I'm sorry"

        "Yselle started running towards while wearing a heavy expression to the ship they were preparing just a few seconds ago."

        y "I thank whatever deity guided you here Quinn, a few more seconds and you had been left behind."

        q "I don't know about deities, but I'm really thankful about that."

        "Just before they started boarding the ship, another loud thud could be heard, along with the sound of metal creaking."

        with hpunch

        "The creature had punched a hole right through the door."

        y "It is breaking through, we have to go now! Hurry!" 

        "Through that hole, a glowing red eye could be seen."

        y "Do not look at that! Remember what happened to everyone else!"

        "The ship's engine finally started, and all the people in the docks had boarded."

        "Except for one person, a kid that foolishly stared at the door."

        "He was frozen in place, staring at the eye."

        "Crewmember" "Hey, kid! Snap out of it!"

        "Crewmember" "Someone, grab him!"

        y "Oh no... I...I don't..."

        q "Let's save him!"

        y "We... can't, we will all die if we stop now."

        "The ship started to move, floating in the air, and the hole in the door had gotten bigger by the creature that was using its massive strength to break through."

    menu: 

        "Leave with the rest":

            "Quinn would have leaped towards that kid to help him in a heartbeat, had not the recent events left a scar in his mind."

            "He knew in the back of his mind that he would not be able to help him, and that he would only be able to die with him."

            show gazer angry at truecenter
            with dissolve

            a "WRAAAAAAAAAAAAAAA!!!"

            "They could hear the beast enraged scream, perhaps at the fact that it had lost its prey."

            "Quinn was tempted to look at it, but he knew better than that by now."

            "The ship finally left the docks, and seconds later, had already escaped the ship"

            y "We did it...finally..."

            "Tears ran down Yselle's eyes, she was visibly shaken by the escape, having to leave the kid behind. Who wouldn't be?"

            "He was finally safe, but he could not help but feel like this was not a win."

            "All those deaths...Logan..."

            "Quinn was also shaken, and he embraced Yselle, trying to comfort her, while also crying on his own."

            q "I...don't know what to do from now on..."

            y "Let's just...stay like this for a while, I'm scared that if I let go, this will all be a dream and I'll be on that ship again..."

            "Quinn didn't say anything, but just stayed there, holding her."

            "After going through hell, they were finally safe."

            "..."

            "{i}Or were they{/i}"


        "Save the kid":

            jump sacrifice

label sacrifice:

    scene normal_docks
    show quinn scared at right

    "The moment Quinn jumped out of the ship, he could hear the voices behind me screaming at him to come back, but it was too late for that"

    "He would not be able to live with himself if he didn't at least try to save the child."

    "Although he knew, that it would be futile, as it was in the end."

    show gazer at left
    with flash
    hide gazer

    a "Come see."

    "He tried his best not to look at the beast, that by now had already broken through the door."

    "Quinn went to grab the kid, but he saw the reflection in his eyes."

    "Those malevolent red eyes."

    show gazer angry at left

    "He could not help but look at it, and he felt his mind being torn apart."

    show eye at truecenter
    with fade

    "In a mere second, Quinn was no more."

    hide quinn with dramatic

    "..."

    "The beast had won."

    with dramatic

label sacrifice1:

    scene normal_docks
    show quinn at right

    "The moment Quinn jumped out of the ship, he could hear the voices behind me screaming at him to come back, but it was too late for that"

    "One would have thought Quinn did so to save the child."

    "But that was not the case."
    
    show eye at truecenter
    with dramatic

    "He did so to save himself."

    "He had to save himself from reality, from the pain that was existance."

    "He had to meet the savior sent from heaven to redeem him."

    hide eye
    show gazer at left

    "In a mere second, Quinn was no more."

    hide quinn with dramatic

    "..."

    "The beast had won."

    with dramatic

label aliendock:

    scene alien_docks with redflash

    "And he was greeted by a sight that made him feel like he was going to lose his mind."

    "A gigantic creature was standing in the middle of the docks, and it was looking at him."

    "The bodies of the crew members were scattered all over the place, and the creature was holding the body of the Yselle in its hands, missing her legs."

    "Logan's body was tattered and torn in a corner, skewed in an unnatural position, and it was clear that he had been killed by the creature."

    "Quinn felt like something in his mind snapped."

    show quinn scared at right

    "He grabbed a piece of pipe that was near him, and he started to run towards the creature."

    "Shadowy beasts started crawling up from the ground, trying to grab him, but he swong the pipe at them, and they disappeared."

    "The continued swinging until he reached the creature, and he started to hit it with all his might."

    "Why why why why why why why why"

    show eye at truecenter
    with flash
    hide eye

    "Why"

    show eye at truecenter
    with flash
    hide eye

    "Why"

    show eye at truecenter
    with flash
    hide eye

    "Why"

    show eye at truecenter
    with flash
    hide eye

    "Why"

    "Why did this happen to him?"

    "Why did he have to go through all of this?"

    "Why did he have to suffer so much?"

    scene normal_docks with fade

    "Suddenly, the scene before him changed."

    "There were no shadow beasts, no massive creature."

    "Just the bruised bodies of other crewmembers, and Quinn's hands were red an sticky with blood."

    q "What?...No..."

    q "NOOOOOOO!!!"

    "He started to scream, but it was cut short when he felt a hand placed in his shoulder."

    "He turned back to see, perhaps someone had survived."

    show gazer at left
    with fade

    "But it was no such happy ending."

    show gazer angry at left
    with redflash

    q "The eyes..."

    q "It was the eyes..."

    "And then, the one known as Quinn was no more."

    with dramatic



