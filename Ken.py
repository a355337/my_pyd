import os
class Ken():
    def happy(self, i):
        print(f"{i} Happy hacking!")
    def whoami(self):
        print(f"Hi {os.environ['USERNAME']}, {os.environ['COMPUTERNAME']}")
