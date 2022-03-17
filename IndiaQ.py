import pyttsx3

iorona = pyttsx3.init('sapi5')
voices = iorona.getProperty('voices')
iorona.setProperty('voice', voices[1].id)

def speak(audio):
    iorona.say(audio)
    iorona.runAndWait()
print(' \t\t\t\t\t\t\t INDIA Q')
speak('Hello, welcome to IndiaQ!')
speak('Are you ready to play (yes or no): ')
ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 5
if ans.lower() == 'yes':
    speak('1. India is a federal union comprising twenty-nine states and how many union territories?')
    ans = input('1. India is a federal union comprising twenty-nine states and how many union territories?')
    if ans.lower() == '7':
        score += 1
        speak('Correct')
    else:
        speak('Incorrect')
    speak('Which of the following is the capital of Arunachal Pradesh?')
    ans = input('2. Which of the following is the capital of Arunachal Pradesh?')
    if ans.lower() == 'itanagar':
        score += 1
        speak('Correct')
    else:
       speak('Incorrect')
    speak('Which state has the largest area?')
    ans = input('3. Which state has the largest area?')
    if ans.lower() == 'rajasthan':
        score += 1
        speak('Correct')
    else:
        speak('Incorrect')
    speak('In what state is the Elephant Falls located?')
    ans = input('4. In what state is the Elephant Falls located?')
    if ans.lower() == 'meghalaya':
        score += 1
        speak('Correct')
    else:
        speak('Incorrect')
    speak('Which is the largest coffee producing state of India?')
    ans = input('5. Which is the largest coffee producing state of India?')
    if ans.lower() == 'karnataka':
        score += 1
        speak('Correct')
    else:
        speak('Incorrect') 
        
speak('thaky for playing')
print('Thankyou for playing, you got', score, "questions correct")
mark = (score/total_q) * 100
print("Marks:",str(mark) + '%')
speak('Goodbye')
print('made by Sabuj Golui')