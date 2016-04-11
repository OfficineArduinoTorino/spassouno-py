import io
from PIL import Image
from picamera import PiCamera
import traceback
import logging

class Camera(object):
    _overlay_rederer = None
    _screen_w = 0
    _screen_h = 0

    def __init__(self):
        self._camera = PiCamera()

        self._camera.framerate = 24

        self._camera.sharpness = 0
        self._camera.contrast = 0
        self._camera.brightness = 50

        self._camera.saturation = 0
        self._camera.ISO = 0
        self._camera.video_stabilization = False
        self._camera.exposure_compensation = 0
        self._camera.exposure_mode = 'auto'
        self._camera.meter_mode = 'matrix'
        self._camera.awb_mode = 'auto'
        self._camera.image_effect = 'none'
        self._camera.image_effect = 'none'

        self._camera.rotation = 0
        self._camera.hflip = True
        self._camera.vflip = False

        self._screen_w = self._camera.resolution[0] / 2
        self._screen_h = self._camera.resolution[1]
        self._camera.resolution = (self._screen_w, self._screen_h)

    def annotate_text(self, text):
        self._camera.annotate_text = text

    def start_preview(self):
        w = self._camera.resolution[0]
        h = self._camera.resolution[1]
        self._camera.start_preview(fullscreen=False, window=(0, 0, w, h))

    def stop_preview(self):
        self._camera.stop_preview()

    @property
    def fullscreen(self):
        return self._camera.preview.fullscreen

    @fullscreen.setter
    def fullscreen(self, value):
        if value:
            self._camera.resolution = (self._screen_w * 2, self._screen_h)
        else:
            self._camera.resolution = (self._screen_w, self._screen_h)

        self._camera.preview.fullscreen = value

    def close(self):
        self._camera.close()

    def capture_to_file(self, file_name):
        stream = io.BytesIO()
        self._camera.capture(
            stream, use_video_port=True, format='jpeg')
        frame = Image.open(stream)
        frame.save(file_name, "JPEG")

    def show_frame(self, image_name):
        try:
            img = Image.open(image_name)

            pad = Image.new('RGB', (
                (((self._camera.resolution[0] * 2) + 31) // 32) * 32,
                ((img.size[1] + 15) // 16) * 16,
            ))

            pad.paste(img, (self._camera.resolution[0], 0))
            source = pad.tobytes()
            if not self._overlay_rederer:
                self._overlay_rederer = self._camera.add_overlay(pad.tobytes(), size=(self._camera.resolution[0] * 2,
                                                                                      img.size[1]))
            else:
                self._overlay_rederer.update(source)
        except:
            logging.error(traceback.format_exc())

    def zoom_reset(self):
        if self._camera.zoom[1] < 1.0 and self._camera.zoom[2] < 1.0:
            self._camera.zoom = (0.0, 0.0, 1.0, 1.0)

    def zoom_in(self):

        self._camera.zoom = (0.0, 0.0, self._camera.zoom[2] - 0.1, self._camera.zoom[3] - 0.1)

    def zoom_out(self):

        self._camera.zoom = (0.0, 0.0, self._camera.zoom[2] + 0.1, self._camera.zoom[3] + 0.1)

