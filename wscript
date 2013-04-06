#! /usr/bin/env python
## encoding: utf-8

APPNAME = "nerd-golf-tracker"
VERSION = "0.1"

def options(opt):
    opt.load('compiler_c compiler_cxx waf_unit_test')

def configure(ctx):
    ctx.load('compiler_c compiler_cxx waf_unit_test')

def build(ctx):
    from waflib.Tools import waf_unit_test
    ctx.add_post_fun(waf_unit_test.summary)
    ctx.stlib(
    	source='contrib/gtest/gtest-all.cc', 
    	includes='contrib', 
    	target='Gtest')
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
    	features='test',
    	source=ctx.path.ant_glob(['test/*.cpp']),
    	target='testMain',
    	includes='contrib src',
    	use='Gtest MainLib',
    	stlibpath=['build'])
