# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define q = Character(_("Quinn"), color="#c4e143")
define a = Character(_("???"), color="#8d1704")
define l = Character(_("Logan"), color="#ab7e24")
define ladeeva = Character(_("Miss Ladeeva"), color="#377b51")


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

    l "I think I would prefer it there. Here it's like we're on a never-ending loop. Fixing broken equipment, checking inventory, and all that jazz."

    "The sound of the intense hammering from the other side of the cargo bay suddenly intensifies."

    q "And what about that guy? He's been hammering away like a madman for hours now. What is it now, the 5th day in a row?"

    l "Alan? Yeah, some of the guys are really worried about him, he's been acting strange for the past couple of weeks, and now with that hammering, he says he's fixing some loose plates but I don't know...But he's one of the seniors, he's been at this for like two decades."
    
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

    q "What are we having today Miss Ladeeva?"

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

    "They both grab their trays and head towards the tables."

label cargobay:

    scene cargobay

    show quinn at right

    return
