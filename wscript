#! /usr/bin/env python
## encoding: utf-8

APPNAME = "nerd-golf-tracker"
VERSION = "0.1"

def options(opt):
    opt.load('compiler_c compiler_cxx unittest_gtest')

def configure(ctx):
    ctx.load('compiler_c compiler_cxx unittest_gtest')

def build(ctx):
    ctx.stlib(
    	source=ctx.path.ant_glob('src/*.c', excl=['Foo.c']), 
    	includes='src',
    	target='MainLib')
    ctx.program(
    	source='src/Foo.c', 
    	includes='src', 
    	target='Main',
        use='MainLib')
    ctx.program(
    	features='gtest',
    	source=ctx.path.ant_glob('test/BarTest.cpp', excl=['AllTests.cpp']),
    	target='testMain',
    	includes='src',
    	use='MainLib GTEST',
    	stlibpath=['build'])
