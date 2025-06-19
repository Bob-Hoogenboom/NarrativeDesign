# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#backgrounds
#image BG Vehicle = "images/BG_IronBackground.png"

#characters
define h = Character("{color=#ffffff}Commander Hartley{/color}")
define j = Character("{color=#eb4517}Joey{/color}")
define w = Character("{color=#d97223}W.LF5{/color}")
define r = Character("{color=#1952e3}Roderick{/color}")
define f = Character("{color=#2387d9}F.V7{/color}")

define jxr = Character("{color=#1952e3}Roderick{/color} {color=#ffffff}and{/color} {color=#eb4517}Joey{/color}")

#Side Characters
define crowd = Character("Crowd")

#positions
define farrightpos = Position(xpos=0.95)
define farleftpos = Position(xpos=0.05)


#effects
define trans = Fade(0.5, 1.0, 0.5)
define flash = Fade(0.25, 0.0, 0.25, color = "#fff")
define scan = Fade(0.5, 0.25, 0.5, color = "#ff0000")
define blackOut = Fade(0.5, 0.0, 0.5, color = "#000000")


init:
    default joeyIsEnemy = False
    default fv7Health = 100

# The game starts here.

#Chapter 0: Prologue
label start:
    scene black
    pause 1.0 

    show text "In the future, technology has peaked. \nThe world races toward a technological breaking point." with dissolve 
    pause 6.0

    hide text with dissolve
    pause 5.0

    show text "But one thing stands in the way of a true utopia..." with dissolve
    pause 3.0

    show text "Greed." with dissolve
    pause 1.0 

    show text "Power." with dissolve
    pause 1.0 

    show text "And the ignorance of mankind." with dissolve
    pause 1.5

    hide text with dissolve
    pause 0.5

    show text "Two superpowers Dadrium and Luhwhium have been at war since \nthe rise of complex technology." with dissolve
    pause 3.0

    hide text with dissolve
    pause 0.5

    show text "Their lust for dominance led them to weaponize even nature \nitself." with dissolve
    pause 3.0

    hide text with dissolve
    pause 0.5

    show text "Innocent animals encased in technological armor... turned \ninto living weapons called Biotech." with dissolve
    pause 3.0

    hide text with dissolve
    pause 0.5

    show text "They were never meant to fight." with dissolve
    pause 2.0

    show text "They were never meant to kill." with dissolve
    pause 2.0

    hide text with dissolve
    pause 0.5

    show text "They were created for war." with dissolve
    pause 2.0 

    hide text with dissolve
    pause 0.5

    show text "Weaponized for greed." with dissolve
    pause 2.0

    hide text with dissolve
    pause 1.0 

    jump Dont_Yield

#Chapter 1
label Dont_Yield:

    scene black
    pause 1.0 

    #Chapter Intro
    window hide

    show screen chapter_intro_1(1)
    #TODO dawn of the first day type sound
    pause 2.0

    show screen chapter_intro_1(2)
    pause 2.0

    show screen chapter_intro_1(3)
    pause 2.5

    hide screen chapter_intro_1
    window show

    scene bg baracks with trans
    pause 2.0

    show hartley with dissolve 
    pause 0.5

    h "...OKAY MEN! \nLET'S SHOW THE ENEMY TODAY THAT WE WON'T GO DOWN WITHOUT A FIGHT!" with dissolve
    h "WE WILL {b}NOT{/b} YIELD!" with dissolve

    show hartley at right with move
    show crowd at farleftpos with moveinleft

    crowd "{b}YES SIR!{/b}" with hpunch

    hide crowd with moveoutleft
    show hartley at center with move

    h "GREAT! GET YOUR BIOTECH READY {p=1.0} AND GET IN FORMATION"
    #TODO soldier mumbeling sound

    hide hartley with dissolve
    pause 1.0 

    show roderick at left with moveinleft
    show fv7 at farleftpos with moveinleft
    pause 1.0 

    r "Okay buddy {w=1.0} last check... {w} \nThere! {w=1.0} \nall set!"
    r "Ready F.V7?"

    f "{i}Nods yes*{/i}"
    f "Are you ready Roderick?"

    r "Ofcourse, {w=1.0}maybe a bit nervous"

    f "No need to worry we w..."

    show joey at center with moveinright
    show wlf5 at right with moveinright

    j "Oh come on, Roderick, stop treating your Biotech like a pet."
    j "It's a weapon, not your furry best friend."

    r "Get lost Joey"

    j "Aww, how sweet. Gonna kiss your rifle next? Hug a grenade?"

    r "I said {b}GET LOST{/b} Joey!"

    f "{i}growl*{/i}"
    w "{i}growl*{/i}"

    show hartley at farrightpos with moveinright

    h "Quit arguing you two!"
    h "I'm sick of this rivalry"
    h "Now get yourselves and your biotechs ready and in the pantzer vehicle. Thats an order!"

    jxr "{b}Yes SIR{/b}"

    hide hartley with moveoutright


    return

#~~~~~~~~~~~~~~~~~~~~Helper Functions~~~~~~~~~~~~~~~~~~~~ 
screen chapter_intro_1(stage):
    frame:
        background None
        xalign 0.5
        yalign 0.3

        vbox:
            spacing 10
            xalign 0.5
            for i in range(stage):
                if i == 0:
                    text "Chapter 1:" size 60 xalign 0.5
                elif i == 1:
                    text "Don't Yield" size 30 xalign 0.5
                elif i == 2:
                    text "{i}'Location: Border Barrack Dadrium, 05:59 AM'{/i}" size 30 xalign 0.5
#     #Intro:
#     scene black
#     pause(1.0)

#     show text "In the future, a conflict arises between two nations. All for the energy that is the driving factor for the lives of its inhabitants. \n\nTechnology has peaked" with dissolve 
#     pause(5)
    
#     show text "But" with dissolve
#     pause(1)

#     show text "the same cannot be said for the people. Hunger, greed, \nthirst for power and resources are all still factors." with dissolve
#     pause(5)

#     show text "The nation Utopia has its own breed of foxes, which uses cybernetics to kill its targets. \nThe commander leads the mission to weaken the enemy and to take hold of the energy. " with dissolve
#     pause(7)


#     scene bg iron with trans

# #TODO Play engine audio

#     "Multiple AVs are moving, each with soldiers and one fox per AV. They are on their way to the warzone. In one AV, the commander is on board, with a particular fox as well…"
    
#     show soldier at right

#     show hartley at left

#     h "Remember soldiers, take hold of the position. Don't press forward unless I tell you to. Keep the enemies away from the energy. And one last thing, no survivors, got it?"

#     s "Copy that."

#     s "Yes sir!"

#     hide soldier with dissolve

#     show private at right

#     p "What about the fox?"

#     h "V7? He'll be your friend in need. A silent, but deadly type."

#     h "You'll see what he'll do in no time. I know from experience it keeps surprising soldiers."

#     #clear screen
#     hide private with dissolve
#     hide hartley with dissolve
#     pause(1)
#     scene black
    
#     #transition scene
#     show text "The transport door slams open into a big forest." with dissolve
#     pause(3)

# #TODO Play iron audio

#     show text "Smoke and fire fill the air as human soldiers, mechs, and cyber-enhanced animals move in formation." with dissolve
#     pause(4)
#     hide text with dissolve

#     h "(THROUGH WALKIE TALKIE) \nMove up! We take the spot and hold position."

#     show text "Soldiers are moving to a place with cover. They are looking at their surroundings." with dissolve

#     pause(5)

#     scene bg forest with dissolve
#     show hartley at left 
#     show fv7 at right

#     h "F.V.7, scout ahead. We're not stopping until this land is ours!"

#     hide hartley with dissolve


# #Pseudo choice, just continues as normal
#     menu pseudo_scanning:
#         "Scan":
#             pass

#     hide fv7 with dissolve

#     with scan
#     pause(0.5)
#     with scan

#     "F.V7 walks into enemy territory to scan"

#     "As you scan the environment and detect hostilities, you move into position and wait for further instructions."

#     show fv7 with dissolve

#     f "Uploading enemy locations… 100%%"

#     h "(THROUGH COMMS) \nNow, attack!"

#     hide fv7 with dissolve

#     show text "Soldiers begin shooting at the enemies. \nYou sense multiple hostiles, making yourself ready for attack."
#     hide text

#     menu pseudo_attacking:
#         "Attack":
#             pass

#     scene bg forestdark with dissolve
#     pause(1)

#     show text "You kill the first three soldiers using machine guns installed on your back. You become invisible and kill a soldier with something sharp."
#     pause(3)

# #TODO play cut audio

#     show text "The last soldier is looking scared. Suddenly you appear behind him and bite his neck. \nThe soldier dies in an instant."
#     pause(3)

# #TODO play bite audio
    
#     show text "In the midst of battle, A flicker of movement catches your eye: \nshadows, dancing across the forest floor. You snap your gaze upward."
#     pause(3)

#     show text "Drones. Dozens. More than you've ever seen. You don't seem to recognize the type. \nThey are searching - scanning. And seem to only target the foxes."
#     pause(3)
#     hide text

#     h "Shit! Where are they coming from?"

#     show text "You hack a couple of drones while dodging incoming attacks. All of a sudden, \nsomething hit your back and your vision went black for a moment."
#     pause(3)

#     show text "-Internal error: damage detected - code 0023- shows at your visor. \nIn the heat of battle you ignore the damage and continue hunting drones." with vpunch
#     pause(3)

#     show text "The battle continues. You eliminate drone after drone."
#     pause(3)
#     hide text

#     h "(INTO COMMS) \n Need backup! NOW!"

#     show text "Your eyes scan across the battlefield. Then you spot him: Commander Hartley. He's outnumbered. Badly."
#     pause(3)

#     show text "You launch into a sprint, pushing through the smoke and gunfire. \nBut before you can reach him, a deafening crack sounds."
#     pause(4)

# #TODO Tree cracking sound

#     show text " A massive tree topples." with vpunch
#     pause(3)

# #TODO Tree THUMP sound

#     show text "Hartley barely has time to turn before it crashes down on him."
#     pause(3)

#     show text "You sprint your way forward, dodging gunfire, striking down enemies. \nBy the time you reach Hartley, the last soldier falls, his weapon clattering to the ground."
#     pause(3)

#     show text "The massive tree trunk pins the commander beneath its weight. His breaths are shallow, his face smeared with dirt and blood."
#     pause(3)

#     scene bg forest with dissolve

#     show hartley at right, with dissolve

#     h "(GRUNTING SOFTLY) \nCome here, F.V7, come on boy…"

#     menu hartley_is_hurt:
#         "Help Hartley":
#             pass

#         "Scan Environment":

#             hide hartley with dissolve
#             with scan
#             pause(1) 
#             "You scan the environment. Drones are somewhere in the distance. \nYou haven't got the data on how fast these drones can be here." with dissolve 
#             show hartley at right, with dissolve

#             jump hartley_is_hurt

#     show fv7 at left, with dissolve

#     show text "You slowly step towards commander Hartley. Why does it feel off?" with dissolve
#     pause(3)

#     show text "Seeing him plead like this? Something doesn't feel right." with dissolve
#     pause(3)

#     #vision*
#     scene black with dissolve

#     show text "Your vision changes. You're running around in the forest together with other foxes." with dissolve
#     pause(3)

#     show text "No modifications" with dissolve
#     pause(2)
#     hide text with dissolve
#     pause(1)

#     show text "no guns." with dissolve
#     pause(2)
#     hide text with dissolve
#     pause(1)

#     show text "You feel so free." with dissolve
#     pause(2)
#     hide text with dissolve
#     pause(1)

#     show text "When all of a sudden you feel something gripping your neck." with vpunch
#     pause(3)

#     show text "You look up at the human who grabbed you by the neck. \nSomeone you recognize as commander Hartley." with dissolve
#     pause(3)

#     show text "He throws you into a cage, like youre just an object." with hpunch
#     pause(3)
#     hide text with dissolve
#     pause(1)

#     scene bg forest with dissolve

#     show hartley at right, with dissolve
    
#     menu post_vision_hartley:
#         "Help Hartley...":
#             jump help_hartley

#         "Leave":
#             pass
     
#     scene bg forestdark with dissolve

#     show text "You look at the commander, struggling to get the trunk of him."
#     pause(3)
#     hide text

#     h "(GRUNTING,IMPATIENTLY) \nHelp me, F.V7, come on, what are you doing.."
#     h " you stupid fox." with vpunch

#     hide hartley with dissolve

#     show text "All of a sudden you feel sure of what to do. \nYou decide to turn the other way and walk away from the commander." with dissolve
#     pause(3)
#     hide text with dissolve
#     pause(1)

#     show text "That's when you sense something observing you from behind a bush..." with dissolve
#     pause(3)
#     hide text with dissolve
#     pause(1)

#     show text "You look around and see another war fox looking at you..." with dissolve
#     pause(3)
#     hide text with dissolve
#     pause(1)

#     show text "cautiously..." with dissolve
#     pause(3)
#     hide text with dissolve
#     pause(1)

#     jump fox_conflict

#     return

# #choice 1
# label help_hartley:
#     scene bg forestdark with dissolve

#     show fv7 at left, with dissolve
#     show hartley at right with dissolve

#     "You deploy one of the medkits which is installed on your back. A little built-in robot climbs out and bandages the commander." 

#     h "Thank god, good boy *grunt*"

#     "You sense an ally, another fox, observing you. He walks towards you and looks at the trunk laying on top of the commander."

#     "Together you try and push the tree trunk off him." with dissolve
#     hide fv7 with dissolve
#     hide hartley with dissolve

# #TODO play tree cracking noise

#     scene black with flash
#     scene bg forestdark with flash

#     show fv7 at left, with dissolve
#     show fox at right, with dissolve

#     pause(1)

#     "The fox next to you looks up at you and tilts its head."
#     "He tries to scan you for malfunctions." with scan

#     "You jump away from the fox. You give out a sharp short bark. Something in you doesn't want to be diagnosed."

#     jump fox_conflict
#     return

# #choice 2
# label fox_conflict:
#     scene black
        
#     ef "“Warning: Critical malfunction found. \nEliminate the target immediately.”" with vpunch

#     scene bg forest with dissolve
#     show fox with dissolve

#     "Without hesitation, the fox attacks you."

#     menu fox_attacks_1:
#         "Defend":
#             $ fv7IsWounded = True
#             pass

#         "Leave":
#             scene black with dissolve
#             jump leave_the_fight


#     "You stand before the fox, dodging one of his incoming attacks."
#     hide fox with vpunch

#     "You sense a delay in your movements as you try to attack."
#     with vpunch

#     with blackOut

#     "You fall to the ground."
            
#     menu fox_attacks_2:
#         "Defend":
#             pass

#         "Leave":
#             scene black with dissolve
#             jump leave_the_fight

#     "You get up, try and strike a second time."
#     "You notice the other fox is way quicker." with vpunch
#     "He shoots at you... \nyou manage to just dodge his shots, but its a close call."
        
#     menu fox_attacks_3:
#         "Defend":
#             pass

#         "Leave":
#             scene black with dissolve
#             jump leave_the_fight


#     "You try again to fight the fox."
#     "You get ready to shoot, but you can't keep track of the fox."
#     "He shoots you from behind, as you fall to the ground." with hpunch
#     "Your vision slowly fades to black."

#     scene black with dissolve

#     pause(2)
#     show text "{color=#ff0000} Game Over \nF.V7 Died in the battle with the other fox {/color}"
#     pause(10)

#     #"This is the part where F.V7 dies"
#     return


#     label leave_the_fight:
#         scene bg forestdark with dissolve

#         "Every instinct tells you to fight, {p=0.5} but you know you're too weak. {p=0.5} You won't win."
#         "Then{w} a sudden rush floods your veins.{p=1.0} Not strength. {p=1.0} Not courage. {p=0.5}"

#         "{color=#ff0000} FEAR {/color}"

#         "You decide to run away, as quickly as you can. Dodging attacks from a distance"
#         "You sprint deep into the forest, alone."
        
#         jump act_2

#     return

# label act_2:
#     scene black with dissolve
    
#     "You are stranded somewhere deep into the forest."
#     "You look around and take it all in, \nnoticing the contrast between the silent nature of the forest and the loud battlefield."

#     scene bg forestdeep with dissolve

#     "It feels so different… {p=1}but also nostalgic."

#     "As you've winded down from the stress and running, you feel your body needs a place to rest."

#     "After minutes of wandering, you find something which seems like a den. Your instinct tells you a spot like this is a perfect place to rest."
#     scene black with dissolve
#     pause(1)
#     scene bg bearden with dissolve

#     "You try to scan the place for potential threats"

#     with flash
#     pause(1)

#     "It seems your scanner got damaged and won't work anymore."
#     "There is only one way to find out if the den is safe."

#     with blackOut
#     pause(1)

#     show fv7 at left, with moveinleft

#     "As you slowly walk into the den, your eyes and ears become sharper. You can't hear anything, but you feel an inner caution"
#     "for precaution the guns on your back rise up in advance."

#     "As you near the end of the den, you suddenly hear movement and the sound of a growl."
# #TODO Growl sound

#     "It appears to be a bear that was resting. It gets up and looks in your direction."
#     show bear at right, with dissolve

#     "It seems to be startled for a second."

#     "Then, {p=1.0}another loud roar sounded from the bear."
#     "It is agitated, but doesn't lash out yet. It knows you are trouble."
#     "Seeing the weapons on your back automatically adjusting and responding to its movements."

#     menu bear_attack:
#         "Leave":
#             jump bear_attack_leave
#         "Shoot":
#             jump bear_attack_shoot
#         "Stay Still" if not isBearObserved:
#             $ isBearObserved = True
#             pass

#     "You are observing the bear, {w}every movement it makes, every sound."
#     "The bear seems to become more intimidating every second, roaring and slowly coming closer, making itself ready to attack."
#     jump bear_attack
#     return


# label bear_attack_leave:
#     "You decide it's better to leave this place, as you feel tired and just need to rest. You don't feel the need to get into a fight, or kill."
#     "You step back slowly, the bear still having his eyes on you cautiously."

#     hide fv7 with moveoutleft
#     show bear at center, with move
#     show cub at right, with moveinright

#     "You suddenly notice a cub appearing behind the bear."
#     "Scared, {p=1.0}uncertain, and a little curious."
#     "This triggered something in you…"

#     #<<Vision>>
#     scene black with dissolve

#     show text "You are just a small fox, glancing around to see your siblings standing beside you inside some sort of den" with dissolve
#     pause(4)
#     hide text
#     pause(1)

#     show text "Before you stand a larger fox, its back turned to you." with dissolve
#     pause(4)
#     hide text
#     pause(1)

#     "Mom?"

#     show text "You realise she's guarding you and your siblings from something big." with dissolve
#     pause(3)
#     hide text
#     pause(1)

#     show text "You shiver and whimper. You feel vulnerable, helpless." with dissolve
#     pause(3)
#     hide text
#     pause(1)

#     with flash
#     show text "In a flash of movement, your mother lunges forward, attacking the predator." with dissolve
#     pause(3)
#     hide text
#     pause(1)

#     "GRRROOWWWWLLLL" with vpunch

#     scene bg forestdeep with dissolve
#     f "Better go outside before mother bear gets me"

#     jump post_bear_encounter
#     return

# #huh why is leaving so much more confronting the shooting???
# label bear_attack_shoot:
#     "You aim your machine guns at the bear."
#     "The bear lunges forward."
#     show bear at center, with move

#     with flash
#     with flash
#     with flash
#     "You shoot it and it falls to the ground with a loud thump."
#     hide bear with dissolve

#     "As the bear falls down, you notice something else laying behind it."
#     "It's a cub, or at least, it was."

#     scene black with dissolve
#     pause(1)
#     scene bg forestdeep with dissolve

#     "You leave the den, as there is nothing of interest for you anymore."
#     "You'd rather not sleep in this den tonight."
#     "As the scent of death might attract other predators or scavengers…"

#     jump post_bear_encounter
#     return

# label post_bear_encounter:
#     show fv7 at left, with moveinleft

#     "You wander through the calm forest, still with the thought of wat just happend in the den..."
#     "You spot a patch of berries. You sniff them. They are sweet, earthy."
#     "You take a bite, {p=1.0}then another. {p=1.0}Nourishment - finally."

#     scene bg forestriver with dissolve
    
#     show text "To be Continued" with dissolve
#     pause(10)
#     hide text with dissolve
#     pause(1)

