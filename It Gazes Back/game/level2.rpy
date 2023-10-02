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

# Variables

$ saw_gazer = false

# The game starts here.

label corridor3:

    scene bloody_corridor_6 with dramatic

    "He knew that he had to keep moving, but the claustrophobia was getting to him. He felt like the walls were closing in on him, and he couldn't breathe."

    "This shaft had even less space than the one before, he had to crawl through most of it. And because this one went down, he had to crawl downwards, which was even more uncomfortable."

    "Also, as this shaft went below the floor of the room above, there was blood leaking out from the crevices in the ceiling."

    "Quinn crawled slowly through the shaft, his heart pounding in his chest. He could feel the blood dripping onto his skin, and the smell of it was making him gag."

    show quinn worried at right

    q "I have to get out of here, I have to get out of here now."

    if health < 5:

        "The pain was also getting worse due to the crawling"

    "He stopped crawling and took a deep breath. He tried to calm himself down, but it was no use. The claustrophobia was becoming too intense."

    if sanity < 3:

        "He clawed at the walls, trying to find a way out, but there was none."

    else: 

        "He tried to focus on another thoughts, unsuccessfully."
        
    "He took a deep breath and closed his eyes. He focused on his breathing and tried to relax. Even though he could not manage to calm himself, he could at least breathe again."

    "After managing to get his breathing under control, Quinn resumed his journey through the narrow ventilation shaft, until he finally reached the exit, and took a glance from the slits in the door."

    jump cameraroom

label cameraroom:

    scene corridor_3 with dramatic

    "Quinn took a glance from the slits in the door, and found that this room looked particularly untouched, there is no one to be seen."

    show quinn at right

    q "Finally, an open space to breathe..."

    "He steps out of the shaft with confidence, and looks around a bit more."

    "This is the Surveillance Room, where the cameras to most of the ship are located. Not all of the cameras are here, as the security team has their own camera room, but this one is often used to locate team members quickly."

    "Quinn takes a moment to breathe in air, something he felt like a scarce commodity while stuffed in the ventilation."

    "???" "You should be more careful when entering a room kid"

    show quinn scared at right
    with hpunch

    q "Who's that?!"

    "Quinn felt his heart stop for a moment, scared that he had just made a deadly mistake. He turned around to the source of that voice, only to find a wounded old man hiding beneath a desk."

    show han wounded at left
    with fade

    q "Mr. Han?! What happened to you?!"

    "Mr.Han, one of the senior welders in the ship. His face was a mess, with bloody wounds all over it, some of them already colored black."

    han "I... tried to find Ladeeva, I had already helped some other survivors get to the docks, but she wasn't there."

    han "Hoped... she was still alive, and I found her, but..."

    show quinn worried at right

    "Han blinks heavily a couple of times, and it's obvious he doesn't want to say the words."

    han "It was right in front of me... And they got me good when I ran to the ventilation, I won't... last much longer."

    q "Mr. Han, I-I can help you, here, let me just find something for the wounds-"

    han "Don't fool yourself... Quinn, right? You seem like a good kid, don't waste your time pointlessly and just go."

    q "..."

    "Quinn didn't want to leave the old man to his fate, but he was right, those wounds were not the kind of stuff you treated on the go, this room was going to be his resting place."

    q "I'm sorry..."

    han "Me too...just take this route, it will take you to the entrance of the docks, the others have sealed it so... you only need to call them out from the outside."

    q "Won't they suspect I'm like... the other ones?"

    han "No, if you speak... then you are good."

    "Quinn wanted to ask his meaning but refrained himself from doing so."

    "He stepped right in front of the entrance to the next shaft, steeling his mind to the fact that not only he'd be leaving Mr. Han to die alone, but also that he had no other choice but to enter again one of those cramped spaces."

    "There was a screen with the cameras, perhaps he could use that to gain an idea of what he was facing?"

    menu: 

        "Don't look":

            "But he thought again, somehow it felt like if he did so, he would look at something he would regret"

            q "Goodbye Mr. Han... thank you, and I'm sorry"

            "The old man laughed"

            han "Yes yes, go on, don't tell anyone about this, it will leave a sour taste."

            "Quinn smiled wryly, and entered the shaft."

            jump fork1

        "Take a quick glance":

            "Quinn felt he needed to have at least an idea of the situation or he wouldn't be able to make it. What if he ran into another Alan?"

            "He directed a brief look at the control panel which showed all the active cameras. More than half of them only showed a gruesome scenario, rooms full of blood and without any bodies to be seen."

            "But on one camera, he saw Alan, running like a madman, going from one area to another while limping from one leg, perhaps due to their encounter a few minutes ago."

            "And on another camera..."

            han "NO! Don't look at them!"

            "Quinn wanted to retort, but he found the words drowning in his own throat."

            show eye at truecenter
            with flash
            hide eye
            show eye at truecenter
            with flash
            hide eye

            $ sanity -= 1

            "The eye, once again, appeared inside of his own mind."

            "Quinn grabbed his head in pain, as if a screwdriver was being slowly pushed into it, but luckly it subsided faster than before."

            "Han was trying to get up, unsuccessfully, with fear etched in his face."

            han "Never, never try to look at them! You hear me? You can only see the infected ones, but not..."

            "Han clutched his chest mid-sentence, then gasped for air."

            "Quinn got down to help him, but it was too late, the old man had passed away almost immediately, perhaps due to the stress of the moment."

            "He could not make sense of the words of Han, but he decided it would be best to heed them. Honoring his last words, Quinn went in the shaft without trying to look to the cameras again."

            jump fork1

        "Look throughly so you have a better chance":

            "Quinn felt he needed to have at least an idea of the situation or he wouldn't be able to make it. What if he ran into another Alan?"

            "He stepped in front of the control panel which showed all the active cameras. More than half of them only showed a gruesome scenario, rooms full of blood and without any bodies to be seen."

            "But on one camera, he saw Alan, running like a madman, going from one area to another while limping from one leg, perhaps due to their encounter a few minutes ago."

            "And on another camera, he thought at first that it was one of the crazed crew, but on closer inspection, this was not human"

            show gazer at center

            "This was an alien creature. Was this thing responsible of everything that was happening?"

            han "NO! Don't look at them!"

            "Quinn wanted to retort, but he found the words drowning in his own throat."

            show eye at truecenter
            with flash
            hide eye
            show eye at truecenter
            with flash
            hide eye

            $ sanity -= 2
            $ saw_gazer = true

            "The eye, once again, appeared inside of his own mind."

            a "We see..."

            "Quinn grabbed his head in pain, as if multiple screwdrivers were being slowly pushed into it, but luckly it subsided faster than before."

            "Han was trying to get up, unsuccessfully, with fear etched in his face."

            han "Never, never try to look at them! You hear me? You can only see the infected ones, but not..."

            "Han clutched his chest mid-sentence, then gasped for air."

            "Quinn got down to help him, but it was too late, the old man had passed away almost immediately, perhaps due to the stress of the moment."

            "He could not make sense of the words of Han, but he decided it would be best to heed them. Honoring his last words, Quinn went in the shaft without trying to look to the cameras again."

            jump fork1

label corridor4:

    scene bloody_corridor_4 with dramatic

    "He knew that he had to keep moving, but the claustrophobia was getting to him. He felt like the walls were closing in on him, and he couldn't breathe."

    "This shaft had even less space than the one before, he had to crawl through most of it. And because this one went down, he had to crawl downwards, which was even more uncomfortable."

    "Also, as this shaft went below the floor of the room above, there was blood leaking out from the crevices in the ceiling."

    "Quinn crawled slowly through the shaft, his heart pounding in his chest. He could feel the blood dripping onto his skin, and the smell of it was making him gag."

    show quinn worried at right

    q "I have to get out of here, I have to get out of here now."

    if health < 5:

        "The pain was also getting worse due to the crawling"

    "He stopped crawling and took a deep breath. He tried to calm himself down, but it was no use. The claustrophobia was becoming too intense."

    if sanity < 3:

        "He clawed at the walls, trying to find a way out, but there was none."

    else: 

        "He tried to focus on other less disheartening thoughts, unsuccessfully."
        
    "He took a deep breath and closed his eyes. He focused on his breathing and tried to relax. Even though he could not manage to calm himself, he could at least breathe again."

    "After managing to get his breathing under control, Quinn resumed his journey through the narrow ventilation shaft, until he finally reached the exit, and took a glance from the slits in the door."

    jump living_quarters

label living_quarters:

    scene bloody_corridor_5 with dramatic

    "Quinn took a glance from the slits in the door, and found that this room looked particularly untouched, there is no one to be seen."

    show quinn at right

    q "Finally, an open space to breathe..."

    "He steps out of the shaft with confidence, and looks around a bit more."
