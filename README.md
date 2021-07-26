# run-jam

# Install Instructions:
1. To setup virtual env use command, 'python -m venv env'
   1. This will create directory called 'env' where virtual scripts will be saved
   2. Run virtual env by navigating into and running '/env/Scripts/activate'
   3. You should now be running the virtual environment
2. To install requirements use command 'pip install -r requirements.txt'
3. To add/create requirements use command 'pip freeze > requirements.txt'

## TODO ##
1. Need to pull from billboard
2. parse results
3. query Spotify for all
4. sort
5. possibly save dailies for quicker access

## SPOTIFY ENDPOINTS ##
- Get Audio Features needed for temp - https://api.spotify.com/v1/audio-features/{id}
- Get current User account ID - 	https://api.spotify.com/v1/me
- 
## Billboard API Reference Documentation
https://github.com/guoguo12/billboard-charts

## Available Charts ##
 - hot-100
 - billboard-200
 - artist-100
 - social-50
 - streaming-songs
 - radio-songs
 - digital-song-sales
 - top-album-sales
 - current-albums
 - catalog-albums
 - independent-albums
 - soundtracks
 - vinyl-albums
 - summer-songs
 - billboard-global-200
 - billboard-global-excl-us
 - greatest-of-all-time-artists
 - greatest-billboard-200-albums
 - greatest-billboard-200-artists
 - greatest-hot-100-singles
 - greatest-hot-100-artists
 - greatest-hot-100-songs-by-women
 - greatest-hot-100-women-artists
 - greatest-billboard-200-albums-by-women
 - greatest-billboard-200-women-artists
 - greatest-billboards-top-songs-80s
 - greatest-billboards-top-songs-90s
 - greatest-of-all-time-pop-songs
 - greatest-of-all-time-pop-songs-artists
 - greatest-adult-pop-songs
 - greatest-adult-pop-artists
 - greatest-country-songs
 - greatest-country-albums
 - greatest-country-artists
 - greatest-of-all-time-latin-artists
 - greatest-hot-latin-songs
 - greatest-hot-latin-songs-artists
 - greatest-top-dance-club-artists
 - greatest-r-b-hip-hop-songs
 - greatest-r-b-hip-hop-albums
 - greatest-r-b-hip-hop-artists
 - greatest-alternative-songs
 - greatest-alternative-artists
 - greatest-of-all-time-adult-alternative-songs
 - greatest-of-all-time-adult-alternative-artists
 - greatest-of-all-time-mainstream-rock-songs
 - greatest-of-all-time-mainstream-rock-artists
 - pop-songs
 - adult-contemporary
 - adult-pop-songs
 - country-songs
 - country-albums
 - country-streaming-songs
 - country-airplay
 - country-digital-song-sales
 - bluegrass-albums
 - americana-folk-albums
 - rock-songs
 - rock-albums
 - rock-streaming-songs
 - rock-airplay
 - rock-digital-song-sales
 - hot-alternative-songs
 - alternative-albums
 - alternative-streaming-songs
 - alternative-airplay
 - alternative-digital-song-sales
 - hot-hard-rock-songs
 - hard-rock-albums
 - hard-rock-streaming-songs
 - hard-rock-digital-song-sales
 - triple-a
 - hot-mainstream-rock-tracks
 - r-b-hip-hop-songs
 - r-b-hip-hop-albums
 - r-and-b-hip-hop-streaming-songs
 - hot-r-and-b-hip-hop-airplay
 - r-and-b-hip-hop-digital-song-sales
 - r-and-b-songs
 - r-and-b-albums
 - r-and-b-streaming-songs
 - r-and-b-digital-song-sales
 - rap-song
 - rap-albums
 - rap-streaming-songs
 - hot-rap-tracks
 - rap-digital-song-sales
 - mainstream-r-and-b-hip-hop
 - hot-adult-r-and-b-airplay
 - rhythmic-40
 - latin-songs
 - latin-albums
 - latin-streaming-songs
 - latin-airplay
 - latin-digital-song-sales
 - regional-mexican-albums
 - latin-regional-mexican-airplay
 - latin-pop-albums
 - latin-pop-airplay
 - tropical-albums
 - latin-tropical-airplay
 - latin-rhythm-albums
 - latin-rhythm-airplay
 - dance-electronic-songs
 - dance-electronic-albums
 - dance-electronic-streaming-songs
 - dance-electronic-digital-song-sales
 - hot-dance-airplay
 - dance-club-play-songs
 - christian-songs
 - christian-albums
 - christian-streaming-songs
 - christian-airplay
 - christian-digital-song-sales
 - hot-christian-adult-contemporary
 - gospel-songs
 - gospel-albums
 - gospel-streaming-songs
 - gospel-airplay
 - gospel-digital-song-sales
 - classical-albums
 - classical-crossover-albums
 - traditional-classic-albums
 - jazz-albums
 - contemporary-jazz
 - traditional-jazz-albums
 - jazz-songs
 - emerging-artists
 - heatseekers-albums
 - top-triller-global
 - top-triller-us
 - lyricfind-global
 - lyricfind-us
 - next-big-sound-25
 - hot-holiday-songs
 - holiday-albums
 - holiday-streaming-songs
 - holiday-songs
 - holiday-season-digital-song-sales
 - canadian-hot-100
 - canadian-albums
 - hot-canada-digital-song-sales
 - canada-emerging-artists
 - canada-ac
 - canada-all-format-airplay
 - canada-chr-top-40
 - canada-country
 - canada-hot-ac
 - canada-rock
 - mexico
 - mexico-ingles
 - mexico-popular
 - mexico-espanol
 - japan-hot-100
 - billboard-korea-100
 - billboard-argentina-hot-100
 - official-uk-songs
 - official-uk-albums
 - uk-digital-song-sales
 - euro-digital-song-sales
 - france-digital-song-sales
 - germany-songs
 - german-albums
 - greece-albums
 - italy-albums
 - italy-digital-song-sales
 - spain-digital-song-sales
 - switzerland-digital-song-sales
 - australian-albums
 - australia-digital-song-sales
 - blues-albums
 - bubbling-under-hot-100-singles
 - cast-albums
 - comedy-albums
 - compilation-albums
 - hot-singles-recurrents
 - kids-albums
 - new-age-albums
 - reggae-albums
 - tastemaker-albums
 - world-albums
 - world-digital-song-sales