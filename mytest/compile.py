#!/usr/bin/env python
# coding=utf-8


from boa.compiler import Compiler

# bytes = Compiler.load_and_save('./file.py')
# bytes = Compiler.load_and_save('./Hello.py')
# bytes = Compiler.load_and_save('./Domainpy2.py')
# bytes = Compiler.load_and_save('./print.py')
# bytes = Compiler.load_and_save('./base.py')
# bytes = Compiler.load_and_save('./NEP5.py')


# bytes = Compiler.load_and_save('./domain.py')


if __name__ == '__main__':
    compiler = Compiler.load("./mytest/Hello.py")
    # compiler code
    result = compiler.write()
    print("result: ", result)

    # compiler abi
    result = compiler.write_abi()
    print("result: ", result)

    # generate avm, debug, abi file
    # result = Compiler.load_and_save("./mytest/Hello.py")
