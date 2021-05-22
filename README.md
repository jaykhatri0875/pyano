# pyano
Pyano is virtual piano in Air. <br/>
It uses mediapipe for hand recognition purpose. MediaPipe is the simplest tool to build ML based applications. <br/>
No GPU is required to run the project !
# Requires:
python 3.6 <br/>opencv-python<br/> pygame - 1.9.6<br/> mediapipe <br/>

Install using: <br/> pip3 install -r requirements.txt<br/>


# Run using:
python3 pyano.py 

# Demo 
After running the script,put your hand at normal distance from webcam and it will start detecting hand in image.
Move your index finger to the key you want to play.
A3 to G5 keys are available to play on screen.

![not pressed state](https://github.com/jaykhatri0875/pyano/blob/master/sample/not_pressed.png?raw=true)

Make gesture of key pressing in Air and it will play the key for you !

![pressed state](https://github.com/jaykhatri0875/pyano/blob/master/sample/pressed.png?raw=true)
