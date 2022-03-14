import billboard

class Billboard:
    def parse_data(self, chart_data):
        parsed_list = []
        for song in chart_data:
            parsed_list.append({"song":song.title, "artist":song.artist})
        return parsed_list

    def get_chart_data(self, chart_name):
        chart = billboard.ChartData(chart_name)
        return self.parse_data(chart)