# -*- coding: utf-8 -*-

from jbox_gearman.decorators import gearman_task

# DECLARE WORKER NAME AND WORKER PARAMETERS
worker_name = __name__.split('.')[2]

# REGISTER WORKER IN GEARMAN
@gearman_task(name=worker_name, queue='bar')
def function(sentence):
  print "received data on 'worker_name' task : %s" % sentence
  return sentence[::-1]

@gearman_task(name='bar', queue='bar')
def function(sentence):
  print "received data on 'bar' task : %s" % sentence
  return sentence[::-1]

@gearman_task(name='barbar', queue='barbar')
def function(sentence):
  print "received data on 'barbar' task : %s" % sentence
  return sentence[::-1]
