from i3pystatus import IntervalModule
from i3pystatus.core.command import run_through_shell
from shutil import which

# this is weird but xbacklight does not work for me.
class MyBacklight(IntervalModule):

    settings = (
        ('format', 'the format used to display backlight'),
        ('step', 'The step of increase or decrease'),
        ('icon', 'Icon to decorate'),
    )

    format = "{icon}{percentage}{symbole}"
    step = 5
    interval = 5
    icon = ''
    on_upscroll = "lighter"
    on_downscroll = "darker"

    has_light = which('light') is not None


    def run(self):
        if self.has_light:
            self.percentage = run_through_shell(['light']).out.splitlines()[0]
            self.output = {
                'full_text': self.format.format(**{
                    'percentage': self.percentage,
                    'symbole': '%',
                    'icon': self.icon
                })
            }
    
    def lighter(self):
        if self.has_light:
            run_through_shell(["light", "-A", str(self.step)])

    def darker(self):
        if self.has_light:
            run_through_shell(["light", "-U", str(self.step)])
