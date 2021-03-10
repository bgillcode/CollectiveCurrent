# CollectiveCurrent

Retrieve and store all images for chapters, pass in the URL of the series wanted to be downloaded and all images will be saved into their respective chapter folders.

## Parameters:
#### Required parameters:
| Name of paramater | Shorthand name of parameter | Description | Example |
|-------------- | ------------- | ------------- | ------------- |
| --url | -u | Set URL to retrieve the images from. This needs to be the URL which list all of the chapters. | `--url http://www.url.of.series.to.retrieve` |


#### Optional parameters:
| Name of paramater | Shorthand name of parameter | Description | Example |
|-------------- | ------------- | ------------- | ------------- |
| --startrange | -s | Set the number to START the range from for the chapter. | `--startrange 1` this will start the count to retrieve from chapter 1. If set to 3 it will start downloading from chapter 3. |
| --endrange | -e | Set the number to END the range from for the chapter. | `--endrange 5` this will get all of the chapters from the startrange set up to 5. If set to 10, it will retrieve all images from for all of the chapters within the range up to chapter 10. |
| --timedelay | -t | Set the time delay for retrieving each chapter. | `--timedelay 20` if you want to wait 20 seconds between each chapter. |

### Requirements:
Python 3

### Example usage for CollectiveCurrent:

```python collectivecurrent.py --url http://www.url.of.series.to.retrieve --startrange 1 --endrange 5 --timedelay 5```

### Set up a virtual environment for CollectiveCurrent:

##### Mac OSX, Linux:

```python3 -m venv venv```

Then to activate it (make sure you are in the main project folder):

```source venv/bin/activate```

OR:

##### Windows:
```python -m venv venv```

Then to activate it (make sure you are in the main project folder):

```venv\Scripts\activate```

### Install requirements.txt:
```pip3 install -r requirements.txt```

or

```pip install -r requirements.txt --user```
