"""Returns FRC streams"""
import datetime
import tbapi
import streamlink


def get_raw_stream(url):
    """Gets the raw streams"""
    return streamlink.streams(url)


def make_tba(api_key):
    """Makes a TBA parser"""
    return tbapi.TBAParser(api_key, cache=False)


def validdate(event):
    return event.start_date <= datetime.datetime.now() <= event.end_date


class FRCStreamer:
    """FRCStreamer"""

    def __init__(self, api_key):
        self.tba = make_tba(api_key=api_key)

    def get_event_streams(self, event_key):
        """Get all streams for an event"""
        print(event_key)
        strems = []
        event = self.tba.get_event(event_key)
        for cast in event.webcasts:
            if cast.type == "twitch":
                castURL = "https://twitch.tv/{}".format(cast.channel)
            else:
                return
            strems.append(get_raw_stream(castURL))
        return strems

    def get_stream_from_event(self, event_key):
        """Get 1 stream from an event"""
        return self.get_event_streams(event_key)[0]

    def get_all_streams(self):
        """Get every live FRC feed"""
        print("Getting all streams")
        list_of_events = [event for event in self.tba.get_event_list() if validdate(event)]
        streams = []
        for event in list_of_events:
            streams.append({event.name: self.get_event_streams(event.key)})
        return streams
