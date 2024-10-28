metaAI Image
===================
metaAI image is a Python package using which you can use llama's meta model to generate images using your program.

Features
-------------------
* The program uses selenium to web scrap the meta website.
* The program uses your login credentials.
* The program downloads images into an output folder. Make sure to process your output images before sending another prompt.

Set up Library
-------------------
1. Download the library from github repo: https://github.com/shusinghal/metaAimage.git
    `git clone https://github.com/shusinghal/metaAimage.git`

2. Open the library folder.
    `cd metaAimage`

3. Install using pip.
    `pip install -e .`

Requirements
-------------------
* Selenium
* Requests
* Python 3.x

Usage
-------------
Import library
********************
    `from metaAIlib.scripts import myfunctions`

Initialize the class
************************
    `my = myfunctions()`

Open the browser
*****************
Call the openbrowser function. It will open a chrome browser function in the background.
    `my.openbrowser()`

Sign in
************
Call the fblogin or instalogin functions to sign in. Pass your username and password as arguments. Both arguments are mandatory.
    `my.instalogin("your_username", "your_password")`
    `my.fblogin("your_username","your_password")`

Send prompts
*****************
Call the Input (input with capital I) function to send prompts. In return, the system saves your images in the output library.
    `my.Input(prompt="", no_of_images="",directory="")

    * prompt [Mandatory]: enter the text to generate an image.
    * no_of_images [Optional]: Meta genrerates four images by default. Enter the number of images you want to generate. Default is 1.
    * directoroy [Optional]: Choose the output directory to save images. Default directory is output.




Usage
Here is a quick start guide to using My Library in your scripts.

Import the Package

python
Copy code
from my_library import MyFunctions
Initialize the Class and Use Methods

python
Copy code
from my_library import MyFunctions

if __name__ == "__main__":
    # Initialize the MyFunctions class
    my = MyFunctions()
    
    # Open the browser
    my.openbrowser()
    
    # Define the prompt and directory for image generation
    prompt = "cartoon animation: picture of a cat chasing a butterfly"
    no_of_images = "4"  # Enter a value between 1 to 4
    directory = "output"  # Specify the output directory
    
    # Log in to Instagram
    my.instalogin("your_username", "your_password")
    
    # Generate images
    my.input(prompt, no_of_images, directory)
Methods
openbrowser(): Opens a browser session using Selenium.
instalogin(username, password): Logs in to Instagram with the given username and password.
input(prompt, no_of_images, directory): Generates images based on the prompt, specifying the number of images and the output directory.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to open issues or submit pull requests for enhancements or bug fixes. Please ensure any contributions align with the package's purpose and follow best practices for code readability and performance.