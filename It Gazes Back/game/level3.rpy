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
image yselle_note = "ysellenote.png"
image logan_note = "loganote.png"
define flash = Fade(.25, 0.0, .75, color="#fff")

# The game starts here.

label fork1:

    scene bloody_corridor_2 with dramatic

    "He had managed to get here, only a few more steps to get to the docks."

    if sanity < 3:

        "His mind was starting to fill with the images of the horrors he had seen, and he could not help but feel like he was going to lose his mind at any moment now."
    
    else:

        "He could not help to feel a slight ray of hope shine upon him. But the crushing sensation of having to still crawl through the bloody and darkened shafts of the ship was still there."
    
    "This one was a particularly hard one to navigate through, as he had to squeeze through spaces where the gore on the floor was so thick that it felt like glue."

    "He even got some on his mouth, and had to repress the feeling of vomiting out just to avoid having to vomit all over himself."

    show quinn worried at right

    q "I can't believe I'm doing this..."

    q "Not far now, not far now..."

    if health < 4:
        
        "The pain he felt was also contributing to slowing him down."

    else:
        
        "But his efforts paid off, as he finally reached the entrance to the docks."
    
    jump dockentrance with dissolve

label fork2:

    scene bloody_corridor_2 with dramatic

    "He had managed to get here, only a few more steps to get to the docks."

    if sanity < 3:

        "His mind was starting to fill with the images of the horrors he had seen, and he could not help but feel like he was going to lose his mind at any moment now."
    
    else:

        "He could not help to feel a slight ray of hope shine upon him. But the crushing sensation of having to still crawl through the bloody and darkened shafts of the ship was still there."
    
    "This one was a particularly hard one to navigate through, as he had to squeeze through spaces where the gore on the floor was so thick that it felt like glue."

    "He even got some on his mouth, and had to repress the feeling of vomiting out just to avoid having to vomit all over himself."

    show quinn worried at right

    q "I can't believe I'm doing this..."

    q "Not far now, not far now..."

    if health < 4:
        
        "The pain he felt was also contributing to slowing him down."

    else:
        
        "But his efforts paid off, as he finally reached the entrance to the docks."
    
    jump dockentrance with dissolve


label dockentrance:

    scene bloody_corridor_7 with dramatic

    "He had finally reached the entrance to the docks."

    show quinn at right

    q "Finally..."

    q "I made it..."

    "The celebration was cut short, however, as he heard a loud noise coming from behind him."

    show alan crazy at left 
    with flash

    alan "..."

    "He was holding a piece of broken glass in his hand, which was already bloodied from not holding it properly, but it didn't seem like Alan was in the mindset to care about that."


label dock:

    scene normal_docks with dramatic

    "He had finally reached the docks."

label aliendock:

    scene alien_docks with redflash

    "He had finally reached the docks."

    "And he was greeted by a sight that made him feel like he was going to lose his mind."

    "A gigantic creature was standing in the middle of the docks, and it was looking at him."

    "The bodies of the crew members were scattered all over the place, and the creature was holding the body of the Yselle in its hands, missing her legs."

    "Logan's body was tattered and torn in a corner, skewed in an unnatural position, and it was clear that he had been killed by the creature."
