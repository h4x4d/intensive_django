from django.db import models

from Core.models import PublishedBaseModel, NamedBaseModel, SlugBaseModel
from .validators import validate_must_be_param


class Category(PublishedBaseModel, NamedBaseModel, SlugBaseModel):
    weight = models.SmallIntegerField(default=100)

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"

    def __str__(self):
        return self.name


class Tag(PublishedBaseModel, NamedBaseModel, SlugBaseModel):
    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name


class Item(PublishedBaseModel, NamedBaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="items")
    tags = models.ManyToManyField(Tag, related_name="items")
    text = models.TextField("Текст",
                            validators=[validate_must_be_param('превосходно',
                                                               'роскошно')])

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
