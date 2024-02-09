#include <cs50.h>
#include <stdio.h>

int calculateYears(int startPopulation, int endPopulation);

int main()
{
    int startPopulation, endPopulation;

    do
    {
        printf("Starting population size (minimum 9): ");
        scanf("%d", &startPopulation);
    }
    while (startPopulation < 9);

    do
    {
        printf("Ending population size (must be at least 9 and above): ");
        scanf("%d", &endPopulation);
    }
    while (endPopulation < 9 || endPopulation < startPopulation);

    int yearsRequired = calculateYears(startPopulation, endPopulation);

    printf("Years: %d\n", yearsRequired);
    return 0;
}

int calculateYears(int startPopulation, int endPopulation)
{
    int years = 0;
    while (startPopulation < endPopulation)
    {
        startPopulation += startPopulation / 3 - startPopulation / 4;
        years++;
    }
    return years;
}
