#include <stdio.h>

int main() {
    printf("Hello World!\n");
    printf("My name is %s\n", "Ali");
    printf("I am %d years old!\n", 27);
    printf("My height is %.3f cm or %.3f cm tall!\n\n", 169.449, 170.326);
    
    printf("Seperate function call {int func()}\n\n");
    func();

    return 0;
}

int func() {
    char *firstName, *lastName, *country;
    int age;
    float height, weight;

    firstName = "Ali";
    lastName = "Al-Rabaan";
    country = "Qatar";
    age = 27;
    height = 169.74;
    weight = 82.59;

    /* scanf("Type your First Name: ", firstName); */

    printf("Hello, my name is: %s %s\n\n", firstName, lastName);
    printf("I am from %s !\n", country);
    printf("I am %d years old !\n\n", age);
    printf("Also, I obtain a:\n");
    printf(" Height of: %.1fcm\n", height);
    printf(" Weight of: %.1fkg\n\n", weight);
    printf("Goodbye !");
    
    return 0;
}