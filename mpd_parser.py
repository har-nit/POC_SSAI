from mpegdash.parser import MPEGDASHParser
import ffmpeg_streaming
input_file = r"\2.mp4"

root = r"C:\Users\admin\PycharmProjects\test2"
video = ffmpeg_streaming.input(root+input_file)


# Parse from file path
mpd_path = root+'/dash.mpd'
mpd = MPEGDASHParser.parse(mpd_path)

# Parse from url
mpd_url = 'http://localhost/test2/dash.mpd'
mpd = MPEGDASHParser.parse(mpd_url)

# Parse from string
mpd_string = '''
<MPD xmlns="urn:mpeg:DASH:schema:MPD:2011" mediaPresentationDuration="PT0H1M52.43S" minBufferTime="PT1.5S"
profiles="urn:mpeg:dash:profile:isoff-on-demand:2011" type="static">
  <Period duration="PT0H1M52.43S" start="PT0S">
    <AdaptationSet>
      <ContentComponent contentType="video" id="1" />
      <Representation bandwidth="4190760" codecs="avc1.640028" height="1080" id="1" mimeType="video/mp4" width="1920">
        <BaseURL>2.mp4</BaseURL>
        <SegmentBase indexRange="674-981">
          <Initialization range="0-673" />
        </SegmentBase>
      </Representation>
    </AdaptationSet>
  </Period>
</MPD>
'''


mpd = MPEGDASHParser.parse(mpd_string)

# Write to xml file
MPEGDASHParser.write(mpd, './test2/output.mpd')