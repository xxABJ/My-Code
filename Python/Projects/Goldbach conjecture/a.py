

def batch(amount_colums: int, amount_rows: int, start: int, end: int) -> list:

    # batch = [[y for y in range(y)] for x in range(x)]


    # for i in range(lim):
    #     for rows in range(x):
    #         row = []
    #         for cols in range(y):
    #             col = [i
    #             row.append(col)
    #             i += 1
    #         break
    #     batch.append(row)
    #     continue

    batch = []


    if start != 0:

        val = start


    else:

        val = 0


    for rows in range(amount_rows):

        row = []


        for cols in range(amount_colums):

            col = [val]
            row.append(col)
            val += 1


            if val >= end:

                break


        batch.append(row)


        if val >= end:

            break


        continue


    return batch


def print_batch(batch: list, amount_colums, amount_rows, start, end) -> None:

    for row in range(len(batch)):

        for col in batch[row]:

            length = amount_colums * amount_rows
            len_cols = len(str(length))


            print(f"{' '}{col[0]: >{len_cols}}", end=" ")


        print()


# maximum of printed numbers = amount_colums * amount_rows
amount_colums, amount_rows, start, end = 10, 11, 0, 103

print_batch(batch(amount_colums, amount_rows, start, end), amount_colums, amount_rows, start, end)


