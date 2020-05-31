#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int next_permutation(int n, char **s)
{
    int i;
    int j;
    unsigned char result;
    int str_len;
    char temp;
    str_len = n;

    for (j=1; j < str_len; j++){
        for (i=1 ;i <= str_len; i++){
            result = strcmp(s[i], s[i+1]);
            if (result == 0)
            {
                printf("hey")
                return 0;
            }
            else if(result > 0)
            {
                temp = *s[i];
                *s[i] = *s[i+1];
                *s[i+1] = temp;
                printf("%s", temp);
            }
            else if (result < 0)
            {
                temp = *s[i+1];
                *s[i+1] = *s[i];
                *s[i] = temp;
                printf("%s", temp);
            }
        }
        printf("%d\n",j);
        // for ( i = 0; i < n; i++)
        // {
        //     printf("%c", s[i]);
        // }
    }
    return 0;
}

int main()
{
	char **s;
	int n;
	scanf("%d", &n);
	s = calloc(n, sizeof(char*));
	for (int i = 0; i < n; i++)
	{
		s[i] = calloc(11, sizeof(char));
		scanf("%s", s[i]);
	}
	do
	{
		for (int i = 0; i < n; i++)
			printf("%s%c", s[i], i == n - 1 ? '\n' : ' ');
	} while (next_permutation(n, s));
	for (int i = 0; i < n; i++)
		free(s[i]);
	free(s);
	return 0;
}