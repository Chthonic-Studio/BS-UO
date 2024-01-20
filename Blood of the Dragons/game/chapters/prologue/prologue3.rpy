label prologue3:

    centered "7 years later..."

    if player_gender == "Male":

        $ player_pronoun = "he"

        $ player_pronoun3 = "his"

    else:

        $ player_pronoun = "she"

        $ player_pronoun3 = "her"

    domeka "[player_name]! Stop running around the armory in Namaenath's name! You're going to hurt yourself!"

    menu:
        
        "But I'm bored! I want to go outside!":
            
            domeka "Oh c'mon now kid, what does that have to do with you holding a battle axe?"

            pass

        "But Uncle Bernat uses that! Why can't I?":

            domeka "Because you're still a brat that soils [player_pronoun3] underpants at night. Now put that battleaxe before you hurt yourself, or even worse, damage that edge."

            pass

    domeka "Just put it where you found it, carefully, will you?"

    menu:

            "Fine, mom":

                domeka "Thanks [player_name], it's sweet when you are not being a brat"

                jump prologue3_armory

            "*sigh* Alright alright, you party pooper":

                domeka "Who is teaching you those words?... Damn you Roke"

                jump prologue3_armory

return

label prologue3_armory:

    $ checkbow = False
    $ checksword = False
    $ checkdaggers = False
    $ checkspears = False
    $ checkgauntlet = False
    
    "Domeka leaves the armory, leaving you alone with the weapons. You look at the battleaxe in your hands, and then at the door."

    "There's many weapons stored here, even if it's just a tent set up as an armory, because the company does not stay for too long in one place."

    "You look at the battleaxe in your hands and put it back where you found it. But, you take a look at all the other weapons in the armory."

    "You see a Roke's bow, Cyrano's spare sword, some daggers, a few spears, and even an old arcane gauntlet that one of the company members used to use."

    $ prologue_armory = []
    
    menu prologue_armory:

        set prologue_armory

        "Look at the bow":

            "You take a look at the bow. It's a simple bow, but it's well crafted. You take it in your hands and try to pull the string, but it's too hard for you."

            "You put the bow back where you found it."

            $ checkbow = True

        "Look at the sword":

            "You take a look at the sword. You know this one, as Cyrano once let you hold it for a bit. You grab it by the handle try to swing it, but it's too heavy for you."

            "You put the sword back where you found it."

            $ checksword = True

        "Look at the daggers":

            "You take a look at the daggers. They are small, but sharp. You grab one of them and try to throw it as you've seen people do, but it just falls right in front of you."

            "You put the daggers back where you found them."

            $ checkdaggers = True

        "Look at the spears":

            "You take a look at the spears. This one is pretty heavy, and you wonder how some the twins use this so nimbly. You grab one and try to emulate a stab, but you can't even lift it properly."

            "You put the spears back where you found them."

            $ checkspears = True

        "Look at the gauntlet":

            "You take a look at the gauntlet. It's a strange thing, and you've only seen it being used once. You know they use this to help with using magic, but you don't know how it works."

            "You put the gauntlet back where you found it."

            $ checkgauntlet = True

        "Leave the armory":

            jump prologue3_armory_leave
    
    jump prologue_armory

return

label prologue3_armory_leave:

    if checkbow and checksword and checkdaggers and checkspears and checkgauntlet:
        
        $ investigation += 1

    "You leave the armory and come upon the camp."

    jump prologue3_camp

label prologue3_camp:


label prologue3_cyrano:



label prologue3_roke_aina_vassos:



label prologue3_bernat:



label prologue3_thetwins:

    "You spot the twins, Grimbald and Leufroy, a couple of big, bulky and hairy men. You think they are tribesmen from one of those scary tribes in the north, but you're not sure."

    leufroy "Hey [player_name]! Wanna see something cool?"

    "Leufroy spots you and immediately calls you over. He likes to show off random stuff to you, so you're used to this. He has a spear in his hands."

    menu:

        "Sure!": 

            leufroy "That's the spirit! Now, watch this!"

            $ leufroy_rel += 5
            $ leufroy_rel = clamp(leufroy_rel, -100, 100)

            pass

        "Not now":

            leufroy "Awww, well sucks for you, I'm still gonna show you!"

            pass

    "Leufroy grabs the spear with both hands and starts spinning it around."
    
    "He spins it faster and faster, so much that it starts creating a small wind around him. He then throws it up in the air, almost without breaking the spin."

    "You watch as the spear flies up in the air, getting so high that it almost disappears from your sight."


label prologue3_elias:

    "You spot Elias reading a book under the shade of a tree."

    "You approach him but he doesn't seem to notice you, even when you are right in front of him."

    menu:

        "Scare him":

            player "BOO!"

            elias "OH SHI-"

            "He drops his book and almost falls backwards, but he manages to keep his balance."

            elias "Y-you almost gave me a heart attack you rascal!"

            pass

        "Call him":

            player "Elias!"

            "He looks startled, but then he notices you and nods in acknowledgement."

            elias "Oh, hey [player_name]"

            pass

    elias "What are you doing here? Shouldn't you be with your mother?"

    menu:

        "I'm bored":

            elias "Well, I'm sorry to hear that. But I'm sure you'll find something to do."

            pass

        "I was looking for you":

            elias "Oh, really? Well, I'm here, so you found me."

            pass

    elias "Well, if that's all you need, I'll go back to my book."

    "He picks up his book and starts reading again. You remember that this is one of the reasons almost nobody talks to Elias, it's so hard to get his attention away from his books."

    $ prologue3_elias = []
    
    menu prologue3_elias:

        set prologue3_elias

        "Ask him about the book":

            elias "Oh, this? It's a book about theories on how arcana works and how it manifests though people. It has some interesting thoughts but it's mostly just speculation."

            elias "This is something we've spent almost four ages trying to understand, ever since the sundering, and we still don't know much about it."

            elias "Arcanists are able to produce arcana, or magic as some call it, that gets produced from the inside of our their bodies. It is able to take form and shape, and even modify some of the rules of nature."

            elias "A geomancer can open a hole in a mountain, but also generate a magnetic field. A pyromancer can create fire, but also heat up a room. A cryomancer can freeze water, but also regulate the blood flow of the wounded."

            elias "But there's still too many questions on how this works. The only things we know are that since then, arcana and arcanists have existed, as well as the divinities."

            elias "And with divities, divine vessels as well. But that's a whole other topic."

            $ arcana += 1

            $ elias_rel += 5
            $ elias_rel = clamp(elias_rel, -100, 100)

        "Ask why he spends so much time reading":

            elias "I like reading. It's a good way to pass the time, and I learn a lot of things from it."

            elias "You should try it sometime."

        "Ask about the gauntlet":

            elias "Oh, you mean the old gauntlet in the armory? I used to need it to help me regulate my aeromancy but it's not a high quality one so now it's more of a hindrance than a help."

            elias "I've been looking for a better one, but I haven't found one yet."

        "Leave":

            jump prologue3_camp

    jump prologue3_elias


label prologue3_francesca:



return