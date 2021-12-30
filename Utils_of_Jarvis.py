import webbrowser as wb

from wikipedia.exceptions import PageError

import os

import Details

import Tester as t

network_error = 'Sorry but my server is currently down, Sir'
unknown_value_error = 'Sorry, but I did not understand that, Sir'
playsound_error = 'Sorry but my speech service is down, Sir'
Name = 'My name is Jarvis, Sir'
Reply = 'I am fine Sir'
bye_message = 'Bye, Sir! Take Care! Consult me whenever you need. Jarvis is always there to support you Sir!'
limit_search = 'enough search'
limit_search_location = 'enough location'
limit_wiki = 'enough Wikipedia'
limit_songs = 'enough song'
limit_diary = 'no'


def wish():
    import datetime
    hour = float(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak_and_print_with_Jarvis('Good morning Sir!')
    elif hour >= 12 and hour < 18:
        speak_and_print_with_Jarvis('Good afternoon Sir!')
    else:
        speak_and_print_with_Jarvis('Good evening Sir!')


def name():
    speak_and_print_with_Jarvis(Name)


def time():
    from time import ctime
    Time = ctime()
    speak_and_print_with_Jarvis(Time)
    speak_and_print_with_Jarvis('Sir')


def speak_Jarvis(statement):
    import pyttsx3
    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')     # The default mode is male(Jarvis) so it's really up to you
    # engine.setProperty('voice', voices[0].id) # To either specify these two lines
    engine.say(statement)                       # But you really need to type these two in case of female(Friday)
    engine.runAndWait()


def speech_to_text():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:    
            Voice = r.listen(source) 
            text = r.recognize_google(Voice)
            return text
        except sr.UnknownValueError:
            return unknown_value_error
        except sr.RequestError:
            return network_error


def search_url():
    query = ''
    n = 1
    while limit_search not in query: 
        if n == 1:
            question = 'Search for what Sir'
            speak_and_print_with_Jarvis(question)
        else:
            further_question = 'Do you want anything more to search Sir'
            speak_and_print_with_Jarvis(further_question)
        query = speech_to_text()
        confirm = t.Network_Tester(query)
        if confirm:
            speak_and_print_with_Jarvis(network_error)
            exit()
        if 'exit' in query:
            bye()
            exit()
        elif unknown_value_error in query:
            speak_and_print_with_Jarvis(query)
            n = 0
        elif limit_search in query:            
            speak_and_print_with_Jarvis('Fine')
        else:
            url = f'https://google.com/search?q={query}'
            wb.open_new_tab(url)
            speak_and_print_with_Jarvis(f'Here is what I got for {query}, Sir')
        n += 1
    else:
        speak_and_print_with_Jarvis('Sir')
            

def location():
    location = ''
    n = 1
    while limit_search_location not in location:
        if n == 1:
            location_question = 'Please tell me the location, Sir.'
            speak_and_print_with_Jarvis(location_question)
        else:
            further_location_question = 'Do you want to locate anything else, Sir?'
            speak_and_print_with_Jarvis(further_location_question)
        location = speech_to_text()
        confirm = t.Network_Tester(location)
        if confirm:
            speak_and_print_with_Jarvis(network_error)
            exit()
        if 'exit' in location:
            bye()
            exit()
        elif unknown_value_error in location:
            speak_and_print_with_Jarvis(location)
            n = 0 
        elif limit_search_location in location:
            speak_and_print_with_Jarvis('Very')
        else:
            location_url = f'https://google.nl/maps/place/{location}/&amp'
            wb.open_new_tab(location_url)
            speak_and_print_with_Jarvis(f'Here is the location of {location}, Sir')
        n += 1
    else:
        speak_and_print_with_Jarvis('Well, Sir')


def speak_and_print_with_Jarvis(sentence):
    speak_Jarvis(sentence)
    print(sentence)


def respond():
    speak_and_print_with_Jarvis(Reply)


def bye():
    speak_and_print_with_Jarvis(bye_message)
    import datetime
    hour = float(datetime.datetime.now().hour)
    if hour >= 20 and hour <= 4:
        speak_and_print_with_Jarvis('Also, Good night Sir!')


def open_google():
    wb.open('google.com')


def open_youtube():
    wb.open('youtube.com')


def open_stackoverflow():
    wb.open('stackoverflow.com')


def open_wikipedia():
    import wikipedia as wiki
    query = ''
    n = 1
    while limit_wiki not in query: 
        if n == 1:
            question = 'Search whose wikipedia, Sir'
            speak_and_print_with_Jarvis(question)
        else:
            further_question = 'Whose else wikipedia do you want to search, Sir'
            speak_and_print_with_Jarvis(further_question)
        query = speech_to_text() 
        confirm = t.Network_Tester(query)
        if confirm:
            speak_and_print_with_Jarvis(network_error)
            exit()
        if 'exit' in query:
            bye()
            exit()
        elif unknown_value_error in query:
            speak_and_print_with_Jarvis(query)
            n = 0
        elif limit_wiki in query:            
            speak_and_print_with_Jarvis('Alright')
        else:
            try:
                info = wiki.summary(query, sentences = 2)
                speak_and_print_with_Jarvis('According to wikipedia...')
                speak_and_print_with_Jarvis(info)
                speak_and_print_with_Jarvis('Sir')
            except PageError:
                speak_and_print_with_Jarvis(f'Sorry, but I did not find anything for {query} Sir')
        n += 1
    else:
        speak_and_print_with_Jarvis('Sir')
    

def open_code():
    vs_code = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(vs_code)


def play_song():
    n = 1
    Song = ''
    while limit_songs not in Song: 
        if n == 1:
            question = 'Which song do you wish to play, Sir'
            speak_and_print_with_Jarvis(question)
        else:
            further_question = 'Which other song do you wish to play, Sir'
            speak_and_print_with_Jarvis(further_question)
        Song = speech_to_text()
        confirm = t.Network_Tester(Song)
        if confirm:
            speak_and_print_with_Jarvis(network_error)
            exit()
        song = Song.lower()
        if 'exit' in song:
            bye()
            exit()
        elif unknown_value_error in Song:
            speak_and_print_with_Jarvis(Song)
            n = 0
        elif limit_songs in song:            
            speak_and_print_with_Jarvis('Okay')
        else:
            try:
                SONG = # f'Location of your\\{song}.mp3'
                from playsound import playsound as play
                play(SONG)
            except Exception:
                speak_and_print_with_Jarvis(f'I did not get {song} song, Sir')
                n = 0
        n += 1
    else:
        speak_and_print_with_Jarvis('Sir')
        
    
def date_details():
    import datetime as dt
    year = str(dt.datetime.now().year)
    month = str(Details.months[dt.datetime.now().month])
    day = str(dt.datetime.now().day)
    details = year + month + day 
    return details 


def make_diary():
    updates = date_details()
    content = ''
    n = 1
    confirm = False
    while n != 0:
        if n == 1 or confirm == True:
            speak_and_print_with_Jarvis('Say what you want, Sir?')
        else:
            speak_and_print_with_Jarvis('Do you want to modify the content, Sir')
        content = speech_to_text()
        confirm = t.Network_Tester(content)
        if confirm:
            speak_and_print_with_Jarvis(network_error)
            exit()
        if limit_diary == content:
            if n == 1:
                speak_and_print_with_Jarvis('''You didn't even say anything, Sir''')
            else:
                speak_and_print_with_Jarvis('Diary successfully made, Sir')
            break
        elif unknown_value_error in content:
            speak_and_print_with_Jarvis(content)
            confirm = True 
            continue
        elif 'exit' in content:
            bye()
            exit()
        else:    
            try:    
                with open(f'{updates}.txt', 'w') as fh: # fh = filehandler
                    fh.writelines(f'{updates} \n{content}')
            except Exception:
                speak_and_print_with_Jarvis('Something went wrong, Sir')
                n = 0
            finally:
                confirm = False
        n += 1


def see_diary():
    updates = date_details()
    file = (f'{updates}.txt')
    speak_and_print_with_Jarvis('Tell me to close the file when you want it to be, Sir')
    fh = open(file, 'r')
    speak_and_print_with_Jarvis(fh.read())
    response = ''
    while response != 'close':
        response = speech_to_text()
        if 'exit' in response:
            fh.close()
            bye()
        elif network_error in response:
            fh.close()
            speak_and_print_with_Jarvis(network_error)
            exit()
        elif unknown_value_error in response:
            speak_and_print_with_Jarvis(unknown_value_error)
    else:
        fh.close()
    

def send_email():
    # Simple Mail Transfer Protocol = SMTP
    # Secure Sockets Layer (SSL)
    # There are two types of ports sender port and connection port both of which are addresses
    # Sender port has address 25 which can't be changed
    # While connection port commonly has addresses: 465 and 587 and you yourself can add one
    import smtplib
    while 1:    
        speak_and_print_with_Jarvis('Send email to whom, Sir?')
        receiver = speech_to_text()
        confirm = t.Network_Tester(receiver)
        if confirm:
            speak_and_print_with_Jarvis(network_error)
            exit()
        if unknown_value_error in receiver:
            speak_and_print_with_Jarvis(unknown_value_error)
        else:
            try:
                to = Details.Records[receiver]
                break
            except KeyError:
                speak_and_print_with_Jarvis(f'I could not find {receiver} Sir')
    while 1:    
        speak_and_print_with_Jarvis('What should I say, Sir?')
        content = speech_to_text()
        confirm = t.Network_Tester(content)
        if confirm:
            print(network_error)
            exit()
        if unknown_value_error in content:
            speak_and_print_with_Jarvis(unknown_value_error)
        else:
            break
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)# server = smtplib.SMTP_SSL('smtp.gamil.com', 465)
    try:    
        server.login(Details.my_kira_email, Details.my_kira_password)# server.login('youremail', 'password')
    except smtplib.SMTPAuthenticationError:
        speak_and_print_with_Jarvis('Sorry sir but I am not allowed to access your emails')
    try:
        server.sendmail(Details.my_kira_email, to, content)# server.sendmail('youremail', 'receiveremail', 'I am a good boy')
        error = False
    except smtplib.SMTPSenderRefused:
        error = True
    server.quit()
    if not error:
        speak_and_print_with_Jarvis('Email succesfully sent, Sir')


def chatboat_with_Jarvis():
    wish()
    text = ''
    n = 1
    while 'exit' not in text:
        if n == 1:
            inquiry = 'How may I help you, Sir?'
            speak_and_print_with_Jarvis(inquiry)
        else:
            enquiry = 'Any further requests, Sir?'
            speak_and_print_with_Jarvis(enquiry)
        text = speech_to_text()
        confirm = t.Network_Tester(text)
        if confirm:
            speak_and_print_with_Jarvis(network_error)
            exit()
        if 'name' in text:
            name()
        elif 'open Google' in text:
            open_google()
        elif 'open stack overflow' in text or 'open stackoverflow' in text:
            open_stackoverflow()
        elif 'open YouTube' in text:
            open_youtube()
        elif 'open Wikipedia' in text:
            open_wikipedia()
        elif 'time' in text:
            time()
        elif 'search' in text:
            search_url()
        elif 'find location' in text:
            location()
        elif 'how are you' in text:
            respond()
        elif 'open code' in text:
            open_code()
        elif 'play song' in text:
            play_song()
        elif 'write diary' in text:
            make_diary()
        elif 'see diary' in text:
            see_diary()
        elif 'send mail' in text:
            send_email()
        elif 'exit' not in text:
            speak_and_print_with_Jarvis(text)
            if unknown_value_error in text:
                n = 0 
        n += 1
    else:
        bye()