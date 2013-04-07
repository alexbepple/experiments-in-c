#! /usr/bin/env python
## encoding: utf-8

APPNAME = "nerd-golf-tracker"
VERSION = "0.1"

def options(opt):
    opt.load('compiler_c compiler_cxx unittest_gtest waf_unit_test')

def configure(ctx):
    ctx.load('compiler_c compiler_cxx unittest_gtest waf_unit_test')

def build(ctx):
    ctx.stlib(
    	source=ctx.path.ant_glob('src/*.c', excl=['Foo.c']), 
    	includes='src',
    	target='MainLib')
    ctx.stlib(
    	source='contrib/cbehave/cbehave.o', 
    	includes='contrib', 
    	target='CBehaveLib')
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
    ctx.program(
    	features='test',
    	source=ctx.path.ant_glob('test/CBehaveTest.c'),
    	target='behaviourTest',
    	includes='src contrib',
    	use='MainLib CBehaveLib',
    	stlibpath=['build'])
    from waflib.Tools import waf_unit_test
    ctx.add_post_fun(waf_unit_test.summary)
