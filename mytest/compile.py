#!/usr/bin/env python
# coding=utf-8


from boa.compiler import Compiler

# bytes = Compiler.load_and_save('./file.py')
# bytes = Compiler.load_and_save('./Hello.py')
# bytes = Compiler.load_and_save('./Domainpy2.py')
# bytes = Compiler.load_and_save('./print.py')
# bytes = Compiler.load_and_save('./base.py')
# bytes = Compiler.load_and_save('./NEP5.py')
bytes = Compiler.load_and_save('./domain.py')





print(bytes.hex())