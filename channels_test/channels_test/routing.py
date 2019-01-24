from channels.routing import route
from channels_app.consumers import ws_message

channel_routing = [
    route("websocket.receive", ws_message),
    # route("http.request", "channels_app.consumers.http_consumer"),
]
