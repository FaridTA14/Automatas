grammar javaTraductor;

// Tokens
DEF : 'def';                
RETURN : 'return';          
LPAREN : '(';               
RPAREN : ')';               
COMMA : ',';                
COLON : ':';                
ASSIGN : '=';               
PLUS : '+';                 
MINUS : '-';                
MULTIPLY : '*';             
DIVIDE : '/';               
ID : [a-zA-Z_][a-zA-Z0-9_]*; 
Number : [0-9]+;            
WS : [ \t\n\r]+ -> skip;    

// Reglas de análisis sintáctico (parse rules)
program: functionDefinition+;

functionDefinition: DEF ID LPAREN parameters RPAREN COLON block;

parameters: ID (COMMA ID)*;

block: statement+;

statement: expressionStatement  | returnStatement  | assignmentStatement ;

assignmentStatement: ID ASSIGN expression;

expressionStatement: expression;

returnStatement: RETURN expression;

expression: functionCall  | term ((PLUS | MINUS) term)*;

term: factor ((MULTIPLY | DIVIDE) factor)*;

factor: ID  | Number  | LPAREN expression RPAREN;

// Nueva regla para llamadas a funciones
functionCall: ID LPAREN arguments RPAREN;

// Nueva regla para la lista de argumentos en una función
arguments: expression (COMMA expression)*;
