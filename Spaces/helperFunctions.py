from .models import Compound
import time

def helper(compoundId, image, agent):
    # webp_format = 
    data = {}
    if compoundId == '0.1':
        time.sleep(1)
        belong_to = Compound.objects.filter(agent=agent).order_by('-id')[0]
        data['compoundId'] = belong_to.id
    else:
        data['compoundId'] = int(compoundId)
    data['comp_image'] = image
    return data


def room_helper(roomId, image):
    # webp_format = 
    data = {}
    data['room_image'] = image
    data['roomId'] = roomId
    return data