import Tester as t

import webbrowser as wb

from wikipedia.exceptions import PageError

import os

import Details

network_error = 'Sorry but my server is currently down'
unknown_value_error = 'Sorry, but I did not understand that'
playsound_error = 'Sorry but my speech service is down'
Name = 'My name is Kiyomi'
Reply = 'I am fine kira'
bye_message = 'Bye, kira! Take Care! Consult me whenever you need. Kiyomi is always there to support you!'
limit_search = 'enough search'
limit_search_location = 'enough location'
gtts_error = 'You are offline'
limit_wiki = 'enough Wikipedia'
limit_songs = 'enough song'
limit_diary = 'no'


def wish():
    import datetime
    hour = float(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak_and_print('Good morning! kira!')
    elif hour >= 12 and hour < 18:
        speak_and_print('Good afternoon kira!')
    else:
        speak_and_print('Good evening kira!')


def name():
    speak_and_print(Name)


def time():
    from time import ctime
    Time = ctime()
    speak_and_print(Time)


def speak(statement):
    from playsound import PlaysoundException
    from playsound import playsound as play
    import gtts 
    try:
        voice_data = gtts.gTTS(statement, lang = 'en')
        voice_data.save('Voice.mp3')
        play('Voice.mp3')
        os.remove('Voice.mp3')
    except PlaysoundException:
        print(playsound_error)
        os.remove('Voice.mp3')
        exit()
        # If you face this consider uninstalling your playsound module using command prompt by typing in
        # pip uninstall playsound
        # and then re-installing it's 1.2.2 version by typing in
        # pip install playsound==1.2.2
        # As your PC may be facing some plug-in errors so lowering your playsound version is a good approach
        # Hence there is a great chance that this handy alternative will resolve your issues amicably
    except gtts.tts.gTTSError:
        os.remove('Voice.mp3')
        print(gtts_error)
        exit()
        
        
      
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
            question = 'Search for what'
            speak_and_print(question)
        else:
            further_question = 'Do you want anything more to search'
            speak_and_print(further_question)
        query = speech_to_text()
        confirm = t.Network_Tester(query)
        if confirm:
            print(network_error)
            exit()
        if 'exit' in query:
            bye()
            exit()
        elif unknown_value_error in query:
            speak_and_print(query)
            n = 0
        elif limit_search in query:            
            speak_and_print('Very well')
        else:
            url = f'https://google.com/search?q={query}'
            wb.open_new_tab(url)
            speak_and_print(f'Here is what I got for {query}')
        n += 1
    else:
        speak_and_print('Fine')
            

def location():
    location = ''
    n = 1
    while limit_search_location not in location:
        if n == 1:
            location_question = 'Please tell me the location.'
            speak_and_print(location_question)
        else:
            further_location_question = 'Do you want to locate anything else?'
            speak_and_print(further_location_question)
        location = speech_to_text()
        confirm = t.Network_Tester(location)
        if confirm:
            print(network_error)
            exit()
        if 'exit' in location:
            bye()
            exit()
        elif unknown_value_error in location:
            speak_and_print(location)
            n = 0 
        elif limit_search_location in location:
            speak_and_print('Very')
        else:
            location_url = f'https://google.nl/maps/place/{location}/&amp'
            wb.open_new_tab(location_url)
            speak_and_print(f'Here is the location of {location}')
        n += 1
    else:
        speak_and_print('Well')


def speak_and_print(sentence):
    speak(sentence)
    print(sentence)


def respond():
    speak_and_print(Reply)


def bye():
    speak_and_print(bye_message)
    import datetime
    hour = float(datetime.datetime.now().hour)
    if hour >= 20 and hour <= 4:
        speak_and_print('Good night kira!')


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
            question = 'Search whose wikipedia'
            speak_and_print(question)
        else:
            further_question = 'Whose else wikipedia do you want to search'
            speak_and_print(further_question)
        query = speech_to_text() 
        confirm = t.Network_Tester(query)
        if confirm:
            print(network_error)
            exit()
        if 'exit' in query:
            bye()
            exit()
        elif unknown_value_error in query:
            speak_and_print(query)
            n = 0
        elif limit_wiki in query:            
            speak_and_print('Alright')
        else:
            try:
                info = wiki.summary(query, sentences = 2)
                speak_and_print('According to wikipedia...')
                speak_and_print(info)
            except PageError:
                speak_and_print(f'Sorry, but I did not find anything for {query}')
            except Exception:
                speak_and_print(f'Sorry but I can not tell what exactly is {query}.') 
        n += 1                                                                        
    else:
        speak_and_print('kira')
    

def open_code():
    vs_code = # "VSCode Location with .exe extension"
    os.startfile(vs_code)


def play_song():
    n = 1
    Song = ''
    while limit_songs not in Song: 
        if n == 1:
            question = 'Which song do you wish to play'
            speak_and_print(question)
        else:
            further_question = 'Which other song do you wish to play'
            speak_and_print(further_question)
        Song = speech_to_text()
        confirm = t.Network_Tester(Song)
        if confirm:
            print(network_error)
            exit()
        song = Song.lower()
        if 'exit' in song:
            bye()
            exit()
        elif unknown_value_error in Song:
            speak_and_print(song)
            n = 0
        elif limit_songs in song:            
            speak_and_print('Okay')
        else:
            try:
                SONG = #f'Your songs folder location\\{song}.mp3' 
                from playsound import playsound as play
                play(SONG)
            except Exception:
                speak_and_print(f'I did not get {song} song')
                n = 0
        n += 1
    else:
        speak_and_print('kira')
        
    
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
            speak_and_print('Say what you want?')
        else:
            speak_and_print('Do you want to modify the content')
        content = speech_to_text()
        confirm = t.Network_Tester(content)
        if confirm:
            print(network_error)
            exit()
        if limit_diary == content:
            if n == 1:
                speak_and_print('''You didn't even say anything''')
            else:
                speak_and_print('Diary successfully made')
            break
        elif unknown_value_error in content:
            speak_and_print(content)
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
                speak_and_print('Something went wrong')
                n = 0
            finally:
                confirm = False
        n += 1


def see_diary():
    updates = date_details()
    file = (f'{updates}.txt')
    speak_and_print('Tell me to close the file when you want it to be')
    fh = open(file, 'r')
    speak_and_print(fh.read())
    response = ''
    while response != 'close':
        response = speech_to_text()
        if 'exit' in response:
            fh.close()
            bye()
        elif network_error in response:
            fh.close()
            print(network_error)
            exit()
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
        speak_and_print('Send email to whom?')
        receiver = speech_to_text()
        confirm = t.Network_Tester(receiver)
        if confirm:
            print(network_error)
            exit()
        if unknown_value_error in receiver:
            speak_and_print(unknown_value_error)
        else:
            try:
                to = Details.Records[receiver]
                break
            except KeyError:
                speak_and_print(f'I could not find {receiver}')
    while 1:    
        speak_and_print('What should I say?')
        content = speech_to_text()
        confirm = t.Network_Tester(content)
        if confirm:
            print(network_error)
            exit()
        if unknown_value_error in content:
            speak_and_print(unknown_value_error)
        else:
            break
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)# server = smtplib.SMTP_SSL('smtp.gamil.com', 465)
    try:
        server.login(Details.my_kira_email, Details.my_kira_password)# server.login('youremail', 'password')
    except smtplib.SMTPAuthenticationError:
        speak_and_print('Sorry but I am not allowed to access your emails')
    try:    
        server.sendmail(Details.my_kira_email, to, content)# server.sendmail('youremail', 'receiveremail', 'message')
        error = False
    except smtplib.SMTPSenderRefused:
        error = True
    server.quit()
    if not error:
        speak_and_print('Email succesfully sent')


def chatbot():
    wish()
    text = ''
    n = 1
    while 'exit' not in text:
        if n == 1:
            inquiry = 'How may I help you?'
            speak_and_print(inquiry)
        else:
            enquiry = 'Any further requests?'
            speak_and_print(enquiry)
        text = speech_to_text()
        confirm = t.Network_Tester(text)
        if confirm:
            print(network_error)
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
            speak_and_print(text)
            if unknown_value_error in text:
                n = 0 
        n += 1
    else:
        bye()
