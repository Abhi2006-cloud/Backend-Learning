from datetime import datetime
import uuid

sessions = {}

def create_session(user):
    """
    Creates a new session for the given user.
    Returns the generated session ID.
    """
    session_id = str(uuid.uuid4())
    sessions[session_id] = user
    return session_id


def get_user(session_id):
    """
    Returns the user associated with the session ID.
    """
    return sessions.get(session_id)


def delete_session(session_id):
    """
    Removes the session from memory.
    """
    sessions.pop(session_id, None)






