#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int char2int()
{

    char c1 = '\0';
    int i1 = 0;

    printf("\nTesting the input buffer (scanf, fgets).\n");

    printf("Order 1: input char  -->  input int\n");
    printf("Enter char: ");
    scanf("%c", &c1);
    printf("Enter int: ");
    scanf("%d", &i1);

    printf("------\n");
    printf("Char: %c\n", c1);
    printf("------\n");
    printf("Int: %d\n", i1);
    printf("------\n");

    printf("\nOrder 2: input int  -->  input char\n");
    printf("Enter int: ");
    scanf("%d", &i1);
    printf("Enter char: ");
    //
    getchar(); // clears the '/n' when getting input in this order:  any datatype input --> char/string input
    scanf("%c", &c1);
    //
    printf("------\n");
    printf("Int: %d\n", i1);
    printf("------\n");
    printf("Char: %c\n", c1);
    printf("------\n");

    return 0;
}

int string2int()
{

    char c1[10] = ""; // array '*' of chars ' c1 *[10]* '
    int i1 = 0;

    printf("\nTesting the input buffer (scanf, fgets).\n");

    printf("Order 1: input string  -->  input int\n");
    printf("Enter string: ");
    //
    fgets(c1, sizeof(c1), stdin);
    c1[strlen(c1) - 1] = '\0'; // for fgets this clears the automatic '/n' after executing the func; c1 = ".....\n"  -->  c1 = "....."
    //
    printf("Enter int: ");
    scanf("%d", &i1);

    printf("------\n");
    printf("String: %s\n", c1);
    printf("------\n");
    printf("Int: %d\n", i1);
    printf("------\n");

    printf("\nOrder 2: input int  -->  input string\n");
    printf("Enter int: ");
    scanf("%d", &i1);
    printf("Enter String: ");
    //
    getchar(); // clears the '/n' when getting input in this order:  any datatype input --> char/string input
    fgets(c1, sizeof(c1), stdin);
    c1[strlen(c1) - 1] = '\0'; // for fgets this clears the automatic '/n' after executing the func; c1 = ".....\n"  -->  c1 = "....."
    //
    printf("------\n");
    printf("Int: %d\n", i1);
    printf("------\n");
    printf("String: %s\n", c1);
    printf("------\n");

    return 0;
}

int main()
{

    // char2int();
    string2int();

    /*
    If the order of any inputs proceeds to a char input or a string input, that inputer will take the built-in /n that comes after the func itself, i.e:


    printf("Enter int: ");
    scanf("%d", &i1);        <--  There is a '/n' after "%d"
    getchar();
    printf("Enter char: ");
    scanf("%c", &c1);        <--  This
                                  will become '\n' and move on to the next line of code, skipping the user input entering sequence, because "%c" does not support whitespaces and counts '/n' as the input itself.


    or


    printf("Enter int: ");
    scanf("\d", i1);               <--  There is a '/n' after "%d"
    printf("Enter String: ");
    fgets(c1, sizeof(c1), stdin);  <-- For
                                       fgets(), it acts like a char input request '~ scanf("%c", &c1)' where it would take the built-in '/n' that comes after the func itself, AND also adds a '\n' automatically after executing the func itself; '~ fgets(c1, sizeof(c1), stdin)' == f'~ {c1}\n'.
    */

    return 0;
}