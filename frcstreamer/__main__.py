import tbapi
import streamlink
import datetime


def get_raw_stream(url):
	return streamlink.streams(url)


def make_tba(api_key):
	return tbapi.TBAParser(api_key)


class FRCStreamer:
	api_key = ""

	tba = make_tba(api_key)

	def get_event_streams(self, event_key):
		print(event_key)
		return []

	def get_stream_from_event(self, event_key):
		return self.get_event_streams(event_key)[0]

	def get_all_streams(self):
		print("Getting all streams")
		list_of_events = [event for event in self.tba.get_event_list() if event.start_date < datetime.datetime.now() < event.end_date]
		streams = []
		for event in list_of_events:
			streams.append({event.name: self.get_event_streams(event.key)})
		return streams
