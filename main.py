import speech_recognition as sr
from lupa import LuaRuntime
from utils import log_command, confirm_command

# Initialize Lua environment
lua = LuaRuntime(unpack_returned_tuples=True)
lua.execute('dofile("lua_scripts/command_processor.lua")')  # Update path as needed
process_command = lua.globals().process_command

def capture_voice_command():
    """Capture and process voice command."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        # Capture audio input from the microphone
        audio = recognizer.listen(source)

        try:
            # Recognize the speech
            command = recognizer.recognize_google(audio)
            print(f"Recognized Command: {command}")

            # Ask for confirmation
            if confirm_command(command):
                # Send the command to Lua for processing
                response = process_command(command)
                print(f"Lua Response: {response}")

                # Log the command and response
                log_command(command, response)
            else:
                print("Command cancelled.")

        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    capture_voice_command()
