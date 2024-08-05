# ZOL Grammar Tester

import sys
from antlr4 import *
from ZOLLexer import ZOLLexer
from ZOLParser import ZOLParser
from ZOLVisitor import ZOLVisitor

class ZOLPrintVisitor(ZOLVisitor):
    def __init__(self):
        self.indent = 0

    def print_indent(self):
        return "  " * self.indent

    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    def visitFunctionDecl(self, ctx):
        name = ctx.IDENTIFIER().getText()
        params = self.visit(ctx.paramList()) if ctx.paramList() else []
        out_reg = ctx.register().getText() if ctx.register() else None
        print(f"{self.print_indent()}Function: {name}")
        print(f"{self.print_indent()}  Parameters: {params}")
        print(f"{self.print_indent()}  Output Register: {out_reg}")
        self.indent += 1
        body = self.visit(ctx.block())
        self.indent -= 1
        return f"Function {name}"

    def visitParamList(self, ctx):
        return [self.visit(param) for param in ctx.param()]

    def visitParam(self, ctx):
        name = ctx.IDENTIFIER().getText()
        type_ = ctx.type_().getText()
        reg = ctx.register().getText() if ctx.register() else None
        return f"{name}: {type_}" + (f" in {reg}" if reg else "")

    def visitStatement(self, ctx):
        if ctx.expr():
            return f"{self.print_indent()}Expr: {self.visit(ctx.expr())}"
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        elif ctx.block():
            return self.visit(ctx.block())

    def visitIfStatement(self, ctx):
        print(f"{self.print_indent()}If Statement:")
        self.indent += 1
        print(f"{self.print_indent()}Condition: {self.visit(ctx.expr())}")
        self.visit(ctx.block(0))
        if ctx.block(1):
            print(f"{self.print_indent()}Else:")
            self.visit(ctx.block(1))
        self.indent -= 1
        return "If Statement"

    def visitWhileStatement(self, ctx):
        print(f"{self.print_indent()}While Statement:")
        self.indent += 1
        print(f"{self.print_indent()}Condition: {self.visit(ctx.expr())}")
        self.visit(ctx.block())
        self.indent -= 1
        return "While Statement"

    def visitBlock(self, ctx):
        print(f"{self.print_indent()}Block:")
        self.indent += 1
        for stmt in ctx.statement():
            self.visit(stmt)
        self.indent -= 1
        return "Block"

    def visitExpr(self, ctx):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.INTEGER():
            return ctx.INTEGER().getText()
        else:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.op.text
            return f"{left} {op} {right}"

def main(input_file):
    input_stream = FileStream(input_file)
    lexer = ZOLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ZOLParser(stream)
    tree = parser.program()
    
    visitor = ZOLPrintVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide a ZOL file as an argument.")