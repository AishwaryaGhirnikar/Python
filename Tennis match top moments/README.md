# Tennis match top moments

In this project, only Python is used to get this project done. Speech analysis is used for this task. When something exciting happens during a game, there is a rise in the commentator’s voice. Let’s take a tennis match as an example for this project. Whenever any player in the match get the point, there is a rise in the commentator’s voice. Both the audience and the commentators have high pitch during that event. We can use these changes in audio to capture interesting moments from a video.

Libraries/modules used: Pandas, moviepy, pyloudnorm.

1) Pandas is used to read .CSV file.
2) moviepy is used to break videos and to convert them into audio(.WAV file) and concatenate the broken videos.
3) pyloudnorm is used to measure the loudness of each broken videos.

The process we’ll be following is added down below:
1. Input the video file
2. Extract the audio
3. Break the audio into chunks
4. Compute short-time energy of every chunk
5. Classify every chunk as excitement or not (based on a threshold value)
6. Merge all the excitement-clips to form the video highlights
7. Generate the final video highlights
