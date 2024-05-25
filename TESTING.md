# PU90PX - TESTING

[View the live site here](https://pu90px-bb0793838f63.herokuapp.com/)

I carried out test along the process of building the website. Getting the images to work was the biggest struggle for me and I'm greatful for the tutor team helping me and teaching me more about it. As for the design in comparison to the Wireframes I made before starting building the project it is quite similar. 

I've mostly used Chromes Developer Tool to solve bugs and also going back and forth between my workspace and deploying to Heroku to make sure that the deployed version works as well as the local one. 

## Tests & results

### W3C HTML Validator
I used the W3C HTML Validator to validate the HTML code. 

#### base.html:

![W3C HTML Validator](readme_images/w3c_base.png)
Apart from the errors occuring due to the implemented Django Template Language. Other than that, there was no error occuring.

#### index.html:

The same was for index.html but a couple of more errors, which is expected, since we are inheriting the base from base.html. Other than that it is the same as the base.html showing the errors since we're using Django. 

#### post_detail.html:

- Apart from the same error as mentioned above the validator found:
    - A space in the script source, bug was fixed by removing that extra space. 
    - comment_id attribute in the button tag was throwing an error. Fixing this bug could be to change the comment_id to data-comment-id would solve that issue but will throw other errors since we're using different languages in this project. The function works as it should and therefor I will highlight this error and leave it as it is. 

### W3C CSS Validator
I used the W3C CSS Validator to validate the HTML code. 

![W3C CSS Validator](readme_images/w3c_css.png)

No errors occured in for the CSS - woho!

### JSHint Validator
I used JSHint Validator to validate the JavaScript files.

![JSHint Validator](readme_images/pu_jshint.png)

All errors from JSHint indicating ES6 errors which will be ignored after consulting my mentor and tutor. 

### Google Chrome Dev Tools

Was throwing console errors about third party cookie, this is caused because of the content upload via Django admin. I've added a sessions_cookie_name to None in the settings.py. I have commented the code out for now since login to admin panel doesn't work if it's on but I have still stored it in the settings.py file. 

Lighthouse also indicated on the PErformance which was at a low 32. I changed all the images to webp from jpg/png which got it up to 46. I then compressed the images using Djangos Pillow which got it up to 76.