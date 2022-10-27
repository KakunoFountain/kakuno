import os
import ffmpeg
import glob


class mp4_mp3():

    def all(self, path = ''):
        self.search_mp4()
        self.change_mp4(path)
        self.remove()


    def search_mp4(self):

        mp4 = "*.mp4"
        mp4_name, = glob.glob(mp4)
        self.name = mp4_name[:-4]

    def change_mp4(self, path=''):

        # 入力 
        stream = ffmpeg.input(self.name +".mp4") 
        # 出力 
        if path == '':
            stream = ffmpeg.output(stream, self.name +".mp3") 
        else:
            stream = ffmpeg.output(stream, path+"/"+self.name +".mp3") 
        
        # 実行 
        ffmpeg.run(stream)


    def remove(self):
        os.remove(self.name +".mp4")