#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// * is required at this function to let the processor know that you already have a pointer, pointed already to a data type, so you become able to modify it and/or assign it to that specific pointer location (memory address)
char *bool_to_str(bool booleanValue)
{

    if (booleanValue == 1)
    {
        return "ALIVE!";
    }
    else
    {
        return "DEAD!";
    }
}

int variables()
{

    char bloodType[3]; // Undefied variable, which can be assigned through a user input (scanf), can have a limiter: char bloodType[20]
    char food[30];     // Undefied variable, which can be assigned through a user input (fgets)

    char name[] = "Ali";           // String (" " DOUBLE qoutes)!
    char lastname_character = 'J'; // Character (' ' SINGLE qoutes)!
    int age;                       // Integer
    float height;                  // Float (6 decimal points)
    double weight;                 // Long Float (15-16 decimal points)
    bool isAlive = true;           // Boolean (0 & 1 as well)

    printf("\nWhat is your Age?: ");
    scanf("%d", &age); // Use & when assigning to datatypes that are not char , scanf can NOT have whitespaces

    printf("\nWhat is your Height?: ");
    scanf("%f", &height);

    getchar(); // This is required when fgets because /n is in the input buffer above "scanf(.../n)", so it does not use /n in the next input answer
    printf("\nWhat is your Favourite food/foods?: ");
    fgets(food, sizeof(food), stdin); // fgets can have whitespaces
    // Using <string.h>
    food[strlen(food) - 1] = '\0'; // This is so the print statement does not add an extra line in the terminal because the buffer (food) ends with a \n "fgets(...\n)"
    // It is like when *food is recalled,
    // it will also obtain an "\n" from a prevoius input buffer and add on it's own buffer a /n too

    printf("\nWhat is your Weight?: ");
    scanf("%lf", &weight);

    printf("\nWhat is your Blood type?: ");
    scanf("%s", bloodType);

    printf("\nName variable: %s\n", name);
    printf("Lastname Character variable: %c\n", lastname_character);
    printf("Age variable: %d\n", age);
    printf("Height variable %.2f\n", height);
    printf("Weight variable: %.13lf\n", weight);
    printf("\n\n------\n");
    printf("Your Blood Type is:\n  - %s\n", bloodType);
    printf("And your favourite food is:\n  - %s\n", food);
    printf("------\n");

    // * is required to make the code know that you want to point to this address and highlight it, it is required if you predefined a variable, and want to modify it through for example
    char *lifeStatus = bool_to_str(isAlive);
    if (isAlive)
    {
        char feeling[] = "cool";
        printf("\nHello %s !\nYou are %s <3 !\nAnd you are %s !\n", name, lifeStatus, feeling);
    }
    else
    {
        char feeling[] = "not cool";
        printf("\nHello %s !\nYou are %s <3 !\nAnd you are %s !\n", name, lifeStatus, feeling);
    }

    return 0;
}

int main()
{

    variables();

    return 0;
}