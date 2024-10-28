
**metaAI Image**
===================

The *metaAI Image* is a Python package that allows you to generate images using Llama’s Meta model through your program.

**Features**
-------------------
* The program uses Selenium to scrape the Meta website.
* It utilizes your login credentials for authentication.
* The program downloads images into an output folder. Be sure to process your output images before sending another prompt.

**Set Up Library**
-------------------
1. Download the library from the GitHub repository: https://github.com/shusinghal/metaAimage.git  
   ```git clone https://github.com/shusinghal/metaAimage.git
   ```

2. Open the library folder:
   ```cd metaAimage
   ```

3. Install using pip:
   ```pip install -e .
   ```

**Requirements**
-------------------
* Selenium
* Requests
* Python 3.x

**Usage**
-------------------

**Import the Library**
-------------------
```from metaAIlib.scripts import myfunctions
```

**Initialize the Class**
-------------------
```my = myfunctions()
```

**Open the Browser**
-------------------
Call the `openbrowser` function. It will open a Chrome browser in the background.
```my.openbrowser()
```

**Sign In**
-------------------
Use the `fblogin` or `instalogin` functions to sign in. Provide your username and password as arguments (both are mandatory).
```my.instalogin(user="", password="")
   my.fblogin(user="", password="")
```

**Send Prompts**
-------------------
Call the `Input` (with a capital "I") function to send prompts. The system saves your images in the specified output directory.

```my.Input(prompt="", no_of_images="", directory="")
```

- *prompt* **(Mandatory)**: Enter the text to generate an image.
- *no_of_images* **(Optional)**: By default, Meta generates four images. Specify the number of images you want to generate; the default is 1.
- *directory* **(Optional)**: Specify the directory to save images. The default directory is `output`.

**License**
-----------
This project is licensed under the MIT License. See the LICENSE file for details.

**Contributing**
---------------
Feel free to open issues or submit pull requests for enhancements or bug fixes. Ensure contributions align with the package's purpose and follow best practices for code readability and performance.
