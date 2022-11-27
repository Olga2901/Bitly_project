# Bitly_project

Turning a long link into a short one using a bit.ly or a link bit.ly decrypt into a long one. 
There is also a visit counter at the url bit.ly.

## How to install

   1. You need Python3; 
   2. Get your bitly token on  [bit.ly](https://app.bitly.com/settings/api/);
   3. Save your token in .env file with variable BITLY_TOKEN=yourtoken;
   4. Use  `virtualenv` for isolating the project: \
        `python3 -m venv env`;  
        `source venv/bin/activate`
   5. Install dependencies using pip:  
     `pip install -r requirements.txt`   
   6. File requirements.txt will install freeze modules. 

## How to use:

Use command `-l`  or `--link` and put your url

### Example:
```
- bitly$ python3 main.py -l https://ya.ru
Битлинк: bit.ly/3igVhMf
- bitly$ python3 main.py -l bit.ly/3igVhMf
По вашей ссылке прошли 0 раз(а)
```

      

