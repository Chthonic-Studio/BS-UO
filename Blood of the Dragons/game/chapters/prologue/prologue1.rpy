label prologue1:

    gritta "AAAAAAAAHHHHHHHH!!!"

    "A woman's painful scream echoes through the town, only to be muted by the sound of the terrified townsfolk."

    "Flames danced among the timber frames and thatched roofs, leaving behind only charred wood."

    "The town was engulfed in fire, with the perpetrator in sight of all that went to the plaza."

    "A blue-scaled leviathan with piercing red eyes."
    
    "A dragon."

    elder_cedric "Breathe, child! Find your strength!"

    "Cobalt scales glinted under the moon's wan gaze, each one an icy shard reflecting the inferno below."

    "The dragon's wings were spread wide, as if to embrace the flames."

    "Its two eyes, molten suns embedded in a skull of bone, scanned the chaos, seeking something."

    gritta "AAAARRRRGGGHHHH!!!"

    elder_cedric "Push... just a little more!"

    "With a final, earth-shaking heave, Gritta falls back, gasping. Elder Cedric lifts a bundle of rough cloth, revealing a wet, mewling child."
    
    "He holds it close, cradling its fragile life against his chest."

    elder_cedric "Look upon your child, Gritta, you've done well."

    elder_cedric "It's a healthy..."

    # Player gender selection

    menu:

        "Boy":
            $ player_gender = "Male" # Set gender as male
            pass

        "Girl":
            $ player_gender = "Female" # Set gender as female
            pass

    "Gritta's expression is grim, a mix of pain and terror."

    gritta "Tell me uncle, is it...?"

    if player_gender == "Male":

        elder_cedric "It's a strong boy, Gritta. You've done well."

    else: 
    
        elder_cedric "It's a strong girl, Gritta. You've done well."
    
    "Gritta, eyes glistening with exhaustion and wonder, reaches out a trembling hand. Tears streak her soot-stained face as she reaches a hand out to touch the child."

    gritta "Please...uncle, save my baby..."

    "The dragon dips lower, its shadow swallowing the square."
    
    "A guttural ROAR splits the air, rattling the shutters of the few buildings still standing."

    gritta "There's no time, please!"

    "The dragon's eyes narrow, letting out a growl and turning its head towards the direction of the rundown church where Gritta and Elder Cedric took refuge."

    elder_cedric "I...I will, Gritta. I promise."

    "The ground trembles as the dragon draws near to the church, its colossal shadow engulfing the half-crumbled building."

    gritta "Go, now! Take my child and run!"

    "Elder Cedric looks hesistant to leave Gritta by herself against the impending doom coming their way, but biting his own lip, he nods and takes the child in his arms."

    "The old man muttered a prayer to his niece, and took the fastest route out of the church, avoiding the burning debris falling from the burning ceiling."

    "As he leaves the church, the dragon languidly lands in front of the it, taking no time in destroying the building with a single swipe of its massive tail."

    "The church groaned its final lament. Beams and rafters, stripped of their protective straw, burst into flame, their outlines etched against the night sky."

    "Then, with a grace that belied its bulk, the dragon landed squarely on the church's remains."

    "The dragon tilted its head, gaze boring into the smoldering rubble, still looking for something."

    "The town square is a scene of utter chaos. Flames dance amongst fallen timbers, casting grotesque shadows on what was left of its inhabitants, most left of them laying on the ground, victims of the dragonfire."

    "Tears stream down Cedric's weathered cheeks as he cradles the mewling babe. He's still running, trying to get away from the collosal beast."

    elder_cedric " Oh Gritta. Gritta..."

    "As he runs, he looks back at the dragon, which is still looking for something, but by turning, he fails to notice a falling beam, ripped from a burning house, crashes on his leg, missing the baby by only a few inches."

    "Pain lances through his leg, but he pushes on, driven by the child's whimpers and the ever-present shadow of the dragon."

    "Finally, he reaches the outer town well, and an idea comes to his mind. A desperate one, but it's the only one he has left."

    "Cedric lowers the child gently, whispering soothing words as he places the babe's tiny body on the rough wooden bucket."

    elder_cedric "I'm sorry, child. I'm so sorry."

    "He takes a deep breath, and with a grunt, he pushes the bucket down the well, the child's cries fading as it descends."

    "Just as he pulls back, the dragon crashes down, its cobalt bulk blotting out the night's sky."

    "The dragon's chest heaves up, and immediately afterwards, a blast of blue fire incinerates the top of the well."

    "Cedric throws his body towards the top of the well at the last moment, trying to shield the interior from the blast as the searing heat washes over him."

    "The old man doesn't even manage to scream as the flames engulf him, his body turning into ash in a matter of seconds."

    "But his struggle was not in vain. The flames were not able to reach the bottom of the well, and the child was safe."

    "The dragon's eyes scan the area, but as it finds nothing but rubble, it decides to continue its destruction of the rest of the town."

    "As the newborn cries out unnoticed inside of the well, the dragon finally takes flight, leaving the town in ruins."

    jump prologue2

    return