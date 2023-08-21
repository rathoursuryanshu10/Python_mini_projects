import requests 
import shutil 

url = input('Please enter an image URL (string):: ') 
file_name = input('Save image as (string):: ') 

res = requests.get(url, stream = True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')
