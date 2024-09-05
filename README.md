# **Reminder: This is mainly supposed to be a project to get me started into more sophisticated software development, i plan to add things like machine learning and more advanced detection models in the future :)**

# **Vocalis**

## **Overview**

Welcome to **Vocalis**! 🚀 This cutting-edge application integrates Python and Lua to capture, recognize, and process your voice commands effortlessly. Whether you're automating tasks or exploring new ways to interact with your computer, **Vocalis** is designed to streamline your experience.

## **Features**

- **🎙️ Voice Command Capture:** Seamlessly captures voice commands using your microphone.
- **🧠 Command Recognition:** Transcribes spoken commands into text using Google Speech Recognition.
- **✔️ Command Confirmation:** Ensures accuracy by asking for user confirmation before executing commands.
- **📜 Command Logging:** Keeps a log of commands and responses with timestamps for easy tracking.
- **🔧 Lua Integration:** Processes commands through Lua scripts, offering flexible and customizable responses.

## **Getting Started**

### **Prerequisites**

- **Python 3.x**
- Required Python packages (listed below)
- Lua environment setup

### **Installation**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mrcfull/vocalis.git
   cd vocalis
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure Lua Script is in Place:**
   Place `command_processor.lua` in the `lua_scripts` directory.

### **Usage**

Start capturing and processing voice commands by running:

```bash
python main.py
```

## **TODO List**

### **Planned Features**

- **🔇 Noise Suppression and Filtering:**
  - Implement advanced techniques to reduce noise and improve recognition in noisy environments.

- **🌐 Automatic Language Detection and Translation:**
  - Detect the language of commands automatically and translate them before processing.

- **🗂️ Command History Retrieval:**
  - Add functionality to view and manage a history of past commands and their responses.

- **🔍 Enhanced Command Recognition:**
  - Improve the accuracy of recognizing complex names and phrases.

- **🖥️ User Interface (UI):**
  - Develop a graphical or web-based interface for a more interactive and user-friendly experience.

- **📅 Advanced Command Features:**
  - Implement features such as scheduled commands and more sophisticated command processing in Lua.

## **Contributing**

We welcome contributions! 💡 If you have ideas for improvements or want to fix an issue, please submit a pull request or open an issue on GitHub.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

