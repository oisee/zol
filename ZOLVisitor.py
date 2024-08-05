# Generated from ZOL.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZOLParser import ZOLParser
else:
    from ZOLParser import ZOLParser

# This class defines a complete generic visitor for a parse tree produced by ZOLParser.

class ZOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZOLParser#program.
    def visitProgram(self, ctx:ZOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#functionDecl.
    def visitFunctionDecl(self, ctx:ZOLParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#paramList.
    def visitParamList(self, ctx:ZOLParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#param.
    def visitParam(self, ctx:ZOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#structDecl.
    def visitStructDecl(self, ctx:ZOLParser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#enumDecl.
    def visitEnumDecl(self, ctx:ZOLParser.EnumDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#variableDecl.
    def visitVariableDecl(self, ctx:ZOLParser.VariableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#statement.
    def visitStatement(self, ctx:ZOLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#block.
    def visitBlock(self, ctx:ZOLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#ifStatement.
    def visitIfStatement(self, ctx:ZOLParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#whileStatement.
    def visitWhileStatement(self, ctx:ZOLParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#repeatStatement.
    def visitRepeatStatement(self, ctx:ZOLParser.RepeatStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#forStatement.
    def visitForStatement(self, ctx:ZOLParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#matchStatement.
    def visitMatchStatement(self, ctx:ZOLParser.MatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#matchCase.
    def visitMatchCase(self, ctx:ZOLParser.MatchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#expressionStatement.
    def visitExpressionStatement(self, ctx:ZOLParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#returnStatement.
    def visitReturnStatement(self, ctx:ZOLParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#asmBlock.
    def visitAsmBlock(self, ctx:ZOLParser.AsmBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#expression.
    def visitExpression(self, ctx:ZOLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#primary.
    def visitPrimary(self, ctx:ZOLParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:ZOLParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#structLiteral.
    def visitStructLiteral(self, ctx:ZOLParser.StructLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#typeSpec.
    def visitTypeSpec(self, ctx:ZOLParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZOLParser#register.
    def visitRegister(self, ctx:ZOLParser.RegisterContext):
        return self.visitChildren(ctx)



del ZOLParser