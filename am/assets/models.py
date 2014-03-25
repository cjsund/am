#coding=utf-8
from django.db import models

class Group(models.Model):
	group_name = models.CharField(max_length=10)
	group_id = models.CharField(max_length=100)
	def __unicode__(self):
		return self.group_name
#	def create_group(self, group_name, group_id):
#		group = self.model(group_name='group_name', group_id='group_id')
#		group.save()

class User(models.Model):
#	user_id = models.CharField(max_length=100)
	user_name = models.CharField(max_length=10, verbose_name=u'姓名')
	password = models.CharField(max_length=20, verbose_name=u'密码')
	email = models.EmailField(max_length=30, blank=True)
	phone = models.CharField(max_length=11, verbose_name=u'电话')
	last_login = models.DateField(auto_now=True)
	date_joined = models.DateField(auto_now=True)
	group = models.ForeignKey(Group, verbose_name=u'用户组')
	def __unicode__(self):
		return u'%s %s' % (self.user_name, self.group)
				

class Asset(models.Model):
	MODELSTYPE = (
		(u'r710', u'r710'),
		(u'r410', u'r410'),
	)
	IDC = (
		(u'cc', u'dd'),
		(u'sh', u'aa'),
	)
	MEMBER = (
		(u'8', '1024*8MB'),
		(u'16', '1024*16MB'),
		)
	itmodels = models.CharField(max_length=4, choices=MODELSTYPE, verbose_name=u'设备型号')
	pdate = models.DateField(auto_now=True)
	twdate = models.DateField(auto_now=True)
	hostname = models.CharField(max_length=10, verbose_name=u'主机名')
	servicenum = models.CharField(max_length=20, verbose_name=u'服务编码')
	qservicenum = models.CharField(max_length=20, verbose_name=u'快速服务码')
	mem = models.CharField(max_length=10, verbose_name=u'内存', choices=MEMBER)
	idc = models.CharField(max_length=8, choices=IDC)
	note = models.TextField(verbose_name=u'备注')
	def __unicode__(self):
		return u'%s %s %s' % (self.hostname, self.itmodels, self.idc)
# Create your models here.
