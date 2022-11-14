from django.db import models
from django.db.models import Prefetch

from Core.models import PublishedBaseModel, NamedBaseModel, SlugBaseModel, \
    ImageBaseModel
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_NULL

from .validators import validate_must_be_param


class ItemManager(models.Manager):
    def published(self):
        return (self.get_queryset().filter(is_published=True)
                .select_related('category', 'mainimage')
                .prefetch_related(Prefetch('tags',
                                           queryset=Tag.objects.all())))

    def category_sorted(self):
        return self.published().order_by('category__name')

    def on_main(self):
        return self.published().filter(is_on_main=True)


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
    objects = ItemManager()

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="items")
    tags = models.ManyToManyField(Tag, related_name="items")
    text = MarkdownField(rendered_field='text_rendered',
                         validator=VALIDATOR_NULL,
                         validators=[validate_must_be_param("превосходно",
                                                            "роскошно")])
    text_rendered = RenderedMarkdownField(default="")

    is_on_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']

    def __str__(self):
        return self.name


class MainImage(ImageBaseModel):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Главное изображение"
        verbose_name_plural = "Главные изображения"

    def __str__(self):
        return "Изображение " + self.item.name


class GalleryImage(ImageBaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name='images')

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return "Изображение '" + self.item.name + "'"
