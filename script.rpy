# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Clippy")

define a = Character("3")
define b = Character("<")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg frontofschool

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show clippy neutral at right

    # These display lines of dialogue.

    c "Welcome to Symbols of Love!"

    c "You are playing as the character 3!"
    
    c "Your role as 3 Senpai is to guarantee the smitten status of the other symbols at your school!"

    
    show character three at right
    
    a "I'm very happy testo testo"
    
    scene bg hallway
    show character three at right
    
    show character lessthan at left
    
    b "haha hehe xd"
    
    # This ends the game.

    return
       