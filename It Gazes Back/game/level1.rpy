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
image gazer baby = "gazer_baby.png"
image yselle_note = "ysellenote.png"
image logan_note = "loganote.png"
define flash = Fade(.25, 0.0, .75, color="#fff")
define redflash = Fade(.25, 0.0, .75, color="#bc1212")


# The game starts here.

label tunnels_logan:

    scene tunnels_logan with dramatic

    "An unknown amout of time passes before Quinn manages to wake up"

    show quinn at right
    with dissolve

    q "Ugh...my head"

    "Quinn grabs his head, as he has a splitting headache that threatens to turn the content of his stomach the opposite way."

    q "What... eh? A note?"

    show logan_note at truecenter
    with fade

    "He grabs the note with his hand, and recognizes Logan's handwriting from this"

    "He reads it for a while but fails to make sense of it immediately"

    q "But, what does this all mean? 'Use the shafts'? 'don't be seen'? 'red'-wait"

    hide logan_note
    show eye at truecenter
    with flash
    hide eye
    show eye at truecenter
    with flash
    hide eye

    q "That thing... I remember"

    "He glances around, and recognizes that he is not inside a room or the medical bay..."

    "He is inside a ventilation shaft."

    "The ventilation shaft was a narrow, dark, and compressed passageway that wound its way through the heart of the spaceship." 
    
    "It was barely large enough for a human to squat through, and the only light came from the faint glow of the emergency lights that were scattered at intervals along the walls."

    q "Just what the hell happened here?"

    "Had he not experienced the red eye's glance before, he would not have believed any of this to be anything but a joke, a prank played to him by some of the crew"

    "But he felt it in his guts, there was something else going on here"

    q "Alright, let's just do as he said, keep to the shafts... fuck"

    "There was one problem with that...Quinn had a problem with enclosed spaces, especifically, he suffered from claustrophobia."

    q "Well, this had to happened sooner or later, facing your fears... I should have gone to therapy sooner"

    q "Forget about it, let's see, the shafts are not connected to each other, they connect areas to other areas but they are not connected to each other, so I have to use the shaft to go to a room, and then enter the next shaft there"

    q "Why did they really have to design this freaking ship like this...I have no idea where I am right now, so I guess I have to go to the next room and see, find out how far I am from the docks"

    q "Alright Quinn, you've got this... you've got this"

    hide quinn
    with fade

    "The air in the shaft felt thick and heavy, as if he was walking through a swamp, and it was difficult to breathe. The metal walls grated against Quinn's skin as he had to advance some parts squatting, some parts crawling through the narrow space."

    "Quinn's heart pounded in his chest, and breaths came in shallow gasps."

    "He had to swallow his own panic to be able to continue forward. And he did, until he finally found the end of this particular shaft. The shafts had the particularity of being easy to enter, as a ship so crowded like this one needed a way for emergency staff to move through rooms without having to navigate crowds of people."

    "At the end of the shaft, a small door, barely enough to crawl out of, was a beacon of misguided hope for Quinn, who at this point only wished to be out of this horrible situation."

    "But then, the smell, it hit him... A ventilation shaft does, well, ventilate, and the many smells of each room go through it until they are extinguished by the next room's smell. But this smell, it was not a smell that should be found here, it was metallic and acrid, leaving a foul taste in one's mouth."

    "It smelled of {i}blood{/i}."

    scene bloody_corridor_4
    with dramatic

    show quinn scared at right
    
    q "..."

    "Quinn's heart skipped a beat, and he felt his stomach turn. He had to swallow his own vomit, and he felt his eyes water."

    "He recognized this pathway, this is one of the main corridors of the ship, connected on one side to the dining hall, and another to one of the living quarters."

    "The once dark silver metallic pathway is now a sickly red, splattered with blood and gore, painting a macabre scene that sends shivers down the spine."

    "The walls are adorned with dark streaks and handprints, radiating the desperation of the ones that were here before."

    "This... this was a massacre, a slaughter, a bloodbath. What the hell happened here?!"

    menu:

        "Turn back":

            $ sanity -= 1
            
            scene tunnels_logan with fade
            
            "As Quinn turns back as fast as he can, he can no longer hold his puke, and let's it all out inside the shaft, now filled with the combinated smells of blood and vomit."

            show quinn worried at right
            
            q "...I-I can't..."

            "His breathing was ragged, he felt like he was about to pass out, but the memory of what happened before came to him. Who knew how things would look if he were to pass out again? He had to move, quickly."

            "He focused as much as possible on his survival, trying to forget about the smells and how it felt like the walls of the shaft moved and closed in on him. He moved forward..."

            "Only to find himself face to face with debris blocking the other side of the shaft."

            "He felt his heart skip a beat, and his mind struggling to accept this."

            q "The note..."

            "Yeah, the note he found on himselft when he woke up, perhaps it had been Logan that blocked this exit when he left him there."

            "If so, then going back would not be any better, which made Quinn think how could the sight of that corridor be the better choice between the two."

            "He didn't want to find out. As hard as it was to go through this again, he returned to the entrance of the corridor, and went in."

            jump corridor1

        "Go in":

            jump corridor1


label corridor1:

    scene bloody_corridor_4 with dramatic
    
    "The floor, normally a sturdy structure, now sinks beneath Quinn's feet, slick with a combination of blood and bodily fluids."

    "He feels his stomach turn when he takes a step forward and feels something squishy get crushed by his foot, and he has to swallow his own vomit again."

    show quinn scared at right

    q "Oh God..."

    "He had to move, get to the next shaft and keep moving like that until he reached the docks."

    "The entrance to the next shaft was luckily very close, just a couple dozen steps away from him. As he was finally out of the ventilation system, he could at least move around with more freedom."

    "Quinn took careful steps, trying to be as stealthy as possible, even though there was no one close, no one alive at least."

    "In a moment, he was already in front of the next shaft."

    "He went to open it, as he could do so by just flipping a couple of switches near it and pressing a confirmation button."

    "When we was about to press the button, the last step to open the shaft, he heard a noice behind him."

    "It was still far away, probably even on the previous room, but he was sure he heard something moving."

    menu: 

        "Turn back":

            "Quinn reacted by inertia, without really thinking, forgetting for a moment the contents of the letter."

            "At first, there was nothing, but then, a familiar face popped up from the end of the corridor."

            show alan crazy at left

            "It was Alan, but there was something... unnerving about him."

            "He was covered from head to toe in blood stains, some looked dry and some fresh."

            "And he was looking straight at Quinn, with the most crazed smile he had ever seen."

            q "Alan?..."

            "Quinn muttered the name, but he refrained from calling out to him. But it was of no use, Alan immediately started sprinting towards Quinn."

            "Quinn felt his heart skip a beat, and rushed to open the shaft."

            "He managed to get it open but Alan got to him before he could get down to enter"

            $ sanity -= 1
            $ health -= 1

            with redflash
            
            "Quinn felt something piercing his shoulder, and he felt his body go numb. He looked at his shoulder, and saw a knife sticking out of it."

            with vpunch
            
            "He pushed Alan back, and empowered by pure adrenaline, managed to even make him tumble to the ground. Quinn used this moment to get inside the shaft and close it behind him."

            hide alan
            
            "He started crawling as fast as possible to get away from him, but he noticed after a few seconds that Alan was not pursuing him."

            "Why was that, he did not understand, but he was grateful of it. "

            "He had been stabbed in the shoulder, and the knife was still there. Quinn knew he had to remove it if he wanted to survive. The thought of being trapped in the shaft, covered in his own blood, was too much to bear. "

            "He was still having a hard time taking all in and know he had been stabbed! And he wasn't even allowed the time to process all of this. He took a deep breath and tried to calm himself down. He told himself that he had to be strong, that he had to survive."

            "He carefully reached up with his other hand and felt for the knife. He could feel the warm, sticky blood on his fingers. Taking another deep breath, Quinn gripped the handle of the knife and pulled it out in a swift motion."

            "The blood spurted out of the wound, and he felt himself getting dizzy. The pain was immense, making him drop the knife into a deep crevice."

            if sanity < 3:

                "Perhaps due to his own deteriorating state of mind, he managed to put the pain behind and continue through the shaft."

                jump corridor3

            else: 

                "But the mental pressure that came from the fact that he knew that Alan was still behind the other side of the shaft put enough pressure into Quinn that he soldiered through and advanced down the shaft."

                jump corridor3

        "Open the shaft and get in quickly!":

            "Quinn pressed the button, and the door opened with a click."

            "He had to get on his knees to get in and he did so as fast as he could possibly manage"

            menu:

                "Continue forward":

                    jump corridor3

                "Look back":

                    "Quinn felt the need to look back, the curiosity getting the better of him, and how to blame him? He had just seen a scene straight out of the most terrible nightmares one could have, and still had no idea of exactly what was going on."

                    "He soon regretted his decision."

                    show alan crazy at left

                    q "Alan?..."

                    "Quinn muttered the name, but he refrained from calling out to him."

                    "Alan looked haggard, with blood all over his body, but one could tell, even from a distance, that there was a crazed smile on his face, as if he was having the time of his life."

                    "He was holding a knife, and was looking at the entrance of the shaft, as if he was waiting for someone to come out of it."

                    $ sanity -= 1

                    with vpunch
                    
                    "Quinn felt his heart skip a beat, and his mind struggling to take this all in."

                    "He had to move, quickly."

                    with fade

                    jump corridor3


label tunnels_yselle:

    scene tunnels_yselle with dramatic

    "An unknown amout of time passes before Quinn manages to wake up"

    show quinn at right
    with dissolve

    q "Ugh...my head"

    "Quinn grabs his head, as he has a splitting headache that threatens to turn the content of his stomach the opposite way."

    q "What... eh? A note?"

    show yselle_note at truecenter
    with fade

    "He grabs the note with his hand, and recognizes Yselle's handwriting from this. He sees that same handrwiting in all of his performance reviews."

    "He reads it for a while but fails to make sense of it immediately"

    q "But, what does this all mean? 'Keep to the shafts'? 'don't be seen'? 'red'-wait"

    hide yselle_note
    show eye at truecenter
    with flash
    hide eye
    show eye at truecenter
    with flash
    hide eye

    q "That thing... I remember"

    "He glances around, and recognizes that he is not inside a room or the medical bay..."

    "He is inside a ventilation shaft."

    "The ventilation shaft was a narrow, dark, and compressed passageway that wound its way through the heart of the spaceship." 
    
    "It was barely large enough for a human to squat through, and the only light came from the faint glow of the emergency lights that were scattered at intervals along the walls."

    q "Just what the hell happened here?"

    "Had he not experienced the red eye's glance before, he would not have believed any of this to be anything but a joke, a prank played to him by some of the crew"

    "But he felt it in his guts, there was something else going on here"

    q "Alright, let's just do as she said, keep to the shafts... fuck"

    "There was one problem with that...Quinn had a problem with enclosed spaces, especifically, he suffered from claustrophobia."

    q "Well, this had to happened sooner or later, facing your fears... I should have gone to therapy sooner"

    q "Forget about it, let's see, the shafts are not connected to each other, they connect areas to other areas but they are not connected to each other, so I have to use the shaft to go to a room, and then enter the next shaft there"

    q "Why did they really have to design this freaking ship like this...I have no idea where I am right now, so I guess I have to go to the next room and see, find out how far I am from the docks"

    q "Alright Quinn, you've got this... you've got this"

    hide quinn
    with fade

    "The air in the shaft felt thick and heavy, as if he was walking through a swamp, and it was difficult to breathe. The metal walls grated against Quinn's skin as he had to advance some parts squatting, some parts crawling through the narrow space."

    "Quinn's heart pounded in his chest, and breaths came in shallow gasps."

    "He had to swallow his own panic to be able to continue forward. And he did, until he finally found the end of this particular shaft. The shafts had the particularity of being easy to enter, as a ship so crowded like this one needed a way for emergency staff to move through rooms without having to navigate crowds of people."

    "At the end of the shaft, a small door, barely enough to crawl out of, was a beacon of misguided hope for Quinn, who at this point only wished to be out of this horrible situation."

    "But then, the smell, it hit him... A ventilation shaft does, well, ventilate, and the many smells of each room go through it until they are extinguished by the next room's smell. But this smell, it was not a smell that should be found here, it was metallic and acrid, leaving a foul taste in one's mouth."

    "It smelled of {i}blood{/i}."

    scene b_dining_hall with dramatic

    show quinn scared at right
    
    q "..."

    "Quinn's heart skipped a beat, and he felt his stomach turn. He had to swallow his own vomit, and he felt his eyes water."

    "This was the dining hall of the ship."

    "The dining hall was a scene of carnage. The floor was slick with blood, and blood stains splattered the walls and tables. Some of the chairs were overturned, as if diners had fled in terror. Others remained upright, empty and silent."

    "The air was thick with the smell of blood and rot. It was a smell that made one's stomach churn and skin crawl."

    "There were no bodies in sight, but it was clear that someone or something had been killed in this room. The blood was still fresh, and there were pools of it on the floor that had not yet had time to congeal."

    "A few of the tables were still set, with plates, silverware, and glasses arranged neatly. But the food that had been served on them was long gone, and the plates were now covered in a thick layer of blood."

    "This... this was a massacre, a slaughter, a bloodbath. What the hell happened here?!"

    menu:

        "Turn back":

            $ sanity -= 1
            
            scene tunnels_yselle with fade
            
            "As Quinn turns back as fast as he can, he can no longer hold his puke, and let's it all out inside the shaft, now filled with the combinated smells of blood and vomit."

            show quinn worried at right
            
            q "...I-I can't..."

            "His breathing was ragged, he felt like he was about to pass out, but the memory of what happened before came to him. Who knew how things would look if he were to pass out again? He had to move, quickly."

            "He focused as much as possible on his survival, trying to forget about the smells and how it felt like the walls of the shaft moved and closed in on him. He moved forward..."

            "Only to find that on the other side of the shaft, there were people moving around. He could hear the footsteps and the murmurs, and he used the fact that the door of the shaft could allow him to take a peek."

            "He soon regretted that."

            scene cultist_corridor with dissolve

            "A group of crewmembers were walking towards the direction of the cargobay. But every single one of them had a strange look in their eyes, without focus, like they were mindless husks."

            "Their faces were all full of lacerations, and the accumulated blood from all of them was starting to turn the floor of the corridor red."

            "They did not seem to mind their own wounds, even as some of them looked like they could be fatal."
            
            "He felt his heart skip a beat, and his mind struggling to accept this."

            q "The note..."

            "Yeah, the note he found on himselft when he woke up, perhaps that's what Yselle meant by keeping to the shafts and don't let them see you"

            "If so, then going back would not be any better, which made Quinn think how could the sight of that dining hall be the better choice between the two."

            "He didn't want to find out. As hard as it was to go through this again, he returned to the entrance of the hall, and went in."

            jump b_dining_hall

        "Go in":

            jump b_dining_hall


label b_dining_hall:

    scene b_dining_hall with dramatic

    "The floor was so full of blood and fat that if Quinn didn't actively balance himself, he would fall headfirst into the gore."

    "He has to swallow his own vomit when he sees what appears to be guts tangled in one of the chairs."

    show quinn scared at right

    q "Oh God..."
    
    "He had to move, get to the next shaft and keep moving like that until he reached the docks."

    "The entrance to the next shaft was near, close to the entrance to the kitchen area of the hall. As he was finally out of the ventilation system, he could at least move around with more freedom."

    show quinn worried at right
    
    "Quinn took careful steps, trying to be as stealthy as possible, even though there was no one close, no one alive at least."

    "In a moment, he was already in front of the next shaft."

    "He went to open it, as he could do so by just flipping a couple of switches near it and pressing a confirmation button."

    "When we was about to press the button, the last step to open the shaft, he heard a noice behind him."

    "It was still far away, probably even on the previous room, but he was sure he heard something moving."

    menu: 

        "Turn back":

            "Quinn reacted by inertia, without really thinking, forgetting for a moment the contents of the letter."

            "At first, there was nothing to be seen, but when he heard a noise again coming from the ground, he saw something that made his brain feel a shock."

            show gazer baby at truecenter
            with dramatic

            "It was a ball of flesh, with two eyes that looked straight at Quinn."

            "He felt an instinctive horror at that creature, like this was not something that should exist."

            "???" "Run!"

            q "What?"

            "Quinn heard a voice that took him out of the trance he entered when looking at the creature. When he looked up, he saw Mr. Han, one of the senior welders in the ship, standing above the creature with a leg up."

            show han at left
            
            han "..."

            with vpunch
            
            "With a powerful stomp, Mr. Han crushed the creature instantly, scateering blood all around as if it had been made purely out of gore."

            hide gazer baby
            with flash

            han "You have to run now boy"

            $ sanity -= 2

            q "What? Mr. Han, just what is..."

            han "They are coming boy! Just run! Go in there!"

            "Quinn didn't lose the opportunity and open the shaft and went inside, leaving it open so that Mr. Han could get to safety as well."

            "But the shaft's door closed violently, Quinn hearing the clicking sound it made when it got closed for good."

            "He hurried to reopen it from the inside but he heard Mr. Han's voice again."

            han "Get to the docks, we'll meet there."

            "After he said that, a screeching sound was heard."

            han "Go now, run!"

            "Quinn was partially reluctant to leave his savior there, but his survival instinct kicked in, and he heeded the words of Mr. Han, rushing forward into the shaft."

            jump corridor4

        "Open the shaft and get in quickly!":

            "Quinn pressed the button, and the door opened with a click."

            "He had to get on his knees to get in and he did so as fast as he could possibly manage."

            jump corridor4

