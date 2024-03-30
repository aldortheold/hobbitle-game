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
    statsLight = PhotoImage(file="img/stats_light.png")
    settings = PhotoImage(file="img/settings.png")
    settingsLight = PhotoImage(file="img/settings_light.png")
    enter = PhotoImage(file="img/enter.png")
    enterLight = PhotoImage(file="img/enter_light.png")
    backspace = PhotoImage(file="img/backspace.png")
    backspaceLight = PhotoImage(file="img/backspace_light.png")
    label = PhotoImage(file="img/label.png")
    awesome = PhotoImage(file="img/awesome.png")
    awesomeRu = PhotoImage(file="img/awesome_ru.png")
    excellent = PhotoImage(file="img/excellent.png")
    excellentRu = PhotoImage(file="img/excellent_ru.png")
    greatJob = PhotoImage(file="img/great_job.png")
    greatJobRu = PhotoImage(file="img/great_job_ru.png")
    outstanding = PhotoImage(file="img/outstanding.png")
    outstandingRu = PhotoImage(file="img/outstanding_ru.png")
    wellDone = PhotoImage(file="img/well_done.png")
    wellDoneRu = PhotoImage(file="img/well_done_ru.png")
    theSolWas = PhotoImage(file="img/the_sol_was.png")
    theSolWasRu = PhotoImage(file="img/the_sol_was_ru.png")
    playAgain = PhotoImage(file="img/play_again.png")
    playAgainRu = PhotoImage(file="img/play_again_ru.png")
    imgExit = PhotoImage(file="img/img_exit.png")
    imgExitRu = PhotoImage(file="img/img_exit_ru.png")
    rules = PhotoImage(file="img/rules.png")
    rulesRu = PhotoImage(file="img/rules_ru.png")
    closeR = PhotoImage(file="img/close_r.png")
    settingsList = PhotoImage(file="img/settings_list.png")
    settingsListRu = PhotoImage(file="img/settings_list_ru.png")
    darkButton = PhotoImage(file="img/dark_button.png")
    darkButtonRu = PhotoImage(file="img/dark_button_ru.png")
    lightButton = PhotoImage(file="img/light_button.png")
    lightButtonRu = PhotoImage(file="img/light_button_ru.png")
    englishButton = PhotoImage(file="img/english_button.png")
    englishButtonRu = PhotoImage(file="img/english_button_ru.png")
    russianButton = PhotoImage(file="img/russian_button.png")
    russianButtonRu = PhotoImage(file="img/russian_button_ru.png")
    statsW = PhotoImage(file="img/stats_w.png")
    statsWRu = PhotoImage(file="img/stats_w_ru.png")
    closeSt = PhotoImage(file="img/close_st.png")

    characters = [
        "gandalf", "bilbo", "thorin", "elrond", "beorn", "balin", "dwalin",
        "gloin", "fili", "kili", "troll", "gollum", "greatGoblin", "smaug"
    ]

    keyboard = [PhotoImage(file=f"img/{character}.png") for character in characters]
    solution = random.sample(keyboard, 5)

    guesses, gButtons = [[], [], [], [], [], []], [[], [], [], [], [], []]

    congrats = random.choice([awesome, excellent, greatJob, outstanding, wellDone])
    congratsRu = random.choice([awesomeRu, excellentRu, greatJobRu, outstandingRu, wellDoneRu])

    def rulesCall():

        def closeInfo():
            rulesLabel.destroy()
            closeButton.destroy()

        rulesLabel = Label(window, bg=WIDGET_BLUE)
        closeButton = Button(window, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=closeInfo)
        if LANG == "ENG":
            rulesLabel.config(image=rules), closeButton.config(image=closeR)
        elif LANG == "RU":
            rulesLabel.config(image=rulesRu), closeButton.config(image=closeR)
        rulesLabel.place(x=0, y=0), closeButton.place(x=494, y=18)

    aboutButton = Button(window, width=50, height=50, image=logo, command=rulesCall)
    titleLabel = Label(window, text="HOBBITLE", font=("Courier New", 50, "bold"), fg="#daaf00")

    lines = [Label(window, width=110, height=70, image=label, relief=RAISED) for _ in range(30)]
    lineGroups = [lines[:5], lines[5:10], lines[10:15], lines[15:20], lines[20:25], lines[25:]]
    
    if THEME == "LIGHT":
        aboutButton.config(bg=BG_LIGHT, activebackground=BG_LIGHT)
        if LANG == "ENG":
            titleLabel.config(text="HOBBITLE", bg=BG_LIGHT)
        elif LANG == "RU":
            titleLabel.config(text="ХОББИТЛИ", bg=BG_LIGHT)    
        for field in lines:
            field.config(bg=BG_LIGHT)
    elif THEME == "DARK":
        aboutButton.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK)
        if LANG == "ENG":
            titleLabel.config(text="HOBBITLE", bg=BG_DARK)
        elif LANG == "RU":
            titleLabel.config(text="ХОББИТЛИ", bg=BG_DARK)
        for field in lines:
            field.config(bg=WIDGET_DARK)

    aboutButton.place(x=10, y=10), titleLabel.place(x=100, y=0)

    xPlace, yPlace = 10, 70
    for yAxis in range(6):
        for xAxis in range(5):
            lines[xAxis + yAxis * 5].place(x=xPlace, y=yPlace)
            xPlace += 110
        xPlace = 10
        yPlace += 70

    count = 0

    def charCall(char: PhotoImage):
        global count
        currentGuess = min(count // 5, 5)
        while count < 30:
            lines[count].config(image=char)
            guesses[currentGuess].append(char)
            gButtons[currentGuess].append(charButtons[keyboard.index(char)])
            count += 1
            break

    def enterCall():
        global count, ALL_TRIES, ALL_WINS, CURRENT_STREAK, BEST_STREAK
        congratsLabel = Label(window, width=554, height=215, bg="#179923")
        theSolWasLabel = Label(window, width=554, height=215, bg="#9a0000")
        newGameButton = Button(window, bg=WIDGET_BLUE, command=lambda: window.destroy())
        exitButton = Button(window, bg="#f0a510", command=quit)
        currentGuess = count // 5 - 1
        guessedCombo = guesses[currentGuess]
        currentLine, currentGButton = lineGroups[currentGuess], gButtons[currentGuess]
        if LANG == "ENG":
            congratsLabel.config(image=congrats), theSolWasLabel.config(image=theSolWas)
            newGameButton.config(image=playAgain), exitButton.config(image=imgExit)
        elif LANG == "RU":
            congratsLabel.config(image=congratsRu), theSolWasLabel.config(image=theSolWasRu)
            newGameButton.config(image=playAgainRu), exitButton.config(image=imgExitRu)
        if count % 5 == 0:
            if guessedCombo == solution:
                for character in currentLine:
                    character.config(bg=GREEN_TILE)
                for keyButton in currentGButton:
                    keyButton.config(bg=GREEN_TILE, activebackground=GREEN_TILE)
                congratsLabel.place(x=10, y=500)
                newGameButton.place(x=62, y=610)
                exitButton.place(x=312, y=610)
                ALL_TRIES += 1
                ALL_WINS += 1
                CURRENT_STREAK += 1
                STREAKS.append(CURRENT_STREAK)
                BEST_STREAK = max(STREAKS)
            else:
                for character in guessedCombo:
                    if character in solution:
                        if guessedCombo.index(character) == solution.index(character):
                            currentLine[guessedCombo.index(character)].config(bg=GREEN_TILE)
                            currentGButton[guessedCombo.index(character)].config(bg=GREEN_TILE, activebackground=GREEN_TILE)
                        else:
                            currentLine[guessedCombo.index(character)].config(bg=YELLOW_TILE)
                            currentGButton[guessedCombo.index(character)].config(bg=YELLOW_TILE, activebackground=YELLOW_TILE)
                    else:
                        currentLine[guessedCombo.index(character)].config(bg=GRAY_TILE)
                        currentGButton[guessedCombo.index(character)].config(bg=GRAY_TILE, activebackground=GRAY_TILE)
                if count == 30:
                    theSolWasLabel.place(x=10, y=500)
                    Label(window, image=solution[0], width=104, height=68, bg=BG_RED).place(x=28, y=550)
                    Label(window, image=solution[1], width=104, height=68, bg=BG_RED).place(x=130, y=550)
                    Label(window, image=solution[2], width=104, height=68, bg=BG_RED).place(x=233, y=550)
                    Label(window, image=solution[3], width=104, height=68, bg=BG_RED).place(x=336, y=550)
                    Label(window, image=solution[4], width=104, height=68, bg=BG_RED).place(x=439, y=550)
                    newGameButton.place(x=62, y=625)
                    exitButton.place(x=312, y=625)
                    ALL_TRIES += 1
                    CURRENT_STREAK = 0

    def backspaceCall():
        global count
        currentGuess = min(count // 5, 5)
        if count % 5 == 0:
            currentGuess -= 1
        while count > 0:
            lines[count - 1].config(image=label)
            guesses[currentGuess].pop()
            gButtons[currentGuess].pop()
            count -= 1
            break

    keyButtons, bIndex = [Button(window, height=70) for _ in range(16)], 0
    for newButton in keyButtons:
        if bIndex < 10:
            newButton.config(width=110, image=keyboard[bIndex], command=lambda: charCall(keyboard[bIndex]))
        elif bIndex == 10:
            newButton.config(width=70, image=enter, command=enterCall)
        elif 10 < bIndex < 15:
            newButton.config(width=110, image=keyboard[bIndex - 2], command=lambda: charCall(keyboard[bIndex - 2]))
        elif bIndex == 15:
            newButton.config(width=70, image=backspace, command=backspaceCall)
        bIndex += 1

    buttonX, buttonY, charButtons = 10, 500, keyButtons.copy()
    charButtons.pop(10), charButtons.pop(-1)
    for yAxis in range(3):
        for xAxis in range(6):
            if ((yAxis == 0) or (yAxis == 1)) and (xAxis == 5):
                continue
            keyButtons[xAxis + yAxis * 5].place(x=buttonX, y=buttonY)
            if (yAxis == 2) and (xAxis == 0):
                buttonX += 55
            else:
                buttonX += 110
        buttonX = 10
        buttonY += 70

    if THEME == "LIGHT":
        for keyButton in keyButtons:
            keyButton.config(bg=BG_LIGHT, activebackground=BG_LIGHT)
        keyButtons[10].config(image=enter), keyButtons[15].config(image=backspace)  
    elif THEME == "DARK":
        for keyButton in keyButtons:
            keyButton.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK)
        keyButtons[10].config(image=enterLight), keyButtons[15].config(image=backspaceLight)
    
    def russian():
        global LANG
        LANG = "RU"
        titleLabel.config(text="ХОББИТЛИ"), window.title("Хоббитли")

    def english():
        global LANG
        LANG = "ENG"
        titleLabel.config(text="HOBBITLE"), window.title("Hobbitle")

    def lightTheme():
        global THEME
        THEME = "LIGHT"
        for line in lines:
            line.config(bg=BG_LIGHT)
        for keyButton in keyButtons:
            keyButton.config(bg=BG_LIGHT, activebackground=BG_LIGHT)
        window.config(background=BG_LIGHT), titleLabel.config(bg=BG_LIGHT)
        aboutButton.config(bg=BG_LIGHT, activebackground=BG_LIGHT)
        statsButton.config(bg=BG_LIGHT, activebackground=BG_LIGHT, image=stats)
        settingsButton.config(bg=BG_LIGHT, activebackground=BG_LIGHT, image=settings)
        keyButtons[10].config(image=enter), keyButtons[15].config(image=backspace)

    def darkTheme():
        global THEME
        THEME = "DARK"
        for line in lines:
            line.config(bg=WIDGET_DARK)
        for keyButton in keyButtons:
            keyButton.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK)
        window.config(background=BG_DARK), titleLabel.config(bg=BG_DARK)
        aboutButton.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK)
        statsButton.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK, image=statsLight)
        settingsButton.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK, image=settingsLight)
        keyButtons[10].config(image=enterLight), keyButtons[15].config(image=backspaceLight)

    def settingsCall():

        def closeSettings():
            settingsListLabel.destroy(), closeButton.destroy()
            lightButtonB.destroy(), darkButtonB.destroy()
            russianButtonB.destroy(),englishButtonB.destroy()

        settingsListLabel = Label(window, width=574, height=725, bg=WIDGET_BLUE)
        closeButton = Button(window, image=closeR, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=closeSettings)
        lightButtonB = Button(window, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=lightTheme)
        darkButtonB = Button(window, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=darkTheme)
        russianButtonB = Button(window, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=russian)
        englishButtonB = Button(window, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=english)
        if LANG == "ENG":
            settingsListLabel.config(image=settingsList), lightButtonB.config(image=lightButton)
            darkButtonB.config(image=darkButton), russianButtonB.config(image=russianButton) 
            englishButtonB.config(image=englishButton)
        elif LANG == "RU":
            settingsListLabel.config(image=settingsListRu), lightButtonB.config(image=lightButtonRu)
            darkButtonB.config(image=darkButtonRu), russianButtonB.config(image=russianButtonRu) 
            englishButtonB.config(image=englishButtonRu)
        settingsListLabel.place(x=0, y=0), closeButton.place(x=494, y=18), lightButtonB.place(x=300, y=220),
        darkButtonB.place(x=300, y=300), russianButtonB.place(x=300, y=410), englishButtonB.place(x=300, y=490)

    def statsCall():

        def closeStats():
            statsWLabel.destroy(), closeButton1.destroy()
            allTriesLabel.destroy(), percentageLabel.destroy()
            currentStreakLabel.destroy(), bestStreakLabel.destroy()
            
        statsWLabel = Label(window, width=560, height=248, bg=WIDGET_BLUE)

        if LANG == "ENG":
            statsWLabel.config(image=statsW)
        elif LANG == "RU":
            statsWLabel.config(image=statsWRu)
        statsWLabel.place(x=5, y=242)
        closeButton1 = Button(window, image=closeSt, bg=WIDGET_BLUE, activebackground=WIDGET_BLUE, command=closeStats)
        closeButton1.place(x=498, y=262)
        allTriesLabel = Label(window, bg=BG_BLUE, fg=WIDGET_BLUE, width=3, text=ALL_TRIES, font=("Bandshift", 38))
        allTriesLabel.place(x=44, y=348)
        if ALL_TRIES == 0:
            winRate = "0%"
        else:
            winRate = f"{round((ALL_WINS / ALL_TRIES) * 100)}%"
        percentageLabel = Label(window, bg=BG_BLUE, fg=WIDGET_BLUE, width=4, font=("Bandshift", 38), text=winRate)
        percentageLabel.place(x=142, y=348)
        currentStreakLabel = Label(window, bg=BG_BLUE, fg=WIDGET_BLUE, width=3, text=CURRENT_STREAK, font=("Bandshift", 38))
        currentStreakLabel.place(x=280, y=348)
        bestStreakLabel = Label(window, bg=BG_BLUE, fg=WIDGET_BLUE, width=3, text=BEST_STREAK, font=("Bandshift", 38))
        bestStreakLabel.place(x=420, y=348)
    
    settingsButton = Button(window, width=50, height=50, command=settingsCall)
    statsButton = Button(window, width=50, height=50, command=statsCall)
    
    if THEME == "LIGHT":
        settingsButton.config(image=settings, bg=BG_LIGHT, activebackground=BG_LIGHT)
        statsButton.config(image=stats, bg=BG_LIGHT, activebackground=BG_LIGHT)
    elif THEME == "DARK":
        settingsButton.config(image=settingsLight, bg=WIDGET_DARK, activebackground=WIDGET_DARK)
        statsButton.config(image=statsLight, bg=WIDGET_DARK, activebackground=WIDGET_DARK)

    settingsButton.place(x=510, y=10), statsButton.place(x=450, y=10)
    
    window.mainloop()
