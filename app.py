
#* module imports
import subprocess
from time import sleep


#* shutdown class used for making and exicuting the command
class ShutdownController:

  #* constructor
  def __init__(self) -> None:
    self.command = "shutdown"
    self.params = ""
  
  #* destructor
  def __del__(self):
    # comment this out later
    print("removing the call...")
    sleep(1)
    #subprocess.call("shutdown -a -fw")
    pass
  
  #* for shutdown
  def shutdown(self, *kwargs):
    self.params = " ".join(list(kwargs))
    self.call = self.command + " /s " + self.params

    print(f"{self.call}")
    #subprocess.run(self.call)
  
  #* for restart
  def restart(self, *kwargs):
    self.params = " ".join(list(kwargs))
    self.call = self.command + " /r " + self.params

    print(f"{self.call}")
    #subprocess.run(self.call)
  
  #* for logging off
  def logoff(self, *kwargs):
    self.params = " ".join(list(kwargs))
    self.call = self.command + " /l " + self.params

    print(f"{self.call}")
    #subprocess.run(self.call)


#* ui class which serves as menu
class UserInterface:

  #* constructor
  def __init__(self):
    self.isTimed = False # "/t"
    self.time = 0 
    self.withMsg = False # "/c"
    self.message = ""
    self.exit = False
    self.commands = ["shutdown", "restart", "logoff", "quit"]
    self.params = []

  def print_menu(self):

    print("- - - - - - - - - - - - - - - - - - - -")
    print("OPTIONS:")

    for num, val in enumerate(self.commands):
      print("   ", num+1, val.title())

  def checkOption(self, message) -> bool:
    return True if input(f"{message} (Y/N)?") in "YyYesyes" else False

  #* app mainloop
  def run(self):

    call = ShutdownController()

    while not self.exit:

      self.print_menu()
      choice = int(input(">>> Enter your choice: "))
      print(choice)

      if choice != 4:
        
        self.isTimed = self.checkOption("Do you want to set a time delay")
        if self.isTimed:
          self.time = str(input("Enter the time delay (in seconds): "))
          self.params.append("/t")
          self.params.append(self.time)

        self.withMsg = self.checkOption("Do you want to attach a message")
        if self.withMsg:
          self.message = '"' + input("Enter the message: ") + '"'
          self.params.append("/c")
          self.params.append(self.message)


      if choice == 1:
        call.shutdown(*self.params)
        pass
      elif choice == 2:
        call.restart(*self.params)
        pass
      elif choice == 3:
        call.logoff(*self.params)
        pass
      elif choice == 4:
        self.exit = True
      else:
        "Choose again!"



if __name__ == "__main__":
  #shut = ShutdownController()
  #shut.restart("/t", "3600")

  app = UserInterface()
  app.run()
