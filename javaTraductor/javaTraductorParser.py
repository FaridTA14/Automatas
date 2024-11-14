# Generated from javaTraductor.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("m\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\6\2\36\n\2\r\2\16\2\37\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\7\4-\n\4\f\4\16\4\60\13\4\3\5\6\5")
        buf.write("\63\n\5\r\5\16\5\64\3\6\3\6\3\6\5\6:\n\6\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\7\nI\n\n\f\n\16")
        buf.write("\nL\13\n\5\nN\n\n\3\13\3\13\3\13\7\13S\n\13\f\13\16\13")
        buf.write("V\13\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f^\n\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\7\16h\n\16\f\16\16\16k\13\16\3\16")
        buf.write("\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\4\3\2\n\13")
        buf.write("\3\2\f\r\2j\2\35\3\2\2\2\4!\3\2\2\2\6)\3\2\2\2\b\62\3")
        buf.write("\2\2\2\n9\3\2\2\2\f;\3\2\2\2\16?\3\2\2\2\20A\3\2\2\2\22")
        buf.write("M\3\2\2\2\24O\3\2\2\2\26]\3\2\2\2\30_\3\2\2\2\32d\3\2")
        buf.write("\2\2\34\36\5\4\3\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35\3")
        buf.write("\2\2\2\37 \3\2\2\2 \3\3\2\2\2!\"\7\3\2\2\"#\7\16\2\2#")
        buf.write("$\7\5\2\2$%\5\6\4\2%&\7\6\2\2&\'\7\b\2\2\'(\5\b\5\2(\5")
        buf.write("\3\2\2\2).\7\16\2\2*+\7\7\2\2+-\7\16\2\2,*\3\2\2\2-\60")
        buf.write("\3\2\2\2.,\3\2\2\2./\3\2\2\2/\7\3\2\2\2\60.\3\2\2\2\61")
        buf.write("\63\5\n\6\2\62\61\3\2\2\2\63\64\3\2\2\2\64\62\3\2\2\2")
        buf.write("\64\65\3\2\2\2\65\t\3\2\2\2\66:\5\16\b\2\67:\5\20\t\2")
        buf.write("8:\5\f\7\29\66\3\2\2\29\67\3\2\2\298\3\2\2\2:\13\3\2\2")
        buf.write("\2;<\7\16\2\2<=\7\t\2\2=>\5\22\n\2>\r\3\2\2\2?@\5\22\n")
        buf.write("\2@\17\3\2\2\2AB\7\4\2\2BC\5\22\n\2C\21\3\2\2\2DN\5\30")
        buf.write("\r\2EJ\5\24\13\2FG\t\2\2\2GI\5\24\13\2HF\3\2\2\2IL\3\2")
        buf.write("\2\2JH\3\2\2\2JK\3\2\2\2KN\3\2\2\2LJ\3\2\2\2MD\3\2\2\2")
        buf.write("ME\3\2\2\2N\23\3\2\2\2OT\5\26\f\2PQ\t\3\2\2QS\5\26\f\2")
        buf.write("RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\25\3\2\2\2V")
        buf.write("T\3\2\2\2W^\7\16\2\2X^\7\17\2\2YZ\7\5\2\2Z[\5\22\n\2[")
        buf.write("\\\7\6\2\2\\^\3\2\2\2]W\3\2\2\2]X\3\2\2\2]Y\3\2\2\2^\27")
        buf.write("\3\2\2\2_`\7\16\2\2`a\7\5\2\2ab\5\32\16\2bc\7\6\2\2c\31")
        buf.write("\3\2\2\2di\5\22\n\2ef\7\7\2\2fh\5\22\n\2ge\3\2\2\2hk\3")
        buf.write("\2\2\2ig\3\2\2\2ij\3\2\2\2j\33\3\2\2\2ki\3\2\2\2\13\37")
        buf.write(".\649JMT]i")
        return buf.getvalue()


class javaTraductorParser ( Parser ):

    grammarFileName = "javaTraductor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "'('", "')'", "','", 
                     "':'", "'='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "DEF", "RETURN", "LPAREN", "RPAREN", 
                      "COMMA", "COLON", "ASSIGN", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "ID", "Number", "WS" ]

    RULE_program = 0
    RULE_functionDefinition = 1
    RULE_parameters = 2
    RULE_block = 3
    RULE_statement = 4
    RULE_assignmentStatement = 5
    RULE_expressionStatement = 6
    RULE_returnStatement = 7
    RULE_expression = 8
    RULE_term = 9
    RULE_factor = 10
    RULE_functionCall = 11
    RULE_arguments = 12

    ruleNames =  [ "program", "functionDefinition", "parameters", "block", 
                   "statement", "assignmentStatement", "expressionStatement", 
                   "returnStatement", "expression", "term", "factor", "functionCall", 
                   "arguments" ]

    EOF = Token.EOF
    DEF=1
    RETURN=2
    LPAREN=3
    RPAREN=4
    COMMA=5
    COLON=6
    ASSIGN=7
    PLUS=8
    MINUS=9
    MULTIPLY=10
    DIVIDE=11
    ID=12
    Number=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaTraductorParser.FunctionDefinitionContext)
            else:
                return self.getTypedRuleContext(javaTraductorParser.FunctionDefinitionContext,i)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = javaTraductorParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.functionDefinition()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==javaTraductorParser.DEF):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(javaTraductorParser.DEF, 0)

        def ID(self):
            return self.getToken(javaTraductorParser.ID, 0)

        def LPAREN(self):
            return self.getToken(javaTraductorParser.LPAREN, 0)

        def parameters(self):
            return self.getTypedRuleContext(javaTraductorParser.ParametersContext,0)


        def RPAREN(self):
            return self.getToken(javaTraductorParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(javaTraductorParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(javaTraductorParser.BlockContext,0)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = javaTraductorParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(javaTraductorParser.DEF)
            self.state = 32
            self.match(javaTraductorParser.ID)
            self.state = 33
            self.match(javaTraductorParser.LPAREN)
            self.state = 34
            self.parameters()
            self.state = 35
            self.match(javaTraductorParser.RPAREN)
            self.state = 36
            self.match(javaTraductorParser.COLON)
            self.state = 37
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(javaTraductorParser.ID)
            else:
                return self.getToken(javaTraductorParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(javaTraductorParser.COMMA)
            else:
                return self.getToken(javaTraductorParser.COMMA, i)

        def getRuleIndex(self):
            return javaTraductorParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = javaTraductorParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(javaTraductorParser.ID)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==javaTraductorParser.COMMA:
                self.state = 40
                self.match(javaTraductorParser.COMMA)
                self.state = 41
                self.match(javaTraductorParser.ID)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaTraductorParser.StatementContext)
            else:
                return self.getTypedRuleContext(javaTraductorParser.StatementContext,i)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = javaTraductorParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 47
                self.statement()
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << javaTraductorParser.RETURN) | (1 << javaTraductorParser.LPAREN) | (1 << javaTraductorParser.ID) | (1 << javaTraductorParser.Number))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionStatement(self):
            return self.getTypedRuleContext(javaTraductorParser.ExpressionStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(javaTraductorParser.ReturnStatementContext,0)


        def assignmentStatement(self):
            return self.getTypedRuleContext(javaTraductorParser.AssignmentStatementContext,0)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = javaTraductorParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.expressionStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.returnStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.assignmentStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(javaTraductorParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(javaTraductorParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(javaTraductorParser.ExpressionContext,0)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)




    def assignmentStatement(self):

        localctx = javaTraductorParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(javaTraductorParser.ID)
            self.state = 58
            self.match(javaTraductorParser.ASSIGN)
            self.state = 59
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(javaTraductorParser.ExpressionContext,0)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = javaTraductorParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(javaTraductorParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(javaTraductorParser.ExpressionContext,0)


        def getRuleIndex(self):
            return javaTraductorParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = javaTraductorParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(javaTraductorParser.RETURN)
            self.state = 64
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(javaTraductorParser.FunctionCallContext,0)


        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaTraductorParser.TermContext)
            else:
                return self.getTypedRuleContext(javaTraductorParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(javaTraductorParser.PLUS)
            else:
                return self.getToken(javaTraductorParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(javaTraductorParser.MINUS)
            else:
                return self.getToken(javaTraductorParser.MINUS, i)

        def getRuleIndex(self):
            return javaTraductorParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = javaTraductorParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.functionCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.term()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==javaTraductorParser.PLUS or _la==javaTraductorParser.MINUS:
                    self.state = 68
                    _la = self._input.LA(1)
                    if not(_la==javaTraductorParser.PLUS or _la==javaTraductorParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 69
                    self.term()
                    self.state = 74
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaTraductorParser.FactorContext)
            else:
                return self.getTypedRuleContext(javaTraductorParser.FactorContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(javaTraductorParser.MULTIPLY)
            else:
                return self.getToken(javaTraductorParser.MULTIPLY, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(javaTraductorParser.DIVIDE)
            else:
                return self.getToken(javaTraductorParser.DIVIDE, i)

        def getRuleIndex(self):
            return javaTraductorParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = javaTraductorParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.factor()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==javaTraductorParser.MULTIPLY or _la==javaTraductorParser.DIVIDE:
                self.state = 78
                _la = self._input.LA(1)
                if not(_la==javaTraductorParser.MULTIPLY or _la==javaTraductorParser.DIVIDE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 79
                self.factor()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(javaTraductorParser.ID, 0)

        def Number(self):
            return self.getToken(javaTraductorParser.Number, 0)

        def LPAREN(self):
            return self.getToken(javaTraductorParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(javaTraductorParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(javaTraductorParser.RPAREN, 0)

        def getRuleIndex(self):
            return javaTraductorParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = javaTraductorParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_factor)
        try:
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [javaTraductorParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(javaTraductorParser.ID)
                pass
            elif token in [javaTraductorParser.Number]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(javaTraductorParser.Number)
                pass
            elif token in [javaTraductorParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.match(javaTraductorParser.LPAREN)
                self.state = 88
                self.expression()
                self.state = 89
                self.match(javaTraductorParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(javaTraductorParser.ID, 0)

        def LPAREN(self):
            return self.getToken(javaTraductorParser.LPAREN, 0)

        def arguments(self):
            return self.getTypedRuleContext(javaTraductorParser.ArgumentsContext,0)


        def RPAREN(self):
            return self.getToken(javaTraductorParser.RPAREN, 0)

        def getRuleIndex(self):
            return javaTraductorParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = javaTraductorParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(javaTraductorParser.ID)
            self.state = 94
            self.match(javaTraductorParser.LPAREN)
            self.state = 95
            self.arguments()
            self.state = 96
            self.match(javaTraductorParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(javaTraductorParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(javaTraductorParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(javaTraductorParser.COMMA)
            else:
                return self.getToken(javaTraductorParser.COMMA, i)

        def getRuleIndex(self):
            return javaTraductorParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = javaTraductorParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.expression()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==javaTraductorParser.COMMA:
                self.state = 99
                self.match(javaTraductorParser.COMMA)
                self.state = 100
                self.expression()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





