# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character(_("Dante"), color="#a73113")
define meph = Character(_("Mephistopheles"), color="#857c7a")
define yg = Character(_("Yrrus"), color="#077535")
define rg = Character(_("Reinhilde"), color="#e0e40f")
define ag = Character(_("Arandell"), color="#e0e40f")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
