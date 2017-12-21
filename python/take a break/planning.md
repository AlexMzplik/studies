#First steps BreakTime app

1. define how many times the BreakTime should run
2. define the time it should wait and the page it should open after the wait
3. wait the time defined
4. open the page
5. repeat the steps 3 and 4 as many times we defined

#Breakdown of the code
As we need the open a browser and control the time of execution, we need some libraries to do that
```python
import webbrowser
import time
```
we import the library **webbrowser** which has the method _open_ that we need. Also the **time** library, so we can use the methods _sleep_, that pause the execution in seconds, and _ctime_ which dispay the date-time informetion, that we will use to keep track of the executions whe queued.

```python
def AguardarMinutos(minutos):
  segundos = minutos * 60
  return time.sleep(segundos)
```
we are here creating a function that convert the minutes we've defined to seconds as a parameter for the method _sleep_ from _time_, and then execute _sleep_.

```python
def InciniarBreakTime(vezes, minutos, video_url):
  print "Iniciado em ", time.ctime()
    i = 0
    while i < vezes:
        AguardarMinutos(minutos)
        i += 1
        print "Execução", i, "vez em", time.ctime()
        webbrowser.open(video_url)
    print "Execução terminada em ", time.ctime()
```
Here we made a function that will do all the work. It prints when it has started, make a loop that will run the times informed with the param _vezes_, the minutes it'll wait defined on _minutos_, then print the number of execution and the when, then open the browser with the page we defined with *video_url* param. when the loop ends, it'll print when it finished.

The last line of code is to actually runs the app:
```python
InciniarBreakTime(5, 25, "https://www.youtube.com/watch?v=HyhB3c_whgo")
```
Wich will open 5 times the url *https://www.youtube.com/watch?v=HyhB3c_whgo*, in intervals of 25 minutes.