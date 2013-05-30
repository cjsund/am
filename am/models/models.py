#coding=utf-8
from django.db import models


class Users(models.Model):
#	user_id = models.CharField(max_length=100)
	user_name = models.CharField(max_length=10, verbose_name=u'姓名')
	password = models.CharField(max_length=20, verbose_name=u'密码')
	email = models.EmailField(max_length=30)
	phone = models.CharField(max_length=11, verbose_name=u'电话')
	last_login = models.DateField(auto_now=True)
	date_joined = models.DateField(auto_now=True)
	group_id = models.CharField(max_length=100)
	def __unicode__(self):
		return self.user_name
				

class Group(models.Model):
	group_name = models.CharField(max_length=10)
	group_id = models.CharField(max_length=100)
	def __unicode__(self):
		return self.group_name

class Assets(models.Model):
	MODELSTYPE = (
		(u'r710', u'r710'),
		(u'r410', u'r410'),
	)
	IDC = (
		(u'cc', u'蓝讯'),
		(u'sh', u'森华')
	)
	itmodels = models.CharField(max_length=4, choices=MODELSTYPE, verbose_name=u'设备型号')
	pdate = models.DateField(auto_now=True)
	twdate = models.DateField(auto_now=True)
	hostname = models.CharField(max_length=10, verbose_name=u'主机名')
	servicenum = models.CharField(max_length=20, verbose_name=u'服务编码')
	qservicenum = models.CharField(max_length=20, verbose_name=u'快速服务码')
	mem = models.CharField(max_length=10, verbose_name=u'内存')
	idc = models.CharField(max_length=8, choices=IDC)
	note = models.TextField(verbose_name=u'备注')
# Create your models here.
