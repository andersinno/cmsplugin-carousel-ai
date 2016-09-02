# -*- coding: utf-8 -*-
from cms.models import CMSPlugin, force_text, Page
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField


class Carousel(CMSPlugin):
    """
    Model for storing carousel meta data and configuration.
    """
    name = models.CharField(
        verbose_name=_("name"),
        max_length=160,
    )
    interval = models.FloatField(
        verbose_name=_("slide changing time in seconds"),
        default=5.0,
    )

    def __str__(self):
        return "%s" % self.name

    @property
    def interval_in_ms(self):
        """
        The slide change interval in milliseconds
        :rtype: int
        """
        return int(self.interval * 1000)

    def copy_relations(self, oldinstance):
        """
        Make a copy of the related slides for the new carousel object.
        See docs: http://docs.django-cms.org/en/release-3.3.x/how_to/custom_plugins.html#for-foreign-key-relations-from-other-objects  # NOQA
        """
        for slide in oldinstance.slides.all():
            slide.pk = None
            slide.carousel = self
            slide.save()


class Slide(models.Model):
    """
    Model for storing carousel slide related data.
    """
    carousel = models.ForeignKey(
        Carousel,
        verbose_name=_("carousel"),
        related_name="slides",
    )
    image = FilerImageField(
        verbose_name=_("slide image"),
    )
    caption = models.CharField(
        verbose_name=_("slide caption"),
        max_length=160,
        blank=True,
    )
    url = models.URLField(
        verbose_name=_("link to URL"),
        max_length=250,
        blank=True,
    )
    linked_page = models.ForeignKey(
        Page,
        verbose_name=_("link to page"),
        null=True,
        blank=True,
        help_text=_("Page link overrides given URL."),
        limit_choices_to={"publisher_is_draft": False},
    )
    call_to_action_label = models.CharField(
        verbose_name=_("call to action label"),
        max_length=250,
        blank=True
    )
    ordering = models.IntegerField(
        verbose_name=_("ordering"),
        default=0,
        help_text=_("Number which determines the order of slides in carousel. Smallest value first."),
        db_index=True,
    )

    class Meta:
        ordering = ("ordering",)

    def __str__(self):
        return force_text(self.caption or self.image.label)

    @property
    def link(self):
        """Returns primary link."""
        if self.linked_page_id:
            return self.linked_page.get_absolute_url()
        return self.url

    @property
    def has_link(self):
        return bool(self.linked_page_id or self.url)

    @property
    def has_call_to_action(self):
        """
        States whether the slide has the required information for a Call To Action.
        :rtype: bool
        """
        return bool(self.call_to_action_label and self.has_link)
