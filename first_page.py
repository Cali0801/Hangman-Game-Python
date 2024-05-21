import tkinter
from time import sleep
from tkinter import *
from tkinter import messagebox
from playsound import playsound
from threading import Thread
from pydub import AudioSegment
from PIL import ImageTk,Image
import os
import random
from logging import root
from tkinter import *
from tkinter import messagebox
import PIL
from PIL import ImageTk, Image
import os
import playsound
import random
from logging import root
from tkinter import *
from tkinter import messagebox
from pydub.playback import play
import PIL

from PIL import ImageTk, Image

class home:
    # def thread_function(self):
    #     playsound('a.wav')
    #
    # def __init__(self):
    #     thread = Thread(target=self.thread_function, args=())
    #     thread.start()
    #     thread.join()



    letter_into_word = [0]
    ar_letter_into_word = [0]
    ar_selcted_word = ""
    button_pres = 0
    variable = [0]
    chance = 1
    total_score = 0
    wrong_click_count = 1
    total_click_count = 0
    hint_chance = 2
    chance = 1
    previous_word='no'


    def main(self):



        def call_play():


            if(home.previous_word=='no'):
                answers = ['Ant', 'BABOON', 'BAT', 'CAMEL', 'DONKEY', 'EAGLE', 'GOOSE', 'HAWK', 'MONKEY', 'MOUSE', 'FISH', 'PYTHON',
                       'PIGEON', 'RHINOCEROS', 'HIPPOPOTAMUS', 'ZEBRA', 'PANDA', 'RAVEN', 'HUMAN', 'OWL', 'SHARK', 'PIZZA',
                       'BURGER', 'SAMOSA', 'BUTTER', 'CHUTNEY', 'NOODLES', 'DOSA', 'MANGO', 'BANANA', 'POMEGRANATE', 'PAPAYA',
                       'WATERMELON', 'MUSKMELON', 'DATES', 'MAGNETISM', 'ELECTRICITY']
            else:
                answers=[home.previous_word,]
            home.wrong_click_count=1

            # answers = ['ANT', 'BABOON', 'ELECTRICITY']
            button_variable_list = []
            def remove_nth(text, separator, position):
                parts = text.split(separator)
                return separator.join(parts[:position]) + separator.join(parts[position:])
            def check(press_button, numberic_val=None, score=None, exitbutton=None, hangman_image_label=None,
                      frame1=None,
                      frame2=None, frame3=None):
                global chance, total_score, wrong_click_count, total_click_count, ar_selcted_word,previous_word




                if home.chance <= home.chance:
                    home.no_of_times = home.letter_into_word.count(press_button)
                    home.total_click_count = home.total_click_count + 1
                    if (home.no_of_times == 0):

                        home.wrong_click_count = home.wrong_click_count + 1
                        hangman_imagelocation = os.path.abspath("images\\" + str(home.wrong_click_count) + ".png")

                        hangman_image_open = Image.open(hangman_imagelocation)
                        hangman_image_resize = hangman_image_open.resize((300, 300))
                        hangman_image = ImageTk.PhotoImage(hangman_image_resize)
                        frame2=(root)


                        hangman_image_label = Label(frame2, image=hangman_image)
                        hangman_image_label.configure(image=hangman_image)
                        hangman_image_label.image = hangman_image
                        hangman_image_label.place(x=364, y=134)


                        if home.wrong_click_count >= 7:
                            # def del_sc1():
                            #     sc1.destroy()
                            #
                            # def err_screen():
                            #     global sc1
                            #     sc1 = Tk()
                            #     sc1.geometry('200x80')
                            #     sc1.title('End')
                            #     sc1.configure(background='snow')
                            #     Label(sc1, text='Game Over', fg='#f5427e', bg='white',
                            #           font=('times', 16, ' bold ')).pack()
                            #     Button(sc1, text='OK', command=del_sc1, fg="black", bg="#42bcf5", width=9, height=1,
                            #            activebackground="Red", font=('times', 15, ' bold ')).place(x=90, y=50)

                            # root.attributes('-topmost', True)
                            #messagebox.showwarning("Warning!", "You already entered this room#.", parent=root)
                            messagebox.showerror("End", "Game Over", parent=root)
                            #root.withdraw()
                            #messagebox.showwarning('File exists', 'The database file already exists!')
                            # root.destroy()




                            home.previous_word=words
                            root.destroy()
                            call_play()
                            #root.attributes('-topmost', True)
                            ############################################

                            ############################################
                    else:
                        dd = ("leave")
                        c = remove_nth(home.ar_selcted_word, press_button.lower(), 1)
                        home.ar_selcted_word = str(c)
                        tmp = 0
                        for repeat in range(home.no_of_times):
                            if tmp == 0:
                                pos = home.letter_into_word.index(press_button)
                                home.variable[pos].config(text=press_button)
                                home.letter_into_word.pop(pos)
                                home.variable.pop(pos)
                                tmp = tmp + 1
                        win_count = (len(home.letter_into_word))
                        if (win_count == 0):

                            messagebox.showinfo("WIN!!", "You Win!! :-)", parent=root)
                            home.total_score += 5
                            print(home.total_score)
                            ###################################
                            frame2 = (root)
                            hangman_imagelocation = os.path.abspath("images\\1.png")
                            hangman_image_open = Image.open(hangman_imagelocation)
                            hangman_image_resize = hangman_image_open.resize((300, 300))
                            hangman_image = ImageTk.PhotoImage(hangman_image_resize)
                            hangman_image_label = Label(frame2, image=hangman_image)
                            hangman_image_label.place(x=364, y=134)
                            root.destroy()
                            call_play()




            def a_btn(event=""):
                letter = "A"
                check(letter)

            def b_btn(event=""):
                letter = "B"
                check(letter)

            def c_btn(event=""):
                letter = "C"
                check(letter)

            def d_btn(event=""):
                letter = "D"
                check(letter)

            def e_btn(event=""):
                letter = "E"
                check(letter)

            def f_btn(event=""):
                letter = "F"
                check(letter)

            def g_btn(event=""):
                letter = "G"
                check(letter)

            def h_btn(event=""):
                letter = "H"
                check(letter)

            def i_btn(event=""):
                letter = "I"
                check(letter)

            def j_btn(event=""):
                letter = "J"
                check(letter)

            def k_btn(event=""):
                letter = "K"
                check(letter)

            def l_btn(event=""):
                letter = "L"
                check(letter)

            def m_btn(event=""):
                letter = "M"
                check(letter)

            def n_btn(event=""):
                letter = "N"
                check(letter)

            def o_btn(event=""):
                letter = "O"
                check(letter)

            def p_btn(event=""):
                letter = "P"
                check(letter)

            def q_btn(event=""):
                letter = "Q"
                check(letter)

            def r_btn(event=""):
                letter = "R"
                check(letter)

            def s_btn(event=""):
                letter = "S"
                check(letter)

            def t_btn(event=""):
                letter = "T"
                check(letter)

            def u_btn(event=""):
                letter = "U"
                check(letter)

            def v_btn(event=""):
                letter = "V"
                check(letter)

            def w_btn(event=""):
                letter = "W"
                check(letter)

            def x_btn(event=""):
                letter = "X"
                check(letter)

            def y_btn(event=""):
                letter = "Y"
                check(letter)

            def z_btn(event=""):
                letter = "Z"
                check(letter)
            #root = Tk()
            root =Toplevel()
            global frame1, frame2, frame3, left_side, right_side
            frame1 = Frame(root, bg="red")
            frame1.pack()
            left_side = Frame(frame1, bg="red")
            left_side.pack(side=LEFT, ipadx=128)
            right_side = Frame(frame1, bg="red")
            right_side.pack(side=LEFT)
            frame2 = Frame(root)
            frame2.pack()
            frame3 = Frame(root, bg="white")
            frame3.pack(pady=15)
            # global score, exitbutton, hangman_image_label, ar_selcted_word
            # global hint_chance
            word_pos = random.randint(0, len(answers) - 1)
            words = answers[word_pos]
            hint_chance = 0

            home.letter_into_word.clear()
            home.ar_letter_into_word.clear()

            home.variable.clear()
            ar_selcted_word = words.lower()
            print(ar_selcted_word)

            for word in words:
                home.letter_into_word.append(word)
                home.ar_letter_into_word.append(word)

            for_column_start_pos = round((12 - len(home.letter_into_word)) / 2)
            for position in range(len(home.letter_into_word)):
                home.variable.append(chr(random.randint(65, 91)))
                home.variable[position] = Label(frame3, relief="solid", width=8, bd=4)
                home.variable[position].grid(row=0, column=for_column_start_pos + position, ipady=5, pady=10)
            score = Label(left_side, text=f"Score : {home.total_score}", width=10)
            score.pack(padx=30, side="left", ipady=5)

            billlogin_btn_image_location = os.path.abspath('images\\Hangman.png')
            billlogin_btn_opened_image = Image.open(billlogin_btn_image_location)
            billlogin_btn_resize_image = billlogin_btn_opened_image.resize((400, 100))
            global bill_login_image
            bill_login_image = ImageTk.PhotoImage(billlogin_btn_resize_image)
            score = Label(left_side, image=bill_login_image, bg="white")
            score.pack(ipadx=60, pady=10)

            def call_exit():
                root.destroy()


            exitbutton = Button(right_side, text="Exit", bg="#FFF", relief="groove", font=("century", 9, "bold"), bd=4,
                                width=4, command=call_exit)
            exitbutton.pack(side="right", ipady=5, padx=15)
            #  FRAME 2
            hangman_imagelocation = os.path.abspath('images\\1.png')
            hangman_image_open = Image.open(hangman_imagelocation)
            hangman_image_resize = hangman_image_open.resize((300, 300))
            global hangman_image
            hangman_image = ImageTk.PhotoImage(hangman_image_resize)
            hangman_image_label = Label(frame2, image=hangman_image)
            hangman_image_label.pack(ipadx=60, pady=10)

            a_button = Button(frame3, text="A", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=a_btn)
            a_button.grid(row=1, column=0, ipady=5)
            button_variable_list.append(a_button)
            b_button = Button(frame3, text="B", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=b_btn)
            b_button.grid(row=1, column=1, ipady=5)
            button_variable_list.append(b_button)
            c_button = Button(frame3, text="C", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=c_btn)
            c_button.grid(row=1, column=2, ipady=5)
            button_variable_list.append(c_button)
            d_button = Button(frame3, text="D", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=d_btn)
            d_button.grid(row=1, column=3, ipady=5)
            button_variable_list.append(d_button)
            e_button = Button(frame3, text="E", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=e_btn)
            e_button.grid(row=1, column=4, ipady=5)
            button_variable_list.append(e_button)
            f_button = Button(frame3, text="F", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=f_btn)
            f_button.grid(row=1, column=5, ipady=5)
            button_variable_list.append(f_button)
            g_button = Button(frame3, text="G", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=g_btn)
            g_button.grid(row=1, column=6, ipady=5)
            button_variable_list.append(g_button)
            h_button = Button(frame3, text="H", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=h_btn)
            h_button.grid(row=1, column=7, ipady=5)
            button_variable_list.append(h_button)
            i_button = Button(frame3, text="I", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=i_btn)
            i_button.grid(row=1, column=8, ipady=5)
            button_variable_list.append(i_button)
            j_button = Button(frame3, text="J", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=j_btn)
            j_button.grid(row=1, column=9, ipady=5)
            button_variable_list.append(j_button)
            k_button = Button(frame3, text="K", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=k_btn)
            k_button.grid(row=1, column=10, ipady=5)
            button_variable_list.append(k_button)
            l_button = Button(frame3, text="L", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=l_btn)
            l_button.grid(row=1, column=11, ipady=5)
            button_variable_list.append(l_button)
            m_button = Button(frame3, text="M", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=m_btn)
            m_button.grid(row=2, column=1, ipady=5)
            button_variable_list.append(m_button)
            n_button = Button(frame3, text="N", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=n_btn)
            n_button.grid(row=2, column=2, ipady=5)
            button_variable_list.append(n_button)
            o_button = Button(frame3, text="O", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=o_btn)
            o_button.grid(row=2, column=3, ipady=5)
            button_variable_list.append(o_button)
            p_button = Button(frame3, text="P", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=p_btn)
            p_button.grid(row=2, column=4, ipady=5)
            button_variable_list.append(p_button)
            q_button = Button(frame3, text="Q", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=q_btn)
            q_button.grid(row=2, column=5, ipady=5)
            button_variable_list.append(q_button)
            r_button = Button(frame3, text="R", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=r_btn)
            r_button.grid(row=2, column=6, ipady=5)
            button_variable_list.append(r_button)
            s_button = Button(frame3, text="S", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=s_btn)
            s_button.grid(row=2, column=7, ipady=5)
            button_variable_list.append(s_button)
            t_button = Button(frame3, text="T", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=t_btn)
            t_button.grid(row=2, column=8, ipady=5)
            button_variable_list.append(t_button)
            u_button = Button(frame3, text="U", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=u_btn)
            u_button.grid(row=2, column=9, ipady=5)
            button_variable_list.append(u_button)
            v_button = Button(frame3, text="V", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=v_btn)
            v_button.grid(row=3, column=3, ipady=5)
            button_variable_list.append(v_button)
            w_button = Button(frame3, text="W", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=w_btn)
            w_button.grid(row=3, column=4, ipady=5)
            button_variable_list.append(w_button)
            x_button = Button(frame3, text="X", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=x_btn)
            x_button.grid(row=3, column=5, ipady=5)
            button_variable_list.append(x_button)
            y_button = Button(frame3, text="Y", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=y_btn)
            y_button.grid(row=3, column=6, ipady=5)
            button_variable_list.append(y_button)
            z_button = Button(frame3, text="Z", bg="peachpuff", relief="groove", font=("century", 9, "bold"), bd=4,
                              width=8,
                              command=z_btn)
            z_button.grid(row=3, column=7, ipady=5)
            def hint_btn():
                # global hint_chance
                print("hint_chance" + str(home.hint_chance))

                if 0 < home.hint_chance <= 2:
                    reveal_word = random.randint(0, len(home.letter_into_word) - 1)
                    check(home.letter_into_word[reveal_word])
                    home.hint_chance -= 1
                else:
                    messagebox.showerror("error", "you exceed the hint limit", parent=root)
            button_variable_list.append(z_button)
            hint_button = Button(frame3, text="Hint", bg="peachpuff", relief="groove", font=("century", 9, "bold"),
                                 bd=4,
                                 width=8, command=hint_btn)
            hint_button.grid(row=3, column=11, ipady=5)

            root.bind('<a>', a_btn)
            root.bind('<A>', a_btn)
            root.bind('<b>', b_btn)
            root.bind('<B>', b_btn)
            root.bind('<c>', c_btn)
            root.bind('<C>', c_btn)
            root.bind('<d>', d_btn)
            root.bind('<D>', d_btn)
            root.bind('<e>', e_btn)
            root.bind('<E>', e_btn)
            root.bind('<f>', f_btn)
            root.bind('<F>', f_btn)
            root.bind('<g>', g_btn)
            root.bind('<G>', g_btn)
            root.bind('<h>', h_btn)
            root.bind('<H>', h_btn)
            root.bind('<i>', i_btn)
            root.bind('<I>', i_btn)
            root.bind('<j>', j_btn)
            root.bind('<J>', j_btn)
            root.bind('<k>', k_btn)
            root.bind('<K>', k_btn)
            root.bind('<l>', l_btn)
            root.bind('<L>', l_btn)
            root.bind('<m>', m_btn)
            root.bind('<M>', m_btn)
            root.bind('<n>', n_btn)
            root.bind('<N>', n_btn)
            root.bind('<o>', o_btn)
            root.bind('<O>', o_btn)
            root.bind('<p>', p_btn)
            root.bind('<P>', p_btn)
            root.bind('<q>', q_btn)
            root.bind('<Q>', q_btn)
            root.bind('<r>', r_btn)
            root.bind('<R>', r_btn)
            root.bind('<s>', s_btn)
            root.bind('<S>', s_btn)
            root.bind('<t>', t_btn)
            root.bind('<T>', t_btn)
            root.bind('<u>', u_btn)
            root.bind('<U>', u_btn)
            root.bind('<v>', v_btn)
            root.bind('<V>', v_btn)
            root.bind('<w>', w_btn)
            root.bind('<W>', w_btn)
            root.bind('<x>', x_btn)
            root.bind('<X>', x_btn)
            root.bind('<y>', y_btn)
            root.bind('<Y>', y_btn)
            root.bind('<z>', z_btn)
            root.bind('<Z>', z_btn)
            root.resizable(False, False)
            root.mainloop()




        window = Tk()
        w = 800
        h = 600
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        x = (ws / 3) - (hs / 3)
        y = (hs / 2) - (hs / 2)
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        r2 = Image.open("images/Hangman_Home_Screen.png")
        r2 = r2.resize((800, 600))
        r1 = ImageTk.PhotoImage(r2)
        label = Label(window, image=r1)
        label.image = r1
        label.pack()
        def call_exit():
            window.destroy()

        bt1 = Button(window, text='PLAY', width=30, bg="#00FF00", command=call_play, font=('times', 15, ' bold '))
        bt1.place(x=250, y=200)

        bt = Button(window, text='QUIT', fg='white', width=30, bg="#00FF00", command=call_exit,
                    font=('times', 15, ' bold '))
        bt.place(x=250, y=300)
        window.resizable(False, False)
        window.mainloop()


# def threaded_function(arg):
#     for i in range(arg):
#         print("running")
#         sleep(1)
#         playsound.playsound('a.wav')
#
#
# if __name__ == "__main__":
#     thread = Thread(target = threaded_function, args = (10,))
#     thread.start()
#     thread.join()
#     print("thread finished...exiting")

mm=home()

# x = threading.Thread(target=mm.thread_function, args=(1,))
# x.start()
mm.main()
#


