#! /usr/bin/env python
## encoding: utf-8

APPNAME = "nerd-golf-tracker"
VERSION = "0.1"

def options(opt):
    opt.load('compiler_c')

def configure(ctx):
    ctx.load('compiler_c')
    pass

def build(ctx):
    ctx.program(source='src/foo.c', target='bar')
