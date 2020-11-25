# Python Phones and Logos Scrapper Test

Here, in this repository, you can find my solution to the Python challenge of the
recruitment process for _CIAL dun&bradstreet_.

Using the Scrapy framework, the _contactinfo_ spider can fetch phone numbers through
a regex pattern and image logos urls through an attributes analysis.

## Technical infos
- Python version: 3.8.0
- Main framework: Scrapy

## Running

You can execute the script using both Docker or terminal.

### Terminal
After cloning the repo and installing the correct Python version, you need to activate `venv`,
Python's virtual environment, inside `/pythonscrapptertest` folder.

Then, still on this folder, execute the following command so Python can install all
needed dependencies.

```
pip install -r requirements.txt
```

_Pip_ will install all libraries that are used in this project, in the specific versions 
pointed in the _requirements.txt_ file.

Finally, for the spider to run, you must go inside the scrapy project folder and run 
the main file (which is `run.py`), using a `txt` file with the websites to be scrapped.
Note that there's already an example file, `sites_example.txt`::

```
Terminal:

cd contactscrapper/
cat ../sites_example.txt | python run.py
```

After that, you can watch the _contactinfo spider_ execution logs, along with scrapped
phone numbers and URL image logos.

### Docker

After cloning the repo and installing Docker on your computer, go to `/pythonscrappertest`, 
project's root folder, where there is a `Dockerfile`. There, run the following command 
with your terminal:

```
Terminal:

sudo docker build -t pythonscrappertest .
```

Once the Docker image is ready, you can run it, using a `txt` file with the websites to be scrapped.
Note that there's already an example file, `sites_example.txt`:

```
Terminal:

cat sites_example.txt | docker run -i pythonscrappertest
```

You can customize the sites file. Just remember to put one URL for each line.

After that, you can watch the _contactinfo spider_ execution logs, along with scrapped
phone numbers and URL image logos.

## Contact

You can contact me through:
- [Whatsapp](https://api.whatsapp.com/send?phone=5519981119478)
- [Email](mailto:joaopedroguimaraes96@gmail.com)
- [Telegram](t.me/kurtzeras)