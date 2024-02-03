from tkinter import *
import random

LANG = "ENG"
THEME = "LIGHT"

ALL_TRIES = 0
ALL_WINS = 0
CURRENT_STREAK = 0
STREAKS = [0]
BEST_STREAK = max(STREAKS)

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
        window.config(background="#f0f0f0")
    elif THEME == "DARK":
        window.config(background="#111111")

    def new_game():
        window.destroy()

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
    great_goblin = PhotoImage(file="img/great_goblin.png")
    smaug = PhotoImage(file="img/smaug.png")

    keyboard = [gandalf, bilbo, thorin, elrond, beorn, balin, dwalin, gloin, fili, kili, troll, gollum, great_goblin, smaug]
    solution = random.sample(keyboard, 5)
    guess1, g1_b = [], []
    guess2, g2_b = [], []
    guess3, g3_b = [], []
    guess4, g4_b = [], []
    guess5, g5_b = [], []
    guess6, g6_b = [], []

    congrats_list = [awesome, excellent, great_job, outstanding, well_done]
    congrats = random.choice(congrats_list)

    congrats_list_ru = [awesome_ru, excellent_ru, great_job_ru, outstanding_ru, well_done_ru]
    congrats_ru = random.choice(congrats_list_ru)

    def close_info():
        global rules_label, close_button
        rules_label.destroy()
        close_button.destroy()

    def rules_call():
        global rules_label, close_button
        if LANG == "ENG":
            rules_label = Label(window, image=rules, bg="#002b82")
            close_button = Button(window, image=close_r, bg="#002b82", activebackground="#002b82", command=close_info)
        elif LANG == "RU":
            rules_label = Label(window, image=rules_ru, bg="#002b82")
            close_button = Button(window, image=close_r, bg="#002b82", activebackground="#002b82", command=close_info)
        rules_label.place(x=0, y=0), close_button.place(x=494, y=18)

    if THEME == "LIGHT":
        about_button = Button(window, width=50, height=50, image=logo, command=rules_call, bg="#f0f0f0", activebackground="#f0f0f0")
        if LANG == "ENG":
            title_label = Label(window, text="HOBBITLE", font=("Courier New", 50, "bold"), bg="#f0f0f0", fg="#daaf00")
        elif LANG == "RU":
            title_label = Label(window, text="ХОББИТЛИ", font=("Courier New", 50, "bold"), bg="#f0f0f0", fg="#daaf00")

        l1 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l2 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l3 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l4 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l5 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")

        l6 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l7 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l8 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l9 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l10 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")

        l11 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l12 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l13 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l14 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l15 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")

        l16 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l17 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l18 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l19 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l20 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")

        l21 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l22 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l23 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l24 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l25 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")

        l26 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l27 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l28 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l29 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
        l30 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#f0f0f0")
    
    elif THEME == "DARK":
        about_button = Button(window, width=50, height=50, image=logo, command=rules_call, bg="#222222", activebackground="#222222")
        if LANG == "ENG":
            title_label = Label(window, text="HOBBITLE", font=("Courier New", 50, "bold"), bg="#111111", fg="#daaf00")
        elif LANG == "RU":
            title_label = Label(window, text="ХОББИТЛИ", font=("Courier New", 50, "bold"), bg="#111111", fg="#daaf00")

        l1 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l2 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l3 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l4 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l5 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        
        l6 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l7 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l8 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l9 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l10 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        

        l11 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l12 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l13 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l14 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l15 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        

        l16 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l17 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l18 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l19 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l20 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        

        l21 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l22 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l23 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l24 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l25 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        

        l26 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l27 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l28 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l29 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")        
        l30 = Label(window, width=110, height=70, image=label, relief=RAISED, bg="#222222")

    about_button.place(x=10, y=10), title_label.place(x=100, y=0)
    l1.place(x=10, y=70), l2.place(x=120, y=70), l3.place(x=230, y=70), l4.place(x=340, y=70), l5.place(x=450, y=70)
    l6.place(x=10, y=140), l7.place(x=120, y=140), l8.place(x=230, y=140), l9.place(x=340, y=140), l10.place(x=450, y=140)
    l11.place(x=10, y=210), l12.place(x=120, y=210), l13.place(x=230, y=210), l14.place(x=340, y=210), l15.place(x=450, y=210)
    l16.place(x=10, y=280), l17.place(x=120, y=280), l18.place(x=230, y=280), l19.place(x=340, y=280), l20.place(x=450, y=280)
    l21.place(x=10, y=350), l22.place(x=120, y=350), l23.place(x=230, y=350), l24.place(x=340, y=350), l25.place(x=450, y=350)
    l26.place(x=10, y=420), l27.place(x=120, y=420), l28.place(x=230, y=420), l29.place(x=340, y=420), l30.place(x=450, y=420)

    line1, line2 = [l1, l2, l3, l4, l5], [l6, l7, l8, l9, l10]
    line3, line4 = [l11, l12, l13, l14, l15], [l16, l17, l18, l19, l20]
    line5, line6 = [l21, l22, l23, l24, l25], [l26, l27, l28, l29, l30]

    line1_6 = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16,
               l17, l18, l19, l20, l21, l22, l23, l24, l25, l26, l27, l28, l29, l30]

    count = 0
    def gandalf_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=gandalf)
                count += 1
                guess1.append(gandalf)
                g1_b.append(gandalf_button)
                break
            elif count == 1:
                l2.config(image=gandalf)
                count += 1
                guess1.append(gandalf)
                g1_b.append(gandalf_button)
                break
            elif count == 2:
                l3.config(image=gandalf)
                count += 1
                guess1.append(gandalf)
                g1_b.append(gandalf_button)
                break
            elif count == 3:
                l4.config(image=gandalf)
                count += 1
                guess1.append(gandalf)
                g1_b.append(gandalf_button)
                break
            elif count == 4:
                l5.config(image=gandalf)
                count += 1
                guess1.append(gandalf)
                g1_b.append(gandalf_button)
                break
            elif count == 5:
                l6.config(image=gandalf)
                count += 1
                guess2.append(gandalf)
                g2_b.append(gandalf_button)
                break
            elif count == 6:
                l7.config(image=gandalf)
                count += 1
                guess2.append(gandalf)
                g2_b.append(gandalf_button)
                break
            elif count == 7:
                l8.config(image=gandalf)
                count += 1
                guess2.append(gandalf)
                g2_b.append(gandalf_button)
                break
            elif count == 8:
                l9.config(image=gandalf)
                count += 1
                guess2.append(gandalf)
                g2_b.append(gandalf_button)
                break
            elif count == 9:
                l10.config(image=gandalf)
                count += 1
                guess2.append(gandalf)
                g2_b.append(gandalf_button)
                break
            elif count == 10:
                l11.config(image=gandalf)
                count += 1
                guess3.append(gandalf)
                g3_b.append(gandalf_button)
                break
            elif count == 11:
                l12.config(image=gandalf)
                count += 1
                guess3.append(gandalf)
                g3_b.append(gandalf_button)
                break
            elif count == 12:
                l13.config(image=gandalf)
                count += 1
                guess3.append(gandalf)
                g3_b.append(gandalf_button)
                break
            elif count == 13:
                l14.config(image=gandalf)
                count += 1
                guess3.append(gandalf)
                g3_b.append(gandalf_button)
                break
            elif count == 14:
                l15.config(image=gandalf)
                count += 1
                guess3.append(gandalf)
                g3_b.append(gandalf_button)
                break
            elif count == 15:
                l16.config(image=gandalf)
                count += 1
                guess4.append(gandalf)
                g4_b.append(gandalf_button)
                break
            elif count == 16:
                l17.config(image=gandalf)
                count += 1
                guess4.append(gandalf)
                g4_b.append(gandalf_button)
                break
            elif count == 17:
                l18.config(image=gandalf)
                count += 1
                guess4.append(gandalf)
                g4_b.append(gandalf_button)
                break
            elif count == 18:
                l19.config(image=gandalf)
                count += 1
                guess4.append(gandalf)
                g4_b.append(gandalf_button)
                break
            elif count == 19:
                l20.config(image=gandalf)
                count += 1
                guess4.append(gandalf)
                g4_b.append(gandalf_button)
                break
            elif count == 20:
                l21.config(image=gandalf)
                count += 1
                guess5.append(gandalf)
                g5_b.append(gandalf_button)
                break
            elif count == 21:
                l22.config(image=gandalf)
                count += 1
                guess5.append(gandalf)
                g5_b.append(gandalf_button)
                break
            elif count == 22:
                l23.config(image=gandalf)
                count += 1
                guess5.append(gandalf)
                g5_b.append(gandalf_button)
                break
            elif count == 23:
                l24.config(image=gandalf)
                count += 1
                guess5.append(gandalf)
                g5_b.append(gandalf_button)
                break
            elif count == 24:
                l25.config(image=gandalf)
                count += 1
                guess5.append(gandalf)
                g5_b.append(gandalf_button)
                break
            elif count == 25:
                l26.config(image=gandalf)
                count += 1
                guess6.append(gandalf)
                g6_b.append(gandalf_button)
                break
            elif count == 26:
                l27.config(image=gandalf)
                count += 1
                guess6.append(gandalf)
                g6_b.append(gandalf_button)
                break
            elif count == 27:
                l28.config(image=gandalf)
                count += 1
                guess6.append(gandalf)
                g6_b.append(gandalf_button)
                break
            elif count == 28:
                l29.config(image=gandalf)
                count += 1
                guess6.append(gandalf)
                g6_b.append(gandalf_button)
                break
            elif count == 29:
                l30.config(image=gandalf)
                count += 1
                guess6.append(gandalf)
                g6_b.append(gandalf_button)
                break

    def bilbo_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=bilbo)
                count += 1
                guess1.append(bilbo)
                g1_b.append(bilbo_button)
                break
            elif count == 1:
                l2.config(image=bilbo)
                count += 1
                guess1.append(bilbo)
                g1_b.append(bilbo_button)
                break
            elif count == 2:
                l3.config(image=bilbo)
                count += 1
                guess1.append(bilbo)
                g1_b.append(bilbo_button)
                break
            elif count == 3:
                l4.config(image=bilbo)
                count += 1
                guess1.append(bilbo)
                g1_b.append(bilbo_button)
                break
            elif count == 4:
                l5.config(image=bilbo)
                count += 1
                guess1.append(bilbo)
                g1_b.append(bilbo_button)
                break
            elif count == 5:
                l6.config(image=bilbo)
                count += 1
                guess2.append(bilbo)
                g2_b.append(bilbo_button)
                break
            elif count == 6:
                l7.config(image=bilbo)
                count += 1
                guess2.append(bilbo)
                g2_b.append(bilbo_button)
                break
            elif count == 7:
                l8.config(image=bilbo)
                count += 1
                guess2.append(bilbo)
                g2_b.append(bilbo_button)
                break
            elif count == 8:
                l9.config(image=bilbo)
                count += 1
                guess2.append(bilbo)
                g2_b.append(bilbo_button)
                break
            elif count == 9:
                l10.config(image=bilbo)
                count += 1
                guess2.append(bilbo)
                g2_b.append(bilbo_button)
                break
            elif count == 10:
                l11.config(image=bilbo)
                count += 1
                guess3.append(bilbo)
                g3_b.append(bilbo_button)
                break
            elif count == 11:
                l12.config(image=bilbo)
                count += 1
                guess3.append(bilbo)
                g3_b.append(bilbo_button)
                break
            elif count == 12:
                l13.config(image=bilbo)
                count += 1
                guess3.append(bilbo)
                g3_b.append(bilbo_button)
                break
            elif count == 13:
                l14.config(image=bilbo)
                count += 1
                guess3.append(bilbo)
                g3_b.append(bilbo_button)
                break
            elif count == 14:
                l15.config(image=bilbo)
                count += 1
                guess3.append(bilbo)
                g3_b.append(bilbo_button)
                break
            elif count == 15:
                l16.config(image=bilbo)
                count += 1
                guess4.append(bilbo)
                g4_b.append(bilbo_button)
                break
            elif count == 16:
                l17.config(image=bilbo)
                count += 1
                guess4.append(bilbo)
                g4_b.append(bilbo_button)
                break
            elif count == 17:
                l18.config(image=bilbo)
                count += 1
                guess4.append(bilbo)
                g4_b.append(bilbo_button)
                break
            elif count == 18:
                l19.config(image=bilbo)
                count += 1
                guess4.append(bilbo)
                g4_b.append(bilbo_button)
                break
            elif count == 19:
                l20.config(image=bilbo)
                count += 1
                guess4.append(bilbo)
                g4_b.append(bilbo_button)
                break
            elif count == 20:
                l21.config(image=bilbo)
                count += 1
                guess5.append(bilbo)
                g5_b.append(bilbo_button)
                break
            elif count == 21:
                l22.config(image=bilbo)
                count += 1
                guess5.append(bilbo)
                g5_b.append(bilbo_button)
                break
            elif count == 22:
                l23.config(image=bilbo)
                count += 1
                guess5.append(bilbo)
                g5_b.append(bilbo_button)
                break
            elif count == 23:
                l24.config(image=bilbo)
                count += 1
                guess5.append(bilbo)
                g5_b.append(bilbo_button)
                break
            elif count == 24:
                l25.config(image=bilbo)
                count += 1
                guess5.append(bilbo)
                g5_b.append(bilbo_button)
                break
            elif count == 25:
                l26.config(image=bilbo)
                count += 1
                guess6.append(bilbo)
                g6_b.append(bilbo_button)
                break
            elif count == 26:
                l27.config(image=bilbo)
                count += 1
                guess6.append(bilbo)
                g6_b.append(bilbo_button)
                break
            elif count == 27:
                l28.config(image=bilbo)
                count += 1
                guess6.append(bilbo)
                g6_b.append(bilbo_button)
                break
            elif count == 28:
                l29.config(image=bilbo)
                count += 1
                guess6.append(bilbo)
                g6_b.append(bilbo_button)
                break
            elif count == 29:
                l30.config(image=bilbo)
                count += 1
                guess6.append(bilbo)
                g6_b.append(bilbo_button)
                break

    def thorin_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=thorin)
                count += 1
                guess1.append(thorin)
                g1_b.append(thorin_button)
                break
            elif count == 1:
                l2.config(image=thorin)
                count += 1
                guess1.append(thorin)
                g1_b.append(thorin_button)
                break
            elif count == 2:
                l3.config(image=thorin)
                count += 1
                guess1.append(thorin)
                g1_b.append(thorin_button)
                break
            elif count == 3:
                l4.config(image=thorin)
                count += 1
                guess1.append(thorin)
                g1_b.append(thorin_button)
                break
            elif count == 4:
                l5.config(image=thorin)
                count += 1
                guess1.append(thorin)
                g1_b.append(thorin_button)
                break
            elif count == 5:
                l6.config(image=thorin)
                count += 1
                guess2.append(thorin)
                g2_b.append(thorin_button)
                break
            elif count == 6:
                l7.config(image=thorin)
                count += 1
                guess2.append(thorin)
                g2_b.append(thorin_button)
                break
            elif count == 7:
                l8.config(image=thorin)
                count += 1
                guess2.append(thorin)
                g2_b.append(thorin_button)
                break
            elif count == 8:
                l9.config(image=thorin)
                count += 1
                guess2.append(thorin)
                g2_b.append(thorin_button)
                break
            elif count == 9:
                l10.config(image=thorin)
                count += 1
                guess2.append(thorin)
                g2_b.append(thorin_button)
                break
            elif count == 10:
                l11.config(image=thorin)
                count += 1
                guess3.append(thorin)
                g3_b.append(thorin_button)
                break
            elif count == 11:
                l12.config(image=thorin)
                count += 1
                guess3.append(thorin)
                g3_b.append(thorin_button)
                break
            elif count == 12:
                l13.config(image=thorin)
                count += 1
                guess3.append(thorin)
                g3_b.append(thorin_button)
                break
            elif count == 13:
                l14.config(image=thorin)
                count += 1
                guess3.append(thorin)
                g3_b.append(thorin_button)
                break
            elif count == 14:
                l15.config(image=thorin)
                count += 1
                guess3.append(thorin)
                g3_b.append(thorin_button)
                break
            elif count == 15:
                l16.config(image=thorin)
                count += 1
                guess4.append(thorin)
                g4_b.append(thorin_button)
                break
            elif count == 16:
                l17.config(image=thorin)
                count += 1
                guess4.append(thorin)
                g4_b.append(thorin_button)
                break
            elif count == 17:
                l18.config(image=thorin)
                count += 1
                guess4.append(thorin)
                g4_b.append(thorin_button)
                break
            elif count == 18:
                l19.config(image=thorin)
                count += 1
                guess4.append(thorin)
                g4_b.append(thorin_button)
                break
            elif count == 19:
                l20.config(image=thorin)
                count += 1
                guess4.append(thorin)
                g4_b.append(thorin_button)
                break
            elif count == 20:
                l21.config(image=thorin)
                count += 1
                guess5.append(thorin)
                g5_b.append(thorin_button)
                break
            elif count == 21:
                l22.config(image=thorin)
                count += 1
                guess5.append(thorin)
                g5_b.append(thorin_button)
                break
            elif count == 22:
                l23.config(image=thorin)
                count += 1
                guess5.append(thorin)
                g5_b.append(thorin_button)
                break
            elif count == 23:
                l24.config(image=thorin)
                count += 1
                guess5.append(thorin)
                g5_b.append(thorin_button)
                break
            elif count == 24:
                l25.config(image=thorin)
                count += 1
                guess5.append(thorin)
                g5_b.append(thorin_button)
                break
            elif count == 25:
                l26.config(image=thorin)
                count += 1
                guess6.append(thorin)
                g6_b.append(thorin_button)
                break
            elif count == 26:
                l27.config(image=thorin)
                count += 1
                guess6.append(thorin)
                g6_b.append(thorin_button)
                break
            elif count == 27:
                l28.config(image=thorin)
                count += 1
                guess6.append(thorin)
                g6_b.append(thorin_button)
                break
            elif count == 28:
                l29.config(image=thorin)
                count += 1
                guess6.append(thorin)
                g6_b.append(thorin_button)
                break
            elif count == 29:
                l30.config(image=thorin)
                count += 1
                guess6.append(thorin)
                g6_b.append(thorin_button)
                break

    def elrond_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=elrond)
                count += 1
                guess1.append(elrond)
                g1_b.append(elrond_button)
                break
            elif count == 1:
                l2.config(image=elrond)
                count += 1
                guess1.append(elrond)
                g1_b.append(elrond_button)
                break
            elif count == 2:
                l3.config(image=elrond)
                count += 1
                guess1.append(elrond)
                g1_b.append(elrond_button)
                break
            elif count == 3:
                l4.config(image=elrond)
                count += 1
                guess1.append(elrond)
                g1_b.append(elrond_button)
                break
            elif count == 4:
                l5.config(image=elrond)
                count += 1
                guess1.append(elrond)
                g1_b.append(elrond_button)
                break
            elif count == 5:
                l6.config(image=elrond)
                count += 1
                guess2.append(elrond)
                g2_b.append(elrond_button)
                break
            elif count == 6:
                l7.config(image=elrond)
                count += 1
                guess2.append(elrond)
                g2_b.append(elrond_button)
                break
            elif count == 7:
                l8.config(image=elrond)
                count += 1
                guess2.append(elrond)
                g2_b.append(elrond_button)
                break
            elif count == 8:
                l9.config(image=elrond)
                count += 1
                guess2.append(elrond)
                g2_b.append(elrond_button)
                break
            elif count == 9:
                l10.config(image=elrond)
                count += 1
                guess2.append(elrond)
                g2_b.append(elrond_button)
                break
            elif count == 10:
                l11.config(image=elrond)
                count += 1
                guess3.append(elrond)
                g3_b.append(elrond_button)
                break
            elif count == 11:
                l12.config(image=elrond)
                count += 1
                guess3.append(elrond)
                g3_b.append(elrond_button)
                break
            elif count == 12:
                l13.config(image=elrond)
                count += 1
                guess3.append(elrond)
                g3_b.append(elrond_button)
                break
            elif count == 13:
                l14.config(image=elrond)
                count += 1
                guess3.append(elrond)
                g3_b.append(elrond_button)
                break
            elif count == 14:
                l15.config(image=elrond)
                count += 1
                guess3.append(elrond)
                g3_b.append(elrond_button)
                break
            elif count == 15:
                l16.config(image=elrond)
                count += 1
                guess4.append(elrond)
                g4_b.append(elrond_button)
                break
            elif count == 16:
                l17.config(image=elrond)
                count += 1
                guess4.append(elrond)
                g4_b.append(elrond_button)
                break
            elif count == 17:
                l18.config(image=elrond)
                count += 1
                guess4.append(elrond)
                g4_b.append(elrond_button)
                break
            elif count == 18:
                l19.config(image=elrond)
                count += 1
                guess4.append(elrond)
                g4_b.append(elrond_button)
                break
            elif count == 19:
                l20.config(image=elrond)
                count += 1
                guess4.append(elrond)
                g4_b.append(elrond_button)
                break
            elif count == 20:
                l21.config(image=elrond)
                count += 1
                guess5.append(elrond)
                g5_b.append(elrond_button)
                break
            elif count == 21:
                l22.config(image=elrond)
                count += 1
                guess5.append(elrond)
                g5_b.append(elrond_button)
                break
            elif count == 22:
                l23.config(image=elrond)
                count += 1
                guess5.append(elrond)
                g5_b.append(elrond_button)
                break
            elif count == 23:
                l24.config(image=elrond)
                count += 1
                guess5.append(elrond)
                g5_b.append(elrond_button)
                break
            elif count == 24:
                l25.config(image=elrond)
                count += 1
                guess5.append(elrond)
                g5_b.append(elrond_button)
                break
            elif count == 25:
                l26.config(image=elrond)
                count += 1
                guess6.append(elrond)
                g6_b.append(elrond_button)
                break
            elif count == 26:
                l27.config(image=elrond)
                count += 1
                guess6.append(elrond)
                g6_b.append(elrond_button)
                break
            elif count == 27:
                l28.config(image=elrond)
                count += 1
                guess6.append(elrond)
                g6_b.append(elrond_button)
                break
            elif count == 28:
                l29.config(image=elrond)
                count += 1
                guess6.append(elrond)
                g6_b.append(elrond_button)
                break
            elif count == 29:
                l30.config(image=elrond)
                count += 1
                guess6.append(elrond)
                g6_b.append(elrond_button)
                break

    def beorn_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=beorn)
                count += 1
                guess1.append(beorn)
                g1_b.append(beorn_button)
                break
            elif count == 1:
                l2.config(image=beorn)
                count += 1
                guess1.append(beorn)
                g1_b.append(beorn_button)
                break
            elif count == 2:
                l3.config(image=beorn)
                count += 1
                guess1.append(beorn)
                g1_b.append(beorn_button)
                break
            elif count == 3:
                l4.config(image=beorn)
                count += 1
                guess1.append(beorn)
                g1_b.append(beorn_button)
                break
            elif count == 4:
                l5.config(image=beorn)
                count += 1
                guess1.append(beorn)
                g1_b.append(beorn_button)
                break
            elif count == 5:
                l6.config(image=beorn)
                count += 1
                guess2.append(beorn)
                g2_b.append(beorn_button)
                break
            elif count == 6:
                l7.config(image=beorn)
                count += 1
                guess2.append(beorn)
                g2_b.append(beorn_button)
                break
            elif count == 7:
                l8.config(image=beorn)
                count += 1
                guess2.append(beorn)
                g2_b.append(beorn_button)
                break
            elif count == 8:
                l9.config(image=beorn)
                count += 1
                guess2.append(beorn)
                g2_b.append(beorn_button)
                break
            elif count == 9:
                l10.config(image=beorn)
                count += 1
                guess2.append(beorn)
                g2_b.append(beorn_button)
                break
            elif count == 10:
                l11.config(image=beorn)
                count += 1
                guess3.append(beorn)
                g3_b.append(beorn_button)
                break
            elif count == 11:
                l12.config(image=beorn)
                count += 1
                guess3.append(beorn)
                g3_b.append(beorn_button)
                break
            elif count == 12:
                l13.config(image=beorn)
                count += 1
                guess3.append(beorn)
                g3_b.append(beorn_button)
                break
            elif count == 13:
                l14.config(image=beorn)
                count += 1
                guess3.append(beorn)
                g3_b.append(beorn_button)
                break
            elif count == 14:
                l15.config(image=beorn)
                count += 1
                guess3.append(beorn)
                g3_b.append(beorn_button)
                break
            elif count == 15:
                l16.config(image=beorn)
                count += 1
                guess4.append(beorn)
                g4_b.append(beorn_button)
                break
            elif count == 16:
                l17.config(image=beorn)
                count += 1
                guess4.append(beorn)
                g4_b.append(beorn_button)
                break
            elif count == 17:
                l18.config(image=beorn)
                count += 1
                guess4.append(beorn)
                g4_b.append(beorn_button)
                break
            elif count == 18:
                l19.config(image=beorn)
                count += 1
                guess4.append(beorn)
                g4_b.append(beorn_button)
                break
            elif count == 19:
                l20.config(image=beorn)
                count += 1
                guess4.append(beorn)
                g4_b.append(beorn_button)
                break
            elif count == 20:
                l21.config(image=beorn)
                count += 1
                guess5.append(beorn)
                g5_b.append(beorn_button)
                break
            elif count == 21:
                l22.config(image=beorn)
                count += 1
                guess5.append(beorn)
                g5_b.append(beorn_button)
                break
            elif count == 22:
                l23.config(image=beorn)
                count += 1
                guess5.append(beorn)
                g5_b.append(beorn_button)
                break
            elif count == 23:
                l24.config(image=beorn)
                count += 1
                guess5.append(beorn)
                g5_b.append(beorn_button)
                break
            elif count == 24:
                l25.config(image=beorn)
                count += 1
                guess5.append(beorn)
                g5_b.append(beorn_button)
                break
            elif count == 25:
                l26.config(image=beorn)
                count += 1
                guess6.append(beorn)
                g6_b.append(beorn_button)
                break
            elif count == 26:
                l27.config(image=beorn)
                count += 1
                guess6.append(beorn)
                g6_b.append(beorn_button)
                break
            elif count == 27:
                l28.config(image=beorn)
                count += 1
                guess6.append(beorn)
                g6_b.append(beorn_button)
                break
            elif count == 28:
                l29.config(image=beorn)
                count += 1
                guess6.append(beorn)
                g6_b.append(beorn_button)
                break
            elif count == 29:
                l30.config(image=beorn)
                count += 1
                guess6.append(beorn)
                g6_b.append(beorn_button)
                break

    def balin_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=balin)
                count += 1
                guess1.append(balin)
                g1_b.append(balin_button)
                break
            elif count == 1:
                l2.config(image=balin)
                count += 1
                guess1.append(balin)
                g1_b.append(balin_button)
                break
            elif count == 2:
                l3.config(image=balin)
                count += 1
                guess1.append(balin)
                g1_b.append(balin_button)
                break
            elif count == 3:
                l4.config(image=balin)
                count += 1
                guess1.append(balin)
                g1_b.append(balin_button)
                break
            elif count == 4:
                l5.config(image=balin)
                count += 1
                guess1.append(balin)
                g1_b.append(balin_button)
                break
            elif count == 5:
                l6.config(image=balin)
                count += 1
                guess2.append(balin)
                g2_b.append(balin_button)
                break
            elif count == 6:
                l7.config(image=balin)
                count += 1
                guess2.append(balin)
                g2_b.append(balin_button)
                break
            elif count == 7:
                l8.config(image=balin)
                count += 1
                guess2.append(balin)
                g2_b.append(balin_button)
                break
            elif count == 8:
                l9.config(image=balin)
                count += 1
                guess2.append(balin)
                g2_b.append(balin_button)
                break
            elif count == 9:
                l10.config(image=balin)
                count += 1
                guess2.append(balin)
                g2_b.append(balin_button)
                break
            elif count == 10:
                l11.config(image=balin)
                count += 1
                guess3.append(balin)
                g3_b.append(balin_button)
                break
            elif count == 11:
                l12.config(image=balin)
                count += 1
                guess3.append(balin)
                g3_b.append(balin_button)
                break
            elif count == 12:
                l13.config(image=balin)
                count += 1
                guess3.append(balin)
                g3_b.append(balin_button)
                break
            elif count == 13:
                l14.config(image=balin)
                count += 1
                guess3.append(balin)
                g3_b.append(balin_button)
                break
            elif count == 14:
                l15.config(image=balin)
                count += 1
                guess3.append(balin)
                g3_b.append(balin_button)
                break
            elif count == 15:
                l16.config(image=balin)
                count += 1
                guess4.append(balin)
                g4_b.append(balin_button)
                break
            elif count == 16:
                l17.config(image=balin)
                count += 1
                guess4.append(balin)
                g4_b.append(balin_button)
                break
            elif count == 17:
                l18.config(image=balin)
                count += 1
                guess4.append(balin)
                g4_b.append(balin_button)
                break
            elif count == 18:
                l19.config(image=balin)
                count += 1
                guess4.append(balin)
                g4_b.append(balin_button)
                break
            elif count == 19:
                l20.config(image=balin)
                count += 1
                guess4.append(balin)
                g4_b.append(balin_button)
                break
            elif count == 20:
                l21.config(image=balin)
                count += 1
                guess5.append(balin)
                g5_b.append(balin_button)
                break
            elif count == 21:
                l22.config(image=balin)
                count += 1
                guess5.append(balin)
                g5_b.append(balin_button)
                break
            elif count == 22:
                l23.config(image=balin)
                count += 1
                guess5.append(balin)
                g5_b.append(balin_button)
                break
            elif count == 23:
                l24.config(image=balin)
                count += 1
                guess5.append(balin)
                g5_b.append(balin_button)
                break
            elif count == 24:
                l25.config(image=balin)
                count += 1
                guess5.append(balin)
                g5_b.append(balin_button)
                break
            elif count == 25:
                l26.config(image=balin)
                count += 1
                guess6.append(balin)
                g6_b.append(balin_button)
                break
            elif count == 26:
                l27.config(image=balin)
                count += 1
                guess6.append(balin)
                g6_b.append(balin_button)
                break
            elif count == 27:
                l28.config(image=balin)
                count += 1
                guess6.append(balin)
                g6_b.append(balin_button)
                break
            elif count == 28:
                l29.config(image=balin)
                count += 1
                guess6.append(balin)
                g6_b.append(balin_button)
                break
            elif count == 29:
                l30.config(image=balin)
                count += 1
                guess6.append(balin)
                g6_b.append(balin_button)
                break

    def dwalin_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=dwalin)
                count += 1
                guess1.append(dwalin)
                g1_b.append(dwalin_button)
                break
            elif count == 1:
                l2.config(image=dwalin)
                count += 1
                guess1.append(dwalin)
                g1_b.append(dwalin_button)
                break
            elif count == 2:
                l3.config(image=dwalin)
                count += 1
                guess1.append(dwalin)
                g1_b.append(dwalin_button)
                break
            elif count == 3:
                l4.config(image=dwalin)
                count += 1
                guess1.append(dwalin)
                g1_b.append(dwalin_button)
                break
            elif count == 4:
                l5.config(image=dwalin)
                count += 1
                guess1.append(dwalin)
                g1_b.append(dwalin_button)
                break
            elif count == 5:
                l6.config(image=dwalin)
                count += 1
                guess2.append(dwalin)
                g2_b.append(dwalin_button)
                break
            elif count == 6:
                l7.config(image=dwalin)
                count += 1
                guess2.append(dwalin)
                g2_b.append(dwalin_button)
                break
            elif count == 7:
                l8.config(image=dwalin)
                count += 1
                guess2.append(dwalin)
                g2_b.append(dwalin_button)
                break
            elif count == 8:
                l9.config(image=dwalin)
                count += 1
                guess2.append(dwalin)
                g2_b.append(dwalin_button)
                break
            elif count == 9:
                l10.config(image=dwalin)
                count += 1
                guess2.append(dwalin)
                g2_b.append(dwalin_button)
                break
            elif count == 10:
                l11.config(image=dwalin)
                count += 1
                guess3.append(dwalin)
                g3_b.append(dwalin_button)
                break
            elif count == 11:
                l12.config(image=dwalin)
                count += 1
                guess3.append(dwalin)
                g3_b.append(dwalin_button)
                break
            elif count == 12:
                l13.config(image=dwalin)
                count += 1
                guess3.append(dwalin)
                g3_b.append(dwalin_button)
                break
            elif count == 13:
                l14.config(image=dwalin)
                count += 1
                guess3.append(dwalin)
                g3_b.append(dwalin_button)
                break
            elif count == 14:
                l15.config(image=dwalin)
                count += 1
                guess3.append(dwalin)
                g3_b.append(dwalin_button)
                break
            elif count == 15:
                l16.config(image=dwalin)
                count += 1
                guess4.append(dwalin)
                g4_b.append(dwalin_button)
                break
            elif count == 16:
                l17.config(image=dwalin)
                count += 1
                guess4.append(dwalin)
                g4_b.append(dwalin_button)
                break
            elif count == 17:
                l18.config(image=dwalin)
                count += 1
                guess4.append(dwalin)
                g4_b.append(dwalin_button)
                break
            elif count == 18:
                l19.config(image=dwalin)
                count += 1
                guess4.append(dwalin)
                g4_b.append(dwalin_button)
                break
            elif count == 19:
                l20.config(image=dwalin)
                count += 1
                guess4.append(dwalin)
                g4_b.append(dwalin_button)
                break
            elif count == 20:
                l21.config(image=dwalin)
                count += 1
                guess5.append(dwalin)
                g5_b.append(dwalin_button)
                break
            elif count == 21:
                l22.config(image=dwalin)
                count += 1
                guess5.append(dwalin)
                g5_b.append(dwalin_button)
                break
            elif count == 22:
                l23.config(image=dwalin)
                count += 1
                guess5.append(dwalin)
                g5_b.append(dwalin_button)
                break
            elif count == 23:
                l24.config(image=dwalin)
                count += 1
                guess5.append(dwalin)
                g5_b.append(dwalin_button)
                break
            elif count == 24:
                l25.config(image=dwalin)
                count += 1
                guess5.append(dwalin)
                g5_b.append(dwalin_button)
                break
            elif count == 25:
                l26.config(image=dwalin)
                count += 1
                guess6.append(dwalin)
                g6_b.append(dwalin_button)
                break
            elif count == 26:
                l27.config(image=dwalin)
                count += 1
                guess6.append(dwalin)
                g6_b.append(dwalin_button)
                break
            elif count == 27:
                l28.config(image=dwalin)
                count += 1
                guess6.append(dwalin)
                g6_b.append(dwalin_button)
                break
            elif count == 28:
                l29.config(image=dwalin)
                count += 1
                guess6.append(dwalin)
                g6_b.append(dwalin_button)
                break
            elif count == 29:
                l30.config(image=dwalin)
                count += 1
                guess6.append(dwalin)
                g6_b.append(dwalin_button)
                break

    def gloin_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=gloin)
                count += 1
                guess1.append(gloin)
                g1_b.append(gloin_button)
                break
            elif count == 1:
                l2.config(image=gloin)
                count += 1
                guess1.append(gloin)
                g1_b.append(gloin_button)
                break
            elif count == 2:
                l3.config(image=gloin)
                count += 1
                guess1.append(gloin)
                g1_b.append(gloin_button)
                break
            elif count == 3:
                l4.config(image=gloin)
                count += 1
                guess1.append(gloin)
                g1_b.append(gloin_button)
                break
            elif count == 4:
                l5.config(image=gloin)
                count += 1
                guess1.append(gloin)
                g1_b.append(gloin_button)
                break
            elif count == 5:
                l6.config(image=gloin)
                count += 1
                guess2.append(gloin)
                g2_b.append(gloin_button)
                break
            elif count == 6:
                l7.config(image=gloin)
                count += 1
                guess2.append(gloin)
                g2_b.append(gloin_button)
                break
            elif count == 7:
                l8.config(image=gloin)
                count += 1
                guess2.append(gloin)
                g2_b.append(gloin_button)
                break
            elif count == 8:
                l9.config(image=gloin)
                count += 1
                guess2.append(gloin)
                g2_b.append(gloin_button)
                break
            elif count == 9:
                l10.config(image=gloin)
                count += 1
                guess2.append(gloin)
                g2_b.append(gloin_button)
                break
            elif count == 10:
                l11.config(image=gloin)
                count += 1
                guess3.append(gloin)
                g3_b.append(gloin_button)
                break
            elif count == 11:
                l12.config(image=gloin)
                count += 1
                guess3.append(gloin)
                g3_b.append(gloin_button)
                break
            elif count == 12:
                l13.config(image=gloin)
                count += 1
                guess3.append(gloin)
                g3_b.append(gloin_button)
                break
            elif count == 13:
                l14.config(image=gloin)
                count += 1
                guess3.append(gloin)
                g3_b.append(gloin_button)
                break
            elif count == 14:
                l15.config(image=gloin)
                count += 1
                guess3.append(gloin)
                g3_b.append(gloin_button)
                break
            elif count == 15:
                l16.config(image=gloin)
                count += 1
                guess4.append(gloin)
                g4_b.append(gloin_button)
                break
            elif count == 16:
                l17.config(image=gloin)
                count += 1
                guess4.append(gloin)
                g4_b.append(gloin_button)
                break
            elif count == 17:
                l18.config(image=gloin)
                count += 1
                guess4.append(gloin)
                g4_b.append(gloin_button)
                break
            elif count == 18:
                l19.config(image=gloin)
                count += 1
                guess4.append(gloin)
                g4_b.append(gloin_button)
                break
            elif count == 19:
                l20.config(image=gloin)
                count += 1
                guess4.append(gloin)
                g4_b.append(gloin_button)
                break
            elif count == 20:
                l21.config(image=gloin)
                count += 1
                guess5.append(gloin)
                g5_b.append(gloin_button)
                break
            elif count == 21:
                l22.config(image=gloin)
                count += 1
                guess5.append(gloin)
                g5_b.append(gloin_button)
                break
            elif count == 22:
                l23.config(image=gloin)
                count += 1
                guess5.append(gloin)
                g5_b.append(gloin_button)
                break
            elif count == 23:
                l24.config(image=gloin)
                count += 1
                guess5.append(gloin)
                g5_b.append(gloin_button)
                break
            elif count == 24:
                l25.config(image=gloin)
                count += 1
                guess5.append(gloin)
                g5_b.append(gloin_button)
                break
            elif count == 25:
                l26.config(image=gloin)
                count += 1
                guess6.append(gloin)
                g6_b.append(gloin_button)
                break
            elif count == 26:
                l27.config(image=gloin)
                count += 1
                guess6.append(gloin)
                g6_b.append(gloin_button)
                break
            elif count == 27:
                l28.config(image=gloin)
                count += 1
                guess6.append(gloin)
                g6_b.append(gloin_button)
                break
            elif count == 28:
                l29.config(image=gloin)
                count += 1
                guess6.append(gloin)
                g6_b.append(gloin_button)
                break
            elif count == 29:
                l30.config(image=gloin)
                count += 1
                guess6.append(gloin)
                g6_b.append(gloin_button)
                break

    def fili_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=fili)
                count += 1
                guess1.append(fili)
                g1_b.append(fili_button)
                break
            elif count == 1:
                l2.config(image=fili)
                count += 1
                guess1.append(fili)
                g1_b.append(fili_button)
                break
            elif count == 2:
                l3.config(image=fili)
                count += 1
                guess1.append(fili)
                g1_b.append(fili_button)
                break
            elif count == 3:
                l4.config(image=fili)
                count += 1
                guess1.append(fili)
                g1_b.append(fili_button)
                break
            elif count == 4:
                l5.config(image=fili)
                count += 1
                guess1.append(fili)
                g1_b.append(fili_button)
                break
            elif count == 5:
                l6.config(image=fili)
                count += 1
                guess2.append(fili)
                g2_b.append(fili_button)
                break
            elif count == 6:
                l7.config(image=fili)
                count += 1
                guess2.append(fili)
                g2_b.append(fili_button)
                break
            elif count == 7:
                l8.config(image=fili)
                count += 1
                guess2.append(fili)
                g2_b.append(fili_button)
                break
            elif count == 8:
                l9.config(image=fili)
                count += 1
                guess2.append(fili)
                g2_b.append(fili_button)
                break
            elif count == 9:
                l10.config(image=fili)
                count += 1
                guess2.append(fili)
                g2_b.append(fili_button)
                break
            elif count == 10:
                l11.config(image=fili)
                count += 1
                guess3.append(fili)
                g3_b.append(fili_button)
                break
            elif count == 11:
                l12.config(image=fili)
                count += 1
                guess3.append(fili)
                g3_b.append(fili_button)
                break
            elif count == 12:
                l13.config(image=fili)
                count += 1
                guess3.append(fili)
                g3_b.append(fili_button)
                break
            elif count == 13:
                l14.config(image=fili)
                count += 1
                guess3.append(fili)
                g3_b.append(fili_button)
                break
            elif count == 14:
                l15.config(image=fili)
                count += 1
                guess3.append(fili)
                g3_b.append(fili_button)
                break
            elif count == 15:
                l16.config(image=fili)
                count += 1
                guess4.append(fili)
                g4_b.append(fili_button)
                break
            elif count == 16:
                l17.config(image=fili)
                count += 1
                guess4.append(fili)
                g4_b.append(fili_button)
                break
            elif count == 17:
                l18.config(image=fili)
                count += 1
                guess4.append(fili)
                g4_b.append(fili_button)
                break
            elif count == 18:
                l19.config(image=fili)
                count += 1
                guess4.append(fili)
                g4_b.append(fili_button)
                break
            elif count == 19:
                l20.config(image=fili)
                count += 1
                guess4.append(fili)
                g4_b.append(fili_button)
                break
            elif count == 20:
                l21.config(image=fili)
                count += 1
                guess5.append(fili)
                g5_b.append(fili_button)
                break
            elif count == 21:
                l22.config(image=fili)
                count += 1
                guess5.append(fili)
                g5_b.append(fili_button)
                break
            elif count == 22:
                l23.config(image=fili)
                count += 1
                guess5.append(fili)
                g5_b.append(fili_button)
                break
            elif count == 23:
                l24.config(image=fili)
                count += 1
                guess5.append(fili)
                g5_b.append(fili_button)
                break
            elif count == 24:
                l25.config(image=fili)
                count += 1
                guess5.append(fili)
                g5_b.append(fili_button)
                break
            elif count == 25:
                l26.config(image=fili)
                count += 1
                guess6.append(fili)
                g6_b.append(fili_button)
                break
            elif count == 26:
                l27.config(image=fili)
                count += 1
                guess6.append(fili)
                g6_b.append(fili_button)
                break
            elif count == 27:
                l28.config(image=fili)
                count += 1
                guess6.append(fili)
                g6_b.append(fili_button)
                break
            elif count == 28:
                l29.config(image=fili)
                count += 1
                guess6.append(fili)
                g6_b.append(fili_button)
                break
            elif count == 29:
                l30.config(image=fili)
                count += 1
                guess6.append(fili)
                g6_b.append(fili_button)
                break

    def kili_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=kili)
                count += 1
                guess1.append(kili)
                g1_b.append(kili_button)
                break
            elif count == 1:
                l2.config(image=kili)
                count += 1
                guess1.append(kili)
                g1_b.append(kili_button)
                break
            elif count == 2:
                l3.config(image=kili)
                count += 1
                guess1.append(kili)
                g1_b.append(kili_button)
                break
            elif count == 3:
                l4.config(image=kili)
                count += 1
                guess1.append(kili)
                g1_b.append(kili_button)
                break
            elif count == 4:
                l5.config(image=kili)
                count += 1
                guess1.append(kili)
                g1_b.append(kili_button)
                break
            elif count == 5:
                l6.config(image=kili)
                count += 1
                guess2.append(kili)
                g2_b.append(kili_button)
                break
            elif count == 6:
                l7.config(image=kili)
                count += 1
                guess2.append(kili)
                g2_b.append(kili_button)
                break
            elif count == 7:
                l8.config(image=kili)
                count += 1
                guess2.append(kili)
                g2_b.append(kili_button)
                break
            elif count == 8:
                l9.config(image=kili)
                count += 1
                guess2.append(kili)
                g2_b.append(kili_button)
                break
            elif count == 9:
                l10.config(image=kili)
                count += 1
                guess2.append(kili)
                g2_b.append(kili_button)
                break
            elif count == 10:
                l11.config(image=kili)
                count += 1
                guess3.append(kili)
                g3_b.append(kili_button)
                break
            elif count == 11:
                l12.config(image=kili)
                count += 1
                guess3.append(kili)
                g3_b.append(kili_button)
                break
            elif count == 12:
                l13.config(image=kili)
                count += 1
                guess3.append(kili)
                g3_b.append(kili_button)
                break
            elif count == 13:
                l14.config(image=kili)
                count += 1
                guess3.append(kili)
                g3_b.append(kili_button)
                break
            elif count == 14:
                l15.config(image=kili)
                count += 1
                guess3.append(kili)
                g3_b.append(kili_button)
                break
            elif count == 15:
                l16.config(image=kili)
                count += 1
                guess4.append(kili)
                g4_b.append(kili_button)
                break
            elif count == 16:
                l17.config(image=kili)
                count += 1
                guess4.append(kili)
                g4_b.append(kili_button)
                break
            elif count == 17:
                l18.config(image=kili)
                count += 1
                guess4.append(kili)
                g4_b.append(kili_button)
                break
            elif count == 18:
                l19.config(image=kili)
                count += 1
                guess4.append(kili)
                g4_b.append(kili_button)
                break
            elif count == 19:
                l20.config(image=kili)
                count += 1
                guess4.append(kili)
                g4_b.append(kili_button)
                break
            elif count == 20:
                l21.config(image=kili)
                count += 1
                guess5.append(kili)
                g5_b.append(kili_button)
                break
            elif count == 21:
                l22.config(image=kili)
                count += 1
                guess5.append(kili)
                g5_b.append(kili_button)
                break
            elif count == 22:
                l23.config(image=kili)
                count += 1
                guess5.append(kili)
                g5_b.append(kili_button)
                break
            elif count == 23:
                l24.config(image=kili)
                count += 1
                guess5.append(kili)
                g5_b.append(kili_button)
                break
            elif count == 24:
                l25.config(image=kili)
                count += 1
                guess5.append(kili)
                g5_b.append(kili_button)
                break
            elif count == 25:
                l26.config(image=kili)
                count += 1
                guess6.append(kili)
                g6_b.append(kili_button)
                break
            elif count == 26:
                l27.config(image=kili)
                count += 1
                guess6.append(kili)
                g6_b.append(kili_button)
                break
            elif count == 27:
                l28.config(image=kili)
                count += 1
                guess6.append(kili)
                g6_b.append(kili_button)
                break
            elif count == 28:
                l29.config(image=kili)
                count += 1
                guess6.append(kili)
                g6_b.append(kili_button)
                break
            elif count == 29:
                l30.config(image=kili)
                count += 1
                guess6.append(kili)
                g6_b.append(kili_button)
                break

    def troll_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=troll)
                count += 1
                guess1.append(troll)
                g1_b.append(troll_button)
                break
            elif count == 1:
                l2.config(image=troll)
                count += 1
                guess1.append(troll)
                g1_b.append(troll_button)
                break
            elif count == 2:
                l3.config(image=troll)
                count += 1
                guess1.append(troll)
                g1_b.append(troll_button)
                break
            elif count == 3:
                l4.config(image=troll)
                count += 1
                guess1.append(troll)
                g1_b.append(troll_button)
                break
            elif count == 4:
                l5.config(image=troll)
                count += 1
                guess1.append(troll)
                g1_b.append(troll_button)
                break
            elif count == 5:
                l6.config(image=troll)
                count += 1
                guess2.append(troll)
                g2_b.append(troll_button)
                break
            elif count == 6:
                l7.config(image=troll)
                count += 1
                guess2.append(troll)
                g2_b.append(troll_button)
                break
            elif count == 7:
                l8.config(image=troll)
                count += 1
                guess2.append(troll)
                g2_b.append(troll_button)
                break
            elif count == 8:
                l9.config(image=troll)
                count += 1
                guess2.append(troll)
                g2_b.append(troll_button)
                break
            elif count == 9:
                l10.config(image=troll)
                count += 1
                guess2.append(troll)
                g2_b.append(troll_button)
                break
            elif count == 10:
                l11.config(image=troll)
                count += 1
                guess3.append(troll)
                g3_b.append(troll_button)
                break
            elif count == 11:
                l12.config(image=troll)
                count += 1
                guess3.append(troll)
                g3_b.append(troll_button)
                break
            elif count == 12:
                l13.config(image=troll)
                count += 1
                guess3.append(troll)
                g3_b.append(troll_button)
                break
            elif count == 13:
                l14.config(image=troll)
                count += 1
                guess3.append(troll)
                g3_b.append(troll_button)
                break
            elif count == 14:
                l15.config(image=troll)
                count += 1
                guess3.append(troll)
                g3_b.append(troll_button)
                break
            elif count == 15:
                l16.config(image=troll)
                count += 1
                guess4.append(troll)
                g4_b.append(troll_button)
                break
            elif count == 16:
                l17.config(image=troll)
                count += 1
                guess4.append(troll)
                g4_b.append(troll_button)
                break
            elif count == 17:
                l18.config(image=troll)
                count += 1
                guess4.append(troll)
                g4_b.append(troll_button)
                break
            elif count == 18:
                l19.config(image=troll)
                count += 1
                guess4.append(troll)
                g4_b.append(troll_button)
                break
            elif count == 19:
                l20.config(image=troll)
                count += 1
                guess4.append(troll)
                g4_b.append(troll_button)
                break
            elif count == 20:
                l21.config(image=troll)
                count += 1
                guess5.append(troll)
                g5_b.append(troll_button)
                break
            elif count == 21:
                l22.config(image=troll)
                count += 1
                guess5.append(troll)
                g5_b.append(troll_button)
                break
            elif count == 22:
                l23.config(image=troll)
                count += 1
                guess5.append(troll)
                g5_b.append(troll_button)
                break
            elif count == 23:
                l24.config(image=troll)
                count += 1
                guess5.append(troll)
                g5_b.append(troll_button)
                break
            elif count == 24:
                l25.config(image=troll)
                count += 1
                guess5.append(troll)
                g5_b.append(troll_button)
                break
            elif count == 25:
                l26.config(image=troll)
                count += 1
                guess6.append(troll)
                g6_b.append(troll_button)
                break
            elif count == 26:
                l27.config(image=troll)
                count += 1
                guess6.append(troll)
                g6_b.append(troll_button)
                break
            elif count == 27:
                l28.config(image=troll)
                count += 1
                guess6.append(troll)
                g6_b.append(troll_button)
                break
            elif count == 28:
                l29.config(image=troll)
                count += 1
                guess6.append(troll)
                g6_b.append(troll_button)
                break
            elif count == 29:
                l30.config(image=troll)
                count += 1
                guess6.append(troll)
                g6_b.append(troll_button)
                break

    def gollum_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=gollum)
                count += 1
                guess1.append(gollum)
                g1_b.append(gollum_button)
                break
            elif count == 1:
                l2.config(image=gollum)
                count += 1
                guess1.append(gollum)
                g1_b.append(gollum_button)
                break
            elif count == 2:
                l3.config(image=gollum)
                count += 1
                guess1.append(gollum)
                g1_b.append(gollum_button)
                break
            elif count == 3:
                l4.config(image=gollum)
                count += 1
                guess1.append(gollum)
                g1_b.append(gollum_button)
                break
            elif count == 4:
                l5.config(image=gollum)
                count += 1
                guess1.append(gollum)
                g1_b.append(gollum_button)
                break
            elif count == 5:
                l6.config(image=gollum)
                count += 1
                guess2.append(gollum)
                g2_b.append(gollum_button)
                break
            elif count == 6:
                l7.config(image=gollum)
                count += 1
                guess2.append(gollum)
                g2_b.append(gollum_button)
                break
            elif count == 7:
                l8.config(image=gollum)
                count += 1
                guess2.append(gollum)
                g2_b.append(gollum_button)
                break
            elif count == 8:
                l9.config(image=gollum)
                count += 1
                guess2.append(gollum)
                g2_b.append(gollum_button)
                break
            elif count == 9:
                l10.config(image=gollum)
                count += 1
                guess2.append(gollum)
                g2_b.append(gollum_button)
                break
            elif count == 10:
                l11.config(image=gollum)
                count += 1
                guess3.append(gollum)
                g3_b.append(gollum_button)
                break
            elif count == 11:
                l12.config(image=gollum)
                count += 1
                guess3.append(gollum)
                g3_b.append(gollum_button)
                break
            elif count == 12:
                l13.config(image=gollum)
                count += 1
                guess3.append(gollum)
                g3_b.append(gollum_button)
                break
            elif count == 13:
                l14.config(image=gollum)
                count += 1
                guess3.append(gollum)
                g3_b.append(gollum_button)
                break
            elif count == 14:
                l15.config(image=gollum)
                count += 1
                guess3.append(gollum)
                g3_b.append(gollum_button)
                break
            elif count == 15:
                l16.config(image=gollum)
                count += 1
                guess4.append(gollum)
                g4_b.append(gollum_button)
                break
            elif count == 16:
                l17.config(image=gollum)
                count += 1
                guess4.append(gollum)
                g4_b.append(gollum_button)
                break
            elif count == 17:
                l18.config(image=gollum)
                count += 1
                guess4.append(gollum)
                g4_b.append(gollum_button)
                break
            elif count == 18:
                l19.config(image=gollum)
                count += 1
                guess4.append(gollum)
                g4_b.append(gollum_button)
                break
            elif count == 19:
                l20.config(image=gollum)
                count += 1
                guess4.append(gollum)
                g4_b.append(gollum_button)
                break
            elif count == 20:
                l21.config(image=gollum)
                count += 1
                guess5.append(gollum)
                g5_b.append(gollum_button)
                break
            elif count == 21:
                l22.config(image=gollum)
                count += 1
                guess5.append(gollum)
                g5_b.append(gollum_button)
                break
            elif count == 22:
                l23.config(image=gollum)
                count += 1
                guess5.append(gollum)
                g5_b.append(gollum_button)
                break
            elif count == 23:
                l24.config(image=gollum)
                count += 1
                guess5.append(gollum)
                g5_b.append(gollum_button)
                break
            elif count == 24:
                l25.config(image=gollum)
                count += 1
                guess5.append(gollum)
                g5_b.append(gollum_button)
                break
            elif count == 25:
                l26.config(image=gollum)
                count += 1
                guess6.append(gollum)
                g6_b.append(gollum_button)
                break
            elif count == 26:
                l27.config(image=gollum)
                count += 1
                guess6.append(gollum)
                g6_b.append(gollum_button)
                break
            elif count == 27:
                l28.config(image=gollum)
                count += 1
                guess6.append(gollum)
                g6_b.append(gollum_button)
                break
            elif count == 28:
                l29.config(image=gollum)
                count += 1
                guess6.append(gollum)
                g6_b.append(gollum_button)
                break
            elif count == 29:
                l30.config(image=gollum)
                count += 1
                guess6.append(gollum)
                g6_b.append(gollum_button)
                break

    def great_goblin_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=great_goblin)
                count += 1
                guess1.append(great_goblin)
                g1_b.append(great_goblin_button)
                break
            elif count == 1:
                l2.config(image=great_goblin)
                count += 1
                guess1.append(great_goblin)
                g1_b.append(great_goblin_button)
                break
            elif count == 2:
                l3.config(image=great_goblin)
                count += 1
                guess1.append(great_goblin)
                g1_b.append(great_goblin_button)
                break
            elif count == 3:
                l4.config(image=great_goblin)
                count += 1
                guess1.append(great_goblin)
                g1_b.append(great_goblin_button)
                break
            elif count == 4:
                l5.config(image=great_goblin)
                count += 1
                guess1.append(great_goblin)
                g1_b.append(great_goblin_button)
                break
            elif count == 5:
                l6.config(image=great_goblin)
                count += 1
                guess2.append(great_goblin)
                g2_b.append(great_goblin_button)
                break
            elif count == 6:
                l7.config(image=great_goblin)
                count += 1
                guess2.append(great_goblin)
                g2_b.append(great_goblin_button)
                break
            elif count == 7:
                l8.config(image=great_goblin)
                count += 1
                guess2.append(great_goblin)
                g2_b.append(great_goblin_button)
                break
            elif count == 8:
                l9.config(image=great_goblin)
                count += 1
                guess2.append(great_goblin)
                g2_b.append(great_goblin_button)
                break
            elif count == 9:
                l10.config(image=great_goblin)
                count += 1
                guess2.append(great_goblin)
                g2_b.append(great_goblin_button)
                break
            elif count == 10:
                l11.config(image=great_goblin)
                count += 1
                guess3.append(great_goblin)
                g3_b.append(great_goblin_button)
                break
            elif count == 11:
                l12.config(image=great_goblin)
                count += 1
                guess3.append(great_goblin)
                g3_b.append(great_goblin_button)
                break
            elif count == 12:
                l13.config(image=great_goblin)
                count += 1
                guess3.append(great_goblin)
                g3_b.append(great_goblin_button)
                break
            elif count == 13:
                l14.config(image=great_goblin)
                count += 1
                guess3.append(great_goblin)
                g3_b.append(great_goblin_button)
                break
            elif count == 14:
                l15.config(image=great_goblin)
                count += 1
                guess3.append(great_goblin)
                g3_b.append(great_goblin_button)
                break
            elif count == 15:
                l16.config(image=great_goblin)
                count += 1
                guess4.append(great_goblin)
                g4_b.append(great_goblin_button)
                break
            elif count == 16:
                l17.config(image=great_goblin)
                count += 1
                guess4.append(great_goblin)
                g4_b.append(great_goblin_button)
                break
            elif count == 17:
                l18.config(image=great_goblin)
                count += 1
                guess4.append(great_goblin)
                g4_b.append(great_goblin_button)
                break
            elif count == 18:
                l19.config(image=great_goblin)
                count += 1
                guess4.append(great_goblin)
                g4_b.append(great_goblin_button)
                break
            elif count == 19:
                l20.config(image=great_goblin)
                count += 1
                guess5.append(great_goblin)
                g4_b.append(great_goblin_button)
                break
            elif count == 20:
                l21.config(image=great_goblin)
                count += 1
                guess5.append(great_goblin)
                g5_b.append(great_goblin_button)
                break
            elif count == 21:
                l22.config(image=great_goblin)
                count += 1
                guess5.append(great_goblin)
                g5_b.append(great_goblin_button)
                break
            elif count == 22:
                l23.config(image=great_goblin)
                count += 1
                guess5.append(great_goblin)
                g5_b.append(great_goblin_button)
                break
            elif count == 23:
                l24.config(image=great_goblin)
                count += 1
                guess5.append(great_goblin)
                g5_b.append(great_goblin_button)
                break
            elif count == 24:
                l25.config(image=great_goblin)
                count += 1
                guess1.append(great_goblin)
                g5_b.append(great_goblin_button)
                break
            elif count == 25:
                l26.config(image=great_goblin)
                count += 1
                guess6.append(great_goblin)
                g6_b.append(great_goblin_button)
                break
            elif count == 26:
                l27.config(image=great_goblin)
                count += 1
                guess6.append(great_goblin)
                g6_b.append(great_goblin_button)
                break
            elif count == 27:
                l28.config(image=great_goblin)
                count += 1
                guess6.append(great_goblin)
                g6_b.append(great_goblin_button)
                break
            elif count == 28:
                l29.config(image=great_goblin)
                count += 1
                guess6.append(great_goblin)
                g6_b.append(great_goblin_button)
                break
            elif count == 29:
                l30.config(image=great_goblin)
                count += 1
                guess6.append(great_goblin)
                g6_b.append(great_goblin_button)
                break

    def smaug_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count < 30:
            if count == 0:
                l1.config(image=smaug)
                count += 1
                guess1.append(smaug)
                g1_b.append(smaug_button)
                break
            elif count == 1:
                l2.config(image=smaug)
                count += 1
                guess1.append(smaug)
                g1_b.append(smaug_button)
                break
            elif count == 2:
                l3.config(image=smaug)
                count += 1
                guess1.append(smaug)
                g1_b.append(smaug_button)
                break
            elif count == 3:
                l4.config(image=smaug)
                count += 1
                guess1.append(smaug)
                g1_b.append(smaug_button)
                break
            elif count == 4:
                l5.config(image=smaug)
                count += 1
                guess1.append(smaug)
                g1_b.append(smaug_button)
                break
            elif count == 5:
                l6.config(image=smaug)
                count += 1
                guess2.append(smaug)
                g2_b.append(smaug_button)
                break
            elif count == 6:
                l7.config(image=smaug)
                count += 1
                guess2.append(smaug)
                g2_b.append(smaug_button)
                break
            elif count == 7:
                l8.config(image=smaug)
                count += 1
                guess2.append(smaug)
                g2_b.append(smaug_button)
                break
            elif count == 8:
                l9.config(image=smaug)
                count += 1
                guess2.append(smaug)
                g2_b.append(smaug_button)
                break
            elif count == 9:
                l10.config(image=smaug)
                count += 1
                guess2.append(smaug)
                g2_b.append(smaug_button)
                break
            elif count == 10:
                l11.config(image=smaug)
                count += 1
                guess3.append(smaug)
                g3_b.append(smaug_button)
                break
            elif count == 11:
                l12.config(image=smaug)
                count += 1
                guess3.append(smaug)
                g3_b.append(smaug_button)
                break
            elif count == 12:
                l13.config(image=smaug)
                count += 1
                guess3.append(smaug)
                g3_b.append(smaug_button)
                break
            elif count == 13:
                l14.config(image=smaug)
                count += 1
                guess3.append(smaug)
                g3_b.append(smaug_button)
                break
            elif count == 14:
                l15.config(image=smaug)
                count += 1
                guess3.append(smaug)
                g3_b.append(smaug_button)
                break
            elif count == 15:
                l16.config(image=smaug)
                count += 1
                guess4.append(smaug)
                g4_b.append(smaug_button)
                break
            elif count == 16:
                l17.config(image=smaug)
                count += 1
                guess4.append(smaug)
                g4_b.append(smaug_button)
                break
            elif count == 17:
                l18.config(image=smaug)
                count += 1
                guess4.append(smaug)
                g4_b.append(smaug_button)
                break
            elif count == 18:
                l19.config(image=smaug)
                count += 1
                guess4.append(smaug)
                g4_b.append(smaug_button)
                break
            elif count == 19:
                l20.config(image=smaug)
                count += 1
                guess4.append(smaug)
                g4_b.append(smaug_button)
                break
            elif count == 20:
                l21.config(image=smaug)
                count += 1
                guess5.append(smaug)
                g5_b.append(smaug_button)
                break
            elif count == 21:
                l22.config(image=smaug)
                count += 1
                guess5.append(smaug)
                g5_b.append(smaug_button)
                break
            elif count == 22:
                l23.config(image=smaug)
                count += 1
                guess5.append(smaug)
                g5_b.append(smaug_button)
                break
            elif count == 23:
                l24.config(image=smaug)
                count += 1
                guess5.append(smaug)
                g5_b.append(smaug_button)
                break
            elif count == 24:
                l25.config(image=smaug)
                count += 1
                guess5.append(smaug)
                g5_b.append(smaug_button)
                break
            elif count == 25:
                l26.config(image=smaug)
                count += 1
                guess6.append(smaug)
                g6_b.append(smaug_button)
                break
            elif count == 26:
                l27.config(image=smaug)
                count += 1
                guess6.append(smaug)
                g6_b.append(smaug_button)
                break
            elif count == 27:
                l28.config(image=smaug)
                count += 1
                guess6.append(smaug)
                g6_b.append(smaug_button)
                break
            elif count == 28:
                l29.config(image=smaug)
                count += 1
                guess6.append(smaug)
                g6_b.append(smaug_button)
                break
            elif count == 29:
                l30.config(image=smaug)
                count += 1
                guess6.append(smaug)
                g6_b.append(smaug_button)
                break

    def enter_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6, congrats_label, the_sol_was_label
        global new_game_button, exit_button, ALL_TRIES, ALL_WINS, STREAKS, CURRENT_STREAK, BEST_STREAK
        if LANG == "ENG":
            congrats_label = Label(window, image=congrats, width=554, height=215, bg="#179923")
            the_sol_was_label = Label(window, image=the_sol_was, width=554, height=215, bg="#9a0000")
            new_game_button = Button(window, image=play_again, bg="#002b82", command=new_game)
            exit_button = Button(window, image=img_exit, bg="#f0a510", command=quit)
        elif LANG == "RU":
            congrats_label = Label(window, image=congrats_ru, width=554, height=215, bg="#179923")
            the_sol_was_label = Label(window, image=the_sol_was_ru, width=554, height=215, bg="#9a0000")
            new_game_button = Button(window, image=play_again_ru, bg="#002b82", command=new_game)
            exit_button = Button(window, image=img_exit_ru, bg="#f0a510", command=quit)
        if count == 5:
            if guess1 == solution:
                for x in line1:
                    x.config(bg="#08c700")
                for y in g1_b:
                    y.config(bg="#08c700", activebackground="#08c700")
                congrats_label.place(x=10, y=500)
                new_game_button.place(x=62, y=610)
                exit_button.place(x=312, y=610)
                ALL_TRIES += 1
                ALL_WINS += 1
                CURRENT_STREAK += 1
                STREAKS.append(CURRENT_STREAK)
                BEST_STREAK = max(STREAKS)
            else:
                for i in guess1:
                    if i in solution:
                        if guess1.index(i) == solution.index(i):
                            line1[guess1.index(i)].config(bg="#08c700")
                            g1_b[guess1.index(i)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            line1[guess1.index(i)].config(bg="#ffcd00")
                            g1_b[guess1.index(i)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        line1[guess1.index(i)].config(bg="#9e9e9e")
                        g1_b[guess1.index(i)].config(bg="#9e9e9e", activebackground="#9e9e9e")
        elif count == 10:
            if guess2 == solution:
                for x in line2:
                    x.config(bg="#08c700")
                for y in g2_b:
                    y.config(bg="#08c700", activebackground="#08c700")
                congrats_label.place(x=10, y=500)
                new_game_button.place(x=62, y=610)
                exit_button.place(x=312, y=610)
                ALL_TRIES += 1
                ALL_WINS += 1
                CURRENT_STREAK += 1
                STREAKS.append(CURRENT_STREAK)
                BEST_STREAK = max(STREAKS)
            else:
                for i in guess2:
                    if i in solution:
                        if guess2.index(i) == solution.index(i):
                            line2[guess2.index(i)].config(bg="#08c700")
                            g2_b[guess2.index(i)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            line2[guess2.index(i)].config(bg="#ffcd00")
                            g2_b[guess2.index(i)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        line2[guess2.index(i)].config(bg="#9e9e9e")
                        g2_b[guess2.index(i)].config(bg="#9e9e9e", activebackground="#9e9e9e")
        elif count == 15:
            if guess3 == solution:
                for x in line3:
                    x.config(bg="#08c700")
                for y in g3_b:
                    y.config(bg="#08c700", activebackground="#08c700")
                congrats_label.place(x=10, y=500)
                new_game_button.place(x=62, y=610)
                exit_button.place(x=312, y=610)
                ALL_TRIES += 1
                ALL_WINS += 1
                CURRENT_STREAK += 1
                STREAKS.append(CURRENT_STREAK)
                BEST_STREAK = max(STREAKS)
            else:
                for i in guess3:
                    if i in solution:
                        if guess3.index(i) == solution.index(i):
                            line3[guess3.index(i)].config(bg="#08c700")
                            g3_b[guess3.index(i)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            line3[guess3.index(i)].config(bg="#ffcd00")
                            g3_b[guess3.index(i)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        line3[guess3.index(i)].config(bg="#9e9e9e")
                        g3_b[guess3.index(i)].config(bg="#9e9e9e", activebackground="#9e9e9e")
        elif count == 20:
            if guess4 == solution:
                for x in line4:
                    x.config(bg="#08c700")
                for y in g4_b:
                    y.config(bg="#08c700", activebackground="#08c700")
                congrats_label.place(x=10, y=500)
                new_game_button.place(x=62, y=610)
                exit_button.place(x=312, y=610)
                ALL_TRIES += 1
                ALL_WINS += 1
                CURRENT_STREAK += 1
                STREAKS.append(CURRENT_STREAK)
                BEST_STREAK = max(STREAKS)
            else:
                for i in guess4:
                    if i in solution:
                        if guess4.index(i) == solution.index(i):
                            line4[guess4.index(i)].config(bg="#08c700")
                            g4_b[guess4.index(i)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            line4[guess4.index(i)].config(bg="#ffcd00")
                            g4_b[guess4.index(i)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        line4[guess4.index(i)].config(bg="#9e9e9e")
                        g4_b[guess4.index(i)].config(bg="#9e9e9e", activebackground="#9e9e9e")
        elif count == 25:
            if guess5 == solution:
                for x in line5:
                    x.config(bg="#08c700")
                for y in g5_b:
                    y.config(bg="#08c700", activebackground="#08c700")
                congrats_label.place(x=10, y=500)
                new_game_button.place(x=62, y=610)
                exit_button.place(x=312, y=610)
                ALL_TRIES += 1
                ALL_WINS += 1
                CURRENT_STREAK += 1
                STREAKS.append(CURRENT_STREAK)
                BEST_STREAK = max(STREAKS)
            else:
                for i in guess5:
                    if i in solution:
                        if guess5.index(i) == solution.index(i):
                            line5[guess5.index(i)].config(bg="#08c700")
                            g5_b[guess5.index(i)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            line5[guess5.index(i)].config(bg="#ffcd00")
                            g5_b[guess5.index(i)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        line5[guess5.index(i)].config(bg="#9e9e9e")
                        g5_b[guess5.index(i)].config(bg="#9e9e9e", activebackground="#9e9e9e")
        elif count == 30:
            if guess6 == solution:
                for x in line6:
                    x.config(bg="#08c700")
                for y in g6_b:
                        y.config(bg="#08c700", activebackground="#08c700")
                congrats_label.place(x=10, y=500)
                new_game_button.place(x=62, y=610)
                exit_button.place(x=312, y=610)
                ALL_TRIES += 1
                ALL_WINS += 1
                CURRENT_STREAK += 1
                STREAKS.append(CURRENT_STREAK)
                BEST_STREAK = max(STREAKS)
            else:
                for i in guess6:
                    if i in solution:
                        if guess6.index(i) == solution.index(i):
                            line6[guess6.index(i)].config(bg="#08c700")
                            g6_b[guess6.index(i)].config(bg="#08c700", activebackground="#08c700")
                        else:
                            line6[guess6.index(i)].config(bg="#ffcd00")
                            g6_b[guess6.index(i)].config(bg="#ffcd00", activebackground="#ffcd00")
                    else:
                        line6[guess6.index(i)].config(bg="#9e9e9e")
                        g6_b[guess6.index(i)].config(bg="#9e9e9e", activebackground="#9e9e9e")
                the_sol_was_label.place(x=10, y=500)
                Label(window, image=solution[0], width=104, height=68, bg="#ff9165").place(x=28, y=550)
                Label(window, image=solution[1], width=104, height=68, bg="#ff9165").place(x=130, y=550)
                Label(window, image=solution[2], width=104, height=68, bg="#ff9165").place(x=233, y=550)
                Label(window, image=solution[3], width=104, height=68, bg="#ff9165").place(x=336, y=550)
                Label(window, image=solution[4], width=104, height=68, bg="#ff9165").place(x=439, y=550)
                new_game_button.place(x=62, y=625)
                exit_button.place(x=312, y=625)
                ALL_TRIES += 1
                CURRENT_STREAK = 0

    def backspace_call():
        global count, guess1, guess2, guess3, guess4, guess5, guess6
        while count > 0:
            if count == 30:
                l30.config(image=label)
                count -= 1
                guess6.remove(guess6[-1])
                g6_b.remove(g6_b[-1])
                break
            elif count == 29:
                l29.config(image=label)
                count -= 1
                guess6.remove(guess6[-1])
                g6_b.remove(g6_b[-1])
                break
            elif count == 28:
                l28.config(image=label)
                count -= 1
                guess6.remove(guess6[-1])
                g6_b.remove(g6_b[-1])
                break
            elif count == 27:
                l27.config(image=label)
                count -= 1
                guess6.remove(guess6[-1])
                g6_b.remove(g6_b[-1])
                break
            elif count == 26:
                l26.config(image=label)
                count -= 1
                guess6.remove(guess6[-1])
                g6_b.remove(g6_b[-1])
                break
            elif count == 25:
                l25.config(image=label)
                count -= 1
                guess5.remove(guess5[-1])
                g5_b.remove(g5_b[-1])
                break
            elif count == 24:
                l24.config(image=label)
                count -= 1
                guess5.remove(guess5[-1])
                g5_b.remove(g5_b[-1])
                break
            elif count == 23:
                l23.config(image=label)
                count -= 1
                guess5.remove(guess5[-1])
                g5_b.remove(g5_b[-1])
                break
            elif count == 22:
                l22.config(image=label)
                count -= 1
                guess5.remove(guess5[-1])
                g5_b.remove(g5_b[-1])
                break
            elif count == 21:
                l21.config(image=label)
                count -= 1
                guess5.remove(guess5[-1])
                g5_b.remove(g5_b[-1])
                break
            elif count == 20:
                l20.config(image=label)
                count -= 1
                guess4.remove(guess4[-1])
                g4_b.remove(g4_b[-1])
                break
            elif count == 19:
                l19.config(image=label)
                count -= 1
                guess4.remove(guess4[-1])
                g4_b.remove(g4_b[-1])
                break
            elif count == 18:
                l18.config(image=label)
                count -= 1
                guess4.remove(guess4[-1])
                g4_b.remove(g4_b[-1])
                break
            elif count == 17:
                l17.config(image=label)
                count -= 1
                guess4.remove(guess4[-1])
                g4_b.remove(g4_b[-1])
                break
            elif count == 16:
                l16.config(image=label)
                count -= 1
                guess4.remove(guess4[-1])
                g4_b.remove(g4_b[-1])
                break
            elif count == 15:
                l15.config(image=label)
                count -= 1
                guess3.remove(guess3[-1])
                g3_b.remove(g3_b[-1])
                break
            elif count == 14:
                l14.config(image=label)
                count -= 1
                guess3.remove(guess3[-1])
                g3_b.remove(g3_b[-1])
                break
            elif count == 13:
                l13.config(image=label)
                count -= 1
                guess3.remove(guess3[-1])
                g3_b.remove(g3_b[-1])
                break
            elif count == 12:
                l12.config(image=label)
                count -= 1
                guess3.remove(guess3[-1])
                g3_b.remove(g3_b[-1])
                break
            elif count == 11:
                l11.config(image=label)
                count -= 1
                guess3.remove(guess3[-1])
                g3_b.remove(g3_b[-1])
                break
            elif count == 10:
                l10.config(image=label)
                count -= 1
                guess2.remove(guess2[-1])
                g2_b.remove(g2_b[-1])
                break
            elif count == 9:
                l9.config(image=label)
                count -= 1
                guess2.remove(guess2[-1])
                g2_b.remove(g2_b[-1])
                break
            elif count == 8:
                l8.config(image=label)
                count -= 1
                guess2.remove(guess2[-1])
                g2_b.remove(g2_b[-1])
                break
            elif count == 7:
                l7.config(image=label)
                count -= 1
                guess2.remove(guess2[-1])
                g2_b.remove(g2_b[-1])
                break
            elif count == 6:
                l6.config(image=label)
                count -= 1
                guess2.remove(guess2[-1])
                g2_b.remove(g2_b[-1])
                break
            elif count == 5:
                l5.config(image=label)
                count -= 1
                guess1.remove(guess1[-1])
                g1_b.remove(g1_b[-1])
                break
            elif count == 4:
                l4.config(image=label)
                count -= 1
                guess1.remove(guess1[-1])
                g1_b.remove(g1_b[-1])
                break
            elif count == 3:
                l3.config(image=label)
                count -= 1
                guess1.remove(guess1[-1])
                g1_b.remove(g1_b[-1])
                break
            elif count == 2:
                l2.config(image=label)
                count -= 1
                guess1.remove(guess1[-1])
                g1_b.remove(g1_b[-1])
                break
            elif count == 1:
                l1.config(image=label)
                count -= 1
                guess1.remove(guess1[-1])
                g1_b.remove(g1_b[-1])
                break

    if THEME == "LIGHT":
        gandalf_button = Button(window, width=110, height=70, image=gandalf, command=gandalf_call, bg="#f0f0f0", activebackground="#f0f0f0")
        bilbo_button = Button(window, width=110, height=70, image=bilbo, command=bilbo_call, bg="#f0f0f0", activebackground="#f0f0f0")
        thorin_button = Button(window, width=110, height=70, image=thorin, command=thorin_call, bg="#f0f0f0", activebackground="#f0f0f0")
        elrond_button = Button(window, width=110, height=70, image=elrond, command=elrond_call, bg="#f0f0f0", activebackground="#f0f0f0")
        beorn_button = Button(window, width=110, height=70, image=beorn, command=beorn_call, bg="#f0f0f0", activebackground="#f0f0f0")
        balin_button = Button(window, width=110, height=70, image=balin, command=balin_call, bg="#f0f0f0", activebackground="#f0f0f0")
        dwalin_button = Button(window, width=110, height=70, image=dwalin, command=dwalin_call, bg="#f0f0f0", activebackground="#f0f0f0")
        gloin_button = Button(window, width=110, height=70, image=gloin, command=gloin_call, bg="#f0f0f0", activebackground="#f0f0f0")
        fili_button = Button(window, width=110, height=70, image=fili, command=fili_call, bg="#f0f0f0", activebackground="#f0f0f0")
        kili_button = Button(window, width=110, height=70, image=kili, command=kili_call, bg="#f0f0f0", activebackground="#f0f0f0")
        enter_button = Button(window, width=55, height=70, image=enter, command=enter_call, bg="#f0f0f0", activebackground="#f0f0f0")
        troll_button = Button(window, width=110, height=70, image=troll, command=troll_call, bg="#f0f0f0", activebackground="#f0f0f0")
        gollum_button = Button(window, width=110, height=70, image=gollum, command=gollum_call, bg="#f0f0f0", activebackground="#f0f0f0")
        great_goblin_button = Button(window, width=110, height=70, image=great_goblin, command=great_goblin_call, bg="#f0f0f0", activebackground="#f0f0f0")
        smaug_button = Button(window, width=110, height=70, image=smaug, command=smaug_call, bg="#f0f0f0", activebackground="#f0f0f0")
        backspace_button = Button(window, width=55, height=70, image=backspace, command=backspace_call, bg="#f0f0f0", activebackground="#f0f0f0")
    
    elif THEME == "DARK":
        gandalf_button = Button(window, width=110, height=70, image=gandalf, command=gandalf_call, bg="#222222", activebackground="#222222")        
        bilbo_button = Button(window, width=110, height=70, image=bilbo, command=bilbo_call, bg="#222222", activebackground="#222222")        
        thorin_button = Button(window, width=110, height=70, image=thorin, command=thorin_call, bg="#222222", activebackground="#222222")        
        elrond_button = Button(window, width=110, height=70, image=elrond, command=elrond_call, bg="#222222", activebackground="#222222")        
        beorn_button = Button(window, width=110, height=70, image=beorn, command=beorn_call, bg="#222222", activebackground="#222222")        
        balin_button = Button(window, width=110, height=70, image=balin, command=balin_call, bg="#222222", activebackground="#222222")        
        dwalin_button = Button(window, width=110, height=70, image=dwalin, command=dwalin_call, bg="#222222", activebackground="#222222")        
        gloin_button = Button(window, width=110, height=70, image=gloin, command=gloin_call, bg="#222222", activebackground="#222222")        
        fili_button = Button(window, width=110, height=70, image=fili, command=fili_call, bg="#222222", activebackground="#222222")        
        kili_button = Button(window, width=110, height=70, image=kili, command=kili_call, bg="#222222", activebackground="#222222")        
        enter_button = Button(window, width=55, height=70, image=enter_light, command=enter_call, bg="#222222", activebackground="#222222")        
        troll_button = Button(window, width=110, height=70, image=troll, command=troll_call, bg="#222222", activebackground="#222222")        
        gollum_button = Button(window, width=110, height=70, image=gollum, command=gollum_call, bg="#222222", activebackground="#222222")        
        great_goblin_button = Button(window, width=110, height=70, image=great_goblin, command=great_goblin_call, bg="#222222", activebackground="#222222")        
        smaug_button = Button(window, width=110, height=70, image=smaug, command=smaug_call, bg="#222222", activebackground="#222222")        
        backspace_button = Button(window, width=55, height=70, image=backspace_light, command=backspace_call, bg="#222222", activebackground="#222222")        
    
    gandalf_button.place(x=10, y=500), bilbo_button.place(x=120, y=500), thorin_button.place(x=230, y=500)
    elrond_button.place(x=340, y=500), beorn_button.place(x=450, y=500), balin_button.place(x=10, y=570)
    dwalin_button.place(x=120, y=570), gloin_button.place(x=230, y=570), fili_button.place(x=340, y=570)
    kili_button.place(x=450, y=570), enter_button.place(x=10, y=640), troll_button.place(x=65, y=640)
    gollum_button.place(x=175, y=640), great_goblin_button.place(x=285, y=640), smaug_button.place(x=395, y=640)
    backspace_button.place(x=505, y=640)

    key_buttons = [gandalf_button, bilbo_button, thorin_button, elrond_button, beorn_button, balin_button, dwalin_button,
                   gloin_button, fili_button, kili_button, troll_button, gollum_button, great_goblin_button, smaug_button]

    def close_settings():
        global settings_list_label, close_button, light_button_b, dark_button_b, english_button_b, russian_button_b
        settings_list_label.destroy()
        close_button.destroy()
        light_button_b.destroy()
        dark_button_b.destroy()
        russian_button_b.destroy()
        english_button_b.destroy()
    
    def russian():
        global LANG
        LANG = "RU"
        title_label.config(text="ХОББИТЛИ"), window.title("Хоббитли")

    def english():
        global LANG
        LANG = "ENG"
        title_label.config(text="HOBBITLE"), window.title("Hobbitle")

    def light_theme():
        global THEME
        THEME = "LIGHT"
        for i in line1_6:
            i.config(bg="#f0f0f0")
        for j in key_buttons:
            j.config(bg="#f0f0f0", activebackground="#f0f0f0")
        window.config(background="#f0f0f0"), title_label.config(bg="#f0f0f0")
        about_button.config(bg="#f0f0f0", activebackground="#f0f0f0")
        stats_button.config(bg="#f0f0f0", activebackground="#f0f0f0", image=stats)
        settings_button.config(bg="#f0f0f0", activebackground="#f0f0f0", image=settings)
        enter_button.config(bg="#f0f0f0", activebackground="#f0f0f0", image=enter)
        backspace_button.config(bg="#f0f0f0", activebackground="#f0f0f0", image=backspace)

    def dark_theme():
        global THEME
        THEME = "DARK"
        for i in line1_6:
            i.config(bg="#222222")
        for j in key_buttons:
            j.config(bg="#222222", activebackground="#222222")
        window.config(background="#111111"), title_label.config(bg="#111111")
        about_button.config(bg="#222222", activebackground="#222222")
        stats_button.config(bg="#222222", activebackground="#222222", image=stats_light)
        settings_button.config(bg="#222222", activebackground="#222222", image=settings_light)
        enter_button.config(bg="#222222", activebackground="#222222", image=enter_light)
        backspace_button.config(bg="#222222", activebackground="#222222", image=backspace_light)

    def settings_call():
        global settings_list_label, close_button, light_button_b, dark_button_b, english_button_b, russian_button_b
        if LANG == "ENG":
            settings_list_label = Label(window, image=settings_list, width=574, height=725, bg="#002b82")
            close_button = Button(window, image=close_r, bg="#002b82", activebackground="#002b82", command=close_settings)
            light_button_b = Button(window, image=light_button, bg="#002b82", activebackground="#002b82", command=light_theme)
            dark_button_b = Button(window, image=dark_button, bg="#002b82", activebackground="#002b82", command=dark_theme)
            russian_button_b = Button(window, image=russian_button, bg="#002b82", activebackground="#002b82", command=russian)
            english_button_b = Button(window, image=english_button, bg="#002b82", activebackground="#002b82", command=english)
        elif LANG == "RU":
            settings_list_label = Label(window, image=settings_list_ru, width=574, height=725, bg="#002b82")
            close_button = Button(window, image=close_r, bg="#002b82", activebackground="#002b82", command=close_settings)
            light_button_b = Button(window, image=light_button_ru, bg="#002b82", activebackground="#002b82", command=light_theme)
            dark_button_b = Button(window, image=dark_button_ru, bg="#002b82", activebackground="#002b82", command=dark_theme)
            russian_button_b = Button(window, image=russian_button_ru, bg="#002b82", activebackground="#002b82", command=russian) 
            english_button_b = Button(window, image=english_button_ru, bg="#002b82", activebackground="#002b82", command=english)
        settings_list_label.place(x=0, y=0), close_button.place(x=494, y=18), light_button_b.place(x=300, y=220),
        dark_button_b.place(x=300, y=300), russian_button_b.place(x=300, y=410), english_button_b.place(x=300, y=490)

    def close_stats():
        global stats_w_label, close_button1, all_tries_label, percentage_label, current_streak_label, best_streak_label
        stats_w_label.destroy()
        close_button1.destroy()
        all_tries_label.destroy()
        percentage_label.destroy()
        current_streak_label.destroy()
        best_streak_label.destroy()

    def stats_call():
        global LANG, stats_w_label, close_button1, all_tries_label, percentage_label, current_streak_label, best_streak_label
        if LANG == "ENG":
            stats_w_label = Label(window, image=stats_w, width=560, height=248, bg="#002b82")
        elif LANG == "RU":
            stats_w_label = Label(window, image=stats_w_ru, width=560, height=248, bg="#002b82")
        stats_w_label.place(x=5, y=242)
        close_button1 = Button(window, image=close_st, bg="#002b82", activebackground="#002b82", command=close_stats)
        close_button1.place(x=498, y=262)
        all_tries_label = Label(window, bg="#bdd7ee", fg="#002b82", width=3, text=ALL_TRIES, font=("Bandshift", 38))
        all_tries_label.place(x=44, y=348)
        try:
            percentage_label = Label(window, bg="#bdd7ee", fg="#002b82", width=4,
                                     text=f"{round((ALL_WINS / ALL_TRIES) * 100)}%", font=("Bandshift", 38))
        except ZeroDivisionError:
            percentage_label = Label(window, bg="#bdd7ee", fg="#002b82", width=4,
                                     text="0%", font=("Bandshift", 38))
        percentage_label.place(x=142, y=348)
        current_streak_label = Label(window, bg="#bdd7ee", fg="#002b82", width=3, text=CURRENT_STREAK, font=("Bandshift", 38))
        current_streak_label.place(x=280, y=348)
        best_streak_label = Label(window, bg="#bdd7ee", fg="#002b82", width=3, text=BEST_STREAK, font=("Bandshift", 38))
        best_streak_label.place(x=420, y=348)

    if THEME == "LIGHT":
        settings_button = Button(window, width=50, height=50, image=settings, command=settings_call, bg="#f0f0f0", activebackground="#f0f0f0")
        stats_button = Button(window, width=50, height=50, image=stats, bg="#f0f0f0", activebackground="#f0f0f0", command=stats_call)
    elif THEME == "DARK":
        settings_button = Button(window, width=50, height=50, image=settings_light, command=settings_call, bg="#222222", activebackground="#222222")
        stats_button = Button(window, width=50, height=50, image=stats_light, bg="#222222", activebackground="#222222", command=stats_call)
    settings_button.place(x=510, y=10)
    stats_button.place(x=450, y=10)
    
    window.mainloop()