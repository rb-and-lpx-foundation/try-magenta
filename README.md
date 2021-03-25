# Try Magenta

Many of the instructions here come from the documentation of Magenta. Begin here https://magenta.tensorflow.org/

## Apt

Apt install requirements.

    sudo apt-get install build-essential libasound2-dev libjack-dev portaudio19-dev xvfb python-opengl ffmpeg zip fluidsynth

## Clone repos and create environments

    mkdir repos
    cd repos
    git clone https://github.com/magenta/magenta-demos
    git clone https://github.com/rb-and-lpx-foundation/try-magenta
    cd try-magenta
    mkvirtualenv magenta
    pip install -r requirements.txt
    
Part of this demo will touch on examples depending on TensorFlow 1.x. For these (optionally) create a second virtual environment.

    mkvirtualenv magenta-one
    pip install -r requirements-one.txt

## Download resources

The midi examples require a midi sound font. For this demo, we used Yamaha C5 Grand, which can be downloaded from here https://sites.google.com/site/soundfonts4u

For the NSynth demo, we followed suggestions from the original blog by [Parag Mital](https://magenta.tensorflow.org/nsynth-fastgen) and downloaded a few samples from [Freesound.org](https://freesound.org).

- A [hip hop beat](https://www.freesound.org/people/MustardPlug/sounds/395058/)
- A woman singing [laa](https://www.freesound.org/people/maurolupo/sounds/213259/)
- A bit of [cello](https://www.freesound.org/people/xserra/sounds/176098/)
