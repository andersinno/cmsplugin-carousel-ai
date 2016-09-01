# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Carousel, Slide


class CarouselSlideAdmin(admin.StackedInline):
    model = Slide
    extra = 1


class CarouselPlugin(CMSPluginBase):
    model = Carousel
    module = _("Carousel")
    name = _("Image Carousel")
    inlines = (CarouselSlideAdmin,)
    render_template = "cmsplugin_carousel_ai/carousel.html"

    def render(self, context, instance, placeholder):
        context["carousel"] = instance
        context["slides"] = instance.slides.all().select_related("linked_page")
        return context


plugin_pool.register_plugin(CarouselPlugin)
