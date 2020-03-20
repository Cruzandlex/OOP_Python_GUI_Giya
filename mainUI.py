import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class dashboardUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'GIYA - Customers UI'
        self.x = 50
        self.y = 40
        self.width = 1270
        self.height = 680
        self.Icon = "appLogoico.png"
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon(self.Icon))
        self.imagePath = ""

        #dictionary
        self.userData = {"username":"Zandlex","password":"admin","role":"U","msg": ["hello",'hi'],"pending":{"festival":{"name":"","loc":"","date":"","image":"0"},"tourGuide":{"name":"","loc":"","rating":"0"}},'name':"Zandlex Keano M. Cruz","age":"19","sex":
                        "Male","Location":"Marikina City, Metro Manila, Philippines","EmailAd":"Qzkmcruz@tip.edu.ph","started":"March 20, 2020","FavoriteLoc":"REGION V","TotalTours":"0","contact":"09560594126","aboutme":"I have no bio data yet to show the people",
                        "membership":'1'}

        self.Festivals = {'1':{"name":"Masimbo Festival","date":"March 10-12","location":"Puerto Galera","info":"Established in 2011, Malasimbo Music and Arts festival serves as a venue for the indigenous people of Mindoro to showcase their culture and art. Above the idea of fun and partying, the festival is and will always be a celebration of and for the Mangyans."},
                          '2':{"name":"Katalingkasan Festival","date":"March 22","location":"Albay","info":"The festivity held every 2nd week of July in Libon retraces the valiant story of the virgins of the town who worked hard in making Libon as one of the earliest settlements in Albay. Featured activities are trade fairs, shows, and street dancing"},
                          '3':{"name":"Island of the Garden City of Samal Festival","date":"March 10-12","location":"Samal","info":"This week-long festivals in celebration of the founding anniversary of Island Garden City of Samal. The festival showcases the island's natural endowments and its people's culture."},
                          '4':{"name":"Anibina Bulawanun Festival","date":"March 7","location":"Nabunturan","info":"This week-long festivals in celebration of the founding anniversary of Island Garden City of Samal. The festival showcases the island's natural endowments and its people's culture."},
                          '5':{"name":"Holy Week","date":"April 9","location":"San Agustin Church","info":"The Anibina Bulawanon Festival celebrates the bountiful gold harvest and the founding anniversary of Compostela Province. Compostela Valley is known for its rich gold deposits. The festival is held during the first week of March in the municipality of Nabunturan."},
                          '6':{"name":"Mariones Festival","date":"April 10","location":"Marinduque","info":"Holy Week, in the Christian church, the week between Palm Sunday and Easter, observed with special solemnity as a time of devotion to the Passion of Jesus Christ. In the Greek and Roman liturgical books, it is called the Great Week because great deeds were done by God during this week."},
                          '7':{"name":"Centurion Festival","date":"April 11","location":"Marinduque","info":"This is a folk-religious festival that re-enacts the story of Saint Longinus, a Roman centurion who was blind in one eye. The festival is characterized by colorful Roman costumes, painted masks and helmets, and brightly colored tunics"},
                          '8':{"name":"Ang Pagtatatal","date":"April 15","location":"Guimaras ","info":"Ang Pagtaltal is a holy Lenten presentation staged on the hillside of Jordan every Good Friday, patterned to Oberammergau in Southern Bavaria, Germany. It is the final act of the play when Jesus was taken off from the cross and laid on his mother's lap"},
                          '9':{"name":"Pangalap Ritual ","date":"April 18","location":"Valencia","info":"This is not a festival per se but an interesting ceremony in which believers crawl through Catilaran Cave as they chant various prayers. The ritual is believed to give participants supernatural powers that help protect them against malevolent spirits."},
                          '10':{"name":"Witches Festival","date":"April 19","location":"Siquijor","info":"Siquijor is best known as the land of witchcraft. During the Witches Festivals, sorcerers or mambabarang gather at Crocodile Hill during the full moon to collect herbs, roots and live insects which they throw into enormous cauldrons filled with boiling water. They sit around this concoction while chanting incantations. The festival culminates in dancing and a restricted ritual in an isolated cave at dawn."},
                          }

        self.FestivalPath = {'0':"none.jpg",'1':"Festival Images\AMalasimbo.jpg",'2':"Festival Images\BKatalingkasan.jpg",'3':"Festival Images\CSamal.jpg",
                           '4':"Festival Images\DAnibina Bulawanun.jpg",'5':"Festival Images\EHolyWeek.jpg","6":"Festival Images\FMariones Festival.jpg",
                           '7':"Festival Images\GCenturion.jpg",'8':"Festival Images\HAngPagtataral.jpg",'9':"Festival Images\IPangalap Ritual.jpg",'10':"Festival Images\JWitches.jpg"}
        
        self.tourGuide = { '1':{"name":"Joselito Tanyag","region":"National Capital Region","skills":"A great listener\nA great photographer\nEmphatic\nFluent English","ratings":'4',"package":"The tour will commence with a single minivan which will service you to the venue, the venue will be a hotel in puerto galera with 3 bedrooms for 3-5 persons, During the day you will be toured around several music entertainment by locals","price":"5500.00 php",},
                                '2':{"name":"Federico Cortez","region":"Region 4A - Calabarzon","skills":"A great entertainer\nComedian\nGood english","ratings":'5',"package":"The event will tour you all around albay to see the festivals and the different shows around albay, the tour package includes the food which is the speciality of albay as well. The tour covers 2-3 person","price":"2000.00 php"},
                                '3':{"name":"Mark Gutierrez","region":"Region 4B - Mimaropa","skills":"A great storyteller\nHas a good english accent\nCan translate dialects such such as bisaya","ratings":'5',"package":"The tour will guide up to 5 person to a hotel on the Garden City, this hotel will provide you a room for 3 days and during the day you will be toured around the garden city and the festival","price":"7600.00 php"},
                                '4':{"name":"Alex Del Rosario","region":"CAR- Cordillera Administrative Region","skills":"Good entertainer\nCan speak tagalog and bisaya","ratings":'3',"package":"2-3 person will be driven to Nabarutan where you will get toured around the festival ongoing through the whole area, The driver will tour you to several tourist spots in the local area","price":"2700.00 php"},
                                '5':{"name":"Christian Felipe","region":"Region V - Bicol","skills":"Very religous\nGood preacher\nPhilosopher","ratings":'3',"package":"The tour for two will get you around san agustin church to tour you around history of the venue and its relation to the holy week and its origin.","price":"1400.00 php"},
                                '6':{"name":"Nathaniel Aquino","region":"Region 4B - Mimaropa","skills":"Great entertainer\nActive\nFluent Tagalog and Ilocano","ratings":'4',"package":"The tour guide will show you around the places of marinduque after the procession, the tour will cover for two persons","price":"1700.00 php"},
                                '7':{"name":"James Mendoza","region":"National Capital Region", "skills":"Can speak bikolano and bisaya\nGreat storyteller\nActive","ratings":'5',"package":"After the roman themed festival, up to 2 will get a chance to travel around the great city of mariduque for a day,","price":"1300.00 php"},
                                '8':{"name":"Daniel Mendoza","region":"Region 3 - Central Luzon","skills":"Humorous\nGood speaker\nFluet tagalog\nEnergetic","ratings":'5',"package":"2-3 person will get a chance to see famous plays about jesus. Afterwards will go around town to explore some famous tourist spots.","price":"2000.00 php"},
                                '9':{"name":"Jacob Perez","region":"Region 4A - Calabarzon", "skills":"Can speak fluent english\nHumorous ","ratings":'4',"package":"The tour will include a mysterious ritual said to give protection to the people from bad spirits. The tour involves going around the town of velencia for 2 persons max","price":"1250.00 php"},
                                '10':{"name":"John-Mark Ramos","region":"National Capital Region","skills":"Creative entertainer\nGood at locations\nInformation oriented","ratings":'5',"package":"The festival themed by the sorcery. You will experience a haunting diner for 2 at a witch themed couldron restaurant. Afterward you will get to be toured around a town full of witch themed amusement", "price":"4570.00 php"}}
        self.initUI()
        self.menuBar() 
        self.dashboardPage()
        self.show()

    def initUI(self):
        self.backgroudTaskbar = QLabel(self)
        self.backgroudTaskbar.setStyleSheet("background-color:#494F5B;border: 0px 1px 0px 0px outset #666e7f")
        self.backgroudTaskbar.setGeometry(0,0,100,680)
        self.lineTaskbar1 = QLabel(self)
        self.lineTaskbar1.setStyleSheet("background-color:#2d3139")
        self.lineTaskbar1.setGeometry(0,60,100,2)
        self.backgroudLogo = QLabel(self)
        self.backgroudLogo.setStyleSheet("background-color:#d5d7dd")
        self.backgroudLogo.setGeometry(0,0,100,60)
        self.lineTaskbar = QLabel(self)
        self.lineTaskbar.setStyleSheet("background-color:#aaafbb")
        self.lineTaskbar.setGeometry(100,60,1280,2)
        self.backgroudBar = QLabel(self)
        self.backgroudBar.setStyleSheet("background-color:#f1f2f4;border: 1px outset #c6cad2")
        self.backgroudBar.setGeometry(100,0,1100,60)
        self.backgroundCurrentPage = QLabel(self)
        self.backgroundCurrentPage.setStyleSheet("background-color:#A9A9A9")
        self.backgroundCurrentPage.setGeometry(0,90,100,95)
        self.logo = QLabel(self)
        self.logo.resize(50,50)
        self.logo.move(22,5)
        self.pixmap = QPixmap(self.Icon)
        self.logo.setPixmap(QPixmap(self.pixmap))
        self.logo.setScaledContents(True)

        #Taskbar Buttons
        #Dashboard Page
        self.button1 = QPushButton("", self)
        self.button1.setIcon(QIcon("dashboardico.png"))
        self.button1.setToolTip("Go to your DASHBOARD.")
        self.button1.setIconSize(QSize(60,60))
        self.button1.setGeometry(14,90,70,70)
        self.button1.setStyleSheet("background-color:transparent")
        #self.button3.clicked.connect(self.dashboardPage)
        self.textbox1 = QLabel("DASHBOARD", self)
        self.textbox1.setStyleSheet("font-family:arial;font-weight:bold;color:#F5F5F5")
        self.textbox1.move(16,160)

        #About Us Page
        self.button2 = QPushButton("", self)
        self.button2.setIcon(QIcon("aboutUsico.png"))
        self.button2.setToolTip("Know About Us.")
        self.button2.setIconSize(QSize(45,45))
        self.button2.setGeometry(25,500,50,50)
        self.button2.setStyleSheet("background-color:transparent")
        #self.button4.clicked.connect(self.aboutUsPage)
        self.textbox2 = QLabel("ABOUT US", self)
        self.textbox2.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox2.move(22,560)

        #Profile
        self.button3 = QPushButton("", self)
        self.button3.clicked.connect(self.profilePage)
        self.button3.setIcon(QIcon("profilePageico.png"))
        self.button3.setToolTip("Go to your Profile")
        self.button3.setIconSize(QSize(70,70))
        self.button3.setGeometry(10,195,80,80)
        self.button3.setStyleSheet("background-color:transparent")
        self.textbox3 = QLabel("PROFILE", self)
        self.textbox3.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox3.move(27,275)

        #History Events
        self.button4 = QPushButton("", self)
        self.button4.clicked.connect(self.activitiesPage)
        self.button4.setIcon(QIcon("historyEvents.png"))
        self.button4.setToolTip("Go to your Profile")
        self.button4.setIconSize(QSize(50,50))
        self.button4.setGeometry(20,315,60,60)
        self.button4.setStyleSheet("background-color:transparent")
        self.textbox3 = QLabel("ACTIVITIES", self)
        self.textbox3.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox3.move(20,380)

        #Sign Out 
        self.button5 = QPushButton("SIGN OUT", self)
        self.button5.setIcon(QIcon("signOutico.png"))
        self.button5.setToolTip("Sign Out.")
        self.button5.setIconSize(QSize(30,30))
        self.button5.move(3,620)
        self.button5.resize(90,30)
        self.button5.setStyleSheet("background-color:transparent;color:white")
        #self.button5.clicked.connect(self.signOut)

    def menuBar(self):
        self.textDash = QLabel("Dashboard", self)
        self.textDash.setGeometry(130,18,300,25)
        self.textDash.setStyleSheet("font-family:century gothic;font-size:24px")
        self.taskBarButton = QPushButton("", self)
        self.taskBarButton.setIcon(QIcon("taskBar.png"))
        self.taskBarButton.setIconSize(QSize(30,30))
        self.taskBarButton.setGeometry(270,12,40,40)
        self.taskBarButton.setStyleSheet("background-color:transparent")
        self.buttonPic = QPushButton("", self)
        self.buttonPic.setIcon(QIcon("uploadImageico.ico"))
        self.buttonPic.setIconSize(QSize(70,50))
        self.buttonPic.setGeometry(1200,0,70,60)
        self.buttonPic.setStyleSheet("background-color:transparent")
        self.label = QLabel(self)
        self.label.setGeometry(1200,0,70,60)
        self.textboxUsername = QLabel(self.userData['username'], self)
        self.textboxUsername.setGeometry(1095,30,100,20)
        self.textboxUsername.setStyleSheet("font-family:arial;font-weight:bold;font-size:14px;qproperty-alignment:AlignRight")
        self.textboxUsername1 = QLabel("Welcome to GIYA,", self)
        self.textboxUsername1.move(1110,10)
    
    def dashboardPage(self):
        #profile picture 
        self.buttonProfPic = QPushButton("", self)
        self.buttonProfPic.setIcon(QIcon("uploadImageico.ico"))
        self.buttonProfPic.setIconSize(QSize(130,130))
        self.buttonProfPic.resize(140,140)
        self.buttonProfPic.move(130,80)
        '''
        self.buttonUploadPic2 = QPushButton("Upload image", self)
        self.buttonUploadPic2.resize(120,25)
        self.buttonUploadPic2.move(140,200)
        self.buttonProfPic.clicked.connect(self.uploadProfilePic)
        self.buttonUploadPic2.clicked.connect(self.uploadProfilePic)
        '''
        self.label = QLabel(self)
        self.label.setGeometry(130,80,140,140)

        #profile details
        self.prfName = QLabel(self.userData['name'], self)
        self.prfName.resize(300,28)
        self.prfName.move(290,88)
        self.prfName.setStyleSheet("font-family:arial;font:bold;font-size:26px")
        self.prfEmail = QLabel(self.userData['EmailAd'], self)
        self.prfEmail.resize(300,17)
        self.prfEmail.move(290,118)
        self.prfEmail.setStyleSheet("font-family:arial;font-size:14px")
        self.prfLocation = QLabel(self.userData['Location'], self)
        self.prfLocation.resize(300,17)
        self.prfLocation.move(290,143)
        self.prfLocation.setStyleSheet("font-family:arial;font-size:14px")
        self.prfBio = QLabel(self.userData['aboutme'], self)
        self.prfBio.setGeometry(290,150,380,80)
        self.prfBio.setStyleSheet("font-family:arial;font-size:14px;text-align")
        self.prfBio.setWordWrap(True)

        #recent Activities
        self.dashActivities = QLabel(self)
        self.dashActivities.setStyleSheet("background-color:#F8F8FF;border-style:outset;border-width:1px;border-color:#DCDCDC;border-radius:20px")
        self.dashActivities.setGeometry(120,250,550,200)
        self.lineDashAct = QLabel(self)
        self.lineDashAct.setStyleSheet("background-color:#aaafbb")
        self.lineDashAct.setGeometry(120,305,550,2)
        self.dashActIcon = QLabel(self)
        self.dashActIcon.setPixmap(QPixmap("upcomingActs.png"))
        self.dashActIcon.setGeometry(130,260,40,40)
        self.dashActIcon.setScaledContents(True)
        self.dashActText = QLabel("Upcoming Event", self)
        self.dashActText.setGeometry(180,268,400,20)
        self.dashActText.setStyleSheet("font-family:Arial;font-weight:bold;font-size:16px")

        self.imageFest = QLabel(self)
        self.imageFest.setStyleSheet("background-color:#F8F8FF;border-style:outset;border-width:1px;border-color:#DCDCDC;border-radius:20px")
        self.imageFest.setGeometry(425,310,230,135)
        self.read()
        festImg = self.FestivalPath[f"{self.value2}"]
        self.userData['pending']['festival']['image'] = str(festImg)
        self.imageFest.setPixmap(QPixmap(self.userData['pending']['festival']['image']))
        self.imageFest.setScaledContents(True)
        self.nameOfFestIcon = QLabel(self)
        self.nameOfFestIcon.setGeometry(130,310,40,40)
        self.nameOfFestIcon.setPixmap(QPixmap("festivalName.png"))
        self.nameOfFestIcon.setScaledContents(True)
        festName = self.Festivals[f"{self.value2}"]['name']
        self.userData['pending']['festival']['name'] = str(festName)
        self.nameOfFest = QLabel(self.userData['pending']['festival']['name'], self)
        self.nameOfFest.setGeometry(180,320,200,20)
        self.nameOfFest.setStyleSheet("font-family:Arial;font-weight:bold;font-size:16px")
        self.locOfFestIcom = QLabel(self)
        self.locOfFestIcom.setGeometry(130,355,40,40)
        self.locOfFestIcom.setPixmap(QPixmap("festivalLoc.png"))
        self.locOfFestIcom.setScaledContents(True)
        festLoc = self.Festivals[f"{self.value2}"]['location']
        self.userData['pending']['festival']['loc'] = str(festLoc)
        self.locOfFest = QLabel(self.userData['pending']['festival']['loc'], self)
        self.locOfFest.setGeometry(180,365,200,20)
        self.locOfFest.setStyleSheet("font-family:Arial;font-weight:bold;font-size:16px")
        self.dateOfFestIcon = QLabel(self)
        self.dateOfFestIcon.setGeometry(130,400,40,40)
        self.dateOfFestIcon.setPixmap(QPixmap("festivalDate.png"))
        self.dateOfFestIcon.setScaledContents(True)
        festDate = self.Festivals[f"{self.value2}"]['date']
        self.userData['pending']['festival']['date'] = str(festDate)
        self.dateOfFest = QLabel(self.userData['pending']['festival']['date'], self)
        self.dateOfFest.setGeometry(180,410,200,20)
        self.dateOfFest.setStyleSheet("font-family:Arial;font-weight:bold;font-size:16px")

        self.dashActivities2 = QLabel(self)
        self.dashActivities2.setStyleSheet("background-color:#F8F8FF;border-style:outset;border-width:1px;border-color:#DCDCDC;border-radius:20px")
        self.dashActivities2.setGeometry(120,470,550,200)
        self.lineDashAct2 = QLabel(self)
        self.lineDashAct2.setStyleSheet("background-color:#aaafbb")
        self.lineDashAct2.setGeometry(120,525,550,2)
        self.dashActIcon2 = QLabel(self)
        self.dashActIcon2.setPixmap(QPixmap("tourGuide.png"))
        self.dashActIcon2.setGeometry(130,480,50,40)
        self.dashActIcon2.setScaledContents(True)
        self.dashActText2 = QLabel("Your Tourguide", self)
        self.dashActText2.setGeometry(185,490,400,20)
        self.dashActText2.setStyleSheet("font-family:Arial;font-weight:bold;font-size:16px")

        self.tourGImage = QLabel(self)
        self.tourGImage.setStyleSheet("background-color:#F8F8FF;border-style:solid;border-width:3px;border-color:#DCDCDC")
        self.tourGImage.setGeometry(135,535,125,125)
        self.tourGImage.setPixmap(QPixmap("tourGprofile.png"))
        self.tourGImage.setScaledContents(True)
        tourGname1 = self.tourGuide[f"{self.value2}"]['name']
        self.userData['pending']['tourGuide']['name'] = tourGname1
        self.tourGname = QLabel(self.userData['pending']['tourGuide']['name'], self)
        self.tourGname.setGeometry(280,550,200,20)
        self.tourGname.setStyleSheet("font-family:Arial;font-weight:bold;font-size:16px")
        tourGlocale1 = self.tourGuide[f"{self.value2}"]['region']
        self.userData['pending']['tourGuide']['loc'] = str(tourGlocale1)
        self.tourGlocale = QLabel(self.userData['pending']['tourGuide']['loc'], self)
        self.tourGlocale.setGeometry(280,580,220,20)
        self.tourGlocale.setStyleSheet("font-family:Arial;font-weight:bold;font-size:16px")
        self.tourGratings = QLabel("RATINGS:", self)
        self.tourGratings.setGeometry(280,620,220,20)
        self.tourGratings.setStyleSheet("font-family:Arial;font-weight:bold;font-size:16px")
        self.StarBlack = QPixmap("StarBlack.png")
        self.StarYellow = QPixmap("StarYellow.png")
        tourGratings1 = self.tourGuide[f"{self.value2}"]['ratings']
        self.userData['pending']['tourGuide']['rating'] = tourGratings1
        self.tgRatings = int(self.userData['pending']['tourGuide']['rating'])
        if  self.tgRatings == 1:
            self.Rating1 = QLabel(self) 
            self.Rating1.setScaledContents(True)
            self.Rating1.setGeometry(363,612,35,35)
            self.Rating1.setPixmap(self.StarYellow)
            self.Rating2 = QLabel(self)
            self.Rating2.setScaledContents(True)
            self.Rating2.setGeometry(403,612,35,35)
            self.Rating2.setPixmap(self.StarBlack)
            self.Rating3 = QLabel(self)
            self.Rating3.setScaledContents(True)
            self.Rating3.setGeometry(443,612,35,35)
            self.Rating3.setPixmap(self.StarBlack)
            self.Rating4 = QLabel(self)
            self.Rating4.setScaledContents(True)
            self.Rating4.setGeometry(483,612,35,35)
            self.Rating4.setPixmap(self.StarBlack)
            self.Rating5 = QLabel(self)
            self.Rating5.setScaledContents(True)
            self.Rating5.setGeometry(524,612,35,35)
            self.Rating5.setPixmap(self.StarBlack)
        elif self.tgRatings == 2:
            self.Rating1 = QLabel(self) 
            self.Rating1.setScaledContents(True)
            self.Rating1.setGeometry(363,612,35,35)
            self.Rating1.setPixmap(self.StarYellow)
            self.Rating2 = QLabel(self)
            self.Rating2.setScaledContents(True)
            self.Rating2.setGeometry(403,612,35,35)
            self.Rating2.setPixmap(self.StarYellow)
            self.Rating3 = QLabel(self)
            self.Rating3.setScaledContents(True)
            self.Rating3.setGeometry(443,612,35,35)
            self.Rating3.setPixmap(self.StarBlack)
            self.Rating4 = QLabel(self)
            self.Rating4.setScaledContents(True)
            self.Rating4.setGeometry(483,612,35,35)
            self.Rating4.setPixmap(self.StarBlack)
            self.Rating5 = QLabel(self)
            self.Rating5.setScaledContents(True)
            self.Rating5.setGeometry(524,612,35,35)
            self.Rating5.setPixmap(self.StarBlack)
        elif self.tgRatings == 3:
            self.Rating1 = QLabel(self) 
            self.Rating1.setScaledContents(True)
            self.Rating1.setGeometry(363,612,35,35)
            self.Rating1.setPixmap(self.StarYellow)
            self.Rating2 = QLabel(self)
            self.Rating2.setScaledContents(True)
            self.Rating2.setGeometry(403,612,35,35)
            self.Rating2.setPixmap(self.StarYellow)
            self.Rating3 = QLabel(self)
            self.Rating3.setScaledContents(True)
            self.Rating3.setGeometry(443,612,35,35)
            self.Rating3.setPixmap(self.StarYellow)
            self.Rating4 = QLabel(self)
            self.Rating4.setScaledContents(True)
            self.Rating4.setGeometry(483,612,35,35)
            self.Rating4.setPixmap(self.StarBlack)
            self.Rating5 = QLabel(self)
            self.Rating5.setScaledContents(True)
            self.Rating5.setGeometry(524,612,35,35)
            self.Rating5.setPixmap(self.StarBlack)
        elif self.tgRatings == 4:
            self.Rating1 = QLabel(self) 
            self.Rating1.setScaledContents(True)
            self.Rating1.setGeometry(363,612,35,35)
            self.Rating1.setPixmap(self.StarYellow)
            self.Rating2 = QLabel(self)
            self.Rating2.setScaledContents(True)
            self.Rating2.setGeometry(403,612,35,35)
            self.Rating2.setPixmap(self.StarYellow)
            self.Rating3 = QLabel(self)
            self.Rating3.setScaledContents(True)
            self.Rating3.setGeometry(443,612,35,35)
            self.Rating3.setPixmap(self.StarYellow)
            self.Rating4 = QLabel(self)
            self.Rating4.setScaledContents(True)
            self.Rating4.setGeometry(483,612,35,35)
            self.Rating4.setPixmap(self.StarYellow)
            self.Rating5 = QLabel(self)
            self.Rating5.setScaledContents(True)
            self.Rating5.setGeometry(524,612,35,35)
            self.Rating5.setPixmap(self.StarBlack)
        elif self.tgRatings == 5:
            self.Rating1 = QLabel(self) 
            self.Rating1.setScaledContents(True)
            self.Rating1.setGeometry(363,612,35,35)
            self.Rating1.setPixmap(self.StarYellow)
            self.Rating2 = QLabel(self)
            self.Rating2.setScaledContents(True)
            self.Rating2.setGeometry(403,612,35,35)
            self.Rating2.setPixmap(self.StarYellow)
            self.Rating3 = QLabel(self)
            self.Rating3.setScaledContents(True)
            self.Rating3.setGeometry(443,612,35,35)
            self.Rating3.setPixmap(self.StarYellow)
            self.Rating4 = QLabel(self)
            self.Rating4.setScaledContents(True)
            self.Rating4.setGeometry(483,612,35,35)
            self.Rating4.setPixmap(self.StarYellow)
            self.Rating5 = QLabel(self)
            self.Rating5.setScaledContents(True)
            self.Rating5.setGeometry(524,612,35,35)
            self.Rating5.setPixmap(self.StarYellow)
        else:
            pass

        #festival of the Month
        self.dashFestival = QLabel(self)
        self.dashFestival.setStyleSheet("background-color:#F8F8FF;border-style:outset;border-width:1px;border-color:#DCDCDC;border-radius:20px")
        self.dashFestival.setGeometry(700,250,550,420)
        self.lineDashFest = QLabel(self)
        self.lineDashFest.setStyleSheet("background-color:#aaafbb")
        self.lineDashFest.setGeometry(700,305,550,2)
        self.dashFestIcon = QLabel(self)
        self.dashFestIcon.setPixmap(QPixmap("festivalMonth.png"))
        self.dashFestIcon.setGeometry(710,255,48,48)
        self.dashFestIcon.setScaledContents(True)
        self.dashFestText = QLabel("Festivals of the Month", self)
        self.dashFestText.setGeometry(765,270,400,20)
        self.dashFestText.setStyleSheet("font-family:Arial;font-weight:bold;font-size:16px")

        self.calendarTable = QTableWidget(self)
        self.calendarTable.setRowCount(10)
        self.calendarTable.setColumnCount(3)
        self.calendarTable.setColumnWidth(0,160)
        self.calendarTable.setColumnWidth(1,200)
        self.calendarTable.setColumnWidth(2,170)
        for i in range(10):
            self.calendarTable.setRowHeight(i,50)
        self.calendarTable.setItem(0,0, QTableWidgetItem(self.Festivals['1']['date']+" "+self.Festivals['1']['location']))
        self.calendarTable.setItem(0,1, QTableWidgetItem(self.Festivals['1']['name']))
        self.bookButton1 = QPushButton("BOOK NOW", clicked = lambda:self.BookWindow(value=1))
        self.bookButton1.setStyleSheet("background-color:#7382A0;color:white;border: 10px solid;border-color:transparent;border-radius:15px;font-family:arial;font-weight:bold")
        self.calendarTable.setCellWidget(0,2, self.bookButton1)
        self.calendarTable.setItem(1,0, QTableWidgetItem(self.Festivals['2']['date']+" "+self.Festivals['2']['location']))
        self.calendarTable.setItem(1,1, QTableWidgetItem(self.Festivals['2']['name']))
        self.bookButton2 = QPushButton("BOOK NOW", clicked = lambda:self.BookWindow(value=2))
        self.bookButton2.setStyleSheet("background-color:#7382A0;color:white;border: 10px solid;border-color:transparent;border-radius:15px;font-family:arial;font-weight:bold")
        self.calendarTable.setCellWidget(1,2, self.bookButton2)
        self.calendarTable.setItem(2,0, QTableWidgetItem(self.Festivals['3']['date']+" "+self.Festivals['3']['location']))
        self.calendarTable.setItem(2,1, QTableWidgetItem(self.Festivals['3']['name']))
        self.bookButton3 = QPushButton("BOOK NOW", clicked = lambda:self.BookWindow(value=3))
        self.bookButton3.setStyleSheet("background-color:#7382A0;color:white;border: 10px solid;border-color:transparent;border-radius:15px;font-family:arial;font-weight:bold")
        self.calendarTable.setCellWidget(2,2, self.bookButton3)
        self.calendarTable.setItem(3,0, QTableWidgetItem(self.Festivals['4']['date']+" "+self.Festivals['4']['location']))
        self.calendarTable.setItem(3,1, QTableWidgetItem(self.Festivals['4']['name']))
        self.bookButton4 = QPushButton("BOOK NOW", clicked = lambda:self.BookWindow(value=4))
        self.bookButton4.setStyleSheet("background-color:#7382A0;color:white;border: 10px solid;border-color:transparent;border-radius:15px;font-family:arial;font-weight:bold")
        self.calendarTable.setCellWidget(3,2, self.bookButton4)
        self.calendarTable.setItem(4,0, QTableWidgetItem(self.Festivals['5']['date']+" "+self.Festivals['5']['location']))
        self.calendarTable.setItem(4,1, QTableWidgetItem(self.Festivals['5']['name']))
        self.bookButton5 = QPushButton("BOOK NOW", clicked = lambda:self.BookWindow(value=5))
        self.bookButton5.setStyleSheet("background-color:#7382A0;color:white;border: 10px solid;border-color:transparent;border-radius:15px;font-family:arial;font-weight:bold")
        self.calendarTable.setCellWidget(4,2, self.bookButton5)
        self.calendarTable.setItem(5,0, QTableWidgetItem(self.Festivals['6']['date']+" "+self.Festivals['6']['location']))
        self.calendarTable.setItem(5,1, QTableWidgetItem(self.Festivals['6']['name']))
        self.bookButton6 = QPushButton("BOOK NOW", clicked = lambda:self.BookWindow(value=6))
        self.bookButton6.setStyleSheet("background-color:#7382A0;color:white;border: 10px solid;border-color:transparent;border-radius:15px;font-family:arial;font-weight:bold")
        self.calendarTable.setCellWidget(5,2, self.bookButton6)
        self.calendarTable.setItem(6,0, QTableWidgetItem(self.Festivals['7']['date']+" "+self.Festivals['7']['location']))
        self.calendarTable.setItem(6,1, QTableWidgetItem(self.Festivals['7']['name']))
        self.bookButton7 = QPushButton("BOOK NOW", clicked = lambda:self.BookWindow(value=7))
        self.bookButton7.setStyleSheet("background-color:#7382A0;color:white;border: 10px solid;border-color:transparent;border-radius:15px;font-family:arial;font-weight:bold")
        self.calendarTable.setCellWidget(6,2, self.bookButton7)
        self.calendarTable.setItem(7,0, QTableWidgetItem(self.Festivals['8']['date']+" "+self.Festivals['8']['location']))
        self.calendarTable.setItem(7,1, QTableWidgetItem(self.Festivals['8']['name']))
        self.bookButton8 = QPushButton("BOOK NOW", clicked = lambda:self.BookWindow(value=8))
        self.bookButton8.setStyleSheet("background-color:#7382A0;color:white;border: 10px solid;border-color:transparent;border-radius:15px;font-family:arial;font-weight:bold")
        self.calendarTable.setCellWidget(7,2, self.bookButton8)
        self.calendarTable.setItem(8,0, QTableWidgetItem(self.Festivals['9']['date']+" "+self.Festivals['9']['location']))
        self.calendarTable.setItem(8,1, QTableWidgetItem(self.Festivals['9']['name']))
        self.bookButton9 = QPushButton("BOOK NOW", clicked = lambda:self.BookWindow(value=9))
        self.bookButton9.setStyleSheet("background-color:#7382A0;color:white;border: 10px solid;border-color:transparent;border-radius:15px;font-family:arial;font-weight:bold")
        self.calendarTable.setCellWidget(8,2, self.bookButton9)
        self.calendarTable.setItem(9,0, QTableWidgetItem(self.Festivals['10']['date']+" "+self.Festivals['10']['location']))
        self.calendarTable.setItem(9,1, QTableWidgetItem(self.Festivals['10']['name']))
        self.bookButton10 = QPushButton("BOOK NOW", clicked = lambda:self.BookWindow(value=10))
        self.bookButton10.setStyleSheet("background-color:#7382A0;color:white;border: 10px solid;border-color:transparent;border-radius:15px;font-family:arial;font-weight:bold")
        self.calendarTable.setCellWidget(9,2, self.bookButton10)
        self.calendarTable.setGeometry(700,307,550,362)
        self.calendarTable.setStyleSheet("background-color:transparent;border-style:outset;border-width:1px;border-color:#DCDCDC;border-bottom-right-radius:20px;border-bottom-left-radius:20px;font-family:arial;font-size:16px")
        self.calendarTable.verticalHeader().setVisible(False)
        self.calendarTable.horizontalHeader().setVisible(False)
        self.calendarTable.setShowGrid(False)
        self.calendarTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #statistics
        self.statBackground = QLabel(self)
        self.statBackground.setStyleSheet("background-color:#F8F8FF;border-style:outset;border-width:1px;border-color:#DCDCDC")
        self.statBackground.setGeometry(710,80,300,70)
        self.statToursIcon = QLabel(self)
        self.statToursIcon.setPixmap(QPixmap("numTours.png"))
        self.statToursIcon.setGeometry(710,80,70,70)
        self.statToursIcon.setScaledContents(True)
        self.statToursIcon.setStyleSheet("background-color:#1E90FF")
        self.statToursText = QLabel("TOURS", self)
        self.statToursText.setStyleSheet("font-family:Arial;font-weight:bold;font-size:16px;color:#808080")
        self.statToursText.move(860,125)
        self.statToursNum = QLabel(self.userData['TotalTours'], self)
        self.statToursNum.setStyleSheet("font-family:Arial;font-weight:bold;font-size:28px;qproperty-alignment:AlignCenter")
        self.statToursNum.setGeometry(862,88,53,30)

        self.statBackground1 = QLabel(self)
        self.statBackground1.setStyleSheet("background-color:#F8F8FF;border-style:outset;border-width:1px;border-color:#DCDCDC")
        self.statBackground1.setGeometry(710,160,300,70)
        self.statFavLocIcon = QLabel(self)
        self.statFavLocIcon.setPixmap(QPixmap("favLoc.png"))
        self.statFavLocIcon.setGeometry(710,160,70,70)
        self.statFavLocIcon.setScaledContents(True)
        self.statFavLocIcon.setStyleSheet("background-color:#FCE043")
        self.statFavLocText = QLabel("FAVORITE LOCATION", self)
        self.statFavLocText.setStyleSheet("font-family:Arial;font-weight:bold;font-size:16px;color:#808080")
        self.statFavLocText.setGeometry(810,205,400,20)
        self.statFavLoc = QLabel(self.userData['FavoriteLoc'], self)
        self.statFavLoc.setStyleSheet("font-family:Arial;font-weight:bold;font-size:28px;qproperty-alignment:AlignCenter")
        self.statFavLoc.setGeometry(811,168,163,30)

        self.statBackground2 = QLabel(self)
        self.statBackground2.setStyleSheet("background-color:#F8F8FF;border-style:outset;border-width:1px;border-color:#DCDCDC")
        self.statBackground2.setGeometry(1040,80,200,150)
        self.statTierImage = QLabel(self)
        self.membership = int(self.userData['membership'])
        if self.membership == 1:
            self.imageTier = "bronzeTier.png"
            self.textTier = "BRONZE TIER"
        elif self.membership == 2:
            self.imageTier = "silverTier.png"
            self.textTier = "SILVER TIER"
        elif self.membership == 3:
            self.imageTier = "goldTier.png"
            self.textTier = "GOLD TIER"
        else:
            pass
        self.statTierImage.setPixmap(QPixmap(self.imageTier))
        self.statTierImage.setScaledContents(True)
        self.statTierImage.setGeometry(1090,105,100,100)
        self.statTierText = QLabel("MEMBERSHIP", self)
        self.statTierText.setStyleSheet("font-family:Arial;font-weight:bold;font-size:16px;color:#808080")
        self.statTierText.setGeometry(1085,85,200,20)
        self.statTierText2 = QLabel(self.textTier, self)
        self.statTierText2.setStyleSheet("font-family:Arial;font-weight:bold;font-size:18px;qproperty-alignment:AlignCenter")
        self.statTierText2.setGeometry(1050,205,180,20)

    def uploadProfilePic(self):
        self.image = QFileDialog.getOpenFileName(self,'Open File','c\\','image file(*.jpg)')
        self.imagePath = self.image[0]
        self.pixmap = QPixmap(self.imagePath)
        self.label.setPixmap(QPixmap(self.pixmap))
        self.label.setScaledContents(True)

    def read(self):
        with open('value.txt' ,'r') as f:
            data = f.read()
            self.value2 = data
            return data
    
    def BookWindow(self, value):
        self.ui = BookPopUp(value)
        self.ui.show()

    def profilePage(self):
        self.ui = profileUI()
        self.ui.show()
        self.hide()
    
    def activitiesPage(self):
        self.ui = activitiesUI
        self.ui.show()
        self.hide()

class BookPopUp(QWidget):
    def __init__(self, value, parent=None):
        super().__init__()
        self.setStyleSheet("""
        
            QPushButton#Pressable{
                border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;
                 font-size:15px;font-family: "Arial Narrow", Arial, sans-serif;
                }
            QPushButton#Pressable:hover{
                
                }
            QPushButton#Pressable:pressed{
                background-color:#000000;color:#FFFFFF;
                }
            QWidget{
                background-color:#FFFFFF
            }
            QLabel#Image{
                border:3px solid #1E90FF;border-radius:75px;font-family: "Arial Narrow", Arial, sans-serif;
            }
            QLabel#BottomText{
                border: 2px solid,#494F5B;border-radius: 5px;background-color:#000000;color:#FFFFFF;
                font-size:15px;font-family: "Arial Narrow", Arial, sans-serif;
            } 
            QLabel#Texts{
                font-family: "Arial"; 
                font-size: 19px; font-style: normal; font-weight: 700;background-color: rgba(0, 0, 0, 0.5);
                color:#FFFFFF; qproperty-alignment: AlignCenter;border-radius:10px;border-style:outset;
                border-width:1px;border-color:#808080
            }
            QLabel#NoBg{
                background-color:transparent
            }
            """)
        self.Festivals = {'1':{"name":"Masimbo Festival","date":"March 10-12","location":"Puerto Galera","info":"Established in 2011, Malasimbo Music and Arts festival serves as a venue for the indigenous people of Mindoro to showcase their culture and art. Above the idea of fun and partying, the festival is and will always be a celebration of and for the Mangyans."},
                          '2':{"name":"Katalingkasan Festival","date":"March 22","location":"Albay","info":"The festivity held every 2nd week of July in Libon retraces the valiant story of the virgins of the town who worked hard in making Libon as one of the earliest settlements in Albay. Featured activities are trade fairs, shows, and street dancing"},
                          '3':{"name":"Island of the Garden City of Samal Festival","date":"March 10-12","location":"Samal","info":"This week-long festivals in celebration of the founding anniversary of Island Garden City of Samal. The festival showcases the island's natural endowments and its people's culture."},
                          '4':{"name":"Anibina Bulawanun Festival","date":"March 7","location":"Nabunturan","info":"This week-long festivals in celebration of the founding anniversary of Island Garden City of Samal. The festival showcases the island's natural endowments and its people's culture."},
                          '5':{"name":"Holy Week","date":"April 9","location":"San Agustin Church","info":"The Anibina Bulawanon Festival celebrates the bountiful gold harvest and the founding anniversary of Compostela Province. Compostela Valley is known for its rich gold deposits. The festival is held during the first week of March in the municipality of Nabunturan."},
                          '6':{"name":"Mariones Festival","date":"April 10","location":"Marinduque","info":"Holy Week, in the Christian church, the week between Palm Sunday and Easter, observed with special solemnity as a time of devotion to the Passion of Jesus Christ. In the Greek and Roman liturgical books, it is called the Great Week because great deeds were done by God during this week."},
                          '7':{"name":"Centurion Festival","date":"April 11","location":"Marinduque","info":"This is a folk-religious festival that re-enacts the story of Saint Longinus, a Roman centurion who was blind in one eye. The festival is characterized by colorful Roman costumes, painted masks and helmets, and brightly colored tunics"},
                          '8':{"name":"Ang Pagtatatal","date":"April 15","location":"Guimaras ","info":"Ang Pagtaltal is a holy Lenten presentation staged on the hillside of Jordan every Good Friday, patterned to Oberammergau in Southern Bavaria, Germany. It is the final act of the play when Jesus was taken off from the cross and laid on his mother's lap"},
                          '9':{"name":"Pangalap Ritual ","date":"April 18","location":"Valencia","info":"This is not a festival per se but an interesting ceremony in which believers crawl through Catilaran Cave as they chant various prayers. The ritual is believed to give participants supernatural powers that help protect them against malevolent spirits."},
                          '10':{"name":"Witches Festival","date":"April 19","location":"Siquijor","info":"Siquijor is best known as the land of witchcraft. During the Witches Festivals, sorcerers or mambabarang gather at Crocodile Hill during the full moon to collect herbs, roots and live insects which they throw into enormous cauldrons filled with boiling water. They sit around this concoction while chanting incantations. The festival culminates in dancing and a restricted ritual in an isolated cave at dawn."},
                          }

        self.FestivalPath = {'1':"Festival Images\AMalasimbo.jpg",'2':"Festival Images\BKatalingkasan.jpg",'3':"Festival Images\CSamal.jpg",
                           '4':"Festival Images\DAnibina Bulawanun.jpg",'5':"Festival Images\EHolyWeek.jpg","6":"Festival Images\FMariones Festival.jpg",
                           '7':"Festival Images\GCenturion.jpg",'8':"Festival Images\HAngPagtataral.jpg",'9':"Festival Images\IPangalap Ritual.jpg",'10':"Festival Images\JWitches.jpg"}
        
        self.tourGuide = {'1':{"name":"Joselito Tanyag","skills":"A great listener\nA great photographer\nEmphatic\nFluent English","ratings":'4',"package":"The tour will commence with a single minivan which will service you to the venue, the venue will be a hotel in puerto galera with 3 bedrooms for 3-5 persons, During the day you will be toured around several music entertainment by locals","price":"5500.00",},
                        '2':{"name":"Federico Cortez","skills":"A great entertainer\nComedian\nGood english","ratings":'5',"package":"The event will tour you all around albay to see the festivals and the different shows around albay, the tour package includes the food which is the speciality of albay as well. The tour covers 2-3 person","price":"2000.00"},
                        '3':{"name":"Mark Gutierrez","skills":"A great storyteller\nHas a good english accent\nCan translate dialects such such as bisaya","ratings":'5',"package":"The tour will guide up to 5 person to a hotel on the Garden City, this hotel will provide you a room for 3 days and during the day you will be toured around the garden city and the festival","price":"7600.00"},
                        '4':{"name":"Alex Del Rosario","skills":"Good entertainer\nCan speak tagalog and bisaya","ratings":'3',"package":"2-3 person will be driven to Nabarutan where you will get toured around the festival ongoing through the whole area, The driver will tour you to several tourist spots in the local area","price":"2700.00"},
                        '5':{"name":"Christian Felipe","skills":"Very religous\nGood preacher\nPhilosopher","ratings":'3',"package":"The tour for two will get you around san agustin church to tour you around history of the venue and its relation to the holy week and its origin.","price":"1400.00"},
                        '6':{"name":"Nathaniel Aquino","skills":"Great entertainer\nActive\nFluent Tagalog and Ilocano","ratings":'4',"package":"The tour guide will show you around the places of marinduque after the procession, the tour will cover for two persons","price":"1700.00"},
                        '7':{"name":"James Mendoza","skills":"Can speak bikolano and bisaya\nGreat storyteller\nActive","ratings":'5',"package":"After the roman themed festival, up to 2 will get a chance to travel around the great city of mariduque for a day,","price":"1300.00"},
                        '8':{"name":"Daniel Mendoza","skills":"Humorous\nGood speaker\nFluet tagalog\nEnergetic","ratings":'5',"package":"2-3 person will get a chance to see famous plays about jesus. Afterwards will go around town to explore some famous tourist spots.","price":"2000.00"},
                        '9':{"name":"Jacob	Perez","skills":"Can speak fluent english\nHumorous ","ratings":'4',"package":"The tour will include a mysterious ritual said to give protection to the people from bad spirits. The tour involves going around the town of velencia for 2 persons max","price":"1250.00"},
                        '10':{"name":"John-Mark Ramos","skills":"Creative entertainer\nGood at locations\nInformation oriented","ratings":'5',"package":"The festival themed by the sorcery. You will experience a haunting diner for 2 at a witch themed couldron restaurant. Afterward you will get to be toured around a town full of witch themed amusement", "price":"4570.00"}}         
        self.value = value
        self.setWindowTitle("BOOK")
        self.resize(750,550)
        self.setFixedSize
        self.Design()
        self.BookLeftWindow()
        self.BookRightWindow()
        self.show()

    def Design(self):
        '''
        self.backgroundPopUp = QLabel(self)
        self.backgroundPopUp.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #A3B6C2, stop:1 #5BC7D7)")
        self.backgroundPopUp.setGeometry(0,0,750,550)
        '''
        self.bg1 = QLabel(self)
        self.bg1.setPixmap(QPixmap("Book-right2.jpg"))
        self.bg1.setGeometry(0,0,330,550)
        self.bg1.setScaledContents(True)

        self.bg2 = QLabel(self)
        self.bg2.setPixmap(QPixmap("Book-left.jpg"))
        self.bg2.setGeometry(330,0,420,550)
        self.bg2.setScaledContents(True)
        print(self.value)
    def BookLeftWindow(self):
        self.Profile = QLabel(self)
        self.Profile.setGeometry(90,10,150,150)
        self.Profile.setObjectName("Image")
        self.Profile.setPixmap(QPixmap("BlackIcon.png"))
        self.Profile.setScaledContents(True)

        self.tourguideName = QLabel(self.tourGuide[f"{self.value}"]['name'], self)
        self.tourguideName.setGeometry(15,165,300,50)
        self.tourguideName.setObjectName("Texts")
        self.tgBookRating = int(self.tourGuide[f"{self.value}"]['ratings'])
        self.NoStar = QPixmap("StarBlack.png")
        self.Star=QPixmap("StarYellow.png")#2B2F36 canvas (Darker)
        if self.tgBookRating == 1:
            self.RatingStar1 = QLabel("",self)
            self.RatingStar1.setGeometry(90,220,27,25)
            self.RatingStar1.setPixmap(self.Star)
            self.RatingStar1.setScaledContents(True)
            self.RatingStar1.setObjectName("NoBg")
            self.RatingStar2 = QLabel("",self)
            self.RatingStar2.setGeometry(120,220,27,25)
            self.RatingStar2.setPixmap(self.NoStar)
            self.RatingStar2.setScaledContents(True)
            self.RatingStar2.setObjectName("NoBg")
            self.RatingStar3 = QLabel("",self)
            self.RatingStar3.setGeometry(150,220,27,25)
            self.RatingStar3.setPixmap(self.NoStar)
            self.RatingStar3.setScaledContents(True)
            self.RatingStar3.setObjectName("NoBg")
            self.RatingStar4 = QLabel("",self)
            self.RatingStar4.setGeometry(180,220,27,25)
            self.RatingStar4.setPixmap(self.NoStar)
            self.RatingStar4.setScaledContents(True)
            self.RatingStar4.setObjectName("NoBg")
            self.RatingStar5 = QLabel("",self)
            self.RatingStar5.setGeometry(210,220,27,25)
            self.RatingStar5.setPixmap(self.NoStar)
            self.RatingStar5.setScaledContents(True)
            self.RatingStar5.setObjectName("NoBg")
        elif self.tgBookRating == 2:
            self.RatingStar1 = QLabel("",self)
            self.RatingStar1.setGeometry(90,220,27,25)
            self.RatingStar1.setPixmap(self.Star)
            self.RatingStar1.setScaledContents(True)
            self.RatingStar1.setObjectName("NoBg")
            self.RatingStar2 = QLabel("",self)
            self.RatingStar2.setGeometry(120,220,27,25)
            self.RatingStar2.setPixmap(self.Star)
            self.RatingStar2.setScaledContents(True)
            self.RatingStar2.setObjectName("NoBg")
            self.RatingStar3 = QLabel("",self)
            self.RatingStar3.setGeometry(150,220,27,25)
            self.RatingStar3.setPixmap(self.NoStar)
            self.RatingStar3.setScaledContents(True)
            self.RatingStar3.setObjectName("NoBg")
            self.RatingStar4 = QLabel("",self)
            self.RatingStar4.setGeometry(180,220,27,25)
            self.RatingStar4.setPixmap(self.NoStar)
            self.RatingStar4.setScaledContents(True)
            self.RatingStar4.setObjectName("NoBg")
            self.RatingStar5 = QLabel("",self)
            self.RatingStar5.setGeometry(210,220,27,25)
            self.RatingStar5.setPixmap(self.NoStar)
            self.RatingStar5.setScaledContents(True)
            self.RatingStar5.setObjectName("NoBg")
        elif self.tgBookRating == 3:
            self.RatingStar1 = QLabel("",self)
            self.RatingStar1.setGeometry(90,220,27,25)
            self.RatingStar1.setPixmap(self.Star)
            self.RatingStar1.setScaledContents(True)
            self.RatingStar1.setObjectName("NoBg")
            self.RatingStar2 = QLabel("",self)
            self.RatingStar2.setGeometry(120,220,27,25)
            self.RatingStar2.setPixmap(self.Star)
            self.RatingStar2.setScaledContents(True)
            self.RatingStar2.setObjectName("NoBg")
            self.RatingStar3 = QLabel("",self)
            self.RatingStar3.setGeometry(150,220,27,25)
            self.RatingStar3.setPixmap(self.Star)
            self.RatingStar3.setScaledContents(True)
            self.RatingStar3.setObjectName("NoBg")
            self.RatingStar4 = QLabel("",self)
            self.RatingStar4.setGeometry(180,220,27,25)
            self.RatingStar4.setPixmap(self.NoStar)
            self.RatingStar4.setScaledContents(True)
            self.RatingStar4.setObjectName("NoBg")
            self.RatingStar5 = QLabel("",self)
            self.RatingStar5.setGeometry(210,220,27,25)
            self.RatingStar5.setPixmap(self.NoStar)
            self.RatingStar5.setScaledContents(True)
            self.RatingStar5.setObjectName("NoBg")
        elif self.tgBookRating == 4:
            self.RatingStar1 = QLabel("",self)
            self.RatingStar1.setGeometry(90,220,27,25)
            self.RatingStar1.setPixmap(self.Star)
            self.RatingStar1.setScaledContents(True)
            self.RatingStar1.setObjectName("NoBg")
            self.RatingStar2 = QLabel("",self)
            self.RatingStar2.setGeometry(120,220,27,25)
            self.RatingStar2.setPixmap(self.Star)
            self.RatingStar2.setScaledContents(True)
            self.RatingStar2.setObjectName("NoBg")
            self.RatingStar3 = QLabel("",self)
            self.RatingStar3.setGeometry(150,220,27,25)
            self.RatingStar3.setPixmap(self.Star)
            self.RatingStar3.setScaledContents(True)
            self.RatingStar3.setObjectName("NoBg")
            self.RatingStar4 = QLabel("",self)
            self.RatingStar4.setGeometry(180,220,27,25)
            self.RatingStar4.setPixmap(self.Star)
            self.RatingStar4.setScaledContents(True)
            self.RatingStar4.setObjectName("NoBg")
            self.RatingStar5 = QLabel("",self)
            self.RatingStar5.setGeometry(210,220,27,25)
            self.RatingStar5.setPixmap(self.NoStar)
            self.RatingStar5.setScaledContents(True)
            self.RatingStar5.setObjectName("NoBg")
        elif self.tgBookRating == 5:
            self.RatingStar1 = QLabel("",self)
            self.RatingStar1.setGeometry(90,220,27,25)
            self.RatingStar1.setPixmap(self.Star)
            self.RatingStar1.setScaledContents(True)
            self.RatingStar1.setObjectName("NoBg")
            self.RatingStar2 = QLabel("",self)
            self.RatingStar2.setGeometry(120,220,27,25)
            self.RatingStar2.setPixmap(self.Star)
            self.RatingStar2.setScaledContents(True)
            self.RatingStar2.setObjectName("NoBg")
            self.RatingStar3 = QLabel("",self)
            self.RatingStar3.setGeometry(150,220,27,25)
            self.RatingStar3.setPixmap(self.Star)
            self.RatingStar3.setScaledContents(True)
            self.RatingStar3.setObjectName("NoBg")
            self.RatingStar4 = QLabel("",self)
            self.RatingStar4.setGeometry(180,220,27,25)
            self.RatingStar4.setPixmap(self.Star)
            self.RatingStar4.setScaledContents(True)
            self.RatingStar4.setObjectName("NoBg")
            self.RatingStar5 = QLabel("",self)
            self.RatingStar5.setGeometry(210,220,27,25)
            self.RatingStar5.setPixmap(self.Star)
            self.RatingStar5.setScaledContents(True)
            self.RatingStar5.setObjectName("NoBg")

        self.skillsDescript = QLabel("SKILLS DESCRIPTION", self)
        self.skillsText = QLabel(self.tourGuide[f"{self.value}"]['skills'], self)
        self.skillsDescript.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);color:#FFFFFF; qproperty-alignment: AlignTop;padding:5px;border-radius:10px;border-style:outset;border-width:1px;border-color:#808080;font-family:arial;font-size:16px;font-weight:bold")
        self.skillsDescript.setGeometry(15,260,300,280)
        self.skillsText.setStyleSheet("background-color:transparent;color:#FFFFFF; qproperty-alignment: AlignTop;padding:5px;border-radius:10px;font-family:arial;font-size:14px;font-weight:bold")
        self.skillsText.setGeometry(15,290,300,250)
        self.skillsText.setWordWrap(True)

        self.skillsDescriptIcon = QLabel(self)
        self.skillsDescriptIcon.setPixmap(QPixmap("skillsDes.png"))
        self.skillsDescriptIcon.setGeometry(201,263,25,25)
        self.skillsDescriptIcon.setStyleSheet("background-color:transparent")
        self.skillsDescriptIcon.setScaledContents(True)

        self.horizontalLine1 = QLabel(self)
        self.horizontalLine1.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);color:#FFFFFF")
        self.horizontalLine1.setGeometry(15,290,300,2)

    def BookRightWindow(self):
        self.packageOffer = QLabel("PACKAGE OFFERS", self)
        self.packageText = QLabel(self.tourGuide[f"{self.value}"]['package'], self)
        self.packageOffer.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);color:#FFFFFF; qproperty-alignment: AlignTop;padding:5px;border-style:outset;border-width:1px;border-color:#808080;border-radius:10px;font-family:arial;font-size:16px;font-weight:bold")
        self.packageOffer.setGeometry(345,15,390,220)
        self.packageText.setStyleSheet("background-color:transparent;color:#FFFFFF; qproperty-alignment: AlignTop;padding:5px;border-radius:10px;font-family:arial;font-size:14px;font-weight:bold")
        self.packageText.setGeometry(345,50,390,185)
        self.packageText.setWordWrap(True)

        self.packageOfferIcon = QLabel(self)
        self.packageOfferIcon.setPixmap(QPixmap("packOff.png"))
        self.packageOfferIcon.setGeometry(510,18,25,25)
        self.packageOfferIcon.setStyleSheet("background-color:transparent")
        self.packageOfferIcon.setScaledContents(True)

        self.horizontalLine2 = QLabel(self)
        self.horizontalLine2.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);color:#FFFFFF")
        self.horizontalLine2.setGeometry(345,45,390,2)

        self.info = QLabel(self)
        self.info.setPixmap(QPixmap("infoFest.png"))
        self.info.setStyleSheet("background-color:transparent")
        self.info.setGeometry(695,250,30,30)
        self.info.setScaledContents(True)
        
        self.festInfo = QLabel("BOOKING INFO", self)
        self.festInfo.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);color:#FFFFFF; qproperty-alignment: AlignTop;padding:5px;border-style:outset;border-width:1px;border-color:#808080;border-radius:10px;font-family:arial;font-size:16px;font-weight:bold")
        self.festInfo.setGeometry(345,250,390,220)
        self.festInfo.setToolTip(self.Festivals[f"{self.value}"]['info'])

        self.horizontalLine3 = QLabel(self)
        self.horizontalLine3.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);color:#FFFFFF")
        self.horizontalLine3.setGeometry(345,280,390,2)

        self.festInfoIcon = QLabel(self)
        self.festInfoIcon.setPixmap(QPixmap("bookInfo.png"))
        self.festInfoIcon.setStyleSheet("background-color:transparent")
        self.festInfoIcon.setGeometry(475,252,28,28)
        self.festInfoIcon.setScaledContents(True)

        self.festImage = QLabel(self)
        self.festImage.setPixmap(QPixmap(self.FestivalPath[f"{self.value}"]))
        self.festImage.setGeometry(355,300,200,150)
        self.festImage.setStyleSheet("background-color:black;border-style:outset;border-width:1px;border-color:#F0FFFF")
        self.festImage.setScaledContents(True)

        self.festNameInfo = QLabel(self.Festivals[f"{self.value}"]['name'], self)
        self.festNameInfo.setStyleSheet("background-color:transparent;color:white;font-family:arial;font-size:14px;font-weight:Bold")
        self.festNameInfo.setGeometry(560,315,170,35)
        self.festNameInfo.setWordWrap(True)
        self.festLocInfo = QLabel(self.Festivals[f"{self.value}"]['location'], self)
        self.festLocInfo.setStyleSheet("background-color:transparent;color:white;font-family:arial;font-size:14px;font-weight:Bold")
        self.festLocInfo.setGeometry(560,355,170,35)
        self.festLocInfo.setWordWrap(True)
        self.festDateInfo = QLabel(self.Festivals[f"{self.value}"]['date'], self)
        self.festDateInfo.setStyleSheet("background-color:transparent;color:white;font-family:arial;font-size:14px;font-weight:Bold")
        self.festDateInfo.setGeometry(560,395,170,35)
        self.festDateInfo.setWordWrap(True)

        self.bookButton = QPushButton("BOOK", self)
        self.bookButton.clicked.connect(self.dashboardPageB)
        self.bookButton.setIcon(QIcon("check.png"))
        self.bookButton.setIconSize(QSize(25,25))
        self.bookButton.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #A3B6C2, stop:1 #5BC7D7);color:#001a33;font-family:arial;font-size:16px;font-weight:bold;border-radius:10px;border-width:2px;border-color:#4dff88;border-style:outset")
        self.bookButton.setGeometry(565,485,150,50)

        self.Price = QLabel("Price "+"  "+'PHP'+" "+self.tourGuide[f"{self.value}"]['price'], self)
        self.Price.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #A3B6C2, stop:1 #5BC7D7);color:#001a33;font-family:arial;font-size:16px;font-weight:bold;border-radius:10px;border-width:2px;border-color:#b3d9ff;border-style:outset")
        self.Price.setGeometry(360,485,200,50)

        self.verticalLine = QLabel(self)
        self.verticalLine.setStyleSheet("background-color:white")
        self.verticalLine.setGeometry(408,487,2,47)
  
    def dashboardPageB(self):
        buttonReply = QMessageBox.question(self, "Confirmation","Are you sure you want to book this event?",QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            with open('value.txt','w') as f:
                data = str(self.value)
                f.write(data)
            self.hide()
            self.ui = dashboardUI()
            self.ui.hide()
        else:
            pass
 
class profileUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'GIYA - Customers UI'
        self.setGeometry(50,40,1270,680)
        self.Icon = "appLogoico.png"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.Icon))
        self.imagePath = ""

        self.userData={"username":"Zandlex","password":"Admin","role":"U","msg": ["hello",'hi'],"pending":[],"acc":{"name":"Zandlex Keano M. Cruz","age":"19","sex":
        "Male","loc":"Marikina City, Metro Manila, Philippines","EmailAd":"Qzkmcruz@tip.edu.ph","started":"November 26, 2000","FavoriteLoc":"Region V","TotalTours":"0","contact":"09560594126","aboutme":
        "I have no bio data yet to show the people"}}

        self.initUI()

    def initUI(self):
        self.menuBar()
        self.DashBoardButtons()
        self.profilePage()
        self.show()

    def EditBioButton(self):
        text, okPressed = QInputDialog.getText(self, "Get text","Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.newtext=text
            self.BioText.setText(self.newtext)
            self.BioText.setWordWrap(True)
            self.userData['aboutme']=text
                
    def DashBoardButtons(self):
        self.label = QLabel(self)
        self.label.setGeometry(1200,0,70,60)
        self.textboxUsername = QLabel(self.userData['username'], self)
        self.textboxUsername.setGeometry(1095,30,100,20)
        self.textboxUsername.setStyleSheet("font-family:arial;font-weight:bold;font-size:14px;qproperty-alignment:AlignRight")
        self.textboxUsername1 = QLabel("Welcome to GIYA,", self)
        self.textboxUsername1.move(1110,10)
        self.backgroudTaskbar = QLabel(self)
        self.backgroudTaskbar.setStyleSheet("background-color:#494F5B;border: 0px 1px 0px 0px outset #666e7f")
        self.backgroudTaskbar.setGeometry(0,0,100,680)
        self.lineTaskbar1 = QLabel(self)
        self.lineTaskbar1.setStyleSheet("background-color:#2d3139")
        self.lineTaskbar1.setGeometry(0,60,100,2)
        self.backgroudLogo = QLabel(self)
        self.backgroudLogo.setStyleSheet("background-color:#d5d7dd")
        self.backgroudLogo.setGeometry(0,0,100,60)
        self.lineTaskbar = QLabel(self)
        self.lineTaskbar.setStyleSheet("background-color:#aaafbb")
        self.lineTaskbar.setGeometry(100,60,1280,2)
        self.backgroudBar = QLabel(self)
        self.backgroudBar.setStyleSheet("background-color:#f1f2f4;border: 1px outset #c6cad2")
        self.backgroudBar.setGeometry(100,0,1100,60)
        self.logo = QLabel(self)
        self.logo.setGeometry(22,5,50,50)
        self.pixmap = QPixmap(self.Icon)
        self.logo.setPixmap(QPixmap(self.pixmap))
        self.logo.setScaledContents(True)
        #Taskbar Buttons
        #Dashboard Page
        self.button1 = QPushButton("", self)
        self.button1.clicked.connect(self.dashboardPage)
        self.button1.setIcon(QIcon("dashboardico.png"))
        self.button1.setToolTip("Go to your DASHBOARD.")
        self.button1.setIconSize(QSize(60,60))
        self.button1.setGeometry(14,90,70,70)
        self.button1.setStyleSheet("background-color:transparent")
        #self.button3.clicked.connect(self.dashboardPage)
        self.textbox1 = QLabel("DASHBOARD", self)
        self.textbox1.setStyleSheet("font-family:arial;font-weight:bold;color:#F5F5F5")
        self.textbox1.move(16,160)
        #About Us Page
        self.button2 = QPushButton("", self)
        self.button2.setIcon(QIcon("aboutUsico.png"))
        self.button2.setToolTip("Know About Us.")
        self.button2.setIconSize(QSize(45,45))
        self.button2.setGeometry(25,500,50,50)
        self.button2.setStyleSheet("background-color:transparent")
        #self.button4.clicked.connect(self.aboutUsPage)
        self.textbox2 = QLabel("ABOUT US", self)
        self.textbox2.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox2.move(22,560)
        #Profile
        self.button3 = QPushButton("", self)
        self.button3.setIcon(QIcon("profilePageico.png"))
        self.button3.setToolTip("Go to your Profile")
        self.button3.setIconSize(QSize(70,70))
        self.button3.setGeometry(10,195,80,80)
        self.button3.setStyleSheet("background-color:transparent")
        self.textbox3 = QLabel("PROFILE", self)
        self.textbox3.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox3.move(27,275)
        #History Events
        self.button4 = QPushButton("", self)
        self.button4.clicked.connect(self.activitiesPage)
        self.button4.setIcon(QIcon("historyEvents.png"))
        self.button4.setToolTip("Go to your Activities.")
        self.button4.setIconSize(QSize(50,50))
        self.button4.setGeometry(20,315,60,60)
        self.button4.setStyleSheet("background-color:transparent")
        self.textbox3 = QLabel("ACTIVITIES", self)
        self.textbox3.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox3.move(20,380)
        #Sign Out 
        self.button5 = QPushButton("SIGN OUT", self)
        self.button5.setIcon(QIcon("signOutico.png"))
        self.button5.setToolTip("Sign Out.")
        self.button5.setIconSize(QSize(30,30))
        self.button5.move(3,620)
        self.button5.resize(90,30)
        self.button5.setStyleSheet("background-color:transparent;color:white")
        #self.button5.clicked.connect(self.signOut)
        self.textDash = QLabel("Profile", self)
        self.textDash.setGeometry(130,18,300,25)
        self.textDash.setStyleSheet("font-family:century gothic;font-size:24px")
        self.taskBarButton = QPushButton("", self)
        self.taskBarButton.setIcon(QIcon("taskBar.png"))
        self.taskBarButton.setIconSize(QSize(30,30))
        self.taskBarButton.setGeometry(210,12,40,40)
        self.taskBarButton.setStyleSheet("background-color:transparent")
        self.textboxUsername = QLabel(self.userData['username'], self)
        self.textboxUsername.setGeometry(1095,30,100,20)
        self.textboxUsername.setStyleSheet("font-family:arial;font-weight:bold;font-size:14px;qproperty-alignment:AlignRight")
        self.textboxUsername1 = QLabel("Welcome to GIYA,", self)
        self.textboxUsername1.move(1110,10)

    def menuBar(self):
        self.buttonPic = QPushButton("", self)
        self.buttonPic.setIcon(QIcon("uploadImageico.ico"))
        self.buttonPic.setIconSize(QSize(70,50))
        self.buttonPic.setGeometry(1200,0,70,60)
        #self.buttonPic.setStyleSheet("background-color:transparent")

    def profilePage(self):
        #profile picture 
        self.buttonUploadPic = QPushButton("", self)
        self.buttonUploadPic.setIcon(QIcon("uploadImageico.ico"))
        self.buttonUploadPic.setIconSize(QSize(110,110))
        self.buttonUploadPic.setGeometry(140,80,120,120)
        self.buttonUploadPic2 = QPushButton("Upload image", self)
        self.buttonUploadPic2.setGeometry(140,200,120,25)
        self.buttonUploadPic.clicked.connect(self.uploadProfilePic)
        self.buttonUploadPic2.clicked.connect(self.uploadProfilePic)
        self.label = QLabel(self)
        self.label.setGeometry(140,80,120,120)
        #profile details
        self.prfName = QLabel(self.userData['acc']['name'], self)
        self.prfName.setGeometry(290,98,300,28)
        self.prfName.setStyleSheet("font-family:arial;font:bold;font-size:26px")
        self.prfEmail = QLabel(self.userData['acc']['EmailAd'], self)
        self.prfEmail.setGeometry(290,130,300,17)
        self.prfEmail.setStyleSheet("font-family:arial;font-size:14px")
        self.prfLocation = QLabel(self.userData['acc']['loc'], self)
        self.prfLocation.setGeometry(290,158,300,17)
        self.prfLocation.setStyleSheet("font-family:arial;font-size:14px")
#------------------------Left Portion---------------------------------------------------------------
        self.ProfileBio = QLabel(self)
        self.ProfileBio.setStyleSheet("background-color:#FFFFFF;border 0px 1px 0px 0px outset #666e7f;border-radius:20px;")
        self.ProfileBio.setGeometry(140,250,420,400)
        self.BioIcon=QLabel(self)
        self.BioIcon.setPixmap(QPixmap("AboutMe.png"))
        self.BioIcon.setScaledContents(True)
        self.BioIcon.setGeometry(145,255,50,50)
        self.BioIcon.setStyleSheet("background-color:Transparent")
        self.BioHeader=QLabel("About Me",self)
        self.BioHeader.setGeometry(140,255,420,60)
        self.BioHeader.setStyleSheet("""color:#000000;font-family: Arial; font-size: 20px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 15px;
                                              padding-left:80px;color:#000000;background-color:Transparent;
                                              border: 2px solid #494F5B;border-width:0px 0px 2px 0px;""")
        self.BioText=QLabel(self.userData['acc']['aboutme'],self)
        self.BioText.setWordWrap(True)
        self.BioText.setGeometry(150,330,380,290)
        self.BioText.setStyleSheet("background-color:transparent;font-size:20px;")
        self.EditBio=QPushButton("EDIT NOTE",self)
        self.EditBio.setGeometry(430,265,80,30)
        self.TGButtons=(""" background-color:#747D90  """)
        self.EditBio.setStyleSheet(self.TGButtons)
        self.EditBio.clicked.connect(self.EditBioButton)
#----------------------------Right Portion-----------------------------------------------------------
        self.RightPartLayout=QLabel(self)
        self.RightPartLayout.setGeometry(600,62,700,700)
        self.RightPartLayout.setStyleSheet("Background-color:#CFD0D3")
        self.BiodataBox = QLabel(self)
        self.BiodataBox.setStyleSheet("background-color:#FFFFFF;border 0px 1px 0px 0px outset #666e7f;border-radius:20px;")
        self.BiodataBox.setGeometry(637,200,600,450)
        self.BiodataLogo=QLabel("",self)
        self.BiodataLogo.setScaledContents(True)
        self.BiodataLogo.setPixmap(QPixmap("Biodata.png"))
        self.BiodataLogo.setGeometry(645,200,50,50)
        self.BiodataHeader=QLabel(self.userData['acc']['name'].upper()+"'s "+"Bio data",self)
        self.BiodataHeader.setGeometry(637,200,600,60)
        self.BiodataHeader.setStyleSheet("""color:#000000;font-family: Arial; font-size: 20px; font-style: normal; font-variant: normal; font-weight: 500; line-height: 15px;
                                              padding-left:100px;color:#000000;background-color:Transparent;
                                              border: 2px solid #494F5B;border-width:0px 0px 2px 0px;""")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   
        self.RatingBox=QLabel(self)
        self.RatingBox.setGeometry(637,80,410,50)
        self.RatingBox.setStyleSheet("background-color:#FFFFFF;border 0px 1px 0px 0px outset #666e7f;")
        self.RatingsHeader=QLabel("Total Tours: ",self)
        self.RatingsHeader.setGeometry(685,85,120,35)
        self.RatingsHeader.setStyleSheet("Font-size:19px;font-family:Arial;font-weight:500")
        self.RatingsText=QLabel(self.userData['acc']['TotalTours'],self)
        self.RatingsText.setGeometry(820,87,120,35)
        self.RatingsText.setStyleSheet("Font-size:23px;font-family:Arial;font-weight:200")
        self.NumToursbg=QLabel(self)
        self.NumToursbg.setGeometry(637.5,80,45,50)
        self.NumToursbg.setStyleSheet("background-color:#7ED3E2")
        self.RatingLogo=QLabel(self)
        self.RatingLogo.setGeometry(637.5,80,45,50)
        self.RatingLogo.setPixmap(QPixmap("numTours.png"))#
        self.RatingLogo.setScaledContents(True)
        ### NUMBER OF TOURS====================
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
        self.DateStartBox=QLabel(self)
        self.DateStartBox.setGeometry(637,138,410,50)
        self.DateStartBox.setStyleSheet("background-color:#FFFFFF;")
        self.DateStartLogo=QLabel(self)
        self.DateStartLogo.setPixmap(QPixmap("Date.png"))
        self.DateStartLogo.setGeometry(637,138,45,50)
        self.DateStartLogo.setScaledContents(True)
        self.DateStartHeader=QLabel("Date started:",self)
        self.DateStartHeader.setGeometry(685,138,160,50)
        self.DateStartHeader.setStyleSheet("Font-size:20px;font-family:Arial;font-weight:500;")
        self.DateStartText=QLabel(self.userData['acc']['started'],self)
        self.DateStartText.setGeometry(835,138,200,50)
        self.DateStartText.setStyleSheet("Font-size:22px;font-family:Arial;")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
        self.LocBox=QLabel(self)
        self.LocBox.setGeometry(1070,80,165,108)
        self.LocBox.setStyleSheet("background-color:#FFFFFF;")
        self.LocLogo=QLabel(self)
        self.LocLogo.setGeometry(1070,105,80,80)
        self.LocLogo.setPixmap(QPixmap("PhilLandmark.ico"))
        self.LocLogo.setScaledContents(True)
        self.LocText=QLabel(self.userData['acc']['FavoriteLoc'],self)
        self.LocText.setStyleSheet("""Font-size:20px;font-family:Arial; font-style: normal; font-variant: normal; font-weight: 400; line-height: 15px;
                                                color:#000000;background-color:Transparent;""")
        self.LocText.setGeometry(1143,100,100,100)
        self.LocHeader=QLabel("Local Region",self)
        self.LocHeader.setGeometry(1110,80,130,30)
        self.LocHeader.setStyleSheet("""Font-size:17px;font-family:Arial; font-style: normal; font-variant: normal; font-weight: 400; line-height: 15px;
                                                color:#6E7F8C;background-color:Transparent;""")
#----------------------------------------------------------------------------------------------------
#----------------PROFILE INFORMATION-----------------------------------------------------------------
        self.Profilestyle=("""Font-size:17px;font-family:Arial; font-style: normal; font-variant: normal; font-weight: 700; line-height: 15px;
                                                color:#000000;background-color:Transparent;   """)
        self.Subprofilestyle=(""" Font-size:17px;font-family:Arial; font-style: normal; font-variant: normal; font-weight: 400; line-height: 15px;
                                                color:#000000;background-color:Transparent;  """)
        self.FullNameL=QLabel("Name: ",self)
        self.FullNameL.setGeometry(670,270,400,50)
        self.FullNameL.setStyleSheet(self.Profilestyle)
        self.FullNameT=QLabel(self.userData['acc']['name'],self)
        self.FullNameT.setGeometry(750,270,400,50)
        self.FullNameT.setStyleSheet(self.Subprofilestyle)

        self.AgeL=QLabel("Age: ",self)
        self.AgeL.setGeometry(670,340,400,50)
        self.AgeL.setStyleSheet(self.Profilestyle)
        self.AgeT=QLabel(self.userData['acc']['age'],self)
        self.AgeT.setGeometry(730,340,400,50)
        self.AgeT.setStyleSheet(self.Subprofilestyle)

        self.SexL=QLabel("Sex: ",self)
        self.SexL.setGeometry(670,410,400,50)
        self.SexL.setStyleSheet(self.Profilestyle)
        self.SexT=QLabel(self.userData['acc']['sex'],self)
        self.SexT.setGeometry(730,410,400,50)
        self.SexT.setStyleSheet(self.Subprofilestyle)

        self.EmailL=QLabel("Email address: ",self)
        self.EmailL.setGeometry(670,480,400,50)
        self.EmailL.setStyleSheet(self.Profilestyle)
        self.EmailT=QLabel(self.userData['acc']['EmailAd'],self)
        self.EmailT.setGeometry(820,480,400,50)
        self.EmailT.setStyleSheet(self.Subprofilestyle)

        self.ContactL=QLabel("Contact number: ",self)
        self.ContactL.setGeometry(670,550,400,50)
        self.ContactL.setStyleSheet(self.Profilestyle)
        self.EmailT=QLabel(self.userData['acc']['contact'],self)
        self.EmailT.setGeometry(840,550,400,50)
        self.EmailT.setStyleSheet(self.Subprofilestyle)

#-----------------------------------------------------------------------------------------------------
    def uploadProfilePic(self):
        self.image = QFileDialog.getOpenFileName(self,'Open File','c\\','image file(*.jpg)')
        self.imagePath = self.image[0]
        self.pixmap = QPixmap(self.imagePath)
        self.label.setPixmap(QPixmap(self.pixmap))
        self.label.setScaledContents(True)
        self.buttonPic.setIcon(QIcon(self.image[0]))

    def dashboardPage(self):
        self.ui = dashboardUI()
        self.ui.show()
        self.hide()

    def activitiesPage(self):
        self.ui = activitiesUI()
        self.ui.show()
        self.hide()

class activitiesUI(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'GIYA - Customers UI'
        self.x = 50
        self.y = 40
        self.width = 1270
        self.height = 680
        self.Icon = "appLogoico.png"
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setFixedSize
        self.setWindowIcon(QIcon(self.Icon))
        self.imagePath = ""
        self.userData={"username":"Zandlex","password":"Admin","role":"TG","msg": ["hello",'hi'],"pending":[],"acc":{"name":"Zandlex Keano M. Cruz","age":"19","sex":
        "Male","EmailAd":"Qzkmcruz@tip.edu.ph","started":"November 26, 2000","FavoriteLoc":"Region V","TotalTours":"0","contact":"09560594126","aboutme":
        "I have no bio data yet to show the people"}}
        #profile details
        self.name = "Ivan Norvy Guzman"
        self.email = "qinbguzman@tip.edu.ph"
        self.location = "Marikina City, Metro Manila, Philippines"
        self.username = "qinbguzman"
        self.initUI()

    def initUI(self):
        self.DashBoardButtons()
        self.RecentActivities()
        self.show()
#-----------------------------------------------------------------------------------------------------
    def DashBoardButtons(self):
        self.backgroudTaskbar = QLabel(self)
        self.backgroudTaskbar.setStyleSheet("background-color:#494F5B;border: 0px 1px 0px 0px outset #666e7f")
        self.backgroudTaskbar.setGeometry(0,0,100,680)
        self.lineTaskbar1 = QLabel(self)
        self.lineTaskbar1.setStyleSheet("background-color:#2d3139")
        self.lineTaskbar1.setGeometry(0,60,100,2)
        self.backgroudLogo = QLabel(self)
        self.backgroudLogo.setStyleSheet("background-color:#d5d7dd")
        self.backgroudLogo.setGeometry(0,0,100,60)
        self.lineTaskbar = QLabel(self)
        self.lineTaskbar.setStyleSheet("background-color:#aaafbb")
        self.lineTaskbar.setGeometry(100,60,1280,2)
        self.backgroudBar = QLabel(self)
        self.backgroudBar.setStyleSheet("background-color:#f1f2f4;border: 1px outset #c6cad2")
        self.backgroudBar.setGeometry(100,0,1100,60)
        self.logo = QLabel(self)
        self.logo.setGeometry(22,5,50,50)
        self.pixmap = QPixmap(self.Icon)
        self.logo.setPixmap(QPixmap(self.pixmap))
        self.logo.setScaledContents(True)
        #Taskbar Buttons
        #Dashboard Page
        self.button1 = QPushButton("", self)
        self.button1.clicked.connect(self.dashboardPage)
        self.button1.setIcon(QIcon("dashboardico.png"))
        self.button1.setToolTip("Go to your DASHBOARD.")
        self.button1.setIconSize(QSize(60,60))
        self.button1.setGeometry(14,90,70,70)
        self.button1.setStyleSheet("background-color:transparent")
        #self.button3.clicked.connect(self.dashboardPage)
        self.textbox1 = QLabel("DASHBOARD", self)
        self.textbox1.setStyleSheet("font-family:arial;font-weight:bold;color:#F5F5F5")
        self.textbox1.move(16,160)
        #About Us Page
        self.button2 = QPushButton("", self)
        self.button2.setIcon(QIcon("aboutUsico.png"))
        self.button2.setToolTip("Know About Us.")
        self.button2.setIconSize(QSize(45,45))
        self.button2.setGeometry(25,500,50,50)
        self.button2.setStyleSheet("background-color:transparent")
        #self.button4.clicked.connect(self.aboutUsPage)
        self.textbox2 = QLabel("ABOUT US", self)
        self.textbox2.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox2.move(22,560)
        #Profile
        self.button3 = QPushButton("", self)
        self.button3.clicked.connect(self.profilePage)
        self.button3.setIcon(QIcon("profilePageico.png"))
        self.button3.setToolTip("Go to your Profile")
        self.button3.setIconSize(QSize(70,70))
        self.button3.setGeometry(10,195,80,80)
        self.button3.setStyleSheet("background-color:transparent")
        self.textbox3 = QLabel("PROFILE", self)
        self.textbox3.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox3.move(27,275)
        #History Events
        self.button4 = QPushButton("", self)
        self.button4.setIcon(QIcon("historyEvents.png"))
        self.button4.setToolTip("Go to your Profile")
        self.button4.setIconSize(QSize(50,50))
        self.button4.setGeometry(20,315,60,60)
        self.button4.setStyleSheet("background-color:transparent")
        self.textbox3 = QLabel("ACTIVITIES", self)
        self.textbox3.setStyleSheet("font-family:arial;font-weight:bold;color:white")
        self.textbox3.move(20,380)
        #Sign Out 
        self.button5 = QPushButton("SIGN OUT", self)
        self.button5.setIcon(QIcon("signOutico.png"))
        self.button5.setToolTip("Sign Out.")
        self.button5.setIconSize(QSize(30,30))
        self.button5.move(3,620)
        self.button5.resize(90,30)
        self.button5.setStyleSheet("background-color:transparent;color:white")
        #self.button5.clicked.connect(self.signOut)

    def uploadProfilePic(self):
        self.image = QFileDialog.getOpenFileName(self,'Open File','c\\','image file(*.jpg)')
        self.imagePath = self.image[0]
        self.pixmap = QPixmap(self.imagePath)
        self.label.setPixmap(QPixmap(self.pixmap))
        self.label.setScaledContents(True)
        self.buttonPic.setIcon(QIcon(self.image[0]))

    def RecentActivities(self):## JUST NEEDS TO BE CONNECTED TO DATABASE
#-------------------------MENU BAR---------------------------------------------------------------------------        
        self.textDash = QLabel("Activities", self)
        self.textDash.move(130,15)
        self.textDash.setStyleSheet("font-family:century gothic;font-size:24px")
        self.taskBarButton = QPushButton("", self)
        self.taskBarButton.setIcon(QIcon("taskBar.png"))
        self.taskBarButton.setIconSize(QSize(30,30))
        self.taskBarButton.setGeometry(250,12,40,40)
        self.taskBarButton.setStyleSheet("background-color:transparent")
        self.buttonPic = QPushButton("", self)
        self.buttonPic.setIcon(QIcon("uploadImageico.ico"))
        self.buttonPic.setIconSize(QSize(70,50))
        self.buttonPic.setGeometry(1200,0,70,60)
        #self.buttonPic.setStyleSheet("background-color:transparent")
        self.label = QLabel(self)
        self.label.setGeometry(1200,0,70,60)
        self.textboxUsername = QLabel(self.userData['username'], self)
        self.textboxUsername.setGeometry(1095,30,100,20)
        self.textboxUsername.setStyleSheet("font-family:arial;font-weight:bold;font-size:14px;qproperty-alignment:AlignRight")
        self.textboxUsername1 = QLabel("Welcome to GIYA,", self)
        self.textboxUsername1.move(1110,18)
#------------------ACTIVITY 1--------------------------------------------------------------------------------
        self.A1Border=QLabel("",self)
        self.A1Border.setGeometry(140,120,1100,200)
        self.A1Border.setStyleSheet("border: 2px solid #5E7E58;background-color:#F8F8FF")
        self.Activity1=QLabel("ACTIVITY 1", self)
        self.Activity1.setGeometry(140,120,75,199)
        self.Activity1.setStyleSheet("""padding-left:5px;color:#000000;background-color:#AAB1BB;
                                        border: 2px solid #5E7E58;border-width:50px 3px 50px 3px;""")
        self.TextBoxD1=QLabel("EVENT NAME HERE "+ "\n\n\n\n"+"CUSTOMER NAME HERE"+"\n\n"+"EVENT DATE HERE"+"\n\n""EVENT RATING HERE",self)
        self.TextBoxD1.setGeometry(230,86,250,250)
        self.TextBoxD1.setStyleSheet("color:#000000;font-size:15px;font-family:Arial;")
        self.FestivalBoxD1=QLabel("",self)
        self.FestivalImage1=QPixmap("TGUIDE\Magayon.1.jpg")
        self.FestivalBoxD1.setGeometry(588,122,650,196)
        self.FestivalBoxD1.setPixmap(self.FestivalImage1)
        self.FestivalBoxD1.setScaledContents(True)
        self.HistoButton1=QPushButton("View Details",self)
        self.HistoButton1.setStyleSheet("background-color:#5E7E58")
        self.HistoButton1.setGeometry(400,270,180,40)

#------------------ACTIVITY         2----------------------------------------------------------------------------------------------

        self.A2Border=QLabel("",self)
        self.A2Border.setGeometry(140,330,1100,170)
        self.A2Border.setStyleSheet("border: 2px solid #7EA57F;background-color:#F8F8FF")
        self.Activity2=QLabel("ACTIVITY 2", self)
        self.Activity2.setGeometry(140,332,75,168)
        self.Activity2.setStyleSheet("""padding-left:5px;color:#000000;background-color:#BBC1C9;
                                        border: 2px solid #7EA57F;border-width:40px 3px 40px 3px;""")

        self.TextBoxD2=QLabel("\nEVENT NAME HERE "+ "\n\n\n"+"CUSTOMER NAME HERE"+"\n\n"+"EVENT DATE HERE"+"\n\n""EVENT RATING HERE",self)
        self.TextBoxD2.setGeometry(230,330,250,150)
        self.TextBoxD2.setStyleSheet("color:#000000;font-size:15px;font-family:Arial;")
        self.FestivalBoxD2=QLabel("",self)
        self.FestivalImage2=QPixmap("TGUIDE\Festival Pics\Malatarlak Festival.3.jpg")
        self.FestivalBoxD2.setGeometry(588,332,650,166)
        self.FestivalBoxD2.setPixmap(self.FestivalImage2)
        self.FestivalBoxD2.setScaledContents(True)
        self.HistoButton2=QPushButton("View Details",self)
        self.HistoButton2.setStyleSheet("background-color:#7EA57F")
        self.HistoButton2.setGeometry(400,450,180,40)
#------------------ACTIVITY 3----------------------------------------------------------------------------------------------

        self.A3Border=QLabel("",self)
        self.A3Border.setGeometry(140,511,1100,169)
        self.A3Border.setStyleSheet("border: 2px solid #A2BEA7;background-color:#F8F8FF")
        self.Activity3=QLabel("ACTIVITY 3", self)
        self.Activity3.setGeometry(140,513,75,167)
        self.Activity3.setStyleSheet("""padding-left:5px;color:#000000;background-color:#C9CED4;
                                        border: 2px solid #A2BEA7;border-width:40px 3px 40px 3px;""")
        self.TextBoxD3=QLabel("\nEVENT NAME HERE "+ "\n\n\n"+"CUSTOMER NAME HERE"+"\n\n"+"EVENT DATE HERE"+"\n\n""EVENT RATING HERE",self)
        self.TextBoxD3.setGeometry(230,513,250,150)
        self.TextBoxD3.setStyleSheet("color:#000000;font-size:15px;font-family:Arial;")
        self.FestivalBoxD3=QLabel("",self)
        self.FestivalImage3=QPixmap("TGUIDE\Festival Pics\DRAWER.jpg")
        self.FestivalBoxD3.setGeometry(588,513,650,165)
        self.FestivalBoxD3.setPixmap(self.FestivalImage3)
        self.FestivalBoxD3.setScaledContents(True)
        self.HistoButton3=QPushButton("View Details",self)
        self.HistoButton3.setStyleSheet("background-color:#A2BEA7")
        self.HistoButton3.setGeometry(400,630,180,40)

    def dashboardPage(self):
        self.ui = dashboardUI()
        self.ui.show()
        self.hide()

    def profilePage(self):
        self.ui = profileUI()
        self.ui.show()
        self.hide()

#executes the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = dashboardUI()
    sys.exit(app.exec_())