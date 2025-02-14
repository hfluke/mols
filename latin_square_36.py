PLUS_TABLE_4 = [
    [0, 1, 2, 3],
    [1, 0, 3, 2],
    [2, 3, 0, 1],
    [3, 2, 1, 0]
]

MULT_TABLE_4 = [
    [0, 0, 0, 0],
    [0, 1, 2, 3],
    [0, 2, 3, 1],
    [0, 3, 1, 2]
]

PLUS_TABLE_9 = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [1, 5, 3, 8, 7, 0, 4, 6, 2],
    [2, 3, 6, 4, 1, 8, 0, 5, 7],
    [3, 8, 4, 7, 5, 2, 1, 0, 6],
    [4, 7, 1, 5, 8, 6, 3, 2, 0],
    [5, 0, 8, 2, 6, 1, 7, 4, 3],
    [6, 4, 0, 1, 3, 7, 2, 8, 5],
    [7, 6, 5, 0, 2, 4, 8, 3, 1],
    [8, 2, 7, 6, 0, 3, 5, 1, 4]
]

MULT_TABLE_9 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 2, 3, 4, 5, 6, 7, 8, 1],
    [0, 3, 4, 5, 6, 7, 8, 1, 2],
    [0, 4, 5, 6, 7, 8, 1, 2, 3],
    [0, 5, 6, 7, 8, 1, 2, 3, 4],
    [0, 6, 7, 8, 1, 2, 3, 4, 5],
    [0, 7, 8, 1, 2, 3, 4, 5, 6],
    [0, 8, 1, 2, 3, 4, 5, 6, 7]
]

ORDER4 = 4
ORDER9 = 9
TOTAL_ORDER = 36


def makeSmallSquare(k, order, plusTable, multTable):
    table = [[-1 for col in range(order)] for row in range(order)]
    for row in range(order):
        for col in range(order):
            table[row][col] = plusTable[multTable[row][k]][col]
    
    return table


def makeAllSmallSquares(order, plusTable, multTable):
    tables = []
    for k in range(1, 4):
        tables.append(makeSmallSquare(k, order, plusTable, multTable))
    
    return tables


def makeBigSquare(square4, square9):
    table = [[-1 for col in range(TOTAL_ORDER)] for row in range(TOTAL_ORDER)]
    for row in range(TOTAL_ORDER):
        for col in range(TOTAL_ORDER):
            table[row][col] = 10 * (square4[row % ORDER4][col % ORDER4] + 1) + (square9[row // ORDER4][col // ORDER4] + 1)

    return table


def makeAllBigSquares():
    squaresOrder4 = makeAllSmallSquares(ORDER4, PLUS_TABLE_4, MULT_TABLE_4)
    squaresOrder9 = makeAllSmallSquares(ORDER9, PLUS_TABLE_9, MULT_TABLE_9)
    allSquares = []
    for i in range(ORDER4-1):
        allSquares.append(makeBigSquare(squaresOrder4[i], squaresOrder9[i]))

    return allSquares


def toString(table):
    tableStr = '<table style="width: 100%";>\n'
    for row in range(TOTAL_ORDER):
        tableStr += '<tr>\n'
        for col in range(TOTAL_ORDER):
            tableStr += '<td style="background-color: rgb('           
            tableStr += str(17*table[row][col]%256)
            tableStr += ', '
            tableStr += str(19*table[row][col]%256)
            tableStr += ', '
            tableStr += str(29*table[row][col]%256)
            tableStr += ');">'
            tableStr += str(table[row][col])
            tableStr += '</td>\n'
        tableStr += '</tr>\n'
    tableStr += '</table>\n'

    return tableStr


def toStringAll(tables):
    tableStr = ''
    for table in tables:
        tableStr += toString(table)

    return tableStr


def makeHTML():
    HTML_file = open("mols-order-36.html","w+") 
    HTML_file.write(
"<!DOCTYPE html>\n\
<html>\n\
<style>\n\
html { font-size: 12pt; }\n\
table { border-collapse: collapse; margin-bottom: 8px }\n\
td { border: 2px solid black; text-align: center; }\n\
</style>\n\
<body>\n\
<h1>3 Mutually Orthogonal Latin Squares of Order 36</h1>\n\
" + toStringAll(makeAllBigSquares()) + "\
</body>\n\
</html>\n"
    )          
    HTML_file.close()


if __name__ == "__main__":
    makeHTML()
