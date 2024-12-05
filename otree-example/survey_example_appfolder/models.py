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
from survey_example_appfolder.HelperFunctions import random_number

author = 'Eszter Diána Kocsis'
#'your names and team objective go here'
doc = 'Your app description goes here'

class Constants(BaseConstants):
    name_in_url = 'survey-example'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.group_assignment = random.Random().randint(0, 1)
            #p.group_assignment = random_number(0,2)


class Group(BaseGroup):
    counter = models.IntegerField(initial = 0)


class Player(BasePlayer):
    entry_question = models.StringField(
        label="Please enter your name"
    )
    
    age_question = models.IntegerField(
        label="How old are you?",
        min=16,
        max=99
    )
    
    #gender_question = models.BooleanField(
    #    label="What is your gender?",
    #    choices=['male', 'female', 'other']
    #)
    
    
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
    
    #Assignment 3 - Task1 -image questions
    vision_question = models.BooleanField(
        blank=True,
        label="What number do you see on the picture?",
        choices=['14', '24', '94', '74', 'What number?']
    )
    
    rorschach_question = models.StringField(
        blank=True,
        label="What do you see on the picture?"
    )
    
    # Assigment 3: Task 1
    group_assignment = models.IntegerField()
    
    # Assignment 3: Task2 - popout question
    popout_question = models.IntegerField(blank=True)
    popout_yes = models.StringField(blank=True)
    popout_no = models.StringField(blank=True)
    
    # Assignment 3: Task3 - capturing time & screen size
    device_type = models.IntegerField()
    operating_system = models.IntegerField()
    time_popout = models.StringField(initial='-999')
    screen_height = models.IntegerField(blank=True, 
                                        initial=-999)
    screen_width = models.IntegerField(blank=True, 
                                       initial=-999)
    
    
    # Assignment 4: 
    screenout = models.BooleanField(initial=0)
    quota = models.BooleanField(initial=0)
    eligible_question = models.IntegerField()
    
    #age = models.IntegerField(max=110, min=1)  #we can also have max and min guidelines
    gender = models.IntegerField(initial=-999, label='Gender Question')  #we can add an initial value or a different label
    hidden_input = models.IntegerField(initial=50, blank=True)
    gender_counter = models.IntegerField(initial = 0)