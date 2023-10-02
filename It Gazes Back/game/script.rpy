# The script of the game goes in this file.

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
define flash = Fade(.25, 0.0, .75, color="#fff")

# Definitions of values

default health = 5
default sanity = 5

# The game starts here.

label start:

    $ renpy.clear_game_runtime()

    "This is the Stellaris, a mining and repair ship that has been in service for over 30 years. It is currently on a routine mission to repair a mining station in the outer reaches of the solar system."

    "Due to the design standards of the time, the ship is quite small for the amount of crew members it holds, and that becomes even more notorious when, to try and save costs, Rymond Corp. decided to fit 200 people in a ship meant for 120."

    "The crew has gotten used to the cramped conditions, and the ship has become a second home to them. They have been on this mission for 3 months now, and they still have 2 more to go before they can return to their homes."

    "The cargobay is one of the ship's most concurred areas, as most of its technical crew works there. Among them, a couple of young technicians are working on a broken circuit board."

    "'Hey, can you pass me that laser adaptator?'"
    
    scene cargobay
    with fade

    show quinn at right

    q "Sure, here you go. So, how's the day treating you?"

    "The adaptator leaves Quinn's hands and forms an arc, falling in the hands of the other technician."

    show logan at left

    l "It's so quiet and boring out here. Nothing ever happens on these space travels."

    q "Well, that's a good thing, right? I mean, you don't want anything {i}actually unexpected to happen in space{/i}."

    l "Yeah yeah I know, It's just so boring out here, stuck doing the same repair work day in and day out."
    
    l "The only interesting thing to happen is when a meteorite hits the ship and we have to fix the hull, or a circuit overloads and we have to spend hours in those damn suits while we fix it."

    q "Yeah, I know what you mean. I'm just glad we're not on a military ship. I hear they have to deal with pirates and stuff."

    l "I think I would prefer it there. Here it's like we're on a never-ending loop. Fixing broken equipment, checking inventory, and all that jazz. I'm surprised you've lasted this long, with your claustrophobia and all."

    "The sound of the intense hammering from the other side of the cargo bay suddenly intensifies."

    show alan at center

    alan "..."

    q "And what about that guy? He's been hammering away like a madman for hours now. What is it now, the 5th day in a row?"

    l "Alan? Yeah, some of the guys are really worried about him, he's been acting strange for the past couple of weeks, and now with that hammering, he says he's fixing some loose plates but I don't know...But he's one of the seniors, he's been at this for like two decades."
    
    hide alan

    l "Once they get to that point, they live in their own little world, tinkering away without a care, as if they are robots instead of humans."

    q "Might be the only way to stay sane out here. I mean, we're stuck in this tin can for months at a time."

    "Logan lets out a long sigh."

    l "I always thought being a technician in space would be more adventurous."

    q "Remember that time when the gravity control system malfunctioned? We were floating around like astral explorer minus the cool suits. You could count that as an adventure"

    "They both chuckle at the memory."

    l "Oh man, I thought we were going to be stuck up there forever."

    q "Not everyone gets the chance to work in space, you know? I mean, we're {i}technicians{/i} in space. That's pretty cool."

    l "Yeah, I guess you're right. I just wish we could do something more exciting."

    q "Well, we could always go to the bar and get shitfaced afterwards, you know, the ol'reliable solution to any and all problems in life."

    l "Haha, yeah, I guess we could do that. I shouldn't complain too much. It's still a pretty cool gig when you think about it."

    l "What do you say we head to the dining hall for some dinner? I'd hate to get drunk on an empty stomach again, last time I did that I woke up in the med bay."

    menu:

        "Let's go stuff our faces.":
            jump dininghall

        "Not hungry yet, let's go in a while, let me finish this first.":
            jump cargobay

label dininghall:

    scene dininghall
    with fade

    "The dining hall of the Stellaris is a large room compared to most of the common areas of the ship, but it is still quite small considering that almost two hundred people inhabit the vessel, and usually most of them converge in this very room at the same time."

    "The duo enter the dining hall and head towards the food counter."
    
    show quinn at right

    q "What are we having today Ms. Ladeeva?"

    show ladeeva at center

    ladeeva "Hi Quinn! Japanese omellete with rice, packed meat sticks and microgreens."

    show logan at left
    
    l "Meat! Nice!"

    q "I do not know how you can eat that stuff, it's so bland."

    l "Meat is meat my friend, and as you said, I should not complain, we are in space after all."

    q "Ugh..."

    ladeeva "Oh don't pout Quinn, go eat your protein, you know that for once, Logan is right."

    q "Fine, fine, guess I'll just swalow it down."

    ladeeva "Attaboy!"

    hide ladeeva
    hide logan
    hide quinn
    with fade

    "They both grab their trays and head towards the tables."

    "The dining hall is full of people, which is quite common given the reduced size of the hall for the amount of people it holds, and the noise of the conversations and the clattering of the cutlery is almost deafening."

    show quinn at right
    
    q "Why did they have to enforce that you can't eat in your room? I can barely hear myself think in here."

    show logan at left
    
    l "You can't get rid of the roaches then, you know, they only need a bit of food and a small space to crawl into and then you have a full colony of them."

    q "Well, it does suck to find one of the flying ones in your bed."

    q "Let's just eat fast then."

    "They start eating, but then, there's a commotion on the far side of the hall."

    q "What's that?"

    "They both look towards the commotion."

    hide logan
    hide quinn
    show alan at center

    alan "..."

    show yselle at left

    yselle "What the hell is that?!"

    "Due to the amount of people in front of them, they are not able to see the reason for all the fuzz, but Quinn manages to get a glance at something."

    hide alan
    hide yselle
    hide logan
    show alieneye at truecenter
    with dramatic

    "A red eye, sitting inside a ball of bloody flesh"

    with vpunch

    "Quinn's heart pounded in his chest as he stared at eye. He had seen many strange things in his time in space, but nothing like this. The eye was bloodshot and unblinking, its red iris staring up at him with an intelligence that was both alien and malevolent."

    "He took a step back unconciously and bumped into Logan, who was still trying to see what was going on."

    hide alieneye

    show logan at left

    l "Hey, did you see what happened? What is it?"

    hide logan

    "Quinn could not respond."

    "Even though the people in front of him had blocked his view of the ball of flesh, it was still vivid in his mind, and he felt..."

    "He felt like he could still see the eye, and it looked directly at him"

    show eye at truecenter
    with dissolve

    "Quinn felt a wave of nausea wash over him, as if his brain was being scrambled, trying to make sense of something that was beyond its comprehension. He knew he should turn away, but he couldn't, he could still see that eye even if he closed his own."

    l "Dude, are you ok? You are pale as a ghost."

    "He could hear Logan's voice, but it sounded distant, as if he was underwater."

    menu:

        "Run, anywhere but run!!!":
            jump dininghallrun


        "Ask Logan for help":
            jump askforhelp

label cargobay:

    scene cargobay

    show logan at left
    
    l "Fine, I'm not that hungry yet anyways, how can I help you?"

    show quinn at right

    q "Are you so free that you have time to help someone else?" 

    "They both chuckle"

    l "I have absolutely no issue with just sitting here and watching you slave away, all of my work for the day is basically done."

    q "Alright, then hold this for me will you?"

    scene cargobay
    with fade

    "They keep working around Quinn's tasks for several minutes in where they actually manage to complete everything that Quinn needed to do"

    show quinn at right

    q "Ok, that's done, I'll have to brag to Yselle about this later."

    show logan at left

    l "Ho? Are we that close now? I thought you were still trying to get her to go out with you."

    q "I haven't, we just enjoy talking to each other"

    l "Aha, sure... You want to snuggle your supervisor, nothing wrong with that"

    q "Screw you, punk"

    "Even though it looks like they are arguing, both of them are smiling, so it's all playful banter"

    "But suddenly..."

    with hpunch

    "There's a commotion coming from the dining hall's direction, like multiple people screaming"

    l "What's that?"

    q "I don't know... looks like screams, perhaps there was an accident in the kitchen, let's go there."

    "They start walking towards the dinig hall, but then they see Alan running in full sprint in their direction"

    show alan bloody at center

    q "What the..."

    "Alan looks completely unhinged, and his face looks like it was smeared with blood"

    hide alan

    l "Did he go completely nuts from a moment ago?"

    "Quinn was about to reply to his friend but he saw that Alan was holding something in his arms while running"

    "It was only for a brief moment, but Quinn took a look at it"

    show alieneye at truecenter
    with dramatic

    "A red eye, sitting inside a ball of bloody flesh"

    with vpunch

    "Quinn's heart pounded in his chest as he stared at eye. He had seen many strange things in his time in space, but nothing like this. The eye was bloodshot and unblinking, its red iris staring up at him with an intelligence that was both alien and malevolent."

    hide alieneye
    
    "With all of that going through his head, Quinn is stunned, unable to move."

    "Alan continues running and goes past them, but directs a very suspicious glance at Quinn before he turns his head forward."

    l "What in the...looked like he was carrying something, but why such a rush? Did something happen back there?"

    l "Hey, are you ok? You look pale dude"

    "Quinn could not respond."

    "That thing... he only glanced at it for a mere instant, but in his mind..."

    "He felt like he could still see the eye, and it looked directly at him"

    show eye at truecenter
    with dissolve

    "Quinn felt a wave of nausea wash over him, as if his brain was being scrambled, trying to make sense of something that was beyond its comprehension. He knew he should turn away, but he couldn't, he could still see that eye even if he closed his own."

    l "Hey Quinn, you ok?"

    "He could hear Logan's voice, but it sounded distant, as if he was underwater."

    menu:

        "Run, anywhere but run!!!":
            jump cargobayrun


        "Ask Logan for help":
            jump askforhelp

label cargobayrun:

    scene cargobay
    
    show quinn scared at right

    q "I...I have to go, need to get out of here"

    show logan at left

    l "What do you mean? Where are you going?"

    hide logan

    "Quinn doesn't even reply back to Logan, but starts leaving the cargo bay in a hurry. He's not even looking at where he is going."

    "His footsteps are irregular, and his breathing is shallow."

    "Before he can leave the bay, a figure bumps into him."

    show yselle scared at left

    yselle "Quinn! Thank god, please you have to come with me, something is happening to the others..."

    "Quinn manages to snap out of his trance and looks at Yselle, she's clearly agitated as well"

    q "The others? What..."

    show eye at truecenter
    with flash
    hide eye
    show eye at truecenter
    with flash
    hide eye

    "The eye...it flashes in Quinn's mind again, like a beacon lighting up the darkness"

    show eye at truecenter
    with flash
    hide eye
    show eye at truecenter
    with flash
    hide eye

    "Quinn's consciousness fails, as Yselle panic multiplies when she sees him drop down to the floor"

    yselle "QUINN! No no no we have to get out of here! Help!"

    "The last thing Quinn sees is her face before it all goes to black"

    jump tunnels_yselle

label dininghallrun:

    scene dininghall
    
    show quinn scared at right

    q "I...I have to go, need to get out of here"

    show logan at left

    l "What do you mean get out of here? What, is it your ex or something?"

    hide logan

    "Quinn doesn't even reply back to Logan, but starts leaving the dining hall in a hurry."

    "His footsteps are irregular, and his breathing is shallow."

    "Before he can leave the dining hall, a figure steps in front of him, looking at Quinn with worry."

    show ladeeva at left

    ladeeva "Quinn, son, are you feeling alright? Want seconds? You look pale, let me give you a hand"

    "Quinn was about to turn her down when a scream was heard from the other side of the hall"

    show eye at truecenter
    with flash
    hide eye

    "Another scream, now much closer"

    show eye at truecenter
    with flash
    hide eye
    show eye at truecenter
    with flash
    hide eye

    "Before Quinn is able to react, he feels like his consciousness fails him, and then it all goes black"

    jump tunnels_yselle

label askforhelp:

    show quinn scared at right
    
    "Quinn turned to Logan, who was looking at him with a worried expression, and tried to vocalize a call for help, as he knew his best friend would be there for him, but no voice came out of his throat."

    "He tried to move, but his body felt like it was made of lead, unable of even lifting his own arms."

    "Logan reached out and touched Quinn's arm. Quinn felt a jolt of electricity run through his body, and he staggered backwards. Logan looked at his hand in shock."

    show logan scared at left

    l "What the hell?"

    "Finally, Quinn breathed out, and his voice came back to him."

    menu: 

        "I saw an eye...":

            l "An eye? Whose eye? What the hell was that?"

            q "I...I don't know, I just saw an eye, it was red and it was staring at me, I don't know what it was, but it was..."

            "Before they are able to continue the conversation, there's a scream heard near them."

            l "What was that now?"

            show eye at truecenter
            with flash
            hide eye

            "Another scream, now much closer"

            show eye at truecenter
            with flash
            hide eye
            show eye at truecenter
            with flash
            hide eye

            "Before Quinn is able to react, he feels like his consciousness fails him, and then it all goes black"

            jump tunnels_logan

        "I...I-I don't know":

            l "What do you mean you don't know? You got paler than the meat sticks, spit it out, what was that?"

            q "It's true! I have no idea what that was, it... it is hard to describe it"

            l "Well guess I'll just have to take a look then..."
            
            "Before they are able to continue the conversation, there's a scream heard near them."

            l "What was that now?"

            show eye at truecenter
            with flash
            hide eye

            "Another scream, now much closer"

            show eye at truecenter
            with flash
            hide eye
            show eye at truecenter
            with flash
            hide eye

            "Before Quinn is able to react, he feels like his consciousness fails him, and then it all goes black"

            jump tunnels_logan

        "*Stay silent*":

            "Quinn just stared at Logan like a deer before headlights"

            l "What is it man? You are freaking me out, also how did you pass so much static, are you suddenly made of copper?"

            "Before they are able to continue the conversation, there's a scream heard near them."

            l "What was that now?"

            show eye at truecenter
            with flash
            hide eye

            "Another scream, now much closer"

            show eye at truecenter
            with flash
            hide eye
            show eye at truecenter
            with flash
            hide eye

            "Before Quinn is able to react, he feels like his consciousness fails him, and then it all goes black"

            jump tunnels_logan

    return
