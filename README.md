# StudyNet

A small LMS with the following functionality:

- Auth
- Quizzes
- Access to course
- Comment to course
- Quiz in course
- Embedding videos to lesson
- Tracking progress

![avatar](studynet_imgs/studynet-1.png)


### For Vue

```
cd studynet_vue
yarn install
yarn serve
yarn build
```

### For Django

```
cd studynet_django
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
