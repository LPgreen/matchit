from set_window_size import set_window_size
from functions import vibro
set_window_size()

from kivymd.app import MDApp

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDButton, MDButtonText,MDIconButton
from kivy.clock import Clock

from kivy.lang import Builder
from random import choice

text_color = [(1,0,0,1),]
bg_color = 0,1,0,1
gl_radius = 10
gl_space = 3
gl_answer_cols = 3
gl_answer_rows = 4 # менять при разной ориентации

kv = f'''
MDScreen:
    md_bg_color: app.theme_cls.surfaceColor
    MDBoxLayout:
        id: main_layout
        orientation: 'vertical'
        padding: {gl_space*2}  
        
    
        MDGridLayout:
            id: main_grid
            cols: 1
            rows: 4
            spacing: {gl_space} 
            padding: {gl_space}  
                
            MDBoxLayout:
                id: target_layout
                theme_height: 'Custom'
                theme_height: 'Custom'
                orientation: 'vertical'
                spacing: {gl_space} 
                padding: {gl_space}              
                size_hint: (1, 0.1)
            
                MDButton:
                    id: target_btn
                    style: 'filled'
                    theme_width: 'Custom'
                    theme_height: 'Custom'
                    size_hint: (1, 0.1)
                    pos_hint: {{'center_x':0.5,'center_y':0.5}}
                    radius: {0, 0, gl_radius, gl_radius} 
                    theme_bg_color: 'Custom'
                    md_bg_color: 0.00784313725490196, 0.5333333333333333, 0.8196078431372549, 1.0   
                           
     
                    
                    MDButtonText:         
                        text: '1'
                        theme_width: 'Custom'
                        size_hint_y: 1
                        pos_hint: {{'center_x':0.5, 'center_y':0.5}}
                        font_style: 'Title'
                            
            MDGridLayout:
                id: answers_grid            
                cols: {gl_answer_cols}
                rows: {gl_answer_rows}      
                spacing: {gl_space} 
                padding: {gl_space}       
           
            MDButton:
                id: static_btn
                style: 'filled'
                theme_width: 'Custom'
                size_hint: (1, None)
                pos_hint: {{'center_x':0.5,'center_y':0.5}}
                radius: {gl_radius, gl_radius, 0, 0} 
                theme_bg_color: 'Custom'
                md_bg_color: 0.00784313725490196, 0.5333333333333333, 0.8196078431372549, 1.0          
     
                    
                MDButtonText:         
                    text: 'статистика'
                    theme_width: 'Custom'
                    size_hint_y: 1
                    pos_hint: {{'center_x':0.5, 'center_y':0.5}}
                    font_style: 'Title'                            
            
'''

class MatchIt(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Skyblue'
        self.theme_cls.dynamic_color= True
        main_layout = Builder.load_string(kv)
        self.target = main_layout.ids.target_btn
        answers_grid = main_layout.ids.answers_grid
        cols,rows = gl_answer_cols, gl_answer_rows
        for i in range(rows):
            for j in range(cols):
                answ_btn = MDButton(theme_width = 'Custom', theme_height = 'Custom',
                               size_hint = (1,1),
                               pos_hint = {'center_x':0.5,'center_y':0.5})

                answ_btn.style = 'elevated'
                answ_btn.theme_bg_color = 'Custom'
                answ_btn.theme_shadow_color = 'Custom'
                answ_btn.theme_shadow_offset = 'Custom'

                answ_btn.md_bg_color = 0.00784313725490196, 0.5333333333333333, 0.8196078431372549, 1.0
                answ_btn.shadow_color = 0,0.2,0.3,0.5
                answ_btn.shadow_offset = 2,-2
                answ_btn.elevation_level = 1
                answ_btn.shadow_softness = 0


                answ_btn.radius = 0,0,0,0
                answ_btn.shadow_radius = 0, 0, 0, 0
                if i+j == 0:
                    answ_btn.radius = gl_radius, 0, 0, 0
                    answ_btn.shadow_radius = gl_radius, 0, 0, 0
                if i==0 and j == cols-1:
                    answ_btn.radius = 0, gl_radius, 0, 0
                    answ_btn.shadow_radius = 0, gl_radius, 0, 0
                if i==rows-1 and j == cols-1:
                    answ_btn.radius = 0, 0, gl_radius, 0
                    answ_btn.shadow_radius = 0, 0, gl_radius, 0
                if i==rows-1 and j == 0:
                    answ_btn.radius = 0, 0, 0, gl_radius
                    answ_btn.shadow_radius = 0, 0, 0, gl_radius
                text = MDButtonText(text=str(choice(range(10))),
                                    pos_hint = {'center_x':0.5,'center_y':0.5},
                                    font_style = 'Title',
                                    )
                text.theme_font_size = 'Custom'
                text.font_size = answ_btn.width * 0.9
                text.theme_text_color = 'Custom'
                text.color = 1,1,1,0.9
                answ_btn.bind(on_release = self.on_release_answ_btn)
                answ_btn.add_widget(text)
                answers_grid.add_widget(answ_btn)

        return main_layout

    def on_release_answ_btn(self, instance):
        vibro(0.05, 100) # проверить на устройстве
        instance.disabled = True
        answ_text = instance.children[0]
        target = self.target.children[0]
        if hasattr(answ_text,'text'):
            if answ_text.text == target.text:
                instance.md_bg_color = 0.5,1,0.5,0.6
            else:
                instance.md_bg_color = 1, 0.5, 0.5, 0.8


if __name__ == '__main__':

    MatchIt().run()

    # меню - использовать ExpansionPanel https://kivymd.readthedocs.io/en/latest/components/expansionpanel/
    # и NavigationDrawer https://kivymd.readthedocs.io/en/latest/components/navigationdrawer/


 # TODO: сделать шрифт посветлее и побольше +
 #  - сделать логику приложения +
 #  - сделать answ_btn - через шаблон kv
 #  - terget button - сделать шрифт побольше
 #  - как сделать множественное выделение в pycharm
 #  - сделать курсор влево вправо для пролитывании выбора типа игр
 #  - сделать окностатитики и экран расширенной статистики
 #  - сделать меню для выбора типа игр (крыжики для того какие игры учитывать при пролиствании в курсоре)
 #  - сделать курсор влево вправо для выбора типа игр
 #  - как правильно организовать проект - разделать  - в движок engine только логику? а остально раскижать по экранам и формам?
 #  - сдеалть звук и картинки чтоб показывались
