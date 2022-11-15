from django.core.exceptions import ValidationError


def phone(value):
    if not value.isdigit() or not len(str(value)) == 10:
        raise ValidationError('Please enter only digits')


PARENT_TYPE = [('Mother', 'Mother'), ('Father', 'Father'),
               ('Grandmother', 'Grandmother'), ('Grandfather', 'Grandfather')]

LIST_OF_GRADES = [
    ('insufficient', 'insufficient'),
    ('sufficient', 'sufficient'),
    ('good', 'good'),
    ('very good', 'very good'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
]

TYPE_OF_ACTIVITY = [
    ('Test paper', 'Test paper'),
    ('Listening', 'Listening')
]

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]

ENROLLMENT_CHOICES = [
    ('Preparatory class', 'Preparatory class'),
    ('1st grade', '1st grade'),
    ('2nd grade', '2nd grade'),
    ('3rd grade', '3rd grade'),
    ('4th grade', '4th grade'),
    ('5th grade', '5th grade'),
    ('6th grade', '6th grade'),
    ('7th grade', '7th grade'),
    ('8th grade', '8th grade'),
]

STATUS = [('Active', 'Active'), ('Inactive', 'Inactive')]


def cnp(value):
    if not value.isdigit() or not len(str(value)) == 13:
        raise ValidationError('CNP must contain only numbers of minimum length of 13')


SCHOOL_SUBJECT = [
    ('Math', 'Math'),
    ('Science', 'Science'),
    ('Art', 'Art'),
    ('Geography', 'Geography'),
    ('History', 'History'),
    ('Music', 'Music'),
    ('Logic', 'Logic'),
    ('Chemistry', 'Chemistry'),
    ('Informatics', 'Informatics'),
]

