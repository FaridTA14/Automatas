# Generated from javaTraductor.g4 by ANTLR 4.9.2
from antlr4 import *
from javaTraductorParser import javaTraductorParser
from javaTraductorListener import ParseTreeListener

# This class defines a complete listener for a parse tree produced by javaTraductorParser.
class generadorJava(ParseTreeListener):

    def __init__(self):
        self.java_code = []
        self.indentation = 0
        self.function_name = ""
        self.has_main = False
        self.parameters = []  # Lista para almacenar parámetros
        self.function_call_values = []  # Lista para valores de llamada
        
    def getJavaCode(self):
        return "\n".join(self.java_code)
    
    # Enter a parse tree produced by javaTraductorParser#program.
    def enterProgram(self, ctx:javaTraductorParser.ProgramContext):
        class_name = "pruebaTraductor"
        self.java_code.append(f"public class {class_name} {{")
        self.indentation += 1

    # Salir de un árbol de parseo producido por javaTraductorParser#program.
    def exitProgram(self, ctx):
        if not self.has_main:
            # Buscar la llamada a función y sus valores
            for child in ctx.children:
                if hasattr(child, 'ID') and hasattr(child, 'arguments'):
                    # Obtener los argumentos de la llamada original
                    self.function_call_values = child.arguments().getText().split(',')
                    break
            
            main_code = [
                "    public static void main(String[] args) {",
                f"        System.out.println({self.function_name}({', '.join(self.function_call_values)}));",
                "    }"
            ]
            self.java_code.extend(main_code)
        self.java_code.append("}")


    # Enter a parse tree produced by javaTraductorParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:javaTraductorParser.FunctionDefinitionContext):
        self.function_name = ctx.ID().getText()
        if ctx.parameters():
            self.parameters = ctx.parameters().getText().split(',')
        
        if self.function_name == "main":
            self.has_main = True
            params_str = "String[] args"
        else:
            params_str = ", ".join(f"int {param}" for param in self.parameters)
            
        self.java_code.append(f"    public static int {self.function_name}({params_str}) {{")
        self.indentation += 1

    # Exit a parse tree produced by javaTraductorParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:javaTraductorParser.FunctionDefinitionContext):
        self.indentation -= 1
        self.java_code.append("    }")
        self.java_code.append("")  # Línea en blanco entre funciones


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
        var_name = ctx.ID().getText()
        expression = ctx.expression().getText()
        # Solo declaramos la variable
        self.java_code.append(f"        int {var_name};")
        # En la siguiente línea asignamos el valor
        self.java_code.append(f"        {var_name} = {expression};")

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
        expression = ctx.expression().getText()
        self.java_code.append(f"        return {expression};")

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
        if ctx.ID().getText() != "print":
            self.function_call_values = ctx.arguments().getText().split(',')

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