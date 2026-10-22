from set_window_size import set_window_size
set_window_size()

from kivymd.app import MDApp

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivy.lang import Builder
from random import choice

kv = '''
MDBoxLayout:
    id: main_layout
    orientation: 'vertical'
    

    MDGridLayout:
        id: main_grid
        cols: 1
        rows: 3
        line_width: 2
        line_color: 1,1,1,1
            
        MDBoxLayout:
            id: target_layout
            theme_height: 'Custom'
            orientation: 'vertical'
            line_color: 1,1,0,1
            line_width: 1
            size_hint: (1,None)
            height: 100
        
            MDButton:
                id: target_btn
                style: 'outlined'
                theme_width: 'Custom'
                size_hint: (1,None)
                height: 100
                pos_hint: {'center_x':0.5,'center_y':0.5}
                
                MDButtonText:         
                    text: '1'
                    theme_width: 'Custom'
                    size_hint_y: 1
                    pos_hint: {'center_x':0.5, 'center_y':0.5}
    
        MDBoxLayout:
            id: space_layout 
            theme_height: 'Custom'
            size_hint: (1,None)
            height: 50
            line_width: 2
            line_color: 1,0,0,1     
    
        MDGridLayout:
            id: answers_grid
            line_color: 1,0,1,1
            line_width: 2
            cols: 3
            rows: 4               
            
'''

class MatchIt(MDApp):
    def build(self):
        # main_layout = MDBoxLayout(orientation='vertical')
        # main_grid = MDGridLayout()
        # main_grid.cols = 1
        # main_grid.rows = 3
        # target_layout = MDBoxLayout(orientation='vertical',size_hint = (1,None))
        # target_layout.height = 100
        # target_btn = MDButton(style = 'outlined',
        #                       theme_width = 'Custom',
        #                       size_hint = (1,None),
        #                       height = 100,
        #                       pos_hint = {'center_x':0.5,'center_y':0.5})
        #
        # target_btn.add_widget(MDButtonText(text = '1',theme_width='Custom',
        #                                    size_hint_y = 1,
        #                                    pos_hint = {'center_x':0.5,'center_y':0.5}))
        # target_layout.add_widget(target_btn)
        # target_layout.line_color = 1,1,0,1
        # target_layout.line_width = 1
        # main_grid.add_widget(target_layout)
        # main_grid.line_width = 2
        # main_grid.line_color = 1,1,1,1
        # space_layout = MDBoxLayout(theme_height = 'Custom',size_hint = (1,None),height = 50)
        # space_layout.line_width = 2
        # space_layout.line_color = 1,0,0,1
        #
        main_layout = Builder.load_string(kv)
        answers_grid = main_layout.ids.answers_grid
        for i in range(4):
            for j in range(3):
                btn = MDButton(theme_width = 'Custom', theme_height = 'Custom',
                               size_hint = (1,1),
                               pos_hint = {'center_x':0.5,'center_y':0.5})
                btn.style = 'outlined'
                text = MDButtonText(text=str(choice(range(10))),pos_hint = {'center_x':0.5,'center_y':0.5}
                                    )
                btn.add_widget(text)
                answers_grid.add_widget(btn)
        # main_grid.add_widget(space_layout)
        # main_grid.add_widget(answ _grid)
        # main_layout.add_widget(main_grid)
        return main_layout

if __name__ == '__main__':

    MatchIt().run()

    # меню - использовать ExpansionPanel https://kivymd.readthedocs.io/en/latest/components/expansionpanel/
    # и NavigationDrawer https://kivymd.readthedocs.io/en/latest/components/navigationdrawer/