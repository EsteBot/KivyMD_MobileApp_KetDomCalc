from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

class Tabs(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class Ket_Dom_App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
    
    # functions for KETDOM dosing tab  
    def generate_KETDOM_dose(self):
        try:
            animal_weight = float(self.root.ids.weight_input.text)
            vol = str((round(float((((animal_weight)/100))*0.125),2)))
            self.root.ids.weight_label.color = 0, 0.37, .93
            self.root.ids.weight_label.text = str('Injection Vol = '+vol+'mL')
            self.root.ids.inj_err_msg.text = str("")
            if animal_weight <= 0:
                self.root.ids.inj_err_msg.text = str("weight value must be > 0")
                self.root.ids.weight_label.text = str('')
                self.root.ids.egg_question_text1.text = str('')
                self.root.ids.egg_answer_text1.text = str('')
        except ValueError:
            self.root.ids.inj_err_msg.text = str("weight must be a numerical value")
            self.root.ids.weight_label.text = str('')


    release_count = 0
    def egg_button_on_release1(self):
        if self.release_count == 0:
            self.egg_question1()
            self.release_count += 1
            return

        if self.release_count == 1:
            self.egg_answer1()
            self.release_count = 0
            return 

    def egg_question1(self):
        self.root.ids.egg_question_text1.color = [.6, 0, 1]
        self.root.ids.egg_question_text1.text = str("How to tell if\nyour needle\nfeels used...")


    def egg_answer1(self):
        self.root.ids.egg_answer_text1.color = [.6, 0, 1]
        self.root.ids.egg_answer_text1.text = str("it says it seem's like...\nthere's no point!!!")

    def inj_vol_reset_func(self):
        self.release_count = 0
        self.root.ids.weight_label.color =  1,1,1
        self.root.ids.weight_label.text = str('Inj. Vol = [(weight/100)*0.125]mL')
        self.root.ids.weight_input.text = str('')
        self.root.ids.egg_question_text2.text = str('')
        self.root.ids.egg_answer_text2.text = str('')
        self.root.ids.inj_err_msg.text = str('')

    # functions for KETDOM ratio tab
    def generate_KETDOM_vols(self):
        try:
            final_vol = float(self.root.ids.end_vol_input.text)
            ket_vol = str((round(float((final_vol)*0.6),2)))
            dom_vol = str((round(float((final_vol)*0.4),2)))
            self.root.ids.ket_label.color = 0.51, 0.99, 0.22
            self.root.ids.ket_label.text = str('Ketamine Vol. = '+ket_vol+'mL')
            self.root.ids.dom_label.color = 0.51, 0.99, 0.22
            self.root.ids.dom_label.text = str('Dexdomitor Vol. = '+dom_vol+'mL')
            self.root.ids.ratio_err_msg.text = str("")
            if final_vol <= 0:
                self.root.ids.ratio_err_msg.text = str("Final Vol. must be > 0")
                self.root.ids.ket_label.text = str('')
                self.root.ids.dom_label.text = str('')
                self.root.ids.egg_question_text2.text = str('')
                self.root.ids.egg_answer_text2.text = str('')
        except ValueError:
            self.root.ids.ratio_err_msg.text = str("Vol. must be a numerical value")
            self.root.ids.ket_label.text = str('')
            self.root.ids.dom_label.text = str('')
            self.root.ids.end_vol_input.text = str('')


    release_count = 0
    def egg_button_on_release2(self):
        if self.release_count == 0:
            self.egg_question2()
            self.release_count += 1
            return

        if self.release_count == 1:
            self.egg_answer2()
            self.release_count = 0
            return 

    def egg_question2(self):
        self.root.ids.egg_question_text2.color = [.6, 0, 1]
        self.root.ids.egg_question_text2.text = str("How to tell if\nyour syringe is\ndepressed...")

    def egg_answer2(self):
        self.root.ids.egg_answer_text2.color = [.6, 0, 1]
        self.root.ids.egg_answer_text2.text = str("it says it feels...\nempty inside!!!")

    def ratio_reset_func(self):
        self.release_count = 0
        self.root.ids.ket_label.text = str('Ketamine Vol. = 0.6mL X Final Vol.')
        self.root.ids.ket_label.color = 1,1,1
        self.root.ids.dom_label.text = str('Dexdomitor Vol. = 0.4mL X Final Vol.')
        self.root.ids.dom_label.color = 1,1,1
        self.root.ids.egg_question_text1.text = str('')
        self.root.ids.egg_answer_text1.text = str('')
        self.root.ids.end_vol_input.text = str('')
        self.root.ids.ratio_err_msg.text = str('')

    # function to control switching between tabs
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''
        Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        instance_tab.ids.label.text = tab_text


Ket_Dom_App().run()