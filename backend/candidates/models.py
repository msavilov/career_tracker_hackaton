from django.conf import settings
from django.core.validators import MinLengthValidator, RegexValidator
from django.db.models import (SET_NULL, CharField, DateTimeField, EmailField,
                              ForeignKey, ImageField, IntegerField, Model,
                              TextField,)


class Location(Model):
    """
    Модель, представляющая данные для выбора местоположения
    соискателя или вакансии.
    """
    name = CharField(
        max_length=2,
        choices=settings.LOCATION_CHOICES,
        default='MS',
        verbose_name='Местонахождение',
    )

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class Course(Model):
    """
    Модель, представляющая данные для выбора пройденного
    соискателем курса на Яндекс.Практикум.
    """
    name = CharField(
        max_length=2,
        choices=settings.COURSE_CHOICES,
        default='PR',
        verbose_name='Пройденный курс',
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class WorkFormat(Model):
    """
    Модель, представляющая данные для выбора категории
    формата работы.
    """
    name = CharField(
        max_length=2,
        choices=settings.WORK_FORMAT_CHOICES,
        default='PR',
        verbose_name='Формат работы',
    )

    class Meta:
        verbose_name = 'Формат работы'
        verbose_name_plural = 'Форматы работы'

    def __str__(self):
        return self.name


class Employment(Model):
    """
    Модель, представляющая данные для выбора категории опыта
    соискателя.
    """
    name = CharField(
        max_length=2,
        choices=settings.EMPLOYMENT_CHOICES,
        default='PR',
        verbose_name='Опыт работы соискателя',
    )

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыты работы'

    def __str__(self):
        return self.name


class Education(Model):
    name = CharField(
        max_length=2,
        choices=settings.EDUCATION_CHOICES,
        default='HI',
        verbose_name='Форма обучения',
    )

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'

    def __str__(self):
        return self.name


class Portfolio(Model):
    """
    Модель, хранящая ссылки на портфолио соискателя.
    """
    behance = CharField(
        max_length=settings.MAX_LENGTH,
        verbose_name='Ссылка на Behance',
        null=True,
        blank=True,
    )
    linkedin = CharField(
        max_length=settings.MAX_LENGTH,
        verbose_name='Ссылка на LinkedIn',
        null=True,
        blank=True,
    )
    github = CharField(
        max_length=settings.MAX_LENGTH,
        verbose_name='Ссылка на GitHub',
        null=True,
        blank=True,
    )
    hh = CharField(
        max_length=settings.MAX_LENGTH,
        verbose_name='Ссылка на HH',
        null=True,
        blank=True,
    )
    created_at = DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'

    def __str__(self):
        return (f'Ссылки {self.behance} '
                f'{self.linkedin} {self.github} {self.hh} '
                )


class Contact(Model):
    """
    Модель, хранящая контактные данные пользователя
    """
    phone = CharField(
        max_length=settings.PHONE_MAX_LENGTH,
        validators=[MinLengthValidator(settings.PHONE_MIN_LENGTH),
                    RegexValidator(
                        regex=r'^[-\d\+\)\( ]+\Z',
                        message='Допускаются цифры, (), +- и пробел')],
        blank=True,
        null=True,
        verbose_name='Номер телефона',
    )
    email = EmailField(
        max_length=settings.MAX_LENGTH,
        null=True,
        blank=True,
        verbose_name='Электронная почта',
    )
    telegram = CharField(
        max_length=settings.MAX_LENGTH,
        blank=True,
        null=True,
        verbose_name='Телеграм',
    )
    created_at = DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return (f'Контакты {self.phone} '
                f'{self.email} {self.telegram}'
                )


class Experience(Model):
    candidate = ForeignKey(
        'Candidate',
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='experience_candidate',
    )
    company = CharField(
        max_length=settings.MAX_LENGTH,
        verbose_name='Название компании',
    )
    experience = TextField(
        verbose_name='Опыт и достижения соискателя в компании',
    )
    create_dt = DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время добавления',
    )

    class Meta:
        verbose_name = 'Опыт соискателя'
        verbose_name_plural = 'Опыты соискателя'

    def __str__(self):
        return (f'{self.candidate} в компании {self.company} имел опыт: '
                f'{self.experience}'
                )


class Candidate(Model):
    """
    Модель, хранящая данные резюме соискателя
    """
    name = CharField(
        verbose_name='Фамилия и имя кандидата',
        max_length=settings.MAX_LENGTH,
    )
    specialization = CharField(
        verbose_name='Должность',
        max_length=settings.MAX_LENGTH,
    )
    course = ForeignKey(
        Course,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='candidate_course',
    )
    location = ForeignKey(
        Location,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='candidate_location',
    )
    skills = TextField(
        null=True,
        blank=True,
        verbose_name='Навыки кандидата',
    )
    years_exp = IntegerField(
        null=True,
        blank=True,
        verbose_name='Лет опыта',
    )
    experience = ForeignKey(
        Experience,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='candidate_experience',
    )
    work_format = ForeignKey(
        WorkFormat,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='candidate_work_format',
    )
    employment = ForeignKey(
        Employment,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='candidate_employment',
    )
    education = ForeignKey(
        Education,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='candidate_education',
    )
    about = TextField(
        null=True,
        blank=True,
        verbose_name='О себе',
    )
    capture = ImageField(
        'Аватар',
        null=True,
        blank=True,
    )
    portfolio = ForeignKey(
        Portfolio,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='candidate_portfolio',
    )
    contact = ForeignKey(
        Contact,
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name='candidate_contact',
    )
    create_dt = DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания отклика',
    )
    edit_dt = DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения отклика',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'

    def __str__(self):
        return self.name
