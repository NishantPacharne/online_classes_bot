# A Bot Which Attends the Online classes

This is a bot made with python (selenium & pyautogui), what this bot does is, it opens up whatsapp then opens my school group and checks for the most recent google meet link , if there is any, the link is clicked and then the meeting is joined and the most fascinating part when the bot joins the meeting it also greets according to time and after a particular time the bot leaves meeting by sending a thank you message, so teachers never catch that it is a bot.

---

# Installation
    pip install requirements.txt

---

# How can you use it efficiently

On the first run of program you will have to login your whatsapp account as well as manually sign in into gmail account , and then the program remebers you, After that you will have to do some changes in the code. First in main.py on line no 13 change the path of your chrome driver, then on line no 26 change School Group with your desired user name of whatsapp or with the name of your school whatsapp group so the program clicks on it, then on line no 72 change the time period that is 20 with total time of your class in seconds, so for eg if my class ends in 40 minutes i would enter time 40 minutes so the program sends a message of thank you and leaves meeting in next 40 minutes and again goes to whatsapp and keeps searching for a new link.

#### If you want to completely automate this , you can upload this on cloud so the program would keep running and the bot would keep attending your classes !!
