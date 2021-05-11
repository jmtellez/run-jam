import billboard

chart = billboard.ChartData('hot-100')


def main():
    for song in chart:
        print(song.title)

if __name__=="__main__":
    main()