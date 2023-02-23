import flet
from flet import *
import phonenumbers as pn
import re
import pyperclip


def main(page : Page):
    page.title = "Samixx Web Scrapper"
    page.window_width = 500
    page.window_height = 700
    page.window_resizable = False
    page.theme_mode = "light"
    page.scroll = "adaptive"
    
    
    def copy_output(e):
        pyperclip.copy(info_output.value)
        page.update()
        
     
    def change_theme(e):
        # The Code Below Makes The Theme Dark if the theme is originally light
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        #The code below changes the label from light theme to dark theme
        theme.label = "Light Theme" if page.theme_mode == "light" else "Dark Theme"
        page.update()
    
    
    
    def email_button(e):
        emailRegex =re.compile(r'''(
        [a-zA-Z0-9._%+-]+       # username
        @                       # @ symbol
        [a-zA-Z0-9.-]+          # domail name
        (\.[a-zA-Z]{2,4})       # dot-something
        )''', re.VERBOSE)
        matches = []
        # Find matches in mail
        for groups in emailRegex.findall(info_input.value):
            matches.append(groups[0])
        # Copy results to the clipboard.
        if len(matches) > 0:
            info_input.value.join('\n'.join(matches))
            email_result = '\n'.join(matches)
            email.data = email_result
            info_output.value = f"{email.data}"
            
        elif len(matches) <= 0:
            info_output.value = "No Email Addresses Was Found"
        page.update()
        
        
    
    def number_button(e):
        for match in pn.PhoneNumberMatcher(info_input.value, "NG"):
            number = pn.format_number(match.number, pn.PhoneNumberFormat.INTERNATIONAL)
            info_output.value = number
        page.update()
    
    
    def email_number_button(e):
        pass
        

        
    
    
    page.appbar = AppBar(
        title = Text(
            value = "Samixx numMail-Scrapper 1.0",
            size = 20,
            color = colors.WHITE
        ),
        bgcolor = colors.GREEN_200,
        center_title = True 
    )
    
    
    info_input = TextField(
        label = "Enter Information"
    )
    
    email = ElevatedButton(
        text = "Get Email",
        width = 100,
        height = 50,
        on_click = email_button,
        data = 0
    )
    
    number = ElevatedButton(
        text = "Get Number",
        width = 130,
        height = 50,
        on_click = number_button,
    )
    
    email_number = ElevatedButton(
        text = "Get Email And Phone Number",
        width = 230,
        height = 50,
        on_click = email_number_button,
        data = 0
    )
    
    info_output = TextField(
        multiline = True,
        text_align = "center",
        helper_text = "The Information Above Is The Result Gotten From The URl",
        disabled = True
    )
    
    clip_copy = IconButton(
        icon = icons.COPY_OUTLINED,
        on_click = copy_output,
        data = 0,
        tooltip = "Copy Information"
    )

    
      
    theme = Switch(
        label = "Light Theme",
        on_change = change_theme
    )  
    
    page.add(
        Container(
            content = Column(
                [
                    theme,
                    info_input,
                    Row(
                        [
                            email,
                            number
                        ],
                        spacing = 80,
                        alignment = "center"
                    ),
                    Row(
                      [
                          email_number
                      ],
                      alignment = "center"
                    ),
                    
                    Row(
                        [
                            info_output,
                            clip_copy
                        ],
                        alignment = "center"
                    )
                    
                ],
                spacing = 30
            ),
        )
    )
    
    
flet.app(target = main)