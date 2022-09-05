#include<stdio.h>
#include<string.h>

int main(void) {
	int T;
	scanf("%d", &T);
	char str[51] = { '\0' };

	for (int i = 0; i < T; i++) {
		int Parenthesis=0;

		
		scanf(" %s", &str);

		for (int i = 0; i < strlen(str); i++) {
			if (Parenthesis < 0) {
				break;
			}
			else if (str[i] == '(') {
				Parenthesis++;
			}
			else if (str[i] == ')') {
				Parenthesis--;
			}
		}
		if(Parenthesis == 0) {
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}

	}

}