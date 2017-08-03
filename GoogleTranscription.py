from google.cloud import speech##imports speech class from google speech API
import speech_recognition as sr
import time

##This class is a program that converts whether an audio file or real time voice commands to text using google speech API
##@author Bidhan Bhandari
class GoogleTranscription:
    
    def __init__(self):
        self.speech_client = speech.Client()
        self.r = sr.Recognizer()
        
    ##Function that transcribes a given audio file encoded in .FLAC format in some text file that user desires
    def transcribeAudioFile(self):
        voice_file = input('Enter your properly encoded .flac audio file: ')
        try:
            with open(voice_file, 'rb') as audio_file:##reads audio file given by user
            
                ##initializes a sample object so as to make audio ready for transcription
                sample = speech_client.sample(stream = audio_file, encoding = speech.Encoding.FLAC, sample_rate = 16000)
            
                ##sample object sent for streaming recognition. streaming_recognize can recognize audio of upto 60 seconds.
                ##Returns a list of dictionary
                results = sample.streaming_recognize(language_code = 'en-US', profanity_filter = True, interim_results = False)
            
                print('TRANSCRIBING...')
            
                ##visits each object inside list
                for result in results:
                    ##visits two entities that was in dictionary object, namely; transcript and confidence
                    for alternative in result.alternatives:
                        ##returns transcript of audio file and prints it on console
                        print('Transcript: ' + alternative.transcript)
                        print('\n')
                        ##returns confidence with which google cloud speech transcripts audio file and prints it on console
                        print('Confidence: ' + str(alternative.confidence))
    
        except FileNotFoundError as e:
            print('FILE '+ voice_file + ' NOT FOUND!\nCHECK AVAILIABILTY OF FILE AND MAKE SURE FILENAME AND EXTENSION IS CORRECT!\nSTARTING OVER AGAIN...')
            time.sleep(2)
            transcribeAudioFile()
            
    def transcribeCommand(self):
        with sr.Microphone() as source:
            print("Say something!")
            audio = self.r.listen(source)
            print('TRANSCRIBING...')
 
        # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("You said: " + self.r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def main():
    transcribe = GoogleTranscription()
    functionSelection = int(input('Enter 1 if you have audio file or 2 if you want your real time voice to be transcribed '))
    while (not(functionSelection == 1 or functionSelection == 2)):
        print('You entered other numbers or letters except 1 or 2. Please Check your input and try again!!')
        functionSelection = input('Enter 1 if you have audio file or 2 if you want your real time voice to be transcribed ')
    else:
        if functionSelection == 1:
            transcribe.transcribeAudioFile()
        else:
            transcribe.transcribeCommand()
        
##Execution of program begins here
if __name__ == '__main__':main()
    

            
    
