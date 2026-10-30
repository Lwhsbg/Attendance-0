transform bg_fit:
    xysize(1920,1080)
label start:
    scene black
    with fade 
    with dissolve 
    centered "{size=45}{color=#990000}ATTENDANCE 0{/color}{/size}"
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
            jump hide
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
    "A pen scratched against paper."
    u "Student absent."
    "The footsteps stopped besides you."
    u "Found you."
    $ courage -= 1
    jump final_scene
label final_scene:
    "The school bell rang."
    "Once."
    "Twice."
    "Three times."
    "The speakers then crackled."
    centered "{color=#bbbbbb}CLASS 3-B. FINAL ATTENDANCE.{/color}"
    centered "{color=#bbbbbb}Maya.{/color}"
    m "Present."
    centered "{color=#bbbbbb}Student number 20.{/color}"
    "Silence."
    centered "{color=#bbbbbb}[player_name].{/color}"
    "Your name echoed throughout the building."
    m "Do not answer."
    u "Please confirm your presence."
    menu:
        "What is your answer?"
        "Present.":
            jump ending_present
        "Remain silent.":
            jump ending_erased
        "Call out Maya's name":
            jump ending_last 
label ending_present:
    scene black
    with fade
    p "Present."
    "Every light in the school turned on."
    "The doors unlocked and you walked outside."
    "Your phone vibrated."
    centered "{color=#bbbbbb}ATTENDANCE RECORD UPDATED{/color}"
    centered "{color=#aa3333}[player_name] -- PRESENT{/color}"
    "You then looked at the date on your phone."
    "Three months ago."
    "Your phone recieved one final message."
    m "Thank you for staying."
    "You looked back at the school."
    "Every classroom was filled with students."
    "All of them were staring at you."
    centered "{size=32}{color=#990000}ENDING 1: PRESENT{/color}{/size}"
    return
label ending_erased:
    scene black
    with fade
    "You said nothing."
    centered "{color=#bbbbbb}No response recieved.{/color}"
    "The lights went out."
    m "Do not let them erase you!!"
    "You tried to call out."
    "No sound came out."
    centered "{color=#bbbbbb}Student marked absent.{/color}"
    "The next morning, a teacher entered classroom 3-B."
    "She counted the desks."
    "Twenty."
    "Everything was in order."
    "Nobody remembered that another student had ever existed."
    centered "{size=32}{color=#990000}ENDING 2: ERASED.{/color}{/size}"
    return
label ending_last:
    scene black
    with hpunch
    p  "Maya!!!"
    "The entire building trembled."
    "Every classroom door slammed shut."
    "The speakers fell silent."
    m "What have you done?"
    p "I called your name."
    m "You were not supposed to do that!"
    "The bell rang three times."
    "Every voice in the school began shouting."
    centered "{color=#bbbbbb}PRESENT! PRESENT! PRESENT!{/color}"
    "Maya grabbed your arm."
    m "The list never ends."
    m "Someone has to keep reading it."
    "You took the attenndance register."
    "Hundreds of names filled it's pages."
    "The final page was blank."
    "You wrote three words."
    centered "{color=#aaaaaa}CLASS DISMISSED.{/color}"
    "The school fell silent."
    "The doors unlocked."
    "Maya walked outside."
    "For the first  time, she cast a shadow."
    "Then she disappeared."
    "Your phone vibrated."
    centered "{color=#bbbbbb}NEW STUDENT ENROLLED{/color}"
    centered "{color=#aa3333}[player_name]{/color}"
    "The speakers crackled again."
    u "Good evening, students."
    centered "{size=32}{color=#990000}ENDING 3: THE LAST STUDENT{/color}{/size}"
    return

















    