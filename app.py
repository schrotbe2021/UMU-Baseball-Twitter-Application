import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2
from tweets import SayPioBoof

class UMUTwitterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
  
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        
        container = tk.Frame(self)
        self.title("Official UMU Twitter App")

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
        homeButton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("HomePage"))
        backButton = tk.Button(self, text="<-- Back",
                            command=lambda: controller.show_frame("ChooseTweet"))

        backButton.place(x=50, y=45)
        homeButton.place(x=150, y=45)

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
        
        # Page setup
        label = tk.Label(self, text="Start Game Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        homeButton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("HomePage"))
        backButton = tk.Button(self, text="<-- Back",
                            command=lambda: controller.show_frame("ChooseTweet"))

        # Drop down menus
        oacNonConf = tk.StringVar(self)
        oacNonConf.set("Choose...")
        oacDropDown = tk.OptionMenu(self, oacNonConf, "OAC", "nonconference")

        numGames = tk.StringVar(self)
        numGames.set("# of games...")
        numGamesDropDown = tk.OptionMenu(self, numGames, "doubleheader", "matchup")

        # Labels
        oppenentLabel = tk.Label(self, text="Opponent:")
        locationLabel = tk.Label(self, text="Location:")
        timeLabel = tk.Label(self, text="Time:")
        recordLabel = tk.Label(self, text="Record")
        oacOrNonLabel = tk.Label(self, text="Conf Game:")
        numGamesLabel = tk.Label(self, text="# of Games:")
        gameLinkLabel = tk.Label(self, text="Game Link:")

        # Entries
        opponentEntry = tk.Entry(self, width=25)
        locationEntry = tk.Entry(self, width=25)
        timeEntry = tk.Entry(self, width=25)
        recordEntry = tk.Entry(self, width=25)
        gameLinkEntry = tk.Entry(self, width = 50)

        # Buttons
        sendTweetButton = tk.Button(self, text="Send Tweet", command=SayPioBoof)

        # Placement
        xLabel = 150
        recordLabel.place(x=xLabel, y=75)
        timeLabel.place(x=xLabel, y=150)
        locationLabel.place(x=xLabel, y=125)
        oppenentLabel.place(x=xLabel, y=100)
        oacOrNonLabel.place(x=xLabel, y=200)
        numGamesLabel.place(x=xLabel, y=225)
        gameLinkLabel.place(x=xLabel, y=250)
        
        timeEntry.place(x=250, y=150)
        locationEntry.place(x=250, y=125)
        opponentEntry.place(x=250, y=100)
        recordEntry.place(x=250, y=75)
        gameLinkEntry.place(x=250, y=250)
        
        backButton.place(x=50, y=45)
        homeButton.place(x=150, y=45)
        sendTweetButton.place(x=500, y=500)

        oacDropDown.place(x=250, y=200)
        numGamesDropDown.place(x=250, y=225)

        
class ScoringChange(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scoring Change Game", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        homeButton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("HomePage"))
        backButton = tk.Button(self, text="<-- Back",
                            command=lambda: controller.show_frame("ChooseTweet"))

        backButton.place(x=50, y=45)
        homeButton.place(x=150, y=45)

class EndGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="End Game", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        homeButton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("HomePage"))
        backButton = tk.Button(self, text="<-- Back",
                            command=lambda: controller.show_frame("ChooseTweet"))

        backButton.place(x=50, y=45)
        homeButton.place(x=150, y=45)

class ChooseTweet(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose Tweet", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        startGameButton = tk.Button(self, text="Start Game",
                            command=lambda: controller.show_frame("StartGame"))
        scoringChangeButton = tk.Button(self, text="Scoring Change",
                            command=lambda: controller.show_frame("ScoringChange"))

        endGameButton = tk.Button(self, text="End Game",
                            command=lambda: controller.show_frame("EndGame"))

        subButton = tk.Button(self, text="Substitute",
                            command=lambda: controller.show_frame("SubPage"))
        
        homeButton = tk.Button(self, text="<-- Back",
                           command=lambda: controller.show_frame("HomePage"))
        
        homeButton.place(x=150, y=45)
        startGameButton.place(x=300, y=45)
        scoringChangeButton.place(x=450, y=45)
        subButton.place(x=600, y=45)
        endGameButton.place(x=750, y=45)


if __name__ == "__main__":
    app = UMUTwitterApp()
    app.geometry("1000x750")
    app.mainloop()