class Utilities:
    def __init__(self):
        self.time_to_tempo_conversion = {
            "06:00":190,
            "07:00":180,
            "08:00":170,
            "09:00":160,
            "10:00":150,
            "11:00":140,
            "12:00":130,
            "13:00":120,
            "14:00":110,
            "15:00":100
        }

    def calculate_bpm(self,mile_pace):
        return self.time_to_tempo_converstion[mile_pace]
    
    def find_track(self, id, spotify_chart):
        for track in spotify_chart:
            if track["items"][0]["id"] == id:
                return track
 
    def filter_song_list(self, mile_pace, spotify_analysis_chart, spotify_chart):
        preview_list = []
        for track in spotify_analysis_chart:
            if self.time_to_tempo_conversion[mile_pace] <= int(track["analysis"]["track"]["tempo"]):
                preview_list.append(self.find_track(id=track["id"], spotify_chart=spotify_chart))
        print(preview_list)