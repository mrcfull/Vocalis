import datetime
import speech_recognition as sr

# Log file path
log_file_path = "command_history.log"

def log_command(command, response):
    """Log command and response to a file with a timestamp."""
    with open(log_file_path, "a") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - Command: {command} | Response: {response}\n")

def confirm_command(command):
    """Ask user to confirm the command."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Do you want to execute the command: '{command}'? Please say 'yes' to confirm or 'no' to cancel.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            response = recognizer.recognize_google(audio).lower()
            if 'yes' in response:
                return True
            elif 'no' in response:
                return False
            else:
                print("Confirmation not clear. Cancelling command.")
                return False
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return False
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return False
