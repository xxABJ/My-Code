def indicator_sum(len_normal_sums: int, accounting_number: int, num: list) -> int:
    # Logic2 ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹
    """
*Indicator Sum*

This value is based on a temporary digit as a result of the substition of diviing by zero. When dividing by zero occurs, it produces a a temporary number, for example:

```
15 / 0 = `ind¹⁵`
```

It is created with the help of another value called the *Accounting Sum*. The *Accounting Sum* is a value that is used to account for the ammount of *Normal Sums* Logic1 produces. It simply sums up a specific number called the *Accounting Number*.

**THE ACCOUNT NUMBER IS DYNAMIC & SPECIFIED WHEN CALLING THIS FUNCTION**

The temporary digit comes from a new numberline which hosts the values called the *Indicator Number*'s :

```
. -5       -4       -3       -2       -1        0        1        2        3        4        5
───┼────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┼───
`ind⁻⁵    ind⁻⁴    ind⁻³    ind⁻²    ind⁻¹     ind⁰     ind¹     ind²     ind³     ind⁴     ind⁵`
```

which represents a value that cannot be used with normal math.

Therefore in order to benefit from it, we have to take the absolute value of it:

```
| `ind¹⁵` | = 15
```

A special condition uses an *Indicator Number* that is produced by dividing by zero, to determine the final result of the *Indicator Sum*.
Also a Contingency table is below to show the *Indicator Value* results after calculating the *Indicator Sum*.

```

#Special Condition
```

It uses a special condition where if the resulting value of the:

***Indicator Sum*** = ***Accounting Sum*** -> subtract -> the absolute value of the ***Indicator Number***

results to a positive number, it would produce a specific result, and if it results to a negative number, it would produce a different result.

```

# Indicator Value
```

If positive (Indicator Sum), then (Indicator Sum) x (Accounting Number) -> (Indicator Value)

If negative (Indicator Sum), then the absolute value of (Indicator Sum) -> (Indicator Value)

``` 

#Contingency Table

Accounting Number = 4
┌───────┬───────┬───────┬───────┬───────┐
│   N   │   3   │   2   │   1   │       │
│   E   │───────┼───────┼───────┼───────┤
│   G   │   2   │   1   │       │   4   │
│   A   │───────┼───────┼───────┼───────┤
│   T   │   1   │       │   4   │   8   │
│   I   │───────┼───────┼───────┼───────┤
│   V   │       │   4   │   8   │   16  │
│   E   └───────────────────────────────┤
│                    P O S I T I V E    │
└───────────────────────────────────────┘
```


Then it is put in an equation called the "Indicator Sum Equation" to give us a result, which we benefit in calculating the final result.
@TODO: make the Indicator Sum Equation block

This is the next step in the process of calculating the final result.

    """


    accounting_sum = accounting_number * len_normal_sums


    # Dividing by zero creates a new numberline which hosts the values called the *Indicator Numbers*, which represents a value that cannot be used with normal math. Therefore in order to benefit from it, we have to take the absolute value of it. We write if as indicator_value to proceed with the calculations, hence the creation of the new temporary numberline and digit. But we will not be using it in that form, instead we will be using the absolute value of it.


    if len(num) == 1:
        
        a1 = num[0]
        print(a1)


        # indicator_value = ((a1 * 1) / 0) * 1
        indicator_value = a1 * 1 * 1 # Translating to functional code

        # After simulating the division by zero and taking the absolute value of the resulting value, we can now proceed with the calculations of the *Indicator Sum* value.
        indicator_sum = accounting_sum - abs(indicator_value)


    elif len(num) == 2:
        pass


    elif len(num) == 3:
        pass