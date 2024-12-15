from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player

from survey_example_appfolder.HelperFunctions import detect_screenout, detect_quota

class Welcome(Page):
    form_model = Player
    form_fields = ['device_type', 'operating_system', 'screen_height', 'screen_width', 'entry_question', 'eligible_question']


class QuotaPage(Page):
    form_model = Player
    form_fields = ['age_question', 'gender', 'hidden_input']
    
    def before_next_page(self):
        if self.player.gender == 2:
            self.group.counter += 1
        
        detect_quota(self)
        detect_screenout(self)


class SurveyPage(Page):
    form_model = Player
    form_fields = ['work', 'music_question', 'song_question'] #, 'vision_question', 'rorschach_question'
    
    def vars_for_template(self):
        return {"group_assignment": safe_json(self.player.group_assignment),
                'participant_label': safe_json(self.participant.label),
                'screenout': safe_json(self.player.screenout),
                'quota': safe_json(self.player.quota)}
    
    
class Html_overview(Page):
    form_model = Player

    def is_displayed(self):
        return self.player.group_assignment == 1


class PopoutPage(Page):
    form_model = Player
    form_fields = ['popout_question', 'popout_yes', 'popout_no', 'time_popout']
    
    
class RedirectPage(Page):
    def vars_for_template(self):
        return {'participant_label': safe_json(self.participant.label)}
    
    form_model = Player


class EndPage(Page):
    def vars_for_template(self):
        return {"group_assignment": safe_json(self.player.group_assignment)}


page_sequence = [Welcome,
                QuotaPage,
                SurveyPage,
                PopoutPage,           
                EndPage,
                RedirectPage]