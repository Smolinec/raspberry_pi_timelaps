import cv2
import picamera
import picamera.array

def get_frames(camera):
    frames = []
    with picamera.array.PiRGBArray(camera) as output:
        for i in range(24 * 60): # Capture for 60 seconds
            camera.capture(output, format='bgr')
            frames.append(output.array)
            output.truncate(0)
    return frames

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24

frames = get_frames(camera)

fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter('timelapse.mp4', fourcc, camera.framerate, (640, 480))

for frame in frames:
    out.write(frame)

out.release()
