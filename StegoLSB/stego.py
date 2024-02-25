from PIL import Image
import os

class StegoLSB:
    def __init__(self, img: str | bytes, lsb_value: int = 1) -> None:
        if isinstance(img, str):
            self.img = Image.open(img)
            
            self.imgData = self.img.tobytes()
            self.imgSize = self.img.size
            self.imgFormat = self.img.format
            self.imgMode = self.img.mode
        elif isinstance(img, (bytearray, bytes)):
            self.imgData = img
        else:
            raise ValueError(f"{type(img)} is not supported")
            
        self.lsb_value = lsb_value


    def __splitBytesOnBits(self, bytes: bytes, bits: int = 1) -> list[str]:
        bits_array = []
        for byte in bytes:
            bit_string = bin(byte)[2:].zfill(8)
            for i_bit in range(0, len(bit_string), bits):
                bits_array.append("".join(bit_string[i_bit:i_bit + bits]))

        return bits_array

    def __insertLSBtoRaw(self, LSB_bits: list[str]):
        LSB_l = len(LSB_bits[0])
        LSB_c = len(LSB_bits)
        raw_bits_array = [bin(byte)[2:].zfill(8) for byte in self.imgData[:LSB_c]]

        raw_with_LSB = []
        for i_bits, LSB_bit in zip(range(len(raw_bits_array)), LSB_bits):
            raw_with_LSB.append(int(raw_bits_array[i_bits][:-LSB_l] + LSB_bit, 2))
        
        self.stegoImgData = list(raw_with_LSB) + list(self.imgData[len(raw_with_LSB):])    

        return self.stegoImgData

    def hideData(self, data: bytes, lsb_value: int = 1):
        if len(data) * (8 // lsb_value) > len(self.imgData):
            raise ValueError("Data to hide is larger then original file")

        data += b"!KnKLSB"
        
        splited = self.__splitBytesOnBits(data, lsb_value)
        
        raw_with_LSB = self.__insertLSBtoRaw(splited)
        
        newImg = Image.frombytes(data=bytes(raw_with_LSB), size=self.imgSize, mode=self.imgMode)

        return newImg
        
    def seekData(self, checkLSB: int = 1):
        LSB_bits = ""
        
        for byte in self.imgData:
            LSB_bits += (bin(byte)[2:].zfill(8)[-checkLSB:])
        
        res = []
        for i in range(0, len(LSB_bits), 8):
            res.append(int(LSB_bits[i:i+8], 2))
            if bytes(res[-7:]) == b"!KnKLSB":
                res = res[:-7]
                break
        
        if not bytes(res).find(b"!KnKLSB"):
            raise LookupError("Can't find stegocipher with this LSB_value or file don't have it")
        
        return bytes(res).decode('utf-8')