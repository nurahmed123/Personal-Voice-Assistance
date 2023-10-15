import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
from email.message import EmailMessage

# import dlibw

########################################################         crt voice         ############################################


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')# print(voices[1].id)
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 175)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

########################################################         sign up frmt         ############################################

try:
    speak('hello sir . if you wanna use this software . please sign up first . ');
    speak('enter your name')
    take_name = input('Enter your name: ')
    name = take_name.capitalize()
    speak('thanks for entering your name , now enter your email address please')
    take_email = input("Enter your email address : ")

    ########################################################         send OTP         ############################################

    msg = EmailMessage()
    msg['Subject'] = 'Verify OTP'
    msg['From'] = 'Bong Programiz'
    msg['To'] = take_email

    otp = ''.join([str(random.randint(1, 9)) for i in range(6)])
    real_msg = f"Hello {name} sir! \nWelcome to our Software \n\nYour OTP is : " + str(otp) + "\nThanks for using our software . "

    msg.set_content(real_msg)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('mdnurahmadoli529@gmail.com', 'kdmyfrysceouxilt')
    server.send_message(msg)

    ########################################################         OTP submit         ############################################

    speak('thanks for entering your email address , we already send a verification code in your mail . please check it out and enter the otp to use the software .')
    rcv_otp_email = input('Enter the OTP : ')

    w8_take_otp = rcv_otp_email.replace(" ","")

    if w8_take_otp == otp:

    ########################################################         scs sign up         ############################################

        speak('Congratulation sir . now you are fully sign up . now the software being open . wait a moment , thank you ')
        def wishMe():
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("Good Morning!")

            elif hour >= 16 and hour < 18:
                speak("Good Afternoon!")

            elif hour >= 12 and hour < 16:
                speak("good noon")

            else:
                speak("Good Evening!")

            speak("I am Jarvis Sir. Please tell me how may I help you")


    ########################################################         takeing commend         ############################################

        def takeCommand():
            # It takes microphone input from the user and returns string output

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 0.5
                audio = r.listen(source)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-uk')
                print(f"User said: {query}\n")

            except Exception as e:
                # print(e)
                print("Say that again please...")
                # speak("hmmm")
                return "None"
            return query


        if __name__ == "__main__":
            wishMe()
            while True:
                # if 1:
                query = takeCommand().lower()

                # Logic for executing tasks based on query

                ########################################################         scearch in google         ############################################

                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                    # scearch anythong in google

                elif 'type' in query:
                    speak('searching in google , wait a moment , thank you . ')
                    query.replace("type", "")
                    webbrowser.open(query.replace("type", ""))


                elif 'search' in query:
                    speak('searching in google , wait a moment , thank you . ')
                    query.replace("search", "")
                    webbrowser.open(query.replace("type", ""))

                    # open this in online


                elif 'open youtube' in query:
                    webbrowser.open("https://youtube.com")
                    speak('opening youtube . thanks for commend , wait a moment .')


                elif 'open akinator' in query:
                    webbrowser.open("https://en.akinator.com/")
                    speak('opening akinator . thanks for commend , wait a moment .')


                elif 'open photo colorize' in query:
                    webbrowser.open("https://demos.algorithmia.com/colorize-photos")
                    speak('opening photo colorize , wait a moment . thanks for commend . ')


                elif 'open qr code scaner' in query:
                    webbrowser.open("https://www.the-qrcode-generator.com/scan")
                    speak('opening qr code scaner , wait a moment , thanks for commnend . ')


                elif 'open python package' in query:
                    webbrowser.open("https://www.lfd.uci.edu/~gohlke/pythonlibs/")
                    speak('opening python pakage , wait a moment , thanks for commnend . ')


                elif 'open scratch' in query:
                    webbrowser.open("https://scratch.mit.edu/")
                    speak('opening scratch programming web page , wait a moment , thanks for commnend . ')


                elif 'open typing speed' in query:
                    webbrowser.open("https://www.keybr.com/")
                    speak('opening typing speed checking web page , wait a moment , thanks for commnend . ')


                elif 'open facebook' in query:
                    webbrowser.open("https://www.facebook.com/")
                    speak('opening face book . thanks for commend , wait a moment . ')


                elif 'open office' in query:
                    webbrowser.open("https://www.office.com/?auth=1")
                    speak('opening office , wait a moment . thanks for commend . ')


                elif 'open mail' in query:
                    webbrowser.open("https://mail.google.com/mail/u/0/?tab=om#inbox")
                    speak('opening mail , wait a moment . thanks for commend . ')


                elif 'open ms word' in query:
                    webbrowser.open("https://www.office.com/launch/word?auth=1")
                    speak('opening ms word , wait a moment . thanks for commend . ')


                elif 'open google drive' in query:
                    webbrowser.open("https://drive.google.com/drive/my-drive")
                    speak('opening google drive , wait a moment . thanks for commend . ')


                elif 'open google trends' in query:
                    webbrowser.open("https://trends.google.com/trends/?geo=US")
                    speak('opening google trends , wait a moment . thanks for commend . ')


                elif 'open news' in query:
                    webbrowser.open("https://news.google.com/topstories?tab=on&hl=en-US&gl=US&ceid=US:en")
                    speak('opening google news , wait a moment . thanks for commend . ')


                elif 'open google meet' in query:
                    webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")
                    speak('opening google meet , wait moment , thanks for commend . ')


                elif 'open top up' in query:
                    webbrowser.open("https://shop2g.com/")
                    speak('opening free fire diamond top up center , wait moment , thanks for commend . ')


                elif 'open google photos' in query:
                    webbrowser.open("https://photos.google.com/?pageId=none")
                    speak('opening google photos , wait a moment . thanks for commend . ')


                elif 'open translator' in query:
                    webbrowser.open("https://translate.google.com.bd/?hl=en&tab=qT")
                    speak('opening google translate , wait a moment . thanks for commend . ')


                elif 'open dou' in query:
                    webbrowser.open("https://duo.google.com/?usp=duo_ald")
                    speak('opening google dou , wait a moment . thanks for commend . ')


                elif 'open google docs' in query:
                    webbrowser.open("https://docs.google.com/document/u/0/")
                    speak('opening google docs , wait a moment . thanks for commend . ')


                elif 'open google books' in query:
                    webbrowser.open("https://books.google.com.bd/?hl=en&tab=pp")
                    speak('opening google books searching page , wait a moment , thanks for commend . ')


                elif 'open skype' in query:
                    webbrowser.open("https://web.skype.com/")
                    speak('opening skping , wait a moment . tanks for commend. ')


                elif 'open calender' in query:
                    webbrowser.open("https://outlook.live.com/calendar/0/view/month")
                    speak('opening calender , wait a moment . thanks for commend . ')


                elif 'open map' in query:
                    webbrowser.open("https://www.google.com/maps/@24.5916236,88.2700411,14z")
                    speak('opening map , wait a moment . tanks for commend . ')


                elif 'open railway' in query:
                    webbrowser.open("https://www.esheba.cnsbd.com/#/")
                    speak('opening online Railway e ticket service , wait a moment . tanks for commend . ')


                elif 'open top' in query:
                    webbrowser.open("https://toph.co/")
                    speak('opening toph , wait a moment . thanks for commend . ')


                elif 'open my facebook id' in query:
                    webbrowser.open("https://www.facebook.com/profile.php?id=100050240173688")
                    speak('opening my boss facebook id , wait a moment . thanks for commend . ')


                elif 'open pay fees' in query:
                    webbrowser.open("https://sms.rcs.edu.bd/index.php/sslPayment/paybill")
                    speak('opening online pay pees , wait a moment . tanks for commend . ')


                elif 'open google' in query:
                    webbrowser.open("https://google.com")
                    speak('opening google . thanks for commend , wait a moment .')


                elif 'open python book' in query:
                    webbrowser.open("http://pybook.subeen.com/")
                    speak('opening python book . thanks for commend , wait a moment .')


                elif 'open daraz' in query:
                    webbrowser.open("https://www.daraz.com.bd/")
                    speak('opening daraz . thannks for comme , wait a moment . ')


                elif 'open tiktok' in query:
                    webbrowser.open("https://www.tiktok.com/")
                    speak('opening tiktok . thanks for commend , what a moment . ')


                elif 'open photoshop' in query:
                    webbrowser.open("https://www.photopea.com/")
                    speak('opening photoshop . thanks for commend , wait a moment .')


                elif 'open phone tracker' in query:
                    webbrowser.open("https://myaccount.google.com/find-your-phone")
                    speak('opening phone tracker . thanks for commend , wait a moment .')


                elif 'open cp book' in query:
                    webbrowser.open("https://jakir.me/c/")
                    speak('opening c programming book. thanks for commend , wait a moment.')


                elif 'open telegram' in query:
                    webbrowser.open("https://web.telegram.org/")
                    speak('opening telegram . thanks for commend , wait a moment . ')


                elif 'open stackoverflow' in query:
                    webbrowser.open("https://stackoverflow.com")
                    speak('opening stackoverflow . thanks for commend , wait a moment .')


                elif 'open instagram' in query:
                    webbrowser.open("https://www.instagram.com/accounts/login/")
                    speak('opening instagram . thanks for commend , wait a moment .')


                elif 'open arduino online' in query:
                    webbrowser.open("https://create.arduino.cc/editor/nurahmed123")
                    speak('opening online arduino ide , wait a moment . thanks for commend . ')


                elif 'open whatsapp' in query:
                    webbrowser.open("https://web.whatsapp.com/ ")
                    speak('opening whats app . thanks for commend , wait a moment .')


                elif 'open just for you' in query:
                    webbrowser.open("https://www.facebook.com/messages/t/100050240173688")
                    speak('opening just for you in messenger . thanks for commend , wait a moment .')

                ########################################################        ask date , time and year         ############################################

                elif 'time' in query:

                    speak(f"Sir,the time is")

                    hour = int(datetime.datetime.now().hour)
                    if hour >= 0 and hour < 12:
                        speak("morning")

                    elif hour >= 16 and hour < 18:

                        bn_cnvt_time = hour - 12
                        say_time = datetime.datetime.now().strftime(
                            f"afternoon{bn_cnvt_time} hour %M minutes and %S second ")
                        speak(say_time)

                    elif hour >= 12 and hour < 16:

                        bn_cnvt_time = hour - 12
                        say_time = datetime.datetime.now().strftime(
                            f"noon{bn_cnvt_time} hour %M minutes and %S second ")
                        speak(say_time)

                    elif hour >= 18 and hour < 20:

                        bn_cnvt_time = hour - 12
                        say_time = datetime.datetime.now().strftime(
                            f"Evening{bn_cnvt_time} hour %M minutes and %S second ")
                        speak(say_time)
                        # speak(f'Evening{bn_cnvt_time} hour and %M:%S')

                    else:
                        bn_cnvt_time = hour - 12
                        say_time = datetime.datetime.now().strftime(
                            f"Night{bn_cnvt_time} hour %M minutes and %S second ")
                        speak(say_time)

                    say_time = datetime.datetime.now().strftime("And the international time is %H:%M:%S . thank you")
                    speak(say_time)

                ########################################################         ask something         ############################################

                elif 'day' in query:
                    strDay = datetime.datetime.now().strftime("%A")
                    speak(f'sir , today is {strDay}')


                elif 'date' in query:
                    strDate = datetime.datetime.now().strftime("%d %B %Y")
                    speak(f'sir , date is {strDate} ')


                elif 'year' in query:
                    strYear = datetime.datetime.now().strftime("%Y")
                    speak(f'sir , year is {strYear} ')

                    # asking quiestion


                elif 'what can you do' in query:
                    speak('i can do everything that you learnt me . ')


                elif 'can you hear me' in query:
                    speak('yes sir , i can hear properly. ')


                elif 'hello' in query:
                    speak('hi boss , i am hare , thank you')

                elif 'hi' in query:
                    speak('hello boss , i am hare , thank you')


                elif 'who are you' in query:
                    speak('my name is jarvis , i am your personal assistant and you can ask me anything . ')


                elif 'what are you doing' in query:
                    speak('i following my boss commend .')


                elif 'how are you' in query:
                    speak('i am fine and you?')


                elif 'who is your boss' in query:
                    speak(f"my boss name is {name} and he is a nice human .")


                elif 'laugh' in query:
                    speak('ha ha ha ')  # just for kiding


                elif 'fine' in query:
                    speak('oh, nice.')


                elif 'who is your creator' in query:
                    speak('my creator is a programmer , his name is nur ahmed . ')


                elif 'good' in query:
                    speak('thanks boss , this is my duty . ')


                elif 'what is the character of your boss' in query:
                    speak('my boss character is very nice . he commends me very politely ')

                    # open software from laptop

                ########################################################         open software from laptop         ############################################

                elif 'open pycharm' in query:
                    speak(' opening pycharm . wait a moment . thanks for commend . ')
                    codePath = "F:\\program file\\JetBrains\\PyCharm 2020.3.3\\bin\\pycharm64.exe"
                    os.startfile(codePath)


                elif 'open zoom' in query:
                    speak('opening zoom , wait a moment . thanks for commend .')
                    codePath = "C:\\Users\Morsed\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
                    os.startfile(codePath)


                elif 'open face lock' in query:
                    speak('opening face lock , wait a moment . thanks for commend . ')
                    softwarePath = "F:\\program file\\KeyLemon\\KLGuiManager.exe"
                    os.startfile(softwarePath)


                elif 'open visual studio' in query:
                    speak(' opening code . wait a moment . thanks for commend . ')
                    codePath = "F:\\program file\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)


                elif 'open eclipse' in query:
                    speak('opening eclipse . wait a moment . thanks for commend . ')
                    codePath = "F:\\program file\\eclipse\\java-2020-12\\eclipse\\eclipse.exe"
                    os.startfile(codePath)


                elif 'open music' in query:
                    codePath = "E:\\Music"
                    speak('opening music . wait a moment . thanks for commend . ')
                    os.startfile(codePath)

                elif 'open my file' in query:
                    codePath = "E:\\noor"
                    speak('opening my boss file . wait a moment , thanks for commend . ')
                    os.startfile(codePath)

                elif 'open meme file' in query:
                    codePath = "E:\\noor\\picture class\\amni memes\\amni file"
                    speak('opening meme file . wait a moment , thanks for commend . ')
                    os.startfile(codePath)


                elif 'open download file' in query:
                    codePath = "E:\\Downloads"
                    speak('opening download file . wait a moment , thanks for commend . ')
                    os.startfile(codePath)


                elif 'open books' in query:
                    codePath = "E:\\noor\\picture class\\books"
                    speak('opening books file . wait a moment , thanks for commend .')
                    os.startfile(codePath)


                elif 'open teamviewer' in query:
                    codePath = "F:\\program file\\TeamViwer\\TeamViewer.exe"
                    speak('opening teamviwer . wait a moment , thanks for commend . ')
                    os.startfile(codePath)


                elif 'open screenshot' in query:
                    codePath = "E:\\Pictures\\Screenshots"
                    speak('opening Screenshots file . wait a moment , thanks for commend .')
                    os.startfile(codePath)


                elif 'open c drive' in query:
                    codePath = "C:"
                    speak("opening c drive . wait a moment , thanks for commend . ")
                    os.startfile(codePath)


                elif 'open e drive' in query:
                    codePath = "E:"
                    speak("opening e drive . wait a moment , thanks for commend . ")
                    os.startfile(codePath)


                elif 'open f drive' in query:
                    codePath = "F:"
                    speak("opening f drive . wait a moment , thanks for commend . ")
                    os.startfile(codePath)


                elif 'open code block' in query:
                    codePath = "F:\\program file\\CodeBlocks\\codeblocks.exe"
                    speak('opening code block . wait a moment . thanks for commemnd . ')
                    os.startfile(codePath)


                elif 'open software file' in query:
                    codePath = "E:\\software"
                    speak("opening software file . wait a moment , thanks for commend . ")
                    os.startfile(codePath)


                elif 'open browser' in query:
                    codePath = "C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"
                    speak('opening google chorme . thanks for commend ')
                    os.startfile(codePath)


                elif 'open emulator' in query:
                    codePath = "F:\\program file\\TxGameAssistant\\appmarket\\AppMarket.exe"
                    speak('opening  emulator , wait a moment . thanks for commend . ')
                    os.startfile(codePath)


                elif 'open firefox' in query:
                    codePath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                    speak('opening fire fox , wait a moment . thanks for commend ')
                    os.startfile(codePath)


                elif 'droidcam' in query:
                    codePath = "F:\\program file\\DroidCam\\DroidCamApp.exe"
                    speak('opening droid cam')
                    os.startfile(codePath)


                elif 'open imo' in query:
                    codePath = "C:\\Users\\Morsed\\AppData\\Roaming\\Imo Messenger\\ImoDesktopApp.exe"
                    speak('opening imo , wait a moment . thanks for commend . ')
                    os.startfile(codePath)


                elif 'open arduino' in query:
                    codePath = "F:\\program file\\arduino\\arduino.exe"
                    speak('opening arduino ,wait a moment . thanks for commend . ')
                    os.startfile(codePath)


                elif 'open shortcut' in query:
                    codePath = "F:\\program file\\Shotcut\\shotcut.exe"
                    speak('opening short cut , wait a moment , thanks for commend . ')
                    os.startfile(codePath)

                elif 'open cpu' in query:
                    codePath = "F:\\program file\\CPUID\\CPU-Z\\CPU-Z\\cpuz.exe"
                    speak('opening cpu z , wait a moment , thanks for commend . ')
                    os.startfile(codePath)


                elif 'open lightshot' in query:
                    codePath = "C:\\Program Files (x86)\\Skillbrains\\lightshot\\Lightshot.exe"
                    speak('opening lightshot , wait a moment , thanks for commend . ')
                    os.startfile(codePath)

                elif 'open microsoft browser' in query:
                    codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    speak('opening microsoft browser , wait a moment , thanks for commend . ')
                    os.startfile(codePath)


                elif 'open keyboard' in query:
                    codePath = "C:\\Program Files (x86)\\Avro Keyboard\Avro Keyboard.exe"
                    speak('opening avro keyboard , whait a moment . thanks for commend . ')
                    os.startfile(codePath)


                elif 'open recorder' in query:
                    codePath = "C:\\Program Files (x86)\\Apowersoft\\Apowersoft Free Screen Recorder\\Apowersoft Free Screen Recorder.exe"
                    speak('opening recoder , wait a moment , thanks for commend . ')
                    os.startfile(codePath)


                elif 'open xampp' in query:
                    codePath = "C:\\xampp\\xampp-control.exe"
                    speak('opening xampp control panel , wait a moment , thanks for commend . ')
                    os.startfile(codePath)


                elif 'open windscribe' in query:
                    codePath = "F:\\program file\\Windscribe\\WindscribeLauncher.exe"
                    speak('opening windscribe , wait a moment , thanks for commend . ')
                    os.startfile(codePath)


                elif 'open inno' in query:
                    codePath = "F:\\program file\\Inno Setup 6\\Compil32.exe"
                    speak('opening inno , wait a moment , thanks for commend . ')
                    os.startfile(codePath)


                elif 'open calculator' in query:
                    speak(' opening calculator . wait a moment . thanks for commend . ')
                    codePath = "F:\program file\Calculator\Calculator.exe"
                    os.startfile(codePath)

                # else:
                    # speak('this commend does not exit')

                # elif '' in query:
                #     codePath = ""
                #     speak('opening  , whait a moment . thanks for commend . ')
                #     os.startfile(codePath)

    else:
        speak('You Entered wrong OTP . Check your OTP and enter the right OTP ')



except Exception as e:
    speak('something is wrong , please check your information and internet connection , try again , thank you .')


