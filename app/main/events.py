from flask import session
from flask.ext.socketio import emit, join_room, leave_room
from .. import socketio

@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    print "session1", session
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)

@socketio.on('joinedsecondroom', namespace='/chat')
def joinedsecondroom(message):
    room2 = session.get('room2')
    join_room(room2)
    print "session2", session
    emit('status2', {'msg': session.get('name') + ' has entered the room.'}, room=room2)

@socketio.on('text', namespace='/chat')
def left(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)

@socketio.on('text2', namespace='/chat')
def left(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room2 = session.get('room2')
    emit('message2', {'msg': session.get('name') + ':' + message['msg']}, room=room2)



@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

