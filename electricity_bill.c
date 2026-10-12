**Program: Electricity Bill Calculator**

```c
#include <stdio.h>
#include <conio.h>

void main()
{
    int units;
    float bill;

    clrscr();

    printf("Enter electricity units consumed: ");
    scanf("%d", &units);

    if (units < 0)
    {
        printf("Invalid units!");
    }
    else if (units <= 100)
    {
        bill = units * 1.50;
        printf("Electricity Bill = Rs. %.2f", bill);
    }
    else if (units <= 200)
    {
        bill = 150 + (units - 100) * 2.50;
        printf("Electricity Bill = Rs. %.2f", bill);
    }
    else
    {
        bill = 400 + (units - 200) * 4.00;
        printf("Electricity Bill = Rs. %.2f", bill);
    }

    getch();
}
```

**Note:** The electricity rates used here are assumed sample rates for practice, not actual electricity tariffs.
