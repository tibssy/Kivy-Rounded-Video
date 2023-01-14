from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
# from roundedvideo import RoundedVideo

Builder.load_string('''
#:import RoundedVideo roundedvideo.RoundedVideo

<MyLayout>
    orientation: 'vertical'
    padding: 50
    canvas:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            size: self.size
            pos: self.pos

    RoundedVideo:
        source: 'https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4'
        radius: [20,20,20,20]
        preview: 'preview.png'
        ratio: 'original'
''')

class MyLayout(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        # vid = RoundedVideo(source='https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4')
        # vid.radius = [20,20,20,20]
        # vid.ratio = 'original'
        # vid.preview = 'preview.png'
        # return vid
        return MyLayout()


MainApp().run()
