# GROWW-T8
Team ID: GROWW-T8 | Team Members: Pranjal Goyal &amp; Abhishek Thakur

# Instructions

**GrowwBot** is a context based chatbot which provides FAQs based on user as well as page context.

**GrowwBot** is made with simple HTML,CSS and Javascript and Django as a framework. We have also used Chatterbot library (An AI/ML based training library) to train the chatbot so that it can also answer FAQ using chat input box. The API endpoints are made using Django-Rest Framework.

![Django](https://img.shields.io/badge/django%20-%23092E20.svg?&style=for-the-badge&logo=django&logoColor=white) ![HTML5](https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white") ![Javscript](https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) 
![Chatterbot](https://img.shields.io/badge/Chatterbot-1.0.2-blue)


# Features!
  - Contextual Chatbot with NLP processing using Chatterbot library
  - Admin Page to add more FAQs
  - API support for all parts post, get and patch requests.
  - Easy Intergration
  - AJAX implementation

### Live Demo (Please Give it few seconds to load the gif 😀)
![](livedemo.gif)

### More About Demo
This is a short gif to show how it is working. As you can see when we moved to Stocks page, it asked questions related to stocks.
So it uses page context and user context (if the user is logged in) to display relevant questions.

The UI is kept simple, as the chatbot functionality was the main focus.
We have also made a panel to edit and make new FAQs which is shown in the full demo.

Also, users can directly type questions in the chatbot and even if the question is not related to the current context, it will answer it, the chatbot is trained on all questions and can answer effectively.

### Installation

Install the dependencies and just start the server. (Then you are ready to run)
NOTE : Requires Python3.7

#### Method:
```sh
$ cd groww_chatbot 
$ pip install -r requirements.txt
$ python -m spacy download en
$ python manage.py runserver
```

### Todos
 - Adding A dark theme
 - Improving CSS


License
----

MIT

**You can modilfy it or break it, do whatever you need**

### Mentions

<img src="https://pbs.twimg.com/profile_images/1239848399769202689/5S6D0btQ.jpg" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="100" height="100" />

***We would Like to Thank the [CRIO.DO](https://www.crio.do/) Team and all memebers for orgainsing a event that helps students in thier development skills. The Winter of doing provided a hands on approach on things. I would also like to Thank the members on slack to help me with my queries. I enjoyed making this Project, I hope you too have enjoyed it. Thank You and Have a Nice Day.🎇***
