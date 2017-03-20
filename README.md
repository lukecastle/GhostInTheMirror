# Raspberry Pi Looper
I created this software using some help from Adafruit by looking at their ideas and turning them into a software. This code make videos which are on a memory stick loop.
# Installation
Type in the following code into your Raspberry Pi terminal:
sudo apt-get update
sudo apt-get install -y git
git clone https://github.com/lukecastle/GhostInTheMirror.git
git clone https://github.com/adafruit/pi_video_looper.git
The reason you need to download the adafruit software is that I took inspiration from their project so you need to install parts from their software which I didn't manage to get for the video looper.
Then also type in:
cd pi_video_looper
sudo ./install.sh
This installes the software and will make it start on loop
You should start to see a lot of messages printed to the screen as software is downloaded and installed.
After about 5 minutes you should see the installation stop with the message Finished! If you see this message then the installation succeeded.
If the installation fails for some reason it will immediately stop and display an error.  Check the terminal for the error to see if it's something you can easily correct like a failure to access the internet.
After the software installs you should see the video looper display on the HDMI port.  Assuming no USB drives with movies are connected to your Pi, there should be a message telling you to insert a USB drive like below.
# Ghost In The Mirror
WARNING:
To display the ghost you can check out this youtube video link below:
https://www.youtube.com/watch?v=Nf9yqVH3KyI
This link takes you to a ghost FX. You can download this from youtube using your favourite website, why not make your own fx...
Now copy this to a blank usb stick.
Plug it into the software and bingo, you have a ghost which will reloop.
Now you can build a frame for your mirror and use a spare monitor with a 2 way mirror to finish off your project.
# What Else Can You Use It For?
You can use it for display a instore video if you work in a shop or you can use it like an art gallery. You chose the limits.
# Help
Anyone more info? Email me at: nuexlukecastle@outlook.com
