#pragma once

class Lex
{
private:
	char * sentence;
	char * lex;

public:
	void Get_Gram();				// 문장을 입력 받기 위한 함수
	int Check_Tokentype(char);		// id, 숫자, 공백, 연산자를 구별하기 위한 함수
	int Pass(int, char *, int);		// id나 num을 판단 할때 1개만 보고 판단, 나머지 넘기기 위함
	char * Lexcal();					// 토큰 번호 저장 함수
	~Lex();
};

