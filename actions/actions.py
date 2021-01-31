# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import webbrowser

class ActionVideo(Action):

    def name(self) -> Text:
        return "action_video"

    async def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: "DomainDict",)->List[Dict[Text,Any]]:
          video_url="https://www.youtube.com/watch?v=gVkbhzNzBTY"
          dispatcher.utter_message("please wait......Playing your video in your browser now")
          webbrowser.open(video_url)

          return []


class ActionVideo2(Action):

    def name(self) -> Text:
        return "action_video2"

    async def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: "DomainDict",)->List[Dict[Text,Any]]:
          video_url ="https://www.youtube.com/watch?v=QE7MAyHTNSY"
          dispatcher.utter_message("please wait......Playing your video in your browser now")
          webbrowser.open(video_url)

          return []
