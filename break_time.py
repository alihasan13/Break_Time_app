import time 
import webbrowser

break_time=0
print("current time is"+time.ctime())
while(break_time<3):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=peyU0EOTiy0")
    break_time=break_time+1

    
