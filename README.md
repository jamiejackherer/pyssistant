# :snake: Pyssistant :snake:

Pyssistant is designed to be an conversational interface builder. With some simples lines of code you can create a simple assistente to perform actions to you

## How to use

The first step to create an assistant with pyssistant is to import its dependencies, as shown in the following line

```
from pyssistant.dialog import Dialog
```

Then you'll have to create your dialog list, containing the commands and its answers.

```
features = []
features.append(feature("report", function=get_report))
features.append(feature("bye", answer="See you later :)", function=get_bye))
```

You may use a string type answer or even a function by means of "answer" and "function" parameters, if you are attributing to both of those parameters the "answer" parameter will be printed when the command is found in the inputted command, just like the function in the "function" parameter will be executed. Now that you have created your dialog list is needed to create a dialog itself.

```
dialog = Dialog(features)
```

You are also able to insert new commands to your list directly from Dialog object

```
dialog.add_dialog("hello", answer="Hi, how can i help you? :)")
```

Ok, now you have everything setted up, you just have to start listening! There two ways to start listening:

* You may listen only a single command as in:

```
dialog.listen_once()
```

* You may keep listening in loop as in:

```
dialog.start_listening()
```

* It is also possible to set a keyword, the program will be "sleeping" while you don't say the keyword defined in the function wait_call

```
dialog.wait_call("hello")
```

In this example once the word "hello" is said the function listen once will be called

You may also let it listening in background, it will be listening in loop, once any of the commands is said its respective answer will be returned, when the answer is finished it will keep listening to you, waiting for the next command

```
dialog.listen_in_background()
```

to see the full exemple click [here](https://github.com/Lucasfrota/pyssistant/blob/master/src/main.py)

# dependencies

* [SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition/)
* [PocketSphinx](https://github.com/cmusphinx/pocketsphinx)
* [gTTS](https://pypi.python.org/pypi/gTTS)
* [playsound](https://pypi.python.org/pypi/playsound/1.2.1)

# Extra information

* This project is being built using python 2.7 :snake:
* suggestions are always welcome :)
* It's important to say that for now pyssistant only look for the specific word that was defined as command in the spoken sentence, we're still working to make pyssistant more intelligent :)
