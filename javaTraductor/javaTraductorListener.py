# Generated from javaTraductor.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .javaTraductorParser import javaTraductorParser
else:
    from javaTraductorParser import javaTraductorParser

# This class defines a complete listener for a parse tree produced by javaTraductorParser.
class javaTraductorListener(ParseTreeListener):

    # Enter a parse tree produced by javaTraductorParser#program.
    def enterProgram(self, ctx:javaTraductorParser.ProgramContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#program.
    def exitProgram(self, ctx:javaTraductorParser.ProgramContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:javaTraductorParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:javaTraductorParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#parameters.
    def enterParameters(self, ctx:javaTraductorParser.ParametersContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#parameters.
    def exitParameters(self, ctx:javaTraductorParser.ParametersContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#block.
    def enterBlock(self, ctx:javaTraductorParser.BlockContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#block.
    def exitBlock(self, ctx:javaTraductorParser.BlockContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#statement.
    def enterStatement(self, ctx:javaTraductorParser.StatementContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#statement.
    def exitStatement(self, ctx:javaTraductorParser.StatementContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:javaTraductorParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:javaTraductorParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#expressionStatement.
    def enterExpressionStatement(self, ctx:javaTraductorParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#expressionStatement.
    def exitExpressionStatement(self, ctx:javaTraductorParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#returnStatement.
    def enterReturnStatement(self, ctx:javaTraductorParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#returnStatement.
    def exitReturnStatement(self, ctx:javaTraductorParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#expression.
    def enterExpression(self, ctx:javaTraductorParser.ExpressionContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#expression.
    def exitExpression(self, ctx:javaTraductorParser.ExpressionContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#term.
    def enterTerm(self, ctx:javaTraductorParser.TermContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#term.
    def exitTerm(self, ctx:javaTraductorParser.TermContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#factor.
    def enterFactor(self, ctx:javaTraductorParser.FactorContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#factor.
    def exitFactor(self, ctx:javaTraductorParser.FactorContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#functionCall.
    def enterFunctionCall(self, ctx:javaTraductorParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#functionCall.
    def exitFunctionCall(self, ctx:javaTraductorParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#arguments.
    def enterArguments(self, ctx:javaTraductorParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#arguments.
    def exitArguments(self, ctx:javaTraductorParser.ArgumentsContext):
        pass



del javaTraductorParser