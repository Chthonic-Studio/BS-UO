label prologue2:

    centered "Two days later..."

    with dissolve

    "???" "Hey! Boss! There's something here in the well"

    with fade

    "???" "It's a... baby?! Bernat, what should we do?"

    with dissolve

    bernat "Who throws a baby into a well?...Roke, Cyrano, help me out here"

    "After the three men pull the baby out of the well, they look for wounds and such"

    if player_gender == "Male":

        cyrano "Besides a slight malnourishment, he seems to be fine, strange to find him so warm in this cold weather"

    else:
                
        cyrano "Besides a slight malnourishment, she seems to be fine, strange to find her so warm in this cold weather"

    bernat "Take it to Domeka, she'll know what to do"

    with fade

    domeka "By the gods! Where did you came from?"
    
    cyrano "Roke was scouting the area and found the little surprise here inside of the town's well"

    domeka "I see..."

    domeka "Oh you poor thing, you are a newborn and yet..."
    
    domeka "And your parents, it must have been hard for them to leave you there"

    cyrano "Ultimately it was the best choice, we haven't found any survivors so far, so it's safe to assume that they are dead"

    domeka "Such a vicious attack, dragons are not usually this through when attacking, it must have had a specific reason to do this"

    cyrano "Bernat already mentioned something similar, we'll probably be discussing it later today with the rest of the company"

    cyrano "As for this baby..."

    if player_gender == "Male":

        cyrano "Take a look at him to see if everything's all right, he seems strong but we can't be too sure"

        domeka "He certainly looks healthy, perhaps missing a few meals but nothing too serious"

        domeka "I'll take care of him, don't worry"

        cyrano "We'll probably take him to a nearby town, we can't take care of him while we are on the road"

        domeka "Yeah... we can't, right?"

        cyrano "No, I know that look Domeka, we cannot take care of him, we are not prepared for this"

        cyrano "We are not adopting him, he doesn't even have a name yet"

        domeka "Oh, then why not name him? It is gonna be weird to refer to him as 'the baby' until next town, we are in the middle of a mission after all"

        cyrano "I guess you are right, but I'm not good with names, you do it"

        domeka "Me? Alright, let's see..."

        domeka "How about..."

        menu:

            "Numa":
                    $ player_name = "Numa"
                    pass
            "Drogo":
                    $ player_name = "Drogo"
                    pass
            "Julien":
                    $ player_name = "Julien"
                    pass

    else:

        cyrano "Take a look at her to see if everything's all right, she seems strong but we can't be too sure"

        domeka "She certainly looks healthy, perhaps missing a few meals but nothing too serious"

        domeka "I'll take care of her, don't worry"

        cyrano "We'll probably take her to a nearby town, we can't take care of her while we are on the road"

        domeka "Yeah... we can't, right?"

        cyrano "No, I know that look Domeka, we cannot take care of her, we are not prepared for this"

        cyrano "We are not adopting her, she doesn't even have a name yet"

        domeka "Oh, then why not name her? It is gonna be weird to refer to her as 'the baby' until next town, we are in the middle of a mission after all"

        cyrano "I guess you are right, but I'm not good with names, you do it"

        domeka "Me? Alright, let's see..."

        domeka "How about..."

        menu:

            "Liliana":
                    $ player_name = "Liliana"
                    pass
            "Emma":
                    $ player_name = "Emma"
                    pass
            "Marianne":
                    $ player_name = "Marianne"
                    pass

    domeka "Do you like [player_name]?"

    "The baby is just a newborn, so only a little cooing can be heard"

    cyrano "I guess that's as much of a yes as we are gonna get"

    domeka "Then it's settled, [player_name] it is"

    cyrano "Alright, I'll go and tell the others about the meeting"

    cyrano "Remember, this is only temporary..."

    domeka "Yes yes, I know, don't worry about it"

    jump prologue3

    return