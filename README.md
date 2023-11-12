# OpenAI-API-example
 
# Set-up Instructions



## Set up Python

Ensure you have Python installed. If not, you can download it from [python.org](https://www.python.org/). You'll also need `pip` to install packages. 

You will need to install the `open-ai` package. 
```commandline
pip install open-ai
```

## Set your API key
This is the most secure method to set your API key. Set your API key as an environment variable and then access it within your script. This way, your key is not hard-coded into the script.

### On **Windows**
In the Command Prompt:
```commandline
set SDS617_API_KEY=your_api_key_here
```

### On **macOS/Linux**
In the Terminal:
```bash
export SDS617_API_KEY=your_api_key_here
```

### Instructions for IDEs
#### PyCharm
* Go to Run -> Edit Configurations... in the top menu.
* Select your Python script from the list on the left.
* Find the Environment variables field, click the icon at the right end of this field to open the environment variables dialog.
* Add SDS617_API_KEY as the name and your actual API key as the value.
* Click OK to save and exit.

#### Visual Studio Code (VSCode)
* Open your `.vscode/launch.json` file 
    - If you don't have this file, go to the "Run and Debug" sidebar, and create a new debug configuration for Python.
* In the `launch.json` file, add an "env" field to your Python debug configuration and define your environment variable there. Example:
```json
{
  "name": "Python: Your Script",
  "type": "python",
  "request": "launch",
  "program": "${file}",
  "env": {
    "SDS617_API_KEY": "your_api_key_here"
  }
}
```
* Save the file and run your script through the VSCode debugger.