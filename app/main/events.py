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

@socketio.on('userinput', namespace='/chat')
def left(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('someonesaid', {'msg': session.get('name') + ':' + message['msg']}, room=room)


@socketio.on('userinput2', namespace='/chat')
def left(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room2 = session.get('room2')
    emit('someonesaid2', {'msg': session.get('name') + ':' + message['msg']}, room=room2)

@socketio.on('choosevictim', namespace='/chat')
def choosevictim(data):
    room = session.get('room')
    emit('status', {'msg': data['victim'] + ' has been eliminated'}, room=room)
    emit('eliminated', {'msg': data['victim']}, room=room)



@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room2 = session.get('room2')
    leave_room(room2)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room2)

