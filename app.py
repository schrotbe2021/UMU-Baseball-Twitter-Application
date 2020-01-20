import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2

class UMUTwitterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        print(tk.TkVersion)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (VerifyAccount, ChooseTweet, StartGame, ScoringChange, HomePage, EndGame, SubPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("VerifyAccount")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class VerifyAccount(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Verify Twitter Account", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button3 = tk.Button(self, text="Home Page",
                            command=lambda: controller.show_frame("HomePage"))
    
        button3.pack()

class SubPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Substitute", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button3 = tk.Button(self, text="Home Page",
                            command=lambda: controller.show_frame("HomePage"))
    
        button3.pack()

class HomePage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Home Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Choose Tweet",
                           command=lambda: controller.show_frame("ChooseTweet"))
        button.pack()


class StartGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Start Game Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go home",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()


class ScoringChange(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scoring Change Game", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go home",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()

class EndGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="End Game", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go home",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()

class ChooseTweet(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose Tweet", font=controller.title_font)
        label.pack(side="left", fill="x", pady=10)

        startGameButton = tk.Button(self, text="Start Game",
                            command=lambda: controller.show_frame("StartGame"))
        scoringChangeButton = tk.Button(self, text="Scoring Change",
                            command=lambda: controller.show_frame("ScoringChange"))

        endGameButton = tk.Button(self, text="End Game",
                            command=lambda: controller.show_frame("EndGame"))

        subButton = tk.Button(self, text="Substitute",
                            command=lambda: controller.show_frame("SubPage"))
        
        homeButton = tk.Button(self, text="Go home",
                           command=lambda: controller.show_frame("HomePage"))

        homeButton.pack()
        subButton.pack()
        endGameButton.pack()
        startGameButton.pack()
        scoringChangeButton.pack()


if __name__ == "__main__":
    app = UMUTwitterApp()
    app.geometry("1000x750")
    app.mainloop()