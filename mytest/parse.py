
import ast
import json

class FuncLister(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print(node.name)
        self.generic_visit(node)

if __name__ == '__main__':
    """
            'name',
        'args',
        'body',
        'decorator_list',
        'returns',
    """

    # file = open("/Users/cuijl/PycharmProjects/neo-boa/mytest/Hello.py", "r")
    file = open("/Users/cuijl/PycharmProjects/neo-boa/mytest/domain.py", "r")

    code = file.read()

    tree = ast.parse(code)
    data = {}
    functions = []
    events = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functionMap = {}
            argsList = []
            for item in node.args.args:
                argsMap = {}
                argsMap["name"] = item.arg
                argsMap["type"] = ""
                argsList.append(argsMap)

            functionMap['name'] = node.name
            functionMap["parameters"] = argsList
            functionMap["returntype"] = ""
            functions.append(functionMap)

    data["events"] = events
    data["functions"] = functions

    json_data = json.dumps(data, indent=4)
    print(json_data)
