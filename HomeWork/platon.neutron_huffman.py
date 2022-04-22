__license__ = 'Junior (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: huffman.py 2022-04-17'

"""
Huffman homework
2022
@author: platon.neutron
"""

from algopy import bintree
from algopy import heap

###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import
###############################################################################
## COMPRESSION

def buildfrequencylist(dataIN):
    """
        Builds a tuple list of the character frequencies in the input.
    """
    tempResult = []
    result = []
    present = False

    tempResult.append(dataIN[0])
    tempResult.append(1)

    for i in range(1, len(dataIN)):
        for j in range(0, len(tempResult), 2):
            if (dataIN[i] == tempResult[j]):
                tempResult[j + 1] += 1
                present = True

        if (present == False):
            tempResult.append(dataIN[i])
            tempResult.append(1)

        present = False

    for k in range(1, len(tempResult), 2):
        result.append((tempResult[k], tempResult[k - 1]))

    return result


def __petitTri(tupleList):
    """
        Sort the list take in parameter.
    """
    for i in range(len(tupleList)):
        x = tupleList[i]
        j = i

        while (j > 0 and (tupleList[j - 1][0] < x[0])):
            tupleList[j] = tupleList[j - 1]
            j -= 1

        tupleList[j] = x

def __binTreeList(tupleList):
    """
        Transform char in the tuples in BinTree.
    """
    result = []

    for i in range(len(tupleList)):
        result.append((tupleList[i][0], bintree.BinTree(tupleList[i][1], None, None)))

    return result

def buildHuffmantree(inputList):
    """
        Processes the frequency list into a Huffman tree according to the algorithm.
    """
    __petitTri(inputList)
    binTreeList = __binTreeList(inputList)

    while (len(binTreeList) != 1):
        plusPetit1 = binTreeList.pop()
        plusPetit2 = binTreeList.pop()
        freq = plusPetit1[0] + plusPetit2[0]

        maximum = max((plusPetit1[0], 1), (plusPetit2[0], 2))

        if (maximum[1] == 1):
            maximum = plusPetit1[1]
            minimum = plusPetit2[1]

        else:
            maximum = plusPetit2[1]
            minimum = plusPetit1[1]

        binTreeList.append((freq, bintree.BinTree(None, maximum, minimum)))
        i = len(binTreeList) - 1
        while (len(binTreeList) != 1 and i != 0 and binTreeList[i][0] > binTreeList[i - 1][0]):
            binTreeList[i], binTreeList[i - 1] = binTreeList[i - 1], binTreeList[i]
            i -= 1

    return binTreeList[0][1]


def encodedata(huffmanTree, dataIN):
    """
        Encodes the input string to its binary string representation.
    """
    # FIXME
    pass


def encodetree(huffmanTree):
    """
    Encodes a huffman tree to its binary representation using a preOrder traversal:
        * each leaf key is encoded into its binary representation on 8 bits preceded by '1'
        * each time we go left we add a '0' to the result
    """
    # FIXME
    pass


def tobinary(dataIN):
    """
    Compresses a string containing binary code to its real binary value.
    """
    # FIXME
    pass


def compress(dataIn):
    """
    The main function that makes the whole compression process.
    """
    
    # FIXME
    pass

    
################################################################################
## DECOMPRESSION

def decodedata(huffmanTree, dataIN):
    """
    Decode a string using the corresponding huffman tree into something more readable.
    """
    # FIXME
    pass

    
def decodetree(dataIN):
    """
    Decodes a huffman tree from its binary representation:
        * a '0' means we add a new internal node and go to its left node
        * a '1' means the next 8 values are the encoded character of the current leaf         
    """
    # FIXME
    pass


def frombinary(dataIN, align):
    """
    Retrieve a string containing binary code from its real binary value (inverse of :func:`toBinary`).
    """
    # FIXME
    pass


def decompress(data, dataAlign, tree, treeAlign):
    """
    The whole decompression process.
    """
    # FIXME
    pass
