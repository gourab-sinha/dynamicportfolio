# Dynamic Portfolio

## What is Portfolio?
A portfolio is a compilation of work samples and professional documentation that provides proof of your accomplishments or samples of your work. It can be a physical book or binder that organizes samples of your work, or an online portfolio with electronic files.

## When and why do we use portfolios?
Portfolios are a great way to demonstrate the competencies you would list on a resume or talk about in an interview — they allow you to show and not just tell. During a job search, the portfolio showcases your work to potential employers. It presents evidence of your relevant skills and abilities. Portfolios are also helpful for independent contractors, consultants, or business owners who need to provide work samples to potential clients.

Outside of a job or client search, archiving samples of your work to a portfolio is a great way to keep track of your accomplishments and make note of when you acquired key competencies. Having it all together in a portfolio can be useful during your yearly review or helpful if you decide to go for a promotion. It can take quite a while to put together a portfolio, so make sure it’s up-to-date to prepare you for unexpected situations like layoffs and sudden changes to your job.

## How will dynamic portfolio help you?
As we all know with the passage of time we enhance our skills, we add more achievements, we accomplish many projects but when it comes to showing it on one page resume, it becomes tougher. In order to put our best projects achievements sometimes we do compromise and leave very important details. In order to overcome that issue we can put one line i.e link of portfolio on resume and reviewer will get a chance to understand you in a better way. Reviewer is just one click away to know your achievements, accomplishments. As this is dynamic in nature so you can add delete update details of your achievements, projects, company details, skills. You completed one project add to your portfolio, got a new job add to your company list, achieved something add to your achievement list, all will be displayed on your portfolio. You don't need to code anything anymore. Isn't it cool?

# Setup
## Software Requirements
1. Navigate to requirements file

## Installations
1. Python 3, pip3
2. Virtual Environment
3. Django ( Will be installing django related packages in virtual environment)
4. Git

## Local Enivronment Setup
1. `Forked the repository`  
2. `git clone [your_project_url]`  
3. Create virtual environment `python3 -m venv venv` macOS or linux  
4. Create virtual environment `py -m venv venv` windows  
5. Activate venv `source venv/bin/activate`   
6. `pip3 install -r ~/dynamicportfolio/requirements.txt`  
7. `cd dynamicportfolio`  
8. `open portfolio/settings.py edit the SECRET_KEY. Never expose your SECRET_KEY so use environment variable`   
9. `python3 manage.py makemigrations` this will create the db.sqlite3 and required tables  
10. `python3 manage.py migrate` will apply all the changes  
11. `python3 manage.py createsuperuser` this will create the superuser or your account.  
12. `python3 manage.py runserver` it will run the `dynamicportfolio` 
13. navigate to `127.0.0.0:8000/admin`  
14. Add new details 
15. navigate to `127.0.0.0:8000` to see the changes    

### Update Social Links
1. `edit dynamicportfolio/templates/profiles.html line: 24 - 40.`  
## Deployment to Amazon Lightsail | EC2 | Heroku
### Amazon Host - Ubuntu 20.X.X
1. [Linux Server Configuration](https://www.youtube.com/watch?v=Sa_kQheCnds&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=13)  
### Heroku Host
2. [Heroku Server Configuration](https://www.youtube.com/watch?v=6DI_7Zja8Zc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=17)

### Checkout my portfolio
[Portfolio](http://www.gourabsinha.com/)

## Custom Domain Configuration
### Amazon Host
1. [Connect domain with Amazon EC2](https://www.youtube.com/watch?v=VedY6EjOBWM)
2. [Connect domain with Amazon Lightsail](https://www.youtube.com/watch?v=LHi4k-2NkDQ)
### Heroku Host
1. [Connect domain with Heroku](https://www.youtube.com/watch?v=xWyaV_ZtLS0)

## Note
If you are facing any kind of issue you can raise the issue I will be looking on those issue and fix those. Or you know the fix I would really appreciate if you can do the pull request.  
I want to thank all the video creators without their videos it would have been difficult for me. 

## Suggestion 
You are always welcome to share you suggestion, I would be happy to know. You can email me at gourab19964u@gmail.com
