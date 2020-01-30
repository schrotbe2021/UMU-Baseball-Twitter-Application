import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2
import twitter
import emoji

api = twitter.Api(consumer_key='Kt4rgFjVqsEjUZ7hI2gogLgf3',
                      consumer_secret='XnFrW7acLminsGdPTgiGxpsnSqDdhSu311LDcc0YsTsWTc1hHw',
                      access_token_key='804787884893028356-OSuVoDz3eduTcwq8B50qiXIec5OhFCg',
                      access_token_secret='hTw8k48CIWkQvkbH8yYSrDx9tDav4GWCciPQV5xGOArxa')

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
        

        # Function to take input and format tweet
        def StartGameTweet():
            status = api.PostUpdate('Mount Union (' + recordEntry.get() + ') takes on ' + opponentEntry.get()
                        + ' in a ' + oacNonConf.get() + ' ' + numGames.get() + ' today.\n\n\t' 
                        + emoji.emojize(':round_pushpin:') + ': ' + locationEntry.get() + '\n' 
                        + emoji.emojize(':alarm_clock:') + ': ' + timeEntry.get() + '\n'
                        + emoji.emojize(':link:') + ': ' + gameLinkEntry.get() 
                        + '\n\n\tYou can follow live tweets for today\'s game at #UMUBaseball2020')

        # Drop down menus
        oacNonConf = tk.StringVar(self)
        oacNonConf.set("Choose...")
        oacDropDown = tk.OptionMenu(self, oacNonConf, "OAC", "nonconference")         

        numGames = tk.StringVar(self)
        numGames.set("# of games...")
        numGamesDropDown = tk.OptionMenu(self, numGames, "doubleheader", "matchup")

        # Buttons
        sendTweetButton = tk.Button(self, text="Send Tweet", command=StartGameTweet)

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

     
            

        def ScoringChangeTweet():
            status = api.PostUpdate(playerNameEntry.get() + ' brings in ' + numRunsEntry.get() + ' with a ' 
                + hitType.get() + ' in the ' + inningEntry.get() + ' inning.\n\n' 
                + 'Mount Union - ' + mountScoreEntry.get() + '\n'
                + opponentEntry.get() + ' - ' + opponentScoreEntry.get() + '\n\n'
                + '#UMUBaseball2020 | #D3Baseball')

        # Buttons
        homeButton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("HomePage"))
        backButton = tk.Button(self, text="<-- Back",
                            command=lambda: controller.show_frame("ChooseTweet"))
        sendTweetButton = tk.Button(self, text='Send Tweet', command=ScoringChangeTweet)

        # Radio Button
        whoScoredLabel = tk.Label(self, text='Who Scored?')

        # Option Menus
        hitType = tk.StringVar(self)
        hitType.set('Hit Type...')
        hitTypeMenu = tk.OptionMenu(self, hitType, 'Single', 'Double', 'Triple', 'Home Run', 'Walk')

        # Labels
        playerNameLabel = tk.Label(self, text='Player Name:')
        numRunsLabel = tk.Label(self, text='# of Runs:')
        inningLabel = tk.Label(self, text='Inning:')
        hitTypeLabel = tk.Label(self, text='Hit Type:')
        mountScoreLabel = tk.Label(self ,text='UMU Score:')
        opponentLabel = tk.Label(self, text='Opponent:')
        opponentScoreLabel = tk.Label(self, text='Opponent Score:')


        # Text Fields
        playerNameEntry = tk.Entry(self, width=50)
        numRunsEntry = tk.Entry(self, width=50)
        inningEntry = tk.Entry(self, width=50)
        mountScoreEntry = tk.Entry(self, width=50)
        opponentEntry = tk.Entry(self, width=50)
        opponentScoreEntry = tk.Entry(self, width=50)
       
        # Placement
        playerNameLabel.place(x=150, y=150)
        numRunsLabel.place(x=150, y=175)
        inningLabel.place(x=150, y=225)
        hitTypeLabel.place(x=150, y=200)
        mountScoreLabel.place(x=150, y=250)
        opponentLabel.place(x=150, y=275)
        opponentScoreLabel.place(x=150, y=300)
        whoScoredLabel.place(x=150, y=125)

        playerNameEntry.place(x=250, y=150)
        numRunsEntry.place(x=250, y=175)
        inningEntry.place(x=250, y=225)
        mountScoreEntry.place(x=250, y=250)
        opponentEntry.place(x=250, y=275)
        opponentScoreEntry.place(x=250, y=300)

        hitTypeMenu.place(x=250, y=200)

        sendTweetButton.place(x=400, y=400)
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