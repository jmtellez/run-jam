import billboard

class Billboard:
    song_list = []
    
    def __init__(self, chart_name):
        self.chart_name = chart_name
        chart = billboard.ChartData(self.chart_name)
        for song in chart:
            new_song = {
                "title":song.title,
                "artist":song.artist
            }
            self.song_list.append(new_song)
                
    def get_chart_data(self):
        return self.song_list