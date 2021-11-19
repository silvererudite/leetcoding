class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # calculate the XOR of the binary of the two strings
        x_bin = self.numToBinary(x)
        y_bin = self.numToBinary(y)

        xor_count = 0
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                xor_count += 1
        return xor_count

    def numToBinary(self, n):
        bnr = bin(n).replace('0b', '')
        x = bnr[::-1]  # this reverses an array
        while len(x) < 31:
            x += '0'
        bnr = x[::-1]
        return bnr
