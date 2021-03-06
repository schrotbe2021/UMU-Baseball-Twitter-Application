import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2
import tkFileDialog
from PIL import Image, ImageTk
import twitter
import emoji
import config


api = twitter.Api(consumer_key=config.api_key,
                       consumer_secret=config.api_secret,
                       access_token_key=config.access_token,
                       access_token_secret=config.token_secret)


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
        for F in (ChooseTweet, StartGame, ScoringChange, HomePage, EndGame, SubPage, Lineup, CustomTweet, TweetSentCheck):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class HomePage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    # Page Styling
        # Top Purple Bar
        canvas = tk.Canvas(self, width=1000, height=750)
        canvas.pack()
        canvas.create_rectangle(0, 0, 1000, 100, fill="#542A6D")

        # Logo
        path = "./images/style/logo.png"
        logo = Image.open(path)
        logo = logo.resize((150, 100), Image.ANTIALIAS)
        self.logoPhoto = ImageTk.PhotoImage(logo)
        canvas.create_image(0, -5, image=self.logoPhoto, anchor="nw")

        # Vertical Bar
        canvas.create_line(150, 10, 150, 90, fill='white')
        
        # Header Label
        chooseTweetLabel = tk.Label(self, text='Live Tweet In-Game @umubaseball', bg='#542A6D', fg='white', font=('Industry Inc Base', 25))
        chooseTweetLabel.place(x=175, y=30)

        # Home page Button
        homeButton = tk.Button(self, text='Home', bg='white', bd=0, width=15, height=3, fg='#542A6D',
                           command=lambda: controller.show_frame("HomePage"))
        homeButton.place(x=825, y=18)

        # Header Photo
        headerPath = "./images/style/header.png"
        header = Image.open(headerPath)
        header = header.resize((1000, 350), Image.ANTIALIAS)
        self.headerPhoto = ImageTk.PhotoImage(header)
        canvas.create_image(0, 100, image=self.headerPhoto, anchor="nw")

        # Label
        author = tk.Label(self, text='**Created by Ben Schroth       Questions/Comments: schrotbe2021@mountunion.edu**',
                            fg='#542A6D', font=('Helvetica', 10))

        # Button
        chooseTweetButton = tk.Button(self, text="Choose Tweet", bg='white', bd=0, width=30, height=2, fg='#542A6D', font=('Helvetica', 30),
                                command=lambda: controller.show_frame("ChooseTweet"))
        
        # Placement
        author.place(x=240, y=700)

        chooseTweetButton.place(x=150, y=500)

class ChooseTweet(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    # Page Styling
        # Top Purple Bar
        canvas = tk.Canvas(self, width=1000, height=750)
        canvas.pack()
        canvas.create_rectangle(0, 0, 1000, 100, fill="#542A6D")

        # Logo
        path = "./images/style/logo.png"
        print(path)
        logo = Image.open(path)
        logo = logo.resize((150, 100), Image.ANTIALIAS)
        self.logoPhoto = ImageTk.PhotoImage(logo)
        canvas.create_image(0, -5, image=self.logoPhoto, anchor="nw")

        # Vertical Bar
        canvas.create_line(150, 10, 150, 90, fill='white')
        
        # Header Label
        chooseTweetLabel = tk.Label(self, text='Live Tweet In-Game @umubaseball', bg='#542A6D', fg='white', font=('Industry Inc Base', 25))
        chooseTweetLabel.place(x=175, y=30)

        # Home page Button
        homeButton = tk.Button(self, text='Home', bg='white', bd=0, width=15, height=3, fg='#542A6D',
                           command=lambda: controller.show_frame("HomePage"))
        homeButton.place(x=825, y=18)

        # Top row of buttons
        startGameButton = tk.Button(self, text="Start Game", bd=0, fg='#542A6D',font=('Helvetica',40), width=9, height= 4, bg='white',
                            command=lambda: controller.show_frame("StartGame"))
        lineupButton = tk.Button(self, text="Lineup", bd=0, fg='#542A6D',font=('Helvetica',40), width=9, height= 4, bg='white',
                            command=lambda: controller.show_frame('Lineup'))
        scoringChangeButton = tk.Button(self, text="Scoring\nChange", bd=0, fg='#542A6D',font=('Helvetica',40), width=9, height= 4, bg='white',
                            command=lambda: controller.show_frame("ScoringChange"))
        
        startGameButton.place(x=25, y=120)
        lineupButton.place(x=350, y=120)
        scoringChangeButton.place(x=675, y=120)

        # Bottom row of Buttons
        endGameButton = tk.Button(self, text="End Game", bd=0, fg='#542A6D',font=('Helvetica',40), width=9, height= 4, bg='white',
                            command=lambda: controller.show_frame("EndGame"))

        subButton = tk.Button(self, text="Substitute", bd=0, fg='#542A6D',font=('Helvetica',40), width=9, height= 4, bg='white',
                            command=lambda: controller.show_frame("SubPage"))
        
        customButton = tk.Button(self, text='Custom\nTweet', bd=0, fg='#542A6D',font=('Helvetica',40), width=9, height= 4, bg='white', 
                            command=lambda: controller.show_frame("CustomTweet"))
        
        endGameButton.place(x=25, y=400)
        subButton.place(x=350, y=400)
        customButton.place(x=675, y=400)

class StartGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    # Page Styling
        # Top Purple Bar
        canvas = tk.Canvas(self, width=1000, height=750)
        canvas.pack()
        canvas.create_rectangle(0, 0, 1000, 100, fill="#542A6D")

        # Logo
        path = "./images/style/logo.png"
        logo = Image.open(path)
        logo = logo.resize((150, 100), Image.ANTIALIAS)
        self.logoPhoto = ImageTk.PhotoImage(logo)
        canvas.create_image(0, -5, image=self.logoPhoto, anchor="nw")

        # Vertical Bar
        canvas.create_line(150, 10, 150, 90, fill='white')
        
        # Header Label
        chooseTweetLabel = tk.Label(self, text='Start Game Tweet', bg='#542A6D', fg='white', font=('Industry Inc Base', 25))
        chooseTweetLabel.place(x=175, y=30)

        # Home and back page Button
        homeButton = tk.Button(self, text='Home', bg='white', bd=0, width=15, height=3, fg='#542A6D',
                           command=lambda: controller.show_frame("HomePage"))
        homeButton.place(x=825, y=18)

        backButton = tk.Button(self, text="<-- Back", bg='white', bd=0, width=15, height=3, fg='#542A6D',
                            command=lambda: controller.show_frame("ChooseTweet"))
        backButton.place(x=660, y=18)

        # Function to take input and format tweet
        def StartGameTweet():
            # Pick photo for tweet in dialog
            filename = tkFileDialog.askopenfilename(initialdir = resource_path("/images/StartGame"), title = "Select photo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            
            # Tweet with photo
            status = api.PostUpdate('Mount Union (' + recordEntry.get() + ') takes on ' + opponentEntry.get()
                        + ' in a ' + oacNonConf.get() + ' ' + numGames.get() + ' today.\n\n\t' 
                        + emoji.emojize(':round_pushpin:') + ': ' + locationEntry.get() + '\n' 
                        + emoji.emojize(':alarm_clock:') + ': ' + timeEntry.get() + '\n'
                        + emoji.emojize(':link:') + ': ' + gameLinkEntry.get() 
                        + '\n\n\tYou can follow live tweets for today\'s game at #UMUBaseball2020', media=filename)
        
            self.controller.show_frame('TweetSentCheck')

        # Drop down menus
        oacNonConf = tk.StringVar(self)
        oacNonConf.set("Choose...")
        oacDropDown = tk.OptionMenu(self, oacNonConf, "OAC", "nonconference")         

        numGames = tk.StringVar(self)
        numGames.set("# of games...")
        numGamesDropDown = tk.OptionMenu(self, numGames, "doubleheader", "matchup")

        # Buttons
        sendTweetButton = tk.Button(self, text="Send Tweet", bg='white', bd=0, width=30, height=2, fg='#542A6D', font=('Helvetica', 30),
                            command=StartGameTweet)

        # Labels
        oppenentLabel = tk.Label(self, text="Opponent:", font=('Helvetica', 20))
        locationLabel = tk.Label(self, text="Location:", font=('Helvetica', 20))
        timeLabel = tk.Label(self, text="Time:", font=('Helvetica', 20))
        recordLabel = tk.Label(self, text="Record:", font=('Helvetica', 20))
        oacOrNonLabel = tk.Label(self, text="Conf Game:", font=('Helvetica', 20))
        numGamesLabel = tk.Label(self, text="# of Games:", font=('Helvetica', 20))
        gameLinkLabel = tk.Label(self, text="Game Link:", font=('Helvetica', 20))

        # Entries
        opponentEntry = tk.Entry(self, width=25, font=('Helvetica', 20))
        locationEntry = tk.Entry(self, width=25, font=('Helvetica', 20))
        timeEntry = tk.Entry(self, width=25, font=('Helvetica', 20))
        recordEntry = tk.Entry(self, width=25, font=('Helvetica', 20))
        gameLinkEntry = tk.Entry(self, width =25, font=('Helvetica', 20))

        # Placement
        xLabel = 150
        recordLabel.place(x=xLabel, y=150)
        oppenentLabel.place(x=xLabel, y=200)
        timeLabel.place(x=xLabel, y=250)
        oacOrNonLabel.place(x=xLabel, y=300)
        numGamesLabel.place(x=xLabel, y=350)
        locationLabel.place(x=xLabel, y=400)
        gameLinkLabel.place(x=xLabel, y=450)
        
        entryX = 300
        recordEntry.place(x=entryX, y=150)
        opponentEntry.place(x=entryX, y=200)
        timeEntry.place(x=entryX, y=250)
        oacDropDown.place(x=entryX, y=300)
        numGamesDropDown.place(x=entryX, y=350)
        locationEntry.place(x=entryX, y=400)
        gameLinkEntry.place(x=entryX, y=450)
        
        sendTweetButton.place(x=150, y=550)

class Lineup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    # Page Styling
        # Top Purple Bar
        canvas = tk.Canvas(self, width=1000, height=750)
        canvas.pack()
        canvas.create_rectangle(0, 0, 1000, 100, fill="#542A6D")

        # Logo
        path = "./images/style/logo.png"
        logo = Image.open(path)
        logo = logo.resize((150, 100), Image.ANTIALIAS)
        self.logoPhoto = ImageTk.PhotoImage(logo)
        canvas.create_image(0, -5, image=self.logoPhoto, anchor="nw")

        # Vertical Bar
        canvas.create_line(150, 10, 150, 90, fill='white')
        
        # Header Label
        chooseTweetLabel = tk.Label(self, text='Lineup Tweet', bg='#542A6D', fg='white', font=('Industry Inc Base', 25))
        chooseTweetLabel.place(x=175, y=30)

        # Home and back page Button
        homeButton = tk.Button(self, text='Home', bg='white', bd=0, width=15, height=3, fg='#542A6D',
                           command=lambda: controller.show_frame("HomePage"))
        homeButton.place(x=825, y=18)

        backButton = tk.Button(self, text="<-- Back", bg='white', bd=0, width=15, height=3, fg='#542A6D',
                            command=lambda: controller.show_frame("ChooseTweet"))
        backButton.place(x=660, y=18)

        # Arrays to set up label and entries widgets for lineup and position
        lineup = ['1:', '2:', '3:', '4:', '5:', '6:', '7:', '8:', '9:', 'P:']
        lineUpEntry = []
        posOptionArray = []

        yLabel = 120  # Control for yPos of widget

        # For loop to instantiate and place labels and entries for lineup tweet
        for i in range(len(lineup)):
            yLabel += 40 # Increments yPos to display widgets correctly

            # Widget to be placed through each iteration
            label = tk.Label(self, text=lineup[i], font=('Helvetica', 20))
            entry = tk.Entry(self, width = 20, font=('Helvetica', 20))

            posOption = tk.StringVar(self)
            posOption.set('Position...')
            posOpMenu = tk.OptionMenu(self, posOption, 'C', '1B', '2B', 'SS', '3B', 'LF', 'CF', 'RF', 'DH', 'P')
            posOpMenu.config(width=10)

            # Placement of widget through each iteration
            entry.place(x=200, y=yLabel)
            label.place(x=150, y=yLabel)
            posOpMenu.place(x=525, y=yLabel)

            # Adds widget to array
            lineUpEntry.append(entry)
            posOptionArray.append(posOption)

        
        # PlayerString() takes in lineUpEntry and posOptionArray and returns string for tweet with lineup
        def PlayerString():
            result = ''
            for i in range(len(lineup)):
                if posOptionArray[i].get() == 'P':
                    result += ('P - ' + str(lineUpEntry[i].get()) + ' (' + str(posOptionArray[i].get()) + ')\n')
                else:
                    result += (str(i+1) + ' - ' + str(lineUpEntry[i].get()) + ' (' + str(posOptionArray[i].get()) + ')\n')
                
            return result

        # Tweet for Lineup tweet
        def LineupTweet():
            # Pick photo for tweet in dialog
            filename = tkFileDialog.askopenfilename(initialdir = resource_path("/images/StartGame"), title = "Select photo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

            # Tweet with photo
            api.PostUpdate('Lineup for today\'s game against ' + opponentEntry.get() + '\n\n' 
            + PlayerString() + '\n\n'
            + '#UMUBaseball2020 | #D3Baseball', media=filename)

            self.controller.show_frame("TweetSentCheck")


        # Button
        sendTweetButton = tk.Button(self, text='Send Tweet', bg='white', bd=0, width=30, height=2, fg='#542A6D', font=('Helvetica', 30), 
                                    command=LineupTweet)

        # Label
        opponentLabel = tk.Label(self, text='Opponent:', font=('Helvetica', 20))   

        # Entry
        opponentEntry = tk.Entry(self, width=20, font=('Helvetica', 20))

        # Placement
        opponentLabel.place(x=150, y= 120)

        opponentEntry.place(x=300, y=120)    

        sendTweetButton.place(x=150, y=600)

class ScoringChange(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    # Page Styling
        # Top Purple Bar
        canvas = tk.Canvas(self, width=1000, height=750)
        canvas.pack()
        canvas.create_rectangle(0, 0, 1000, 100, fill="#542A6D")

        # Logo
        path = "./images/style/logo.png"
        logo = Image.open(path)
        logo = logo.resize((150, 100), Image.ANTIALIAS)
        self.logoPhoto = ImageTk.PhotoImage(logo)
        canvas.create_image(0, -5, image=self.logoPhoto, anchor="nw")

        # Vertical Bar
        canvas.create_line(150, 10, 150, 90, fill='white')
        
        # Header Label
        chooseTweetLabel = tk.Label(self, text='Scoring Change Tweet', bg='#542A6D', fg='white', font=('Industry Inc Base', 25))
        chooseTweetLabel.place(x=175, y=30)

        # Home and back page Button
        homeButton = tk.Button(self, text='Home', bg='white', bd=0, width=15, height=3, fg='#542A6D',
                           command=lambda: controller.show_frame("HomePage"))
        homeButton.place(x=825, y=18)

        backButton = tk.Button(self, text="<-- Back", bg='white', bd=0, width=15, height=3, fg='#542A6D',
                            command=lambda: controller.show_frame("ChooseTweet"))
        backButton.place(x=660, y=18)

        def WhoScored():
            if whoScored.get() == str('Mount Union'):
                return (playerNameEntry.get() + ' brings in ' + numRunsEntry.get() + ' runs with a ' 
                + hitType.get() + ' in the ' + inningEntry.get() + ' inning.\n\n')
            else :
                return (opponentEntry.get() + ' scores ' + numRunsEntry.get() + ' with a '
                + hitType.get() + ' in the ' + inningEntry.get() + ' inning.\n\n')

        def ScoringChangeTweet():
            # Pick photo for tweet in dialog
            filename = tkFileDialog.askopenfilename(initialdir = resource_path("/images/Roster"), title = "Select photo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

            # Tweet with photo
            status = api.PostUpdate(WhoScored()
                + 'Mount Union - ' + mountScoreEntry.get() + '\n'
                + opponentEntry.get() + ' - ' + opponentScoreEntry.get() + '\n\n'
                + '#UMUBaseball2020 | #D3Baseball', media=filename)

            self.controller.show_frame("TweetSentCheck")

        # Buttons
        sendTweetButton = tk.Button(self, text='Send Tweet', bg='white', bd=0, width=30, height=2, fg='#542A6D', font=('Helvetica', 30), 
                            command=ScoringChangeTweet)

        # Radio Button
        whoScored = tk.StringVar(self)
        mountScoredRB = tk.Radiobutton(self, text="Mount Union", variable=whoScored, value="Mount Union", font=('Helvetica', 20))
        opponentScoredRB = tk.Radiobutton(self, text="Opponent", variable=whoScored, value="Opponent", font=('Helvetica', 20))

        # Option Menus
        hitType = tk.StringVar(self)
        hitType.set('Hit Type...')
        hitTypeMenu = tk.OptionMenu(self, hitType, 'single', 'double', 'triple', 'home run', 'walk')

        # Labels
        playerNameLabel = tk.Label(self, text='Player Name:', font=('Helvetica', 20))
        numRunsLabel = tk.Label(self, text='# of Runs:', font=('Helvetica', 20))
        inningLabel = tk.Label(self, text='Inning:', font=('Helvetica', 20))
        hitTypeLabel = tk.Label(self, text='Hit Type:', font=('Helvetica', 20))
        mountScoreLabel = tk.Label(self ,text='UMU Score:', font=('Helvetica', 20))
        opponentLabel = tk.Label(self, text='Opponent:', font=('Helvetica', 20))
        opponentScoreLabel = tk.Label(self, text='Opponent Score:', font=('Helvetica', 20))
        whoScoredLabel = tk.Label(self, text='Who Scored?', font=('Helvetica', 20))


        # Text Fields
        playerNameEntry = tk.Entry(self, width=20, font=('Helvetica', 20))
        numRunsEntry = tk.Entry(self, width=20, font=('Helvetica', 20))
        inningEntry = tk.Entry(self, width=20, font=('Helvetica', 20))
        mountScoreEntry = tk.Entry(self, width=20, font=('Helvetica', 20))
        opponentEntry = tk.Entry(self, width=20, font=('Helvetica', 20))
        opponentScoreEntry = tk.Entry(self, width=20, font=('Helvetica', 20))
       
        # Placement
        whoScoredLabel.place(x=150, y=150)
        playerNameLabel.place(x=150, y=200)
        numRunsLabel.place(x=150, y=250)
        inningLabel.place(x=150, y=300)
        hitTypeLabel.place(x=150, y=350)
        mountScoreLabel.place(x=150, y=400)
        opponentLabel.place(x=150, y=450)
        opponentScoreLabel.place(x=150, y=500)

        mountScoredRB.place(x=325, y=150)
        opponentScoredRB.place(x=550, y=150)

        playerNameEntry.place(x=375, y=200)
        numRunsEntry.place(x=375, y=250)
        inningEntry.place(x=375, y=300)
        hitTypeMenu.place(x=375, y=350)
        mountScoreEntry.place(x=375, y=400)
        opponentScoreEntry.place(x=375, y=500)
        opponentEntry.place(x=375, y=450)

        sendTweetButton.place(x=150, y=600)

class EndGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    # Page Styling
        # Top Purple Bar
        canvas = tk.Canvas(self, width=1000, height=750)
        canvas.pack()
        canvas.create_rectangle(0, 0, 1000, 100, fill="#542A6D")

        # Logo
        path = "./images/style/logo.png"
        logo = Image.open(path)
        logo = logo.resize((150, 100), Image.ANTIALIAS)
        self.logoPhoto = ImageTk.PhotoImage(logo)
        canvas.create_image(0, -5, image=self.logoPhoto, anchor="nw")

        # Vertical Bar
        canvas.create_line(150, 10, 150, 90, fill='white')
        
        # Header Label
        chooseTweetLabel = tk.Label(self, text='End Game Tweet', bg='#542A6D', fg='white', font=('Industry Inc Base', 25))
        chooseTweetLabel.place(x=175, y=30)

        # Home and back page Button
        homeButton = tk.Button(self, text='Home', bg='white', bd=0, width=15, height=3, fg='#542A6D',
                           command=lambda: controller.show_frame("HomePage"))
        homeButton.place(x=825, y=18)

        backButton = tk.Button(self, text="<-- Back", bg='white', bd=0, width=15, height=3, fg='#542A6D',
                            command=lambda: controller.show_frame("ChooseTweet"))
        backButton.place(x=660, y=18)

        def WhoWon():
            if whoWon.get() == 'Mount Union':
                return ('Mount Union defeats ' + opponentEntry.get() + '.\n\n')
            else:
                return (opponentEntry.get() + ' defeats Mount Union.\n\n')

        def EndGameTweet():
            
            # Pick photo for tweet in dialog only if Mount wins.
            if whoWon.get() == 'Mount Union':
                filename = tkFileDialog.askopenfilename(initialdir = resource_path("/images/EndGame"), title = "Select photo",filetypes = (("all files","*.*"), ("jpeg files","*.jpg")))
            else:
                filename = ''

            # Tweet with photo
            api.PostUpdate(WhoWon() 
                            + 'Mount Union - ' + mountScoreEntry.get() + '\n'
                            + opponentEntry.get() + ' - ' + opponentScoreEntry.get() + '\n\n'
                            + '#UMUBaseball2020 | #D3Baseball', media=filename)
            
            self.controller.show_frame("TweetSentCheck")

        # Button
        sendTweet = tk.Button(self, text='Send Tweet', command=EndGameTweet, bg='white', bd=0, width=30, height=2, fg='#542A6D', font=('Helvetica', 30))

        # Radio Button
        whoWon = tk.StringVar(self)
        mountWin = tk.Radiobutton(self, text='Mount Union', variable=whoWon, value='Mount Union', font=('Helvetica', 20))
        opponentWin = tk.Radiobutton(self, text='Opponent', variable=whoWon, value='Opponent', font=('Helvetica', 20))

        # Label
        opponentLabel = tk.Label(self, text="Opponent:", font=('Helvetica', 20))
        mountRecordLabel = tk.Label(self, text="Record:", font=('Helvetica', 20))
        mountScoreLabel = tk.Label(self, text="Mount Score:", font=('Helvetica', 20))
        opponentScoreLabel = tk.Label(self, text="Opponent Score:", font=('Helvetica', 20))
        winnerLabel = tk.Label(self, text="Winning Team:", font=('Helvetica', 20))
        
        # Entry
        opponentEntry = tk.Entry(self, width=20, font=('Helvetica', 20))
        mountRecordEntry = tk.Entry(self, width=20, font=('Helvetica', 20))
        mountScoreEntry = tk.Entry(self, width=20, font=('Helvetica', 20))
        opponentScoreEntry = tk.Entry(self, width=20, font=('Helvetica', 20))

        # Placement
        winnerLabel.place(x=150, y=150)
        opponentLabel.place(x=150, y=200)
        mountRecordLabel.place(x=150, y=250)
        mountScoreLabel.place(x=150, y=300)
        opponentScoreLabel.place(x=150, y=350)
        
        mountWin.place(x=350, y=150)
        opponentWin.place(x=550, y=150)
        opponentEntry.place(x=375, y=200)
        mountRecordEntry.place(x=375, y=250)
        mountScoreEntry.place(x=375, y=300)
        opponentScoreEntry.place(x=375, y=350)

        sendTweet.place(x=150, y=600)    

class SubPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    # Page Styling
        # Top Purple Bar
        canvas = tk.Canvas(self, width=1000, height=750)
        canvas.pack()
        canvas.create_rectangle(0, 0, 1000, 100, fill="#542A6D")

        # Logo
        path = "./images/style/logo.png"
        logo = Image.open(path)
        logo = logo.resize((150, 100), Image.ANTIALIAS)
        self.logoPhoto = ImageTk.PhotoImage(logo)
        canvas.create_image(0, -5, image=self.logoPhoto, anchor="nw")

        # Vertical Bar
        canvas.create_line(150, 10, 150, 90, fill='white')
        
        # Header Label
        chooseTweetLabel = tk.Label(self, text='Substitution Tweet', bg='#542A6D', fg='white', font=('Industry Inc Base', 25))
        chooseTweetLabel.place(x=175, y=30)

        # Home and back page Button
        homeButton = tk.Button(self, text='Home', bg='white', bd=0, width=15, height=3, fg='#542A6D',
                           command=lambda: controller.show_frame("HomePage"))
        homeButton.place(x=825, y=18)

        backButton = tk.Button(self, text="<-- Back", bg='white', bd=0, width=15, height=3, fg='#542A6D',
                            command=lambda: controller.show_frame("ChooseTweet"))
        backButton.place(x=660, y=18)

        # Tweet based on chekcbox whether it is a pitching change or pinch hit
        def TweetType():
            if subType.get() == str('Pitching Substitution'):
                return (subInEntry.get() + ' takes the mound for ' + subOutEntry.get() + ' in the '
                + inningEntry.get() + ' inning.\n\n'
                + '#UMUBaseball2020 | #D3Baseball')
            else:
                return (subInEntry.get() + ' will pinch hit for ' + subOutEntry.get() + ' in the '
                + inningEntry.get() + ' inning for Mount Union.\n\n'
                + '#UMUBaseball2020 | #D3Baseball')
        
        def SubstitutionTweet():
            # Pick photo for tweet in dialog
            filename = tkFileDialog.askopenfilename(initialdir = resource_path("/images/Roster"), title = "Select photo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

            # Tweet with photo
            api.PostUpdate(TweetType(), media=filename)

            self.controller.show_frame("TweetSentCheck")

        #Button
        sendTweet = tk.Button(self, text="Send Tweet", command=SubstitutionTweet,  bg='white', bd=0, width=30, height=2, fg='#542A6D', font=('Helvetica', 30))

        # Radio Button
        subType = tk.StringVar(self)
        pitchingSub = tk.Radiobutton(self, text="Pitching Substitution", variable=subType, value="Pitching Substitution", font=('Helvetica', 20))
        pinchHit = tk.Radiobutton(self, text="Pinch Hit", variable=subType, value="Pinch Hit", font=('Helvetica', 20))

        # Label
        subInLabel = tk.Label(self, text="Player:", font=('Helvetica', 20))
        subOutLabel = tk.Label(self, text="Subbing for:", font=('Helvetica', 20))
        inningLabel = tk.Label(self, text="Inning:", font=('Helvetica', 20))
        subTypeLabel = tk.Label(self, text="Substitution type:", font=('Helvetica', 20))

        #Entry
        subInEntry = tk.Entry(self, width=25, font=('Helvetica', 20))
        subOutEntry = tk.Entry(self, width=25, font=('Helvetica', 20))
        inningEntry = tk.Entry(self, width=25, font=('Helvetica', 20))

        # Placements
        subTypeLabel.place(x=150, y=150)
        subInLabel.place(x=150, y=200)
        subOutLabel.place(x=150, y=250)
        inningLabel.place(x=150, y=300)
        
        pitchingSub.place(x=350, y=150)
        pinchHit.place(x=650, y=150)
        subInEntry.place(x=350, y=200)
        subOutEntry.place(x=350, y=250)
        inningEntry.place(x=350, y=300)

        sendTweet.place(x=150, y=600)

class CustomTweet(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    # Page Styling
        # Top Purple Bar
        canvas = tk.Canvas(self, width=1000, height=750)
        canvas.pack()
        canvas.create_rectangle(0, 0, 1000, 100, fill="#542A6D")

        # Logo
        path = "./images/style/logo.png"
        logo = Image.open(path)
        logo = logo.resize((150, 100), Image.ANTIALIAS)
        self.logoPhoto = ImageTk.PhotoImage(logo)
        canvas.create_image(0, -5, image=self.logoPhoto, anchor="nw")

        # Vertical Bar
        canvas.create_line(150, 10, 150, 90, fill='white')
        
        # Header Label
        chooseTweetLabel = tk.Label(self, text='Custom Tweet', bg='#542A6D', fg='white', font=('Industry Inc Base', 25))
        chooseTweetLabel.place(x=175, y=30)

        # Home and back page Button
        homeButton = tk.Button(self, text='Home', bg='white', bd=0, width=15, height=3, fg='#542A6D',
                           command=lambda: controller.show_frame("HomePage"))
        homeButton.place(x=825, y=18)

        backButton = tk.Button(self, text="<-- Back", bg='white', bd=0, width=15, height=3, fg='#542A6D',
                            command=lambda: controller.show_frame("ChooseTweet"))
        backButton.place(x=660, y=18)

        # Get input for tweet
        def GetTextInput():
            result = inputTextField.get('1.0', 'end-1c')
            return result
        
        def Custom():
            # Pick photo for tweet in dialog
            if mediaOption.get() == 'Yes':
                filename = tkFileDialog.askopenfilename(initialdir = resource_path("/images/StartGame"), title = "Select photo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            else:
                filename = ''
            
            # Tweet for custom input
            api.PostUpdate(GetTextInput() 
                          + '\n\n#UMUBaseball2020 | #D3Baseball', media=filename)

            inputTextField.delete('1.0', 'end-1c')
            self.controller.show_frame("TweetSentCheck")

        # Label
        mediaLabel = tk.Label(self, text='Include media?', font=('Helvetica', 20))

        # Radio Button
        mediaOption = tk.StringVar(self)
        yesMedia = tk.Radiobutton(self, text='Yes', variable=mediaOption, value='Yes', font=('Helvetica', 20))
        noMedia = tk.Radiobutton(self, text='No', variable=mediaOption, value='No', font=('Helvetica', 20))

        # Text Field
        inputTextField = tk.Text(self, width=50, height=10, wrap="word", font=('Helvetica', 20))

        # Button
        sendTweetButton = tk.Button(self, text='Send Tweet', command=Custom,  bg='white', bd=0, width=30, height=2, fg='#542A6D', font=('Helvetica', 30))

        # Placement
        mediaLabel.place(x=150, y=150)

        yesMedia.place(x=350, y=150)
        noMedia.place(x=450, y=150)

        inputTextField.place(x=100, y=200)

        sendTweetButton.place(x=150, y=600)

class TweetSentCheck(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    # Page Styling
        # Top Purple Bar
        canvas = tk.Canvas(self, width=1000, height=750)
        canvas.pack()
        canvas.create_rectangle(0, 0, 1000, 100, fill="#542A6D")

        # Logo
        path = "./images/style/logo.png"
        logo = Image.open(path)
        logo = logo.resize((150, 100), Image.ANTIALIAS)
        self.logoPhoto = ImageTk.PhotoImage(logo)
        canvas.create_image(0, -5, image=self.logoPhoto, anchor="nw")

        # Vertical Bar
        canvas.create_line(150, 10, 150, 90, fill='white')
        
        # Header Label
        chooseTweetLabel = tk.Label(self, text='Tweet Sent Check', bg='#542A6D', fg='white', font=('Industry Inc Base', 25))
        chooseTweetLabel.place(x=175, y=30)

        # Home and back page Button
        homeButton = tk.Button(self, text='Home', bg='white', bd=0, width=15, height=3, fg='#542A6D',
                           command=lambda: controller.show_frame("HomePage"))
        homeButton.place(x=825, y=18)

        backButton = tk.Button(self, text="<-- Back", bg='white', bd=0, width=15, height=3, fg='#542A6D',
                            command=lambda: controller.show_frame("ChooseTweet"))
        backButton.place(x=660, y=18)

        # Sets label to confirm that tweet was sent.
        def LastTweet():
            try:
                tweet = api.GetUserTimeline(screen_name ='umubaseball', count=1)
                returnedTweet = [i.AsDict() for i in tweet]
                setLabel = returnedTweet[0]['text']
                latestTweetLabel.config(text=setLabel)
            except:
                latestTweetLabel.config(text="Tweet contains emoji. Check twitter pager to verify.")

        # Deletes most recent tweet
        def DeleteTweet():
            tweet = api.GetUserTimeline(screen_name ='umubaseball', count=1)
            returnedTweet = [i.AsDict() for i in tweet]
            api.DestroyStatus(returnedTweet[0]['id'])

        # Button
        checkTweet = tk.Button(self, text='Check Tweet', command=LastTweet, bg='white', bd=0, width=30, height=5, fg='#542A6D')
        deleteTweet = tk.Button(self, text='Delete Tweet', command=DeleteTweet, bg='white', bd=0, width=30, height=5, fg='#542A6D')

        # Label
        latestTweetLabel = tk.Label(self, text='Press Check Tweet to see latest tweet', bg='white', fg='#542A6D', 
                                    wraplength=750, font=('Helvetica', 20), width=60, height=15)
        
        # Placement
        latestTweetLabel.place(x=50, y=120)

        checkTweet.place(x=200, y=600)
        deleteTweet.place(x=525, y=600)

if __name__ == "__main__":
    app = UMUTwitterApp()
    app.geometry("1000x750")
    app.mainloop()