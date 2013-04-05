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
    	target='libgtest') 
    ctx.stlib(
    	source='src/Bar.cpp',
    	includes='src',
    	target='libBar')
    ctx.program(source='src/foo.c', target='bar')
    ctx.program(
    	features='test',
    	source='test/AllTests.cpp test/BlubbTest.cpp test/BarTest.cpp',
    	target='bartest',
    	includes='contrib src',
    	use='libgtest libBar')
