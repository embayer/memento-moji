#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
100 Blocks a Day
idea stolen from: http://waitbutwhy.com/2016/10/100-blocks-day.html

Most people sleep about seven or eight hours a night.
That leaves 16 or 17 hours awake each day. Or about 1,000 minutes.

Let’s think about those 1,000 minutes as 100 10-minute blocks.
That’s what you wake up with every day.
"""

from datetime import datetime
from sys import argv


class Matrix(object):
    column_count = 6
    row_count = 16
    blocks_total = column_count * row_count

    def __init__(self, remaining_blocks):
        self.remaining_blocks = remaining_blocks
        self.matrix = []
        self.matrix_row = []
        self.consumed_blocks = self.blocks_total - self.remaining_blocks

    def matrix_append(self, block):
        self.matrix_row.append(block)
        if len(self.matrix_row) is self.column_count:
            self.matrix.append(self.matrix_row)
            self.matrix_row = []


class Block(object):
    offset = '  '
    hour_glass_symbol = '⌛  '    # hour glass

    def __init__(self, today_end, theme='emoji'):
        self.today_end = today_end
        self.today_now = datetime.now()
        self.delta = self.today_end - self.today_now
        self.seconds = float(self.delta.total_seconds())
        self.minutes = self.seconds / 60.0
        self.remaining_blocks = int(self.minutes / 10)

        self.block_symbol = '⬜  '    # white block

        if theme == 'block':
            self.consumed_block_symbol = '⬛  '    # black block
            self.remaining_block_symbol = '⬜  '    # white block
            self.current_block_symbol = '⭕  '    # red circle
        elif theme == 'circle':
            self.consumed_block_symbol = '⚫  '    # full black circle
            self.remaining_block_symbol = '⚪  '    # full white circle
            self.current_block_symbol = '🔴  '    # full red circle
        else:    # theme == 'emoji':
            self.consumed_block_symbol = '💀  '    # skull
            self.remaining_block_symbol = '🙂  '    # smiling face
            self.current_block_symbol = '😎  '    # sunglass face
        # self.current_block_symbol = '❌  '    # red cross
        # current_block_symbol = '⬇️  '    # block-down
        # current_block_symbol = '🔳  '    # white square button
        # current_block_symbol = '🔲  '    # black square button
        # current_block_symbol = '🔶  '    # orange diamond
        # current_block_symbol = '🔷  '    # blue diamond
        # current_block_symbol = '🔻  '    # red triangle down
        # current_block_symbol = '🅾️  '    # o-block
        self.matrix = Matrix(self.remaining_blocks)
        self.fill_matrix()

    def fill_matrix(self):
        # prepare a matrix containing all blocks
        for _ in range(self.matrix.consumed_blocks):
            self.matrix.matrix_append(self.consumed_block_symbol)

        self.matrix.matrix_append(self.current_block_symbol)

        for i in range(self.remaining_blocks - 1):
            self.matrix.matrix_append(self.remaining_block_symbol)

    def print_matrix(self):
        print('    1  2  3  4  5  6')
        for i, element in enumerate(self.matrix.matrix):
            print('{:>2}{}{}'.format(i + 1, self.offset,
                                     ''.join(element)))

        # time
        print("\n{} {}".format(self.hour_glass_symbol, self.delta))
        # blocks remaining / blocks consumed
        print("{} {}{} / {}{}".format(self.block_symbol,
                                      self.remaining_block_symbol,
                                      self.remaining_blocks,
                                      self.consumed_block_symbol,
                                      self.matrix.consumed_blocks))

if __name__ == "__main__":
    # assumption: time awake = 7-23 o'clock
    today_end = datetime.now().replace(hour=23, minute=0, second=0)
    if len(argv) > 1:
        block = Block(today_end, theme=str(argv[1]))
    else:
        block = Block(today_end)
    block.print_matrix()
