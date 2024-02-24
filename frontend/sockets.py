import socketio

socket = socketio.SimpleClient()


def connect( url, token):
    socket.connect(url, auth={"token": token})


def joinCourse(courseId):
    socket.emit("join_course", courseId)




def send_message( location, locationId, body):
    socket.emit("sendMessage",
                     {
                         "location": location,
                         "body": body,
                         "locationId": locationId
                     }
                     )



