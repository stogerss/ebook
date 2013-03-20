#!usr/bin/env ruby
# Create a gif from a certain segment of a video file

def create(start, duration, movie, output)
  # use ffmpeg starting at "start", for "duration", with 10 fps, size 200x200,
  # and naming the outputs "out-<num>.jpg".
  `ffmpeg -i #{movie} -ss #{start} -t #{duration} -r 10 -s 200x200 -f image2 out-%03d.jpg`
  # Create a gif from all .jpg files in the current directory
  `convert -delay 20 -loop 0 *.jpg #{output}.gif`
