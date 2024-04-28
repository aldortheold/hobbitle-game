from tkinter import *
import random

LANG = "ENG"
THEME = "LIGHT"

ALL_TRIES = 0
ALL_WINS = 0
CURRENT_STREAK = 0
STREAKS = [0]
BEST_STREAK = max(STREAKS)

BG_LIGHT = "#f0f0f0"
BG_DARK = "#111111"
BG_RED = "#ff9165"
BG_BLUE ="#bdd7ee"
WIDGET_BLUE = "#002b82"
WIDGET_DARK = "#222222"
GREEN_TILE = "#08c700"
YELLOW_TILE = "#ffcd00"
GRAY_TILE = "#9e9e9e"

while True:
    window = Tk()
    window.geometry("574x725")
    window.protocol("WM_DELETE_WINDOW", quit)
    if LANG == "ENG":
        window.title("Hobbitle")
    elif LANG == "RU":
        window.title("Хоббитли")
    window.iconphoto(True, PhotoImage(file="img/logo.png"))
    window.resizable(False, False)
    if THEME == "LIGHT":
        window.config(background=BG_LIGHT)
    elif THEME == "DARK":
        window.config(background=BG_DARK)

    logo = PhotoImage(file="img/logo_about.png")
    stats = PhotoImage(file="img/stats.png")
    stats_light = PhotoImage(file="img/stats_light.png")
    settings = PhotoImage(file="img/settings.png")
    settings_light = PhotoImage(file="img/settings_light.png")
    enter = PhotoImage(file="img/enter.png")
    enter_light = PhotoImage(file="img/enter_light.png")
    backspace = PhotoImage(file="img/backspace.png")
    backspace_light = PhotoImage(file="img/backspace_light.png")
    label = PhotoImage(file="img/label.png")
    awesome = PhotoImage(file="img/awesome.png")
    awesome_ru = PhotoImage(file="img/awesome_ru.png")
    excellent = PhotoImage(file="img/excellent.png")
    excellent_ru = PhotoImage(file="img/excellent_ru.png")
    great_job = PhotoImage(file="img/great_job.png")
    great_job_ru = PhotoImage(file="img/great_job_ru.png")
    outstanding = PhotoImage(file="img/outstanding.png")
    outstanding_ru = PhotoImage(file="img/outstanding_ru.png")
    well_done = PhotoImage(file="img/well_done.png")
    well_done_ru = PhotoImage(file="img/well_done_ru.png")
    the_sol_was = PhotoImage(file="img/the_sol_was.png")
    the_sol_was_ru = PhotoImage(file="img/the_sol_was_ru.png")
    play_again = PhotoImage(file="img/play_again.png")
    play_again_ru = PhotoImage(file="img/play_again_ru.png")
    img_exit = PhotoImage(file="img/img_exit.png")
    img_exit_ru = PhotoImage(file="img/img_exit_ru.png")
    rules = PhotoImage(file="img/rules.png")
    rules_ru = PhotoImage(file="img/rules_ru.png")
    close_r = PhotoImage(file="img/close_r.png")
    settings_list = PhotoImage(file="img/settings_list.png")
    settings_list_ru = PhotoImage(file="img/settings_list_ru.png")
    dark_button = PhotoImage(file="img/dark_button.png")
    dark_button_ru = PhotoImage(file="img/dark_button_ru.png")
    light_button = PhotoImage(file="img/light_button.png")
    light_button_ru = PhotoImage(file="img/light_button_ru.png")
    english_button = PhotoImage(file="img/english_button.png")
    english_button_ru = PhotoImage(file="img/english_button_ru.png")
    russian_button = PhotoImage(file="img/russian_button.png")
    russian_button_ru = PhotoImage(file="img/russian_button_ru.png")
    stats_w = PhotoImage(file="img/stats_w.png")
    stats_w_ru = PhotoImage(file="img/stats_w_ru.png")
    close_st = PhotoImage(file="img/close_st.png")

    characters = [
        "gandalf", "bilbo", "thorin", "elrond", "beorn", "balin", "dwalin",
        "gloin", "fili", "kili", "troll", "gollum", "greatGoblin", "smaug"
    ]

    keyboard = [PhotoImage(file=f"img/{character}.png") for character in characters]
    solution = random.sample(keyboard, 5)

    guesses, g_buttons = [[], [], [], [], [], []], [[], [], [], [], [], []]

    congrats = random.choice([awesome, excellent, great_job, outstanding, well_done])
    congrats_ru = random.choice([awesome_ru, excellent_ru, great_job_ru, outstanding_ru, well_done_ru])

    def rules_call() -> None:

        def close_info() -> None:
            rules_label.destroy()
            close_button.destroy()

        rules_label = Label(window, bg=WIDGET_BLUE)
        close_button = Button(window, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=close_info)
        if LANG == "ENG":
            rules_label.config(image=rules), close_button.config(image=close_r)
        elif LANG == "RU":
            rules_label.config(image=rules_ru), close_button.config(image=close_r)
        rules_label.place(x=0, y=0), close_button.place(x=494, y=18)

    about_button = Button(window, width=50, height=50, image=logo, command=rules_call)
    title_label = Label(window, text="HOBBITLE", font=("Courier New", 50, "bold"), fg="#daaf00")

    lines = [Label(window, width=110, height=70, image=label, relief=RAISED) for _ in range(30)]
    line_groups = [lines[:5], lines[5:10], lines[10:15], lines[15:20], lines[20:25], lines[25:]]
    
    if THEME == "LIGHT":
        about_button.config(bg=BG_LIGHT, activebackground=BG_LIGHT)
        if LANG == "ENG":
            title_label.config(text="HOBBITLE", bg=BG_LIGHT)
        elif LANG == "RU":
            title_label.config(text="ХОББИТЛИ", bg=BG_LIGHT)    
        for field in lines:
            field.config(bg=BG_LIGHT)
    elif THEME == "DARK":
        about_button.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK)
        if LANG == "ENG":
            title_label.config(text="HOBBITLE", bg=BG_DARK)
        elif LANG == "RU":
            title_label.config(text="ХОББИТЛИ", bg=BG_DARK)
        for field in lines:
            field.config(bg=WIDGET_DARK)

    about_button.place(x=10, y=10), title_label.place(x=100, y=0)

    x_place, y_place = 10, 70
    for y_axis in range(6):
        for x_axis in range(5):
            lines[x_axis + y_axis * 5].place(x=x_place, y=y_place)
            x_place += 110
        x_place = 10
        y_place += 70

    count = 0

    def char_call(pos: int) -> None:
        """Makes the clicked character appear on the board in the right spot"""
        global count
        current_guess = min(count // 5, 5)
        lines[count].config(image=keyboard[pos])
        guesses[current_guess].append(keyboard[pos])
        g_buttons[current_guess].append(char_buttons[pos])
        count += 1

    def enter_call() -> None:
        """When called in the right condition, compares player's guess to the solution and does a bit of Wordle magic"""
        global count, ALL_TRIES, ALL_WINS, CURRENT_STREAK, BEST_STREAK
        congrats_label = Label(window, width=554, height=215, bg="#179923")
        the_sol_was_label = Label(window, width=554, height=215, bg="#9a0000")
        new_game_button = Button(window, bg=WIDGET_BLUE, command=lambda: window.destroy())
        exit_button = Button(window, bg="#f0a510", command=quit)
        current_guess = count // 5 - 1
        guessed_combo = guesses[current_guess]
        current_line, current_g_button = line_groups[current_guess], g_buttons[current_guess]
        if LANG == "ENG":
            congrats_label.config(image=congrats), the_sol_was_label.config(image=the_sol_was)
            new_game_button.config(image=play_again), exit_button.config(image=img_exit)
        elif LANG == "RU":
            congrats_label.config(image=congrats_ru), the_sol_was_label.config(image=the_sol_was_ru)
            new_game_button.config(image=play_again_ru), exit_button.config(image=img_exit_ru)
        if count % 5 == 0:
            if guessed_combo == solution:
                for character in current_line:
                    character.config(bg=GREEN_TILE)
                for key_button in current_g_button:
                    key_button.config(bg=GREEN_TILE, activebackground=GREEN_TILE)
                congrats_label.place(x=10, y=500)
                new_game_button.place(x=62, y=610)
                exit_button.place(x=312, y=610)
                ALL_TRIES += 1
                ALL_WINS += 1
                CURRENT_STREAK += 1
                STREAKS.append(CURRENT_STREAK)
                BEST_STREAK = max(STREAKS)
            else:
                for character in guessed_combo:
                    if character in solution:
                        if guessed_combo.index(character) == solution.index(character):
                            current_line[guessed_combo.index(character)].config(bg=GREEN_TILE)
                            current_g_button[guessed_combo.index(character)].config(bg=GREEN_TILE, activebackground=GREEN_TILE)
                        else:
                            current_line[guessed_combo.index(character)].config(bg=YELLOW_TILE)
                            current_g_button[guessed_combo.index(character)].config(bg=YELLOW_TILE, activebackground=YELLOW_TILE)
                    else:
                        current_line[guessed_combo.index(character)].config(bg=GRAY_TILE)
                        current_g_button[guessed_combo.index(character)].config(bg=GRAY_TILE, activebackground=GRAY_TILE)
                if count == 30:
                    the_sol_was_label.place(x=10, y=500)
                    for i in range(5):
                        Label(window, image=solution[i], width=104, height=68, bg=BG_RED).place(x=28 + 103 * i, y=550)
                    new_game_button.place(x=62, y=625), exit_button.place(x=312, y=625)
                    ALL_TRIES += 1
                    CURRENT_STREAK = 0

    def backspace_call() -> None:
        """Deletes the last typed character"""
        global count
        current_guess = min(count // 5, 5)
        if count % 5 == 0:
            current_guess -= 1
        lines[count - 1].config(image=label)
        guesses[current_guess].pop()
        g_buttons[current_guess].pop()
        count -= 1

    key_buttons = [
        Button(window, width=110, height=70, image=keyboard[0], command=lambda: char_call(0)),
        Button(window, width=110, height=70, image=keyboard[1], command=lambda: char_call(1)),
        Button(window, width=110, height=70, image=keyboard[2], command=lambda: char_call(2)),
        Button(window, width=110, height=70, image=keyboard[3], command=lambda: char_call(3)),
        Button(window, width=110, height=70, image=keyboard[4], command=lambda: char_call(4)),
        Button(window, width=110, height=70, image=keyboard[5], command=lambda: char_call(5)),
        Button(window, width=110, height=70, image=keyboard[6], command=lambda: char_call(6)),
        Button(window, width=110, height=70, image=keyboard[7], command=lambda: char_call(7)),
        Button(window, width=110, height=70, image=keyboard[8], command=lambda: char_call(8)),
        Button(window, width=110, height=70, image=keyboard[9], command=lambda: char_call(9)),
        Button(window, height=70, image=enter, command=enter_call),
        Button(window, width=110, height=70, image=keyboard[10], command=lambda: char_call(10)),
        Button(window, width=110, height=70, image=keyboard[11], command=lambda: char_call(11)),
        Button(window, width=110, height=70, image=keyboard[12], command=lambda: char_call(12)),
        Button(window, width=110, height=70, image=keyboard[13], command=lambda: char_call(13)),
        Button(window, height=70, image=backspace, command=backspace_call)
    ]

    button_x, button_y, char_buttons = 10, 500, key_buttons.copy()
    char_buttons.pop(10), char_buttons.pop(-1)
    for y_axis in range(3):
        for x_axis in range(6):
            if ((y_axis == 0) or (y_axis == 1)) and (x_axis == 5):
                continue
            key_buttons[x_axis + y_axis * 5].place(x=button_x, y=button_y)
            if (y_axis == 2) and (x_axis == 0):
                button_x += 55
            else:
                button_x += 110
        button_x = 10
        button_y += 70

    if THEME == "LIGHT":
        for key_button in key_buttons:
            key_button.config(bg=BG_LIGHT, activebackground=BG_LIGHT)
        key_buttons[10].config(image=enter), key_buttons[15].config(image=backspace)  
    elif THEME == "DARK":
        for key_button in key_buttons:
            key_button.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK)
        key_buttons[10].config(image=enter_light), key_buttons[15].config(image=backspace_light)
    
    def russian() -> None:
        global LANG
        LANG = "RU"
        title_label.config(text="ХОББИТЛИ"), window.title("Хоббитли")

    def english() -> None:
        global LANG
        LANG = "ENG"
        title_label.config(text="HOBBITLE"), window.title("Hobbitle")

    def light_theme() -> None:
        global THEME
        THEME = "LIGHT"
        for line in lines:
            line.config(bg=BG_LIGHT)
        for key_button in key_buttons:
            key_button.config(bg=BG_LIGHT, activebackground=BG_LIGHT)
        window.config(background=BG_LIGHT), title_label.config(bg=BG_LIGHT)
        about_button.config(bg=BG_LIGHT, activebackground=BG_LIGHT)
        stats_button.config(bg=BG_LIGHT, activebackground=BG_LIGHT, image=stats)
        settings_button.config(bg=BG_LIGHT, activebackground=BG_LIGHT, image=settings)
        key_buttons[10].config(image=enter), key_buttons[15].config(image=backspace)

    def dark_theme() -> None:
        global THEME
        THEME = "DARK"
        for line in lines:
            line.config(bg=WIDGET_DARK)
        for key_button in key_buttons:
            key_button.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK)
        window.config(background=BG_DARK), title_label.config(bg=BG_DARK)
        about_button.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK)
        stats_button.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK, image=stats_light)
        settings_button.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK, image=settings_light)
        key_buttons[10].config(image=enter_light), key_buttons[15].config(image=backspace_light)

    def settings_call() -> None:

        def close_settings() -> None:
            settings_list_label.destroy(), close_button.destroy()
            light_button_b.destroy(), dark_button_b.destroy()
            russian_button_b.destroy(),english_button_b.destroy()

        settings_list_label = Label(window, width=574, height=725, bg=WIDGET_BLUE)
        close_button = Button(window, image=close_r, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=close_settings)
        light_button_b = Button(window, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=light_theme)
        dark_button_b = Button(window, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=dark_theme)
        russian_button_b = Button(window, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=russian)
        english_button_b = Button(window, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=english)
        if LANG == "ENG":
            settings_list_label.config(image=settings_list), light_button_b.config(image=light_button)
            dark_button_b.config(image=dark_button), russian_button_b.config(image=russian_button) 
            english_button_b.config(image=english_button)
        elif LANG == "RU":
            settings_list_label.config(image=settings_list_ru), light_button_b.config(image=light_button_ru)
            dark_button_b.config(image=dark_button_ru), russian_button_b.config(image=russian_button_ru) 
            english_button_b.config(image=english_button_ru)
        settings_list_label.place(x=0, y=0), close_button.place(x=494, y=18), light_button_b.place(x=300, y=220),
        dark_button_b.place(x=300, y=300), russian_button_b.place(x=300, y=410), english_button_b.place(x=300, y=490)

    def stats_call() -> None:

        def close_stats() -> None:
            stats_w_label.destroy(), close_button1.destroy()
            all_tries_label.destroy(), percentage_label.destroy()
            current_streak_label.destroy(), best_streak_label.destroy()
            
        stats_w_label = Label(window, width=560, height=248, bg=WIDGET_BLUE)

        if LANG == "ENG":
            stats_w_label.config(image=stats_w)
        elif LANG == "RU":
            stats_w_label.config(image=stats_w_ru)
        stats_w_label.place(x=5, y=242)
        close_button1 = Button(window, image=close_st, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=close_stats)
        close_button1.place(x=498, y=262)
        all_tries_label = Label(window, bg=BG_BLUE, fg=WIDGET_BLUE, width=3, text=ALL_TRIES, font=("Bandshift", 38))
        all_tries_label.place(x=44, y=348)
        if ALL_TRIES == 0:
            win_rate = "0%"
        else:
            win_rate = f"{round((ALL_WINS / ALL_TRIES) * 100)}%"
        percentage_label = Label(window, bg=BG_BLUE, fg=WIDGET_BLUE, width=4, font=("Bandshift", 38), text=win_rate)
        percentage_label.place(x=142, y=348)
        current_streak_label = Label(window, bg=BG_BLUE, fg=WIDGET_BLUE, width=3, text=CURRENT_STREAK, font=("Bandshift", 38))
        current_streak_label.place(x=280, y=348)
        best_streak_label = Label(window, bg=BG_BLUE, fg=WIDGET_BLUE, width=3, text=BEST_STREAK, font=("Bandshift", 38))
        best_streak_label.place(x=420, y=348)
    
    settings_button = Button(window, width=50, height=50, command=settings_call)
    stats_button = Button(window, width=50, height=50, command=stats_call)
    
    if THEME == "LIGHT":
        settings_button.config(image=settings, bg=BG_LIGHT, activebackground=BG_LIGHT)
        stats_button.config(image=stats, bg=BG_LIGHT, activebackground=BG_LIGHT)
    elif THEME == "DARK":
        settings_button.config(image=settings_light, bg=WIDGET_DARK, activebackground=WIDGET_DARK)
        stats_button.config(image=stats_light, bg=WIDGET_DARK, activebackground=WIDGET_DARK)

    settings_button.place(x=510, y=10), stats_button.place(x=450, y=10)
    
    window.mainloop()
