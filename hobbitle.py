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

    gandalf = PhotoImage(file="img/gandalf.png")
    bilbo = PhotoImage(file="img/bilbo.png")
    thorin = PhotoImage(file="img/thorin.png")
    elrond = PhotoImage(file="img/elrond.png")
    beorn = PhotoImage(file="img/beorn.png")
    balin = PhotoImage(file="img/balin.png")
    dwalin = PhotoImage(file="img/dwalin.png")
    gloin = PhotoImage(file="img/gloin.png")
    fili = PhotoImage(file="img/fili.png")
    kili = PhotoImage(file="img/kili.png")
    troll = PhotoImage(file="img/troll.png")
    gollum = PhotoImage(file="img/gollum.png")
    greatGoblin = PhotoImage(file="img/great_goblin.png")
    smaug = PhotoImage(file="img/smaug.png")

    keyboard = [
        gandalf, bilbo, thorin, elrond, beorn, balin, dwalin,
        gloin, fili, kili, troll, gollum, greatGoblin, smaug
    ]
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
        for xAxis in range(1, 6):
            lines[xAxis + yAxis * 5 - 1].place(x=xPlace, y=yPlace)
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
            gButtons[currentGuess].append(keyButtons[keyboard.index(char)])
            count += 1
            break

    def enterCall():
        global count, ALL_TRIES, ALL_WINS, CURRENT_STREAK, BEST_STREAK
        congratsLabel = Label(window, width=554, height=215, bg="#179923", image=congrats)
        theSolWasLabel = Label(window, width=554, height=215, bg="#9a0000", image=theSolWas)
        newGameButton = Button(window, bg=WIDGET_BLUE, command=lambda: window.destroy(), image=playAgain)
        exitButton = Button(window, bg="#f0a510", command=quit, image=imgExit)
        currentGuess = count // 5 - 1
        guessedCombo = guesses[currentGuess]
        currentLine, currentGButton = lineGroups[currentGuess], gButtons[currentGuess]
        if LANG == "RU":
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
            currentGuess = min(count // 5, 5) - 1
        while count > 0:
            lines[count - 1].config(image=label)
            guesses[currentGuess].pop()
            gButtons[currentGuess].pop()
            count -= 1
            break

    gandalfButton = Button(window, width=110, height=70, image=gandalf, command=lambda: charCall(gandalf))
    bilboButton = Button(window, width=110, height=70, image=bilbo, command=lambda: charCall(bilbo))
    thorinButton = Button(window, width=110, height=70, image=thorin, command=lambda: charCall(thorin))
    elrondButton = Button(window, width=110, height=70, image=elrond, command=lambda: charCall(elrond))
    beornButton = Button(window, width=110, height=70, image=beorn, command=lambda: charCall(beorn))
    balinButton = Button(window, width=110, height=70, image=balin, command=lambda: charCall(balin))
    dwalinButton = Button(window, width=110, height=70, image=dwalin, command=lambda: charCall(dwalin))
    gloinButton = Button(window, width=110, height=70, image=gloin, command=lambda: charCall(gloin))
    filiButton = Button(window, width=110, height=70, image=fili, command=lambda: charCall(fili))
    kiliButton = Button(window, width=110, height=70, image=kili, command=lambda: charCall(kili))
    enterButton = Button(window, width=55, height=70, image=enter, command=enterCall)
    trollButton = Button(window, width=110, height=70, image=troll, command=lambda: charCall(troll))
    gollumButton = Button(window, width=110, height=70, image=gollum, command=lambda: charCall(gollum))
    greatGoblinButton = Button(window, width=110, height=70, image=greatGoblin, command=lambda: charCall(greatGoblin))
    smaugButton = Button(window, width=110, height=70, image=smaug, command=lambda: charCall(smaug))
    backspaceButton = Button(window, width=55, height=70, image=backspace, command=backspaceCall)
    
    gandalfButton.place(x=10, y=500), bilboButton.place(x=120, y=500), thorinButton.place(x=230, y=500)
    elrondButton.place(x=340, y=500), beornButton.place(x=450, y=500), balinButton.place(x=10, y=570)
    dwalinButton.place(x=120, y=570), gloinButton.place(x=230, y=570), filiButton.place(x=340, y=570)
    kiliButton.place(x=450, y=570), enterButton.place(x=10, y=640), trollButton.place(x=65, y=640)
    gollumButton.place(x=175, y=640), greatGoblinButton.place(x=285, y=640), smaugButton.place(x=395, y=640)
    backspaceButton.place(x=505, y=640)

    keyButtons = [
        gandalfButton, bilboButton, thorinButton, elrondButton, beornButton, balinButton, dwalinButton,
        gloinButton, filiButton, kiliButton, trollButton, gollumButton, greatGoblinButton, smaugButton
    ]

    if THEME == "LIGHT":
        for keyButton in keyButtons:
            keyButton.config(bg=BG_LIGHT, activebackground=BG_LIGHT)
        enterButton.config(image=enter, bg=BG_LIGHT, activebackground=BG_LIGHT)
        backspaceButton.config(image=backspace, bg=BG_LIGHT, activebackground=BG_LIGHT)
    
    elif THEME == "DARK":
        for keyButton in keyButtons:
            keyButton.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK)
        enterButton.config(image=enterLight, bg=WIDGET_DARK, activebackground=WIDGET_DARK)
        backspaceButton.config(image=backspaceLight, bg=WIDGET_DARK, activebackground=WIDGET_DARK)
    
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
        enterButton.config(bg=BG_LIGHT, activebackground=BG_LIGHT, image=enter)
        backspaceButton.config(bg=BG_LIGHT, activebackground=BG_LIGHT, image=backspace)

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
        enterButton.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK, image=enterLight)
        backspaceButton.config(bg=WIDGET_DARK, activebackground=WIDGET_DARK, image=backspaceLight)

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
