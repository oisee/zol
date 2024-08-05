grammar ZOL;

// Parser Rules
program: (functionDecl | structDecl | enumDecl | variableDecl | statement)*;

functionDecl: 'fun' IDENTIFIER '(' paramList? ')' ('->' typeSpec)? block;
paramList: param (',' param)*;
param: IDENTIFIER ':' typeSpec ('in' register)?;

structDecl: 'struct' IDENTIFIER '{' (IDENTIFIER ':' typeSpec ';')* '}';

enumDecl: 'enum' IDENTIFIER '{' IDENTIFIER ('=' INTEGER)? (',' IDENTIFIER ('=' INTEGER)?)* '}';

variableDecl: typeSpec IDENTIFIER ('=' expression)? ';';

statement
    : block
    | ifStatement
    | whileStatement
    | repeatStatement
    | forStatement
    | matchStatement
    | expressionStatement
    | returnStatement
    | asmBlock
    ;

block: '{' statement* '}';

ifStatement: 'if' expression block ('else' (ifStatement | block))?;

whileStatement: 'while' expression block;

repeatStatement: 'repeat' INTEGER block;

forStatement: 'for' IDENTIFIER 'in' IDENTIFIER block;

matchStatement: 'match' expression '{' matchCase* '}';
matchCase: (IDENTIFIER | '_') '=>' (expression | block) ',';

expressionStatement: expression ';';

returnStatement: 'return' expression? ';';

asmBlock: 'asm' '{' .*? '}';

expression
    : primary
    | expression ('*'|'/'|'%') expression
    | expression ('+'|'-') expression
    | expression ('<<'|'>>') expression
    | expression ('&'|'|'|'^') expression
    | expression ('=='|'!='|'<'|'<='|'>'|'>=') expression
    | expression '&&' expression
    | expression '||' expression
    | '!' expression
    | '~' expression
    | '-' expression
    | '(' expression ')'
    | IDENTIFIER '(' (expression (',' expression)*)? ')'
    ;

primary
    : INTEGER
    | FLOAT
    | BOOLEAN
    | IDENTIFIER
    | arrayLiteral
    | structLiteral
    ;

arrayLiteral: '{' (expression (',' expression)*)? '}';
structLiteral: '{' (IDENTIFIER ':' expression (',' IDENTIFIER ':' expression)*)? '}';

typeSpec
    : 'i8' | 'u8' | 'i16' | 'u16' | 'bool' | 'fixed'
    | IDENTIFIER  // For struct types
    | typeSpec '[' INTEGER? ']'  // For array types
    ;

register: 'A' | 'B' | 'C' | 'D' | 'E' | 'H' | 'L' | 'BC' | 'DE' | 'HL' | 'IX' | 'IY';

// Lexer Rules
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
INTEGER: [0-9]+ | '0b' [01]+ | '0x' [0-9a-fA-F]+;
FLOAT: [0-9]+ '.' [0-9]+;
BOOLEAN: 'true' | 'false';

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' .*? '\n' -> skip;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip;

// Meta programming constructs
META: '@' IDENTIFIER .*? '\n' -> skip;