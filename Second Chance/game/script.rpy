# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character(_("Iara"), color="#F329D9")
define b = Character(_("Blake"), color="#7B5A77")
define s = Character(_("Soo-Yeon"), color="#411aac")
define x = Character(_("Xesus"), color="#CC9900")
define death = Character(_("Death"), color="#808080")

image soulstone-inc = "soulstone-inc.png"

# The game starts here.

label start:

    # Clear the game runtime timer, so it doesn't reflect time spent sitting at the main menu.
    $ renpy.clear_game_runtime()

    scene blackscreen
    with fade

    show blake at right

    b "Ugh, what..."

    b "Where is this..."

    hide blake
    show sooyeon at left

    s "Who was that?!"

    hide sooyeon
    show blake at right

    b "Eh? Who are you?"

    hide blake
    show sooyeon at left

    s "Don't get closer! I'll tase you, you weirdo!"

    hide sooyeon
    show blake at right

    b "Weirdo? Lady what the hell? I don't even know who you are... of where we are?"

    hide blake
    show sooyeon at left

    s "I don't trust you! Why is a foreigner here in... what? I don't..."

    show iara at right

    i "Ugh, my head...huh, it doesn't hurt anymore?"

    show sooyeon

    s "And who is this one?!"

    hide iara
    show blake at right

    b "Ma'am, I have no idea who are you, who is this young lady..."

    show xesus at center

    x "..."

    show blake at right

    b "Or who this kid is! And I also don't know where the hell are we"

    hide xesus
    hide blake
    hide sooyeon
    with dissolve
    show death at truecenter

    death "Not really hell child, but close"

    "There is a collective horrified scream at the sudden appearance of a ghostly visitor." with vpunch

    death "Ah, how the powers that be conspired together to bring you here"

    "No introduction is needed, everyone present felt it the moment they were aware of the entity's presence, they were in front of Death itself. A woman with skeletal features, whose voice rippled like spines of ice, cutting through the air with a chill."

    death "I hold no joy of meeting you here in my domain, as for I would have rather spoken with you when your hair was gray and your memories of life far away, but alas, Fate has arranged for us to meet here in my abode"

    death "You, my dear children, have made the transition to the world of the dead, brought forth by none other than your own hands."

    "With Death's words, the realization of mortality swept over them."

    death "You are now in Limbo, the realm between the living and the dead, a place for those that have yet to leave their past lives behind"

    show sooyeon at left

    s "That can't...No! No! No! No! No! No! No! No! No! No! No! No! No! No! No! No! No! No!"  

    hide sooyeon
    show blake at right

    b "Ah, that...I see"

    hide blake
    show iara at right

    i "..."

    "She looks sad, but also relieved in some way."

    hide iara
    show xesus at left

    x "Hmmm..."

    "His face is unreadable, but he seems to be thinking about something."

    hide xesus

    death "This is not the end though... Before you move on, I have a proposition for you four"

    "A momentary flash of light brings them into a white room, where Death appears before them as a dark-robed woman."

    "The room is empty, save for the four of them and the personification of Death. The walls, the ceiling, the floor, and even the drapes were all white."

    "Death was the only thing that stood out, her dark robes and pale skin contrasting with the white room."

    death "There are many lost souls, such as yourselves, wandering about the different areas of this realm, and I cannot do much to help them, as it would require me to forgo my other responsibilities." 

    death "You have just arrived, and your minds are still fresh, unburdened by repeating the woes that plagued your mortal lives."
    
    death "So I would like to ask for your assistance"

    show soulstone-inc at left 
    with fade

    "A small, pulsating bluish stone appears in Death's hand, and she shows it to the group."

    death "What you see before you is the Soulstone, a vessel to hold the essence of those who are ready to leave this plane of existence, and move on to the afterlife."

    death "However, this vessel has lost the ability to sense between those that are truly ready to move on and those that are not ready to advance forward. Therefore, I ask you to find the missing shards and restore the stone"

    "There's a moment of silence as the group takes in the information, which there's a lot of."

    death "I will not force you to undertake this task, but I will ask that you consider it throughly, as it will be the only way for you to ascend to the afterlife without taking the pilgrimage that all souls that reach this place the same way you did must take."

    

    return
