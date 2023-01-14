from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle
from kivy.core.video import Video as CoreVideo
from kivy.properties import StringProperty, ListProperty, OptionProperty
import numpy as np
from kivy.graphics.texture import Texture



class RoundedVideo(Widget):
    source = StringProperty(None)
    preview = StringProperty(None)
    radius = ListProperty([0, 0, 0, 0])
    ratio = OptionProperty('full', options=('full', '16/9', 'original'))

    def __init__(self, **kwargs):
        # self.roundrect = None
        self._video = CoreVideo()
        self._video.bind(on_frame=self._update_texture)
        self.bind(pos=self._redraw, size=self._redraw)
        self.fbind('source', self.play_video)

        super(RoundedVideo,self).__init__(**kwargs)

        self.fbind('radius', self._set_radius)
        self.fbind('preview', self._set_preview)

        with self.canvas:
            Color(1, 1, 1)
            self.roundrect = RoundedRectangle(radius=self.radius, source=self.source, preview=self.preview)


    def _texture_to_image(self, texture):
        rgba_image = np.frombuffer(texture.pixels, 'uint8').reshape(texture.height, texture.width, 4)
        return rgba_image[:, :, :3]

    def _image_to_texture(self, image):
        texture = Texture.create(size=np.flip(image.shape[:2]), colorfmt='rgb', bufferfmt='ubyte')
        buf = image.tostring()
        texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
        return texture


    def keep_ratio(self, frame):
        widget_ratio = self.width / self.height
        video_ratio = self._video.texture.width / self._video.texture.height

        if widget_ratio > video_ratio:
            width = int((widget_ratio * self._video.texture.height - self._video.texture.width) / 2)
            border = 24 * np.ones((self._video.texture.height, width, 3), np.uint8)
            return np.hstack((border, frame, border))

        elif widget_ratio < video_ratio:
            height = int((1 / widget_ratio * self._video.texture.width - self._video.texture.height) / 2)
            border = 24 * np.ones((height, self._video.texture.width, 3), np.uint8)
            return np.vstack((border, frame, border))

    def _set_radius(self, *args):
        self.roundrect.radius = self.radius

    def _set_preview(self, *args):
        self.roundrect.source = self.preview

    def _redraw(self, *args):
        self.roundrect.size = self.size
        self.roundrect.pos = self.pos

    def play_video(self, *args):
        self._video.stop()
        self._video.unload()
        self._video.filename = self.source
        self._video.play()

    def _update_texture(self, *args):
        if self.ratio == 'full':
            self.roundrect.texture = self._video.texture
            print('update')
        # elif self.ratio == '16/9':
        #     print('16/9')
        else:
            frame = self._texture_to_image(self._video.texture)
            bordered_frame = self.keep_ratio(frame)
            texture = self._image_to_texture(bordered_frame)
            self.roundrect.texture = texture


if __name__ == '__main__':
    from kivy.app import App

    class RoundedVideoApp(App):
        def build(self):
            return RoundedVideo()

    RoundedVideoApp().run()