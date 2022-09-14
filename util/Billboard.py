import billboard

class Billboard:
    __song_list = []
    
    def __init__(self, chart_name):
        self.chart_name = chart_name
        chart = billboard.ChartData(self.chart_name)
        for song in chart:
            new_song = {
                "title":song.title,
                "artist":song.artist
            }
            self.__song_list.append(new_song)
                
    def get_chart_data(self):
        return self.__song_list