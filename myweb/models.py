from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'

class Order(models.Model): 
        # fields of the model 
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length = 50) 
    location = models.CharField(max_length = 100) 
    datetime = models.DateTimeField(auto_now_add = False)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self): 
        return f'{self.name} - {self.timestamp}'

class ContactMail(models.Model):
    User_name = models.CharField(max_length=50)
    User_email = models.EmailField(max_length=50)
    User_msg = models.CharField(max_length=255)


    def __str__(self):
        return self.User_name +  '    '   + self.User_email