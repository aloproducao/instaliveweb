import pickle
from flask import session
from InstaLiveCLI import InstaLiveCLI

def start_broadcast():
    ig = InstaLiveCLI(auth=session['settings'])
    print(session['settings'])

    print('> Starting Broadcast')
    start = ig.start_broadcast()
    print('- Broadcast Started',start)
    return start

def stop_broadcast():
    ig = InstaLiveCLI(auth=session['settings'])
    print(session['settings'])
    print('> Stopping Broadcast')
    stop = ig.end_broadcast()
    print('- Broadcast Stopped', stop)
    return stop

def get_viewers():
    ig = InstaLiveCLI(auth=session['settings'])
    print("> Getting Viewers")
    user, id = ig.get_viewer_list()
    return user

def get_comments():
    ig = InstaLiveCLI(auth=session['settings'])
    print("> Getting Comments")
    return ig.get_comments()

def send_comments(text):
    ig = InstaLiveCLI(auth=session['settings'])
    print("> Sending Comments :"+text)
    return ig.send_comment(text)

def toggle_mute_comments(mute):
    ig = InstaLiveCLI(auth=session['settings'])
    if mute:
        print("> Unmute Comments")
        return ig.unmute_comment()
    else:
        print("> Mute Comments")
        return ig.mute_comments()
