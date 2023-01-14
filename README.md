# Kivy-Rounded-Video

Requirements:
  - Python: 3.7 - 3.10
  - Kivy: 2.1.0
  - NumPy
  - ffpyplayer

This Demo Project is using the kivy.core.video texture and put it on a Widget canvas to be able to apply rounded corner on the displayed video.

Usage:

  In py:
  
    from roundedvideo import RoundedVideo
    
    video = RoundedVideo(source='video_file')
    video.radius = [20, 20, 20, 20]
    video.preview = 'loading_image'
    video.ratio = 'original' # can be "original", "full" ...
    
  or in kv:
   
    #:import RoundedVideo roundedvideo.RoundedVideo
    
    RoundedVideo:
        source: 'video_file'
        radius: [20,20,20,20]
        preview: 'loading_image'
        ratio: 'original'

   
    


Work in Progress...


![Screenshot_20230114_073504](https://user-images.githubusercontent.com/72749248/212461593-8fbea06b-b32c-441c-9793-10cf3ebb6f30.png)

![Screenshot_20230114_073406](https://user-images.githubusercontent.com/72749248/212461629-4a81fc49-9c82-4bf8-8d41-f634ae6cfe6e.png)

![Screenshot_20230114_073444](https://user-images.githubusercontent.com/72749248/212461648-04e04284-d74c-4be5-a6df-0e83ba8af3ab.png)
