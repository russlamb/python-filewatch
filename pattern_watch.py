import watchdog.observers
import sys
import time
import shutil
import watchdog.events
import os

class PatternWatch:
    'Class to scan a folder for files matching a pattern'

    def event_handler_builder(self,pattern_file, ignore_file):
        'Builds a watchdog pattern event handler using file input'

        print ("pattern file: "+pattern_file)
        lines = [line.rstrip() for line in open(pattern_file)]
        if len(lines)<1:
            lines = ["*.*"] #default to any pattern
        
        ines = [line.rstrip() for line in open(ignore_file)]
        if len(lines)<1:
            lines = [".DS_Store*",".*"] #default to any pattern
        
        print (lines)
        ignore_patterns = [".DS_Store*"]
        return watchdog.events.PatternMatchingEventHandler(lines, ignore_directories=True)

    def __init__(self, path, target_path , pattern_file, ignore_file):
        'initializes class with observer and event handler'
        self.path = path
        self.documents = dict() # key = file name, value = ?
        self.target_path = target_path
        self.event_handler = self.event_handler_builder(pattern_file, ignore_file)
        self.event_handler.on_created = self.on_created
        self.observer =watchdog.observers.Observer()
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()

    def on_created(self, event):
        'this function is called when the created event is triggered'
        from_file = event.src_path 
        to_dir = self.target_path
        self.move_file(from_file,to_dir)
        

    def move_file(self, from_file, to_dir):
        'this function contains the move logic to ensure files are overwritten'
        path, filename = os.path.split(from_file)
        to_file = os.path.join(to_dir, filename)
        print ("from: " + from_file)
        print ("to: " + to_file)
        shutil.move(from_file,to_file)
        print ("file moved")

    def stop(self):
        'this stops the observer'
        self.observer.stop()
        self.observer.join()

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    target_path = sys.argv[2] if len(sys.argv) > 2 else '.'
    pattern_file = sys.argv[3] if len(sys.argv) > 3 else './pattern_file.txt'
    ignore_file = sys.argv[4] if len(sys.argv) > 4 else './ignore_file.txt'
    w= PatternWatch(path, target_path, pattern_file, ignore_file)

    try:
        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        w.stop()
