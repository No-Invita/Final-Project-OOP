# Peter assistant

## What is Peter assistant

Many first semester students find it difficult to learn their schedule or often forget what class or meeting they have at the moment and resort to search through their gallery with thousands of images that contains their schedule or open the Uninorte.co application that requires biometric authentication to view the schedule and that often like many other things that require biometric authentication access can become a bit complicated if you have your finger sores a little wet or the fingerprint sensor is not in good condition. In addition these students often do not know how to get to the room where they have their respective class and many of them are embarrassed to ask where they have to go and take a long time looking for the block where the room is.

Peter assistant is a virtual assistant that you can ask what class or meeting you have coming up next and it will tell you the time it starts, the time it ends, the name of the class and the location where it will take place. You can also see on a map how far or close the block you need to go to is to your location in real time. You will also be able to see images of the block so you can easily recognize it with your eyes.


## Funcionality requirements

- Authentication of users belonging to the Uninorte organization.
- Access to the user's academic calendar.
- The program must obey the user's orders, which will be given by means of a voice in Spanish.

### Diagram UML

![](assets/20220421_110602_diagram.png)

## How to use PetterAssistent

- You must download or clone this repository, you also must have installed Python 3.10 in order to be able to execute the program.

* You must intall the next dependencies

  * SpeechRecognition 3.8.1
  * pyttsx3 2.90
  * PyAudio v0.2.11
  * pytz
  * google-api-python-client 2.45.0
  * google-auth 2.6.5
* For that, you can execute the next comand:

  `pip install SpeechRecognition pyttsx3 PyAudio pytz google-auth google-api-python-client`
* Once you have the code and the dependecies have been installed you can try the program by executing the file main.py which is in the src folder.
* When Peter ask you what do you want he to do tell him you want to know your next classes or you want to know your classes. It is fundamental that you mention the word "clase".
