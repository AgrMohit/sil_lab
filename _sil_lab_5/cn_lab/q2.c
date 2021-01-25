#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char *argv[])
{
    FILE *fptr;
    char ch;
    fptr = fopen(argv[1], "r");
    if (fptr == NULL)
    {
        printf("unable to open \n");
        exit(0);
    }
    ch = fgetc(fptr);

    if (*argv[2] == 'u')
    {
        printf("Upper case: \n");

        while (ch != EOF)
        {
            if (ch >= 'a' && ch <= 'z')
            {
                ch = ch - 32;
                printf("%c", ch);
                ch = fgetc(fptr);
            }
            else
            {
                printf("%c", ch);
                ch = fgetc(fptr);
            }
        }
        exit(0);
    }
    else if (*argv[2] == 'l')
    {
        printf("Lower case: \n");
        while (ch != EOF)
        {
            if (ch >= 'A' && ch <= 'Z')
            {
                ch = ch + 32;
                printf("%c", ch);
                ch = fgetc(fptr);
            }
            else
            {
                printf("%c", ch);
                ch = fgetc(fptr);
            }
        }
    }
    fclose(fptr);
    return 0;
}
