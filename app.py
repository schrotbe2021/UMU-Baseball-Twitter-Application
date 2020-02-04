import Tkinter as tk     # python 2
import tkFont as tkfont  # python 2
import tkFileDialog
from PIL import Image, ImageTk
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
        for F in (VerifyAccount, ChooseTweet, StartGame, ScoringChange, HomePage, EndGame, SubPage, Lineup, CustomTweet, TweetSentCheck):
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

        def FilePicker():
            filename = tkFileDialog.askopenfilename(initialdir = "./images", title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            img = Image.open(filename)
            img = img.resize((300, 250), Image.ANTIALIAS)
            tkImage = ImageTk.PhotoImage(img)
            displayImg = tk.Label(self, image = tkImage)
            displayImg.image = tkImage
            displayImg.place(x=50, y=200)
        
        filePickerButton = tk.Button(self, text='Choose File', command=FilePicker)
        filePickerButton.place(x=100, y=10)
        
        button3 = tk.Button(self, text="Home Page", bd=0, bg='white',
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
        logo = Image.open(path)
        logo = logo.resize((150, 100), Image.ANTIALIAS)
        self.logoPhoto = ImageTk.PhotoImage(logo)
        canvas.create_image(0, -5, image=self.logoPhoto, anchor="nw")

        # Vertical Bar
        canvas.create_line(150, 10, 150, 90, fill='white')
        
        # Header Label
        chooseTweetLabel = tk.Label(self, text='Live Tweet In-Game @umubaseball', bg='#542A6D', fg='white', font=('Industry Inc Base', 25))
        chooseTweetLabel.place(x=175, y=30)

        startGameButton = tk.Button(self, text="Start Game", bd=0, fg='#542A6D',font=('Helvetica',40), width=9, height= 4, bg='white',
                            command=lambda: controller.show_frame("StartGame"))
                            
        scoringChangeButton = tk.Button(self, text="Scoring\nChange", bd=0, fg='#542A6D',font=('Helvetica',40), width=9, height= 4, bg='white',
                            command=lambda: controller.show_frame("ScoringChange"))

        endGameButton = tk.Button(self, text="End Game", bd=0, fg='#542A6D',font=('Helvetica',40), width=9, height= 4, bg='white',
                            command=lambda: controller.show_frame("EndGame"))

        subButton = tk.Button(self, text="Substitute", bd=0, fg='#542A6D',font=('Helvetica',40), width=9, height= 4, bg='white',
                            command=lambda: controller.show_frame("SubPage"))
        
        customButton = tk.Button(self, text='Custom\nTweet', bd=0, fg='#542A6D',font=('Helvetica',40), width=9, height= 4, bg='white', 
                            command=lambda: controller.show_frame("CustomTweet"))
        
        homeButton = tk.Button(self, text='Home', bg='white', bd=0, width=15, height=3, fg='#542A6D',
                           command=lambda: controller.show_frame("HomePage"))

        lineupButton = tk.Button(self, text="Lineup", bd=0, fg='#542A6D',font=('Helvetica',40), width=9, height= 4, bg='white',
                            command=lambda: controller.show_frame('Lineup'))

        yValue = 200
        
        customButton.place(x=675, y=400)
        homeButton.place(x=825, y=18)
        startGameButton.place(x=25, y=120)
        scoringChangeButton.place(x=675, y=120)
        subButton.place(x=350, y=400)
        endGameButton.place(x=25, y=400)
        lineupButton.place(x=350, y=120)

class SubPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Page Setup
        label = tk.Label(self, text="Substitute", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        homeButton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("HomePage"))
        backButton = tk.Button(self, text="<-- Back",
                            command=lambda: controller.show_frame("ChooseTweet"))

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
            filename = tkFileDialog.askopenfilename(initialdir = "./images/Roster", title = "Select photo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

            # Tweet with photo
            api.PostUpdate(TweetType(), media=filename)

            self.controller.show_frame("TweetSentCheck")

        #Button
        sendTweet = tk.Button(self, text="Send Tweet", command=SubstitutionTweet)

        # Radio Button
        subType = tk.StringVar(self)
        pitchingSub = tk.Radiobutton(self, text="Pitching Substitution", variable=subType, value="Pitching Substitution")
        pinchHit = tk.Radiobutton(self, text="Pinch Hit", variable=subType, value="Pinch Hit")

        # Label
        subInLabel = tk.Label(self, text="Player:")
        subOutLabel = tk.Label(self, text="Subbing for:")
        inningLabel = tk.Label(self, text="Inning:")
        subTypeLabel = tk.Label(self, text="Substitution type:")

        #Entry
        subInEntry = tk.Entry(self, width=25)
        subOutEntry = tk.Entry(self, width=25)
        inningEntry = tk.Entry(self, width=25)

        # Placements
        subInLabel.place(x=150, y=150)
        subOutLabel.place(x=450, y=150)
        inningLabel.place(x=150, y=175)
        subTypeLabel.place(x=150, y=125)

        subInEntry.place(x=225, y=150)
        subOutEntry.place(x=550, y=150)
        inningEntry.place(x=225, y=175)

        pitchingSub.place(x=275, y=125)
        pinchHit.place(x=450, y=125)

        sendTweet.place(x=300, y=300)
        backButton.place(x=50, y=45)
        homeButton.place(x=150, y=45)


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
            # Pick photo for tweet in dialog
            filename = tkFileDialog.askopenfilename(initialdir = "./images/StartGame", title = "Select photo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            
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
        sendTweetButton = tk.Button(self, text="Send Tweet", command=StartGameTweet)
        #imagePickerButton = tk.Button(self, text"Choose Media...", )

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

        # Page Setup
        label = tk.Label(self, text="Scoring Change Game", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        homeButton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("HomePage"))
        backButton = tk.Button(self, text="<-- Back",
                            command=lambda: controller.show_frame("ChooseTweet"))

        def WhoScored():
            if whoScored.get() == str('Mount Union'):
                return (playerNameEntry.get() + ' brings in ' + numRunsEntry.get() + ' runs with a ' 
                + hitType.get() + ' in the ' + inningEntry.get() + ' inning.\n\n')
            else :
                return (opponentEntry.get() + ' scores ' + numRunsEntry.get() + ' with a '
                + hitType.get() + ' in the ' + inningEntry.get() + ' inning.\n\n')

        def ScoringChangeTweet():
            # Pick photo for tweet in dialog
            filename = tkFileDialog.askopenfilename(initialdir = "./images/Roster", title = "Select photo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

            # Tweet with photo
            status = api.PostUpdate(WhoScored()
                + 'Mount Union - ' + mountScoreEntry.get() + '\n'
                + opponentEntry.get() + ' - ' + opponentScoreEntry.get() + '\n\n'
                + '#UMUBaseball2020 | #D3Baseball', media=filename)

            self.controller.show_frame("TweetSentCheck")

        # Buttons
        sendTweetButton = tk.Button(self, text='Send Tweet', command=ScoringChangeTweet)

        # Radio Button
        whoScored = tk.StringVar(self)
        mountScoredRB = tk.Radiobutton(self, text="Mount Union", variable=whoScored, value="Mount Union")
        opponentScoredRB = tk.Radiobutton(self, text="Opponent", variable=whoScored, value="Opponent")

        # Option Menus
        hitType = tk.StringVar(self)
        hitType.set('Hit Type...')
        hitTypeMenu = tk.OptionMenu(self, hitType, 'single', 'double', 'triple', 'home run', 'walk')

        # Labels
        playerNameLabel = tk.Label(self, text='Player Name:')
        numRunsLabel = tk.Label(self, text='# of Runs:')
        inningLabel = tk.Label(self, text='Inning:')
        hitTypeLabel = tk.Label(self, text='Hit Type:')
        mountScoreLabel = tk.Label(self ,text='UMU Score:')
        opponentLabel = tk.Label(self, text='Opponent:')
        opponentScoreLabel = tk.Label(self, text='Opponent Score:')
        whoScoredLabel = tk.Label(self, text='Who Scored?')


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

        mountScoredRB.place(x=250, y=125)
        opponentScoredRB.place(x=350, y=125)

        sendTweetButton.place(x=400, y=400)
        backButton.place(x=50, y=45)
        homeButton.place(x=150, y=45)

class EndGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Page Setup
        label = tk.Label(self, text="End Game", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        homeButton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("HomePage"))
        backButton = tk.Button(self, text="<-- Back",
                            command=lambda: controller.show_frame("ChooseTweet"))

        def WhoWon():
            if whoWon.get() == 'Mount Union':
                return ('Mount Union defeats ' + opponentEntry.get() + '.\n\n')
            else:
                return (opponentEntry.get() + ' defeats Mount Union.\n\n')

        def EndGameTweet():
            
            # Pick photo for tweet in dialog only if Mount wins.
            if whoWon.get() == 'Mount Union':
                filename = tkFileDialog.askopenfilename(initialdir = "./images/EndGame", title = "Select photo",filetypes = (("all files","*.*"), ("jpeg files","*.jpg")))
            else:
                filename = ''

            # Tweet with photo
            api.PostUpdate(WhoWon() 
                            + 'Mount Union - ' + mountScoreEntry.get() + '\n'
                            + opponentEntry.get() + ' - ' + opponentScoreEntry.get() + '\n\n'
                            + '#UMUBaseball2020 | #D3Baseball', media=filename)
            
            self.controller.show_frame("TweetSentCheck")

        # Button
        sendTweet = tk.Button(self, text='Send Tweet', command=EndGameTweet)

        # Radio Button
        whoWon = tk.StringVar(self)
        mountWin = tk.Radiobutton(self, text='Mount Union', variable=whoWon, value='Mount Union')
        opponentWin = tk.Radiobutton(self, text='Opponent', variable=whoWon, value='Opponent')

        # Label
        opponentLabel = tk.Label(self, text="Opponent:")
        mountRecordLabel = tk.Label(self, text="Record:")
        mountScoreLabel = tk.Label(self, text="Mount Score:")
        opponentScoreLabel = tk.Label(self, text="Opponent Score:")
        winnerLabel = tk.Label(self, text="Winning Team:")
        
        # Entry
        opponentEntry = tk.Entry(self, width=50)
        mountRecordEntry = tk.Entry(self, width=50)
        mountScoreEntry = tk.Entry(self, width=50)
        opponentScoreEntry = tk.Entry(self, width=50)

        # Placement
        opponentLabel.place(x=150, y=150)
        mountRecordLabel.place(x=150, y=175)
        mountScoreLabel.place(x=150, y=200)
        opponentScoreLabel.place(x=150, y=225)
        winnerLabel.place(x=150, y=125)

        opponentEntry.place(x=250, y=150)
        mountRecordEntry.place(x=250, y=175)
        mountScoreEntry.place(x=250, y=200)
        opponentScoreEntry.place(x=250, y=225)

        mountWin.place(x=200, y=125)
        opponentWin.place(x=300, y=125)

        sendTweet.place(x=200, y=300)
        backButton.place(x=50, y=45)
        homeButton.place(x=150, y=45)

class Lineup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Page Setup
        label = tk.Label(self, text="Lineup", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        homeButton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("HomePage"))
        backButton = tk.Button(self, text="<-- Back",
                            command=lambda: controller.show_frame("ChooseTweet"))


        # Arrays to set up label and entries widgets for lineup and position
        lineup = ['1:', '2:', '3:', '4:', '5:', '6:', '7:', '8:', '9:', 'P:']
        lineUpEntry = []
        posOptionArray = []

        yLabel = 150  # Control for yPos of widget
        # For loop to instantiate and place labels and entries for lineup tweet
        for i in range(len(lineup)):
            yLabel += 25 # Increments yPos to display widgets correctly

            # Widget to be placed through each iteration
            label = tk.Label(self, text=lineup[i])
            entry = tk.Entry(self, width = 20)

            posOption = tk.StringVar(self)
            posOption.set('Position...')
            posOpMenu = tk.OptionMenu(self, posOption, 'C', '1B', '2B', 'SS', '3B', 'LF', 'CF', 'RF', 'DH', 'P')
            posOpMenu.config(width=10)

            # Placement of widget through each iteration
            entry.place(x=175, y=yLabel)
            label.place(x=150, y=yLabel)
            posOpMenu.place(x=375, y=yLabel)

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

        def LineupTweet():
            # Pick photo for tweet in dialog
            filename = tkFileDialog.askopenfilename(initialdir = "./images/StartGame", title = "Select photo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

            # Tweet with photo
            api.PostUpdate('Lineup for today\'s game against ' + opponentEntry.get() + '\n\n' 
            + PlayerString() + '\n\n'
            + '#UMUBaseball2020 | #D3Baseball', media=filename)

            self.controller.show_frame("TweetSentCheck")


        # Button
        sendTweetButton = tk.Button(self, text='Send Tweet', command=LineupTweet)


        # Label
        opponentLabel = tk.Label(self, text='Opponent:')   

        # Entry
        opponentEntry = tk.Entry(self, width=50)

        # Placement
        opponentLabel.place(x=150, y= 150)

        opponentEntry.place(x=250, y=150)    

        sendTweetButton.place(x=200, y=500)
        backButton.place(x=50, y=45)
        homeButton.place(x=150, y=45)

class CustomTweet(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Page Setup
        label = tk.Label(self, text="Lineup", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        homeButton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("HomePage"))
        backButton = tk.Button(self, text="<-- Back",
                            command=lambda: controller.show_frame("ChooseTweet"))

        # Get input for tweet
        def GetTextInput():
            result = inputTextField.get('1.0', 'end-1c')
            return result
        
        def Custom():
            # Pick photo for tweet in dialog
            if mediaOption.get() == 'Yes':
                filename = tkFileDialog.askopenfilename(initialdir = "./images/StartGame", title = "Select photo",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            else:
                filename = ''
            
            # Tweet for custom input
            api.PostUpdate(GetTextInput() 
                          + '\n\n#UMUBaseball2020 | #D3Baseball', media=filename)

            inputTextField.delete('1.0', 'end-1c')
            self.controller.show_frame("TweetSentCheck")

        # Label
        mediaLabel = tk.Label(self, text='Include media?')

        # Radio Button
        mediaOption = tk.StringVar(self)
        yesMedia = tk.Radiobutton(self, text='Yes', variable=mediaOption, value='Yes')
        noMedia = tk.Radiobutton(self, text='No', variable=mediaOption, value='No')

        # Text Field
        inputTextField = tk.Text(self, width=50, height=25, wrap="word")

        # Button
        sendTweetButton = tk.Button(self, text='Send Tweet', command=Custom)

        # Placement
        mediaLabel.place(x=150, y=150)

        yesMedia.place(x=250, y=150)
        noMedia.place(x=350, y=150)

        inputTextField.place(x=50, y=250)

        sendTweetButton.place(x=400, y=250)
        backButton.place(x=50, y=45)
        homeButton.place(x=150, y=45)

class TweetSentCheck(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Page Setup
        label = tk.Label(self, text="Lineup", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        homeButton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("HomePage"))
        backButton = tk.Button(self, text="<-- Back",
                            command=lambda: controller.show_frame("ChooseTweet"))

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
        checkTweet = tk.Button(self, text='Check Tweet', command=LastTweet)
        deleteTweet = tk.Button(self, text='Delete Tweet', command=DeleteTweet)

        # Label
        latestTweetLabel = tk.Label(self, text='Press Check Tweet to see latest tweet')
        
        # Placement
        latestTweetLabel.place(x=150, y=150)

        deleteTweet.place(x=200, y=450)
        checkTweet.place(x=150, y=450)
        backButton.place(x=50, y=45)
        homeButton.place(x=150, y=45)

if __name__ == "__main__":
    app = UMUTwitterApp()
    app.geometry("1000x750")
    app.mainloop()