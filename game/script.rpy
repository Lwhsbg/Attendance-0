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
    scene black
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
    ""
    