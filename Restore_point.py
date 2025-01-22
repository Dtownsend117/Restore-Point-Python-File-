#// Add RISE voice
# Add import to main code
# Add error handling
# Add confirmation messages and dialog for success and error
# Add noises for completed and failed process
        
import subprocess
import datetime
import ctypes
import sys
import pyttsx3

class RestorePoint:
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)
        self.engine.setProperty("rate", 170)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def is_admin(self):
        """Check if the script is running with admin privileges."""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def create_restore_point(self, description="Restore Point"):
        try:
            self.speak("Creating restore point...")

            # PowerShell command to create a restore point
            command = f"powershell.exe -Command \"Checkpoint-Computer -Description '{description}' -RestorePointType 'MODIFY_SETTINGS'\""
            
            # Execute the command
            result = subprocess.run(command, capture_output=True, text=True, shell=True)

            if result.returncode == 0:
                success_message = f"'{description}' created successfully."
                self.speak(success_message)
            else:
                error_message = f"Failed to create restore point. Error: {result.stderr.strip()}"
                self.speak(error_message)

        except Exception as e:
            error_message = f"An error occurred: {e}"
            self.speak(error_message)

# If you want to run this module directly, you can keep this block
if __name__ == "__main__":
    rp = RestorePoint()
    if rp.is_admin():
        description = f"Restore Point created on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        rp.create_restore_point(description)
    else:
        print("Requesting admin privileges...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

# import subprocess
# import datetime
# import ctypes
# import pyttsx3

# class RestorePointManager:
#     def __init__(self):
#         self.engine = pyttsx3.init()
#         self.voice_id = None  # You can set a default voice ID here if desired

#     def is_admin(self):
#         """Check if the script is running with admin privileges."""
#         try:
#             return ctypes.windll.shell32.IsUserAnAdmin()
#         except:
#             return False

#     def speak(self, message):
#         """Convert text to speech and print the message to the terminal."""
#         print(message)  # Print the message to the terminal
#         if self.voice_id is not None:
#             self.engine.setProperty('voice', self.voice_id)
#         self.engine.say(message)
#         self.engine.runAndWait()

#     def list_voices(self):
#         """List available voices on the system."""
#         voices = self.engine.getProperty('voices')
#         for index, voice in enumerate(voices):
#             print(f"Voice {index}: {voice.name} - ID: {voice.id}")

#     def create_restore_point(self, description="Restore Point"):
#         try:
#             # Announce that we are creating a restore point
#             self.speak("Creating restore point...")

#             # PowerShell command to create a restore point
#             command = f"powershell.exe -Command \"Checkpoint-Computer -Description '{description}' -RestorePointType 'MODIFY_SETTINGS'\""
            
#             # Execute the command
#             result = subprocess.run(command, capture_output=True, text=True, shell=True)

#             if result.returncode == 0:
#                 success_message = f"Restore point '{description}' created successfully."
#                 self.speak(success_message)
#             else:
#                 error_message = f"Failed to create restore point. Error: {result.stderr.strip()}"
#                 self.speak(error_message)

#         except Exception as e:
#             error_message = f"An error occurred: {e}"
#             self.speak(error_message)

#     def run(self):
#         if self.is_admin():
#             # You can customize the description here
#             description = f"Restore Point created on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#             self.create_restore_point(description)
#         else:
#             # Re-run the program with admin rights
#             print("Requesting admin privileges...")
#             ctypes.windll.shell32.ShellExecuteW(None, "runas", __file__, None, 1)
