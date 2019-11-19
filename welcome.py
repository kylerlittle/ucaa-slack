class Welcome:
    """Constructs the onboarding message and stores the state of which tasks were completed."""

    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Welcome to The Movement! :wave: We're so glad you're here. :blush:\n\n"
            ),
        },
    }
    DIVIDER_BLOCK = {"type": "divider"}
    MESSAGE_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Based on the information you've provided, I added you to the following groups:"
                "\n".join(*get_user_channels())
            ),
        },
    }

    def __init__(self, channel):
        self.channel = channel
        self.username = "The Movement Bot"
        self.icon_emoji = ":basketball:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                self.MESSAGE_BLOCK
            ],
        }

    @staticmethod
    def get_user_channels():
        return ["pac-12-saac", "pac-12-m-cross-country"]