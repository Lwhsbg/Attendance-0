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
        "Ignore "








    