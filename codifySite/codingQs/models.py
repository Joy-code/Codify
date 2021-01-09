from django.db import models
from django.urls import reverse


# model representing a category of coding questions
class Category(models.Model):
    QUESTION_CATEGORY = (
        ('AS', 'Arrays and Strings'),
        ('LL', 'Linked Lists'),
        ('SQ', 'Stacks and Queues'),
        ('TG', 'Trees and Graphs'),
        ('RD', 'Recursion and Dynamic Programming'),
        ('SS', 'Sorting and Searching'),
    )

    name = models.CharField(
        max_length=2, 
        choices=QUESTION_CATEGORY,
        blank=True,
        help_text='Question category',
    )

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

# model representing the difficulty of a specific question
class Difficulty(models.Model):
    QUESTION_DIFFICULTY = (
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard'),
    )

    difficulty = models.CharField(
        max_length=1, 
        choices=QUESTION_DIFFICULTY,
        blank=True,
        help_text='Question difficulty',
    )

    class Meta:
        verbose_name_plural = "difficulties"

    def __str__(self):
        return self.difficulty
    

# model representing a specific coding question
class codingQ(models.Model):
    name = models.CharField(max_length=200)

    category = models.ForeignKey(Category, on_delete=models.RESTRICT, help_text='Select a category for this question')

    difficulty = models.ForeignKey(Difficulty, on_delete=models.RESTRICT, help_text='Select a difficulty for this question')

    QUESTION_STATUS = (
        ('N', 'Not attempted'),
        ('P', 'Practicing'),
        ('C', 'Completed'),
    )

    status = models.CharField(
        max_length=1, 
        choices=QUESTION_STATUS,
        blank=True,
        default='N',
        help_text='Question status',
    )
    
    last_studied = models.DateTimeField('Last Studied')

    upcoming_reminder = models.DateTimeField('Upcoming Reminder')

    question_text = models.TextField(max_length=1000, help_text='Enter a description of the question')

    solution_stategy = models.TextField(max_length=1000, help_text='Enter the strategy for solving the problem ')

    # solution_code = models.ImageField() '''install Pillow and change args'''

    # pastAttempts = 

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Coding Questions"

    def __str__(self):
        return self.name

    # returns the url to access a detail record for this question
    def get_absolute_url(self): 
        return reverse('question-detail', args=[str(self.id)])


# model representing an attempt at solving a coding question
class Attempt(models.Model):
    question = models.ForeignKey(codingQ, on_delete=models.RESTRICT)
    time_attempted = models.DateTimeField('Time Attempted')

    ATTEMPT_STATUS = (
        ('S', 'Solved'),
        ('U', 'Unsolved')
    )

    status = models.CharField(
        max_length=1, 
        choices=ATTEMPT_STATUS,
        default='U',
        help_text='Indicate whether attempt was successful'
    )

    time_to_solve = models.DurationField(blank=True)

    notes = models.TextField(max_length=1000, help_text='Enter what you learned from this attempt')
    
    class Meta:
        ordering = ['-time_attempted']

    def __str__(self):
        return f'{self.question} ({self.time_attempted})'

    # returns the url to access a detail record for this attempt
    def get_absolute_url(self): 
        return reverse('attempt-detail', args=[str(self.id)])