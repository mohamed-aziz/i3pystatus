
from i3pystatus.core.command import run_through_shell
from i3pystatus import IntervalModule


class Emacs(IntervalModule):

    interval = 5  # check if emacs is running every 5 seconds

    settings = (
        "format",
        "color",
        "status"        
    )

    format = "{message}"
    status = {
        "RUN": "is running",
        "NRU": "is not running"
    }
    message = status["RUN"]
    color = "#FFFFFF"
    color_not_running = "#E01836"
    on_leftclick = "unleash_the_power"

    def is_running(self):
        return run_through_shell("systemctl is-active --user emacs".split()).out.split()[0] == 'active'

    def run(self):
        if self.is_running():
            self.output = {
                'full_text': self.format.format(**{
                    "status": self.status["RUN"]
                }),
                "color": self.color,
            }
        else:
            self.output = {
                'full_text': self.format.format(**{
                    "status": self.status["NRU"]
                }),
                "color": self.color_not_running,
            }

    def unleash_the_power(self):
        if not self.is_running():
            run_through_shell("systemctl start --user emacs".split())
