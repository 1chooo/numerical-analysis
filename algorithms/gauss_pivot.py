{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 def column(m, c):\
    return [m[i][c] for i in range(len(m))]\
\
\
def row(m, r):\
    return m[r][:]\
\
\
def height(m):\
    return len(m)\
\
\
def width(m):\
    return len(m[0])\
\
\
def print_matrix(m):\
    for i in range(len(m)):\
        print(m[i])\
    print\
    ''\
def gaussian_elimination_with_pivot(m):\
\
    # forward elimination\
    n = height(m)\
    for i in range(n):\
        pivot(m, n, i)\
        for j in range(i + 1, n):\
            m[j] = [m[j][k] - m[i][k] * m[j][i] / m[i][i] for k in range(n + 1)]\
\
    if m[n - 1][n - 1] == 0: raise ValueError('No unique solution')\
    print_matrix(m)\
    # backward substitution\
    x = [0] * n\
    for i in range(n - 1, -1, -1):\
        s = sum(m[i][j] * x[j] for j in range(i, n))\
        x[i] = (m[i][n] - s) / m[i][i]\
    return x\
'''\
def pivot(m, n, i):\
  max_row = max(range(i, n), key=lambda r: abs(m[r][i]))\
  m[i], m[max_row] = m[max_row], m[i]\
'''\
def pivot(m, n, i):\
  max = 1\
  for r in range(i, n):\
    if max < abs(m[r][i]):\
      max_row = r\
      max = abs(m[r][i])\
  m[i], m[max_row] = m[max_row], m[i]\
\
m = [[1, 1, 0, 3, 4], [2, 1, -1, 1, 1], [3, -1, -1, 2, -3], [-1, 2, 3, -1, 4]]\
\
print(gaussian_elimination_with_pivot(m))}