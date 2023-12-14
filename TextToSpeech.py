from gtts import gTTS

s = input("Enter the File name:")

f = open(s)
text = f.read()

obj = gTTS(text=text, lang='en', slow=False)

f1 = input("Enter the Audio name to be saved:")

obj.save(f1)


'''
Output:
Enter the File name:StudentDetails.txt
Enter the Audio name to be saved:SampleAudio.mp3
'''