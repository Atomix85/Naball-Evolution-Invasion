#This script was programmed by MarcoIT to the website : "blenderartists.org"

import bge, aud


device = aud.device()
device.distance_model = aud.AUD_DISTANCE_MODEL_INVERSE_CLAMPED


KX_GameObject = bge.types.KX_GameObject



def playSound(file):
	
	device = aud.device()
	sound = aud.Factory.file(file)
	sound = sound.pitch(2)
	device.play(sound)

class Audio:
    def __init__(self):
        self.buffered = {}
        self.handles = []
        self.scene = bge.logic.getCurrentScene()
        self.music = None
        
        if not self.update in self.scene.pre_draw:
            self.scene.pre_draw.append(self.update)
        
    def play(self, file, gob, loop=0):
        d = self.buffered
        if not file in d:
           print(d)
           d[file] = aud.Factory.buffer(aud.Factory(bge.logic.expandPath("//sounds/")+file))
        buffered = d[file]
        if isinstance(gob, KX_GameObject):
            handle = device.play(buffered)
            handle.relative = False
            handle.loop_count = int(loop)
            self.handles.append((handle, gob))
        
    def update(self):
        cam = self.scene.active_camera
        device.listener_location       = cam.worldPosition 
        device.listener_orientation    = cam.worldOrientation.to_quaternion()


        self.handles = [i for i in self.handles if i[0].status and not i[1].invalid]
        for handle,gob in self.handles:
            handle.location = gob.worldPosition
            
    def playMusic(self, file, vol=1.0):
        if self.music: 
            self.music.stop()
        handle = device.play(aud.Factory(file))
        handle.volume = vol
        handle.loop_count = -1
        self.music = handle
        
        
audio = Audio()