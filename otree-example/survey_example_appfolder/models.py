from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random
#from survey_example_appfolder.HelperFunctions import random_number

author = 'Eszter Diána Kocsis'
#'your names and team objective go here'
doc = 'Your app description goes here'

class Constants(BaseConstants):
    name_in_url = 'survey-example'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    #pass
    def creating_session(self):
        for p in self.get_players():
            p.group_assignment = random.Random().randint(0, 1)
            #p.group_assignment = random_number(0,2)

class Group(BaseGroup):
    #we will only come to the group class when we look at advanced methods
    #pass
    counter = models.IntegerField(initial = 0)


class Player(BasePlayer):
    #this is the most important feature of this file. We can collect all the variables used on the html pages here
    
    #The Variables are structured on the base of pages
    entry_question = models.StringField(
        label="Please enter your name"
    )
    
    age_question = models.IntegerField(
        label="How old are you?",
        min=16,
        max=99
    )
    
    gender_question = models.BooleanField(
        label="What is your gender?",
        choices=['male', 'female', 'other']
    )
    
    work_question = models.BooleanField(
        label="What is your occupation?",
        choices=['student', 'part-time worker', 'full-time worker', 'pensioner', 'jobless', 'other']
    )
    
    music_question = models.FloatField(
        label="How many hours a day do you listen to music on average?",
        min=0,
        max=24
    )
    
    song_question = models.StringField(
        label="What is the title of your favourite song?"
    )           
    
    # Task1 -image questions
    vision_question = models.BooleanField(
        blank=True,
        label="What number do you see on the picture?",
        choices=['14', '24', '94', '74', 'What number?']
    )
    
    rorschach_question = models.StringField(
        blank=True,
        label="What do you see on the picture?"
    )
    
    group_assignment = models.IntegerField()
    
    # Task2 - popout question
    popout_question = models.IntegerField(blank=True)
    popout_yes = models.StringField(blank=True)
    popout_no = models.StringField(blank=True)
    
    # Task3 - capturing time & screen size
    time_popout = models.StringField(initial='-999')
    screen_height = models.IntegerField(blank=True, 
                                        initial=-999)
    screen_width = models.IntegerField(blank=True, 
                                       initial=-999)
    