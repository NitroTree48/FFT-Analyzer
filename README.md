# FFT-Analyzer
Python Program that utilizes the Numpy FFT library to identify individual frequency power levels from any sound data leaving a computer without using a microphone


In order to run FFT_Analyzer.py you will need to follow a few steps:

  1.  First, make sure you have python 3.7 installed on your computer
  2.  Specifically between 3.7.3 - 3.7.9 (3.7.10 will not work with the libraries you will need) 
  3.  Install Virtual Audio Cable for free from this site: https://vb-audio.com/Cable/
  4.  Install Voice Meter Banana for free from this site: https://vb-audio.com/Voicemeeter/banana.htm
  5.  Open a terminal in the location you wish to save FFT_Analyzer.py and run the following commands:
  6.  pip install pyaudio
  7.  pip install numpy
  8.  pip install matplotlib
  9.  pip install math
  10. Next, you will need to change the audio input and output for your computer from pc settings:
  11. Output will be set to “CABLE input(VB-Audio Virtual Cable)
  12. Input will be set to “CABLE output(VB-Audio Virtual Cable)
  13. Finally, you will need to change the audio input and output on Voice Meter Banana:
  14. Open Voice meter and let the sound engine start (ignore any error messages that pop up)
  15. Set “Hardware Input 1” by clicking on the 1 icon and choose CABLE output(VB-Audio Virtual Cable)
  16. Set “Hardware Out” by clicking on the A1 icon and choose “WDM: *name of computer speakers*”
  17. Now open the same terminal as before and run “python FTT_Analyzer.py”
  18. Play music from any online or offline source after seeing the words “connected” print in terminal

Completed Dance routine steps

(if you do not see the printout “connected” then the computer has not successfully connected to the leader romba)
