# -*- coding: utf-8 -*-

from jbox_gearman.decorators import gearman_task

# DECLARE WORKER NAME AND WORKER PARAMETERS
worker_name = __name__.split('.')[2]

# REGISTER WORKER IN GEARMAN
@gearman_task(name=worker_name, queue='foo')
def function(sentence):
  print "received data on 'worker_name' task : %s" % sentence
  return sentence[::-1]

@gearman_task(name='foo', queue='foo')
def function(sentence):
  print "received data on 'foo' task : %s" % sentence
  return sentence[::-1]

@gearman_task(name='foofoo', queue='foofoo')
def function(sentence1, sentence2):
  print "received data on 'foofoo' task : %s %s" % (sentence1, sentence2)
  print "%s %s" % (sentence1[::-1], sentence2[::-1])
  return
