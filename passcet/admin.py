from django.contrib import admin
from passcet.models import *


# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'leavel', 'lastimei', 'logintime', 'registertime', 'img_md5')
    search_fields = ['id']


class emailcodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'time')
    search_fields = ['code']


class wordAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'ph_en', 'ph_am', 'ph_en_mp3', 'ph_am_mp3', 'description', 'sentence', 'cet4', 'cet6')
    search_fields = ['word']


class glossaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'word', 'description')
    search_fields = ['word']


class logAdmin(admin.ModelAdmin):
    list_display = ('id', 'api_part', 'status', 'time')
    search_fields = ['api_part']


class timeAdmin(admin.ModelAdmin):
    list_display = ('id', 'userid', 'learningtime', 'datetime')
    search_fields = ['userid']


class rankAdmin(admin.ModelAdmin):
    list_display = ('id', 'userid', 'username', 'totaltime')
    search_fields = ['userid']


class feedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email', 'feedback','isChecked')
    search_fields = ['phone', 'email']

class paperAdmin(admin.ModelAdmin):
    list_display = ('id','cetype','problemtype','year','problem','answer','source')
    search_fields = ['year']


admin.site.register(passcet_user, userAdmin)
admin.site.register(passcet_emailcode, emailcodeAdmin)
admin.site.register(passcet_word, wordAdmin)
admin.site.register(passcet_glossary, glossaryAdmin)
admin.site.register(passcet_log, logAdmin)
admin.site.register(passcet_time, timeAdmin)
admin.site.register(passcet_ranklist, rankAdmin)
admin.site.register(passcet_feedback, feedbackAdmin)
admin.site.register(passcet_paper,paperAdmin)
