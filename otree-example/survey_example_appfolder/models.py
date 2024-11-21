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

author = 'your names and team objective go here'
doc = 'Your app description goes here'

class Constants(BaseConstants):
    name_in_url = 'survey-example'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    #we will only come to the group class when we look at advanced methods
    pass


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