## The repository contains the contexts of a webpage(currently in developement).

### How to load and execute the program:
* Clone the repository
* Install dart [sass](https://sass-lang.com/dart-sass "sass")
* Add dart sass to path: <https://stackoverflow.com/questions/51571814/how-to-install-dart-sass>
* If you are using vscode install the blade runner extension to auto compile sass into css. Or use the command `sass --watch static/scss/styles.scss static/css/styles.css --style=compressed`
* *Optional: Install node package manager from [node.js](https://nodejs.org/en/) and add it to path to run javascript tests*
* Upon opening the folder in vscode **it should automatically run the server** and open the website in the brave browser. If it doesnt run `python manage.py runserver` and open localhost in your web browser.
* Required python modules to install with pip: django, stripe, Pillow, coinbase-commerce.
* Note that the server won't run instantly unless you have a sqlite server attached to it with actual images uploaded with django admin(it can't access unexisting images for the gallery)
* It also requires your own coinbase commerce api key for it to work.

### Functionality:
* I tried to make the website as responsive as I could.
* I also tried to make the code as orginized as possible and humanly readable.
* Additional testing needs to be done.
* Payments are done with the stripe checkout.
* Payments are also possible with cryptocurrency via the coinbase commerce api.

Author: Lockár Miklós