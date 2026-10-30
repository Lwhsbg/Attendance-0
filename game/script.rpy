transform bg_fit:
    xysize(1920,1080)
label start:
    scene black
    with fade 
    with dissolve 
    centered "{size=45}{color = #990000}ATTENDANCE 0{/color}{/size}"
    pause 2.0
    $ player_name = renpy.input("Enter your name:", default = "Alex").strip()
    if not player_name:
        $ player_name = "Alex"
    scene dark_classroom at bg_fit
    with dissolve
    with fade
    "It was 8:13 PM."
    "You had stayed late at school to finish an assignment."
    "The corridors were empty. The classrooms were locked."
    "You packed your bags and prepared to leave."
    "Then the speakers suddenly crackled."
    centered "{color=#999999}Good evening, students.{/color}"
    "You stopped."
    centered "{color=#999999}Class 3-B. Attendance will now begin.{/color}"
    "There were no evening classes at your school."
    centered "{color=#999999} Maya.{/color}"
    m "Present."
    "You froze."
    "Maya had been your classmate."
    "She had disappeared three months ago."
    menu:
        "What will you do?"
        "Go to classroom 3-B.":
            jump classroom
        "Look for the security guard.":
            jump office
        "Try to leave immediately.":
            jump exit_attempt
label classroom:
    scene hallway at bg_fit
    with dissolve
    with hpunch
    "You walked down the dark corridor."
    "The door to the class 3-B stood open."

    "Inside, every desk was empty."

    "Except one."

    "A schoolbag rested on the teacher's desk."

    "You recognized it."

    "It belonged to Maya."

    "Beside it lay a notebook."

    menu:
        "Investigate the classroom."

        "Open the notebook.":
            jump notebook

        "Look at the blackboard.":
            jump blackboard

        "Leave the classroom.":
            jump office


label notebook:

    $ clues += 1
    $ found_register = True
    "You opened the notebook."
    "The first few pages contained ordinary class note."
    "The final pages were filled with names."

    "Twenty names."

    "All students from class 3-B."

    "At the bottom of the page, someone had written your name."

    centered "{color=#aa3333}[player_name] — ABSENT{/color}"

    "You turned the page."

    "A sentence was written in red ink."

    m "If you can read this, don't answer when they call your name."

    "A chair scraped behind you."

    "You turned around."

    "Nobody was there."

    jump office


label blackboard:
    scene dark_classroom at bg_fit
    with dissolve
    with fade
    $ courage += 1
    "You approached the blackboard."
    "Written in chalk were the words:"
    centered "{color=#aaaaaa}WE ARE STILL WAITING.{/color}"
    "You rubbed the words away."
    "Beneath them was another sentence."
    centered "{color=#aa3333}ONE STUDENT IS STILL MISSING.{/color}"
    "The classroom door slammed shut."
    u "You came back."
    "You tried the handle."
    "It would not open."
    "Then, as suddenly as it had shut, the door opened again."
    jump office
label exit_attempt:
    scene hallway at bg_fit
    with dissolve
    with fade
    "You ran towards the main entrance."
    "You grabbed the handle and pulled."
    "The doors wouldnt move."
    "Outside, the parking lot was completely empty."
    "You looked through the glass again."
    "Your motorcycle was gone."
    centered "{color=#999999}Attendance is not finished.{/color}"
    "The speaker above you crackled."
    "Your phone began ringing."
    "UNKNOWN NUMBER."
    menu:
        "Answer your phone?"
        "Answer.":
            jump phone
        "Ignore it and find another way out.":
            $ courage +=1
            jump office
label phone:
    scene black
    with dissolve
    "You answered."
    m "Why did you not come back for me?"
    p "Maya?"
    m "I have been waiting for three months."
    p "Where are you?"
    m "In the classroom."
    p "You are not alive."
    "Silence."
    m "Neither are you."
    "The call ended."
    $ clues += 1
    jump classroom
label office:
    scene office at bg_fit
    with dissolve
    with fade
    "You entered the security office."
    "The guard's chair was empty."
    "A dusty monitor glowed on the desk."
    "A digital attendance sheet was open."
    centered "{color=#bbbbbb}CLASS 3-B -- NIGHT SESSION{/color}"
    "You recognised the names."
    "Maya."
    "Then twenty other students."
    "Then your own name."
    centered "{color=#aa3333}[player_name] -- PRESENT{/color}"
    "You had never entered your name."
    "A printer started behind you."
    "One sheet of paper emerged."
    centered "{color=#bbbbbb}ONE STUDENT MUST REMAIN.{/color}"
    "Footsteps approached the office."
    m "Can I come in?"
    menu:
        "What will you do?"
        "Let Maya Enter.":
            jump Maya
        "Hide beneath the desk.":
            jump Hide
        "Ask Maya what happened.":
            jump ask_Maya
label ask_Maya:
    "You stood near the door."
    p "What happened three months ago?"
    m "You really do not remember?"
    p "Remember what?"
    m "The final attendance."
    m "Everyone answered except you."
    p "That is impossible."
    m "You left before the teacher finished."
    m "The next morning, nobody remembered you."
    p "But you are here."
    m "I remembered."
    "The door handles begin turning."
    m "Now they are trying to finish the list."
    jump Maya 
label Maya:
    "Maya entered the office."
    show m at truecenter
    with hpunch
    "She looked exactly as she had three months ago."
    "But something was wrong."
    "She did not have a shadow."
    p "Are you really Maya?"
    m "Does it matter?"
    p "Why are you here?"
    m "Because you never answered."
    "She placed an old class photograph on the desk."
    "Everyone was smiling."
    "Except you."
    "Your face had been scratched out."
    m "The final attendance begins at midnight."
    p "What happens then?"
    m "Someone will have to stay."
    hide m 
    with dissolve
    jump final_scene
label hide:
    scene dark_classroom at bg_fit
    with dissolve
    with fade
    "You crawled down beneath the desk."
    "The door opened."
    "Someone entered."
    "A chair scraped across the floor."
    u "Student present."










    