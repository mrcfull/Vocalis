
# **Vocalis**

## **Project Overview**

**Vocalis** is a Python and Lua-based application designed for processing and executing voice commands. The project demonstrates integration between Python for voice recognition and Lua for command processing, with support for Docker to streamline development and deployment.

## **Technical Features**

- **Voice Command Capture:** Utilizes the `speech_recognition` library to capture and process voice input.
- **Command Processing:** Commands are processed using Lua scripts for flexibility.
- **Command Confirmation:** Includes a confirmation step to validate commands before execution.
- **Command Logging:** Logs commands and responses for auditing purposes.
- **Docker Support:** Provides Docker configurations for consistent development and deployment.

## **Development Setup**

### **Prerequisites**

- **Python 3.x**
- **Lua**: Ensure Lua is installed and configured.
- **Docker**: For containerization.

### **Installation**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/vocalis.git
   cd vocalis
   ```

2. **Set Up Python Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Lua Scripts:**
   Ensure `command_processor.lua` is placed in the `lua_scripts` directory.

### **Running Locally**

To start the application:

```bash
python src/main.py
```

### **Docker Setup**

**Docker** simplifies the environment setup and deployment.

1. **Build the Docker Image:**
   ```bash
   docker build -t vocalis .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -it --rm --name vocalis vocalis
   ```

3. **Using Docker Compose (Optional):**
   Define services and manage dependencies with Docker Compose.

   ```bash
   docker-compose up
   ```

### **Development and Contributions**

- **Code Structure:** Source code resides in the `src` directory. Lua scripts are in `lua_scripts`.
- **Development Workflow:**
  1. Create a new branch for features or fixes.
  2. Commit changes and test locally.
  3. Submit a pull request with a detailed description of changes.

### **Testing**

Ensure functionality by running unit tests. Add test cases under the `tests` directory if needed.

### **Configuration**

Adjust configurations in the `config` file or environment variables as necessary.

## **Additional Resources**

- **[PyInstaller Documentation](https://pyinstaller.org/)**
- **[Lua Documentation](https://www.lua.org/manual/5.1/)**
- **[Docker Documentation](https://docs.docker.com/)**
- **[Docker Compose Documentation](https://docs.docker.com/compose/)**
  
## **TODO List**

- **🔍 Advanced Command Recognition:** Enhance recognition accuracy for complex commands.
- **🔇 Noise Suppression:** Implement algorithms to reduce background noise.
- **🌐 Language Detection and Translation:** Automatically detect and translate commands.
- **🗂️ Command History:** Develop functionality for command history management.
- **🖥️ User Interface:** Design and implement a graphical interface.

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
