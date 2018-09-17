import tbapi
import streamlink


def get_raw_stream(url):
	return streamlink.streams(url)


class FRCStreamer:
	api_key = ""

	def get_event_streams(self, event_key):
		print(event_key)

	def get_stream_from_event(self, event_key):
		print(event_key)

	def get_all_streams(self):
		print("Getting all streams")
